import pandas as pd
import numpy as np
import requests
from getpass import getpass
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
ruta = "../data/raw/BD_SERPAVI_2011-2024.xlsx"
xls = pd.ExcelFile(ruta)
print(xls.sheet_names)
df_metadatos = pd.read_excel(ruta, sheet_name='Metadatos')
print(df_metadatos.shape)
print(df_metadatos.columns)
print(df_metadatos.iloc[18, 1]); print(df_metadatos.iloc[17, 0]); print(df_metadatos.iloc[38, 0]); print(df_metadatos.iloc[39, 0])
df = pd.read_excel(ruta, sheet_name='Secciones censales')
df['CUSEC'] = df['CUSEC'].astype(str).str.zfill(10)
filtro_municipio_madrid =df['CUSEC'].str.startswith("28079")
print(filtro_municipio_madrid.sum())
df_madrid = df.loc[filtro_municipio_madrid].copy()
columna = list(df_madrid.columns[4:5])
columnas_restantes = df_madrid.columns[5:]
prefijos = ['BI_ALVHEPCO_TVC_', 'ALQM2_LV_M_VC_', 'ALQM2_LV_25_VC_', 'ALQM2_LV_75_VC_','ALQTBID12_M_VC_', 'ALQTBID12_25_VC', 'ALQTBID12_75_VC']
columnas_filtradas = []

for c in columnas_restantes:
    for p in prefijos:
        if c.startswith(p):
            año = c[-2:]
            if año.isdigit() and 15 <= int(año) <= 24:
                columnas_filtradas.append(c)
                break

columnas_unidas = columna + columnas_filtradas
df_alquileres_madrid = df_madrid[columnas_unidas]        
df_alquileres_madrid = df_alquileres_madrid.rename(columns={'CUSEC': 'COD_SEC_MADRID'})
largo = df_alquileres_madrid.melt(id_vars="COD_SEC_MADRID", var_name="col", value_name="valor")
largo["Año"] = 2000 + largo["col"].str[-2:].astype(int)
largo["indicador"] = largo["col"].str[:-3]

alq = (largo.pivot(index=["COD_SEC_MADRID", "Año"], columns="indicador", values="valor").reset_index())
alq.columns.name = None
alq = alq.rename(columns={
    "BI_ALVHEPCO_TVC": "n_alquileres",
    "ALQM2_LV_M_VC": "eur_m2_media",
    "ALQM2_LV_25_VC": "eur_m2_p25",
    "ALQM2_LV_75_VC": "eur_m2_p75",
    "ALQTBID12_M_VC": "alq_inmueble_media",
    "ALQTBID12_25_VC": "alq_inmueble_p25",
    "ALQTBID12_75_VC": "alq_inmueble_p75",})
alq_analisis = alq[alq["Año"] <= 2022].copy()
alq_validacion = alq[alq["Año"] >= 2023].copy()
alq.to_csv("../data/clean/alquiler.csv", index=False)
df_demografia = pd.read_csv("../data/raw/demografia.csv", sep=";")
print(df_demografia.columns)
df_filtrado = df_demografia[df_demografia["Municipios"].str.contains("^28079 Madrid", case=False, na=False)]
df_filtrado = df_filtrado[df_filtrado['Periodo'].between(2015,2022)]
print(df_filtrado.isna().sum())
df_filtrado = df_filtrado.drop(columns=['Municipios', 'Distritos'])
df_filtrado = df_filtrado.rename(columns={'Secciones': 'COD_SEC_MADRID', 'Periodo': 'Año', 'Indicadores demográficos': 'indicadores'})
df_dem = df_filtrado.copy()
df_sec_dem = df_dem[df_dem["COD_SEC_MADRID"].notna()].copy()
nombres = {'Edad media de la población': 'edad_media',
 'Porcentaje de población menor de 18 años':'pct_menor18',
 'Porcentaje de población de 65 y más años': 'pct_65mas',
                   'Tamaño medio del hogar':'tam_hogar',
      'Porcentaje de hogares unipersonales':'pct_unipersonal',
                                'Población': 'poblacion',
         'Porcentaje de población española': 'pct_española'}

df_sec_dem['indicadores'] = df_sec_dem['indicadores'].map(nombres)
df_sec_dem['COD_SEC_MADRID'] = df_sec_dem['COD_SEC_MADRID'].astype(str).str[:10]
df_sec_dem = df_sec_dem[df_sec_dem['indicadores'] != 'pct_española']
print(df_sec_dem["indicadores"].unique())
for ind in df_sec_dem["indicadores"].unique():
    print(ind, df_sec_dem.loc[df_sec_dem["indicadores"] == ind, "Total"].dropna().head().tolist())
    df_sec_dem['Total'] = df_sec_dem['Total'].astype(str).str.strip()
df_sec_dem['Total'] = np.where(
    df_sec_dem['indicadores'] == 'poblacion',
    df_sec_dem['Total'].str.replace('.', '', regex=False),
    df_sec_dem['Total'].str.replace(',', '.', regex=False))
df_sec_dem['Total'] = pd.to_numeric(df_sec_dem['Total'], errors='coerce')
df_sec_dem = (df_sec_dem.groupby(["COD_SEC_MADRID", "Año", "indicadores"])["Total"].first().unstack("indicadores").reset_index())
df_sec_dem["pct_18_64"] = 100 - df_sec_dem["pct_menor18"] - df_sec_dem["pct_65mas"]
df_dem_sec_madrid = df_sec_dem
df_dem_sec_madrid = df_dem_sec_madrid.drop(columns=['pct_menor18', 'pct_18_64'])
df_dem_sec_madrid.columns.name = None
df_dem_sec_madrid.to_csv("../data/clean/demografia.csv", index=False)
url = 'https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=846:'
api_distritos = requests.get(url)
datos_json = api_distritos.json()
df = pd.DataFrame(datos_json)
df_expandido = df.explode("Data").copy()
import json

def extraer_campo(x, campo):
    if isinstance(x, str):
        try:
            x = json.loads(x.replace("'", '"'))
        except:
            return None
    if isinstance(x, dict):
        return x.get(campo)
    return None
df_expandido["Fecha"] = df_expandido["Data"].apply(lambda x: extraer_campo(x, "Anyo"))
df_expandido["Valor"] = df_expandido["Data"].apply(lambda x: extraer_campo(x, "Valor"))
filtro_madrid = df_expandido["Nombre"].str.contains("^Madrid", case=False, na=False)
filtro_fechas = df_expandido["Fecha"].isin(list(range(2015, 2023)))
filtro_T3unidad = df_expandido["T3_Unidad"].str.strip() == "Euros"
df_madrid_filtrado = df_expandido[filtro_madrid & filtro_fechas & filtro_T3unidad].copy()
separacion_nombre = df_madrid_filtrado["Nombre"].str.split(".", n=1, expand=True)
df_madrid_filtrado["Distrito madrid"] = separacion_nombre[0].str.strip()
df_madrid_filtrado["Dato base"] = separacion_nombre[1].str.strip()
indicadores_datobase = ["Dato base. Renta neta media por persona.","Dato base. Renta neta media por hogar."]
filtro_rentas = df_madrid_filtrado["Dato base"].isin(indicadores_datobase)
df_madrid_filtrado = df_madrid_filtrado[filtro_rentas]
df_madrid_filtrado['Distrito madrid'] = df_madrid_filtrado['Distrito madrid'].str[-2:]
columnas_drop = ["Data", "T3_Escala", "T3_Unidad", "Nombre"]
df_madrid_distritos = df_madrid_filtrado.drop(columns=columnas_drop).rename(columns={"Fecha": "Año"})
df_madrid_distritos["tipo"] = df_madrid_distritos["Dato base"].str.contains("hogar").map({True: "hogar", False: "persona"})
df_madrid_distritos = df_madrid_distritos.drop(columns=['COD', 'Dato base'])
df_madrid_distritos = df_madrid_distritos.rename(columns={'Distrito madrid': 'COD_DIS_MADRID'})
df_madrid_distritos['COD_DIS_MADRID'] = "28079" + df_madrid_distritos['COD_DIS_MADRID'].astype(str)
print(df_madrid_distritos["Año"].isna().sum())      
print(df_madrid_distritos["COD_DIS_MADRID"].nunique())
renta_dis_madrid = (df_madrid_distritos.pivot(index=["COD_DIS_MADRID", "Año"], columns="tipo", values="Valor")
           .reset_index().rename(columns={"hogar": "renta_hogar", "persona": "renta_persona"}))
renta_dis_madrid.columns.name = None
print(renta_dis_madrid.shape)
renta_dis_madrid.to_csv("../data/clean/renta_distrito.csv", index=False)
url2015 = 'https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20150101:20150101'
url2016 = 'https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20160101:20160101'
url2017 = 'https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20170101:20170101'
url2018 = 'https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20180101:20180101'
url2019 = 'https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20190101:20190101'
url2020 = 'https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20200101:20200101'
url2021 = 'https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20210101:20210101'
url2022 = 'https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20220101:20220101'
def procesar_datos_ine(url2016):
    api_sec = requests.get(url2016)
    datos_json = api_sec.json()
    df = pd.DataFrame(datos_json)

    df_expandido = df.explode("Data").copy()

    df_expandido["Año"] = df_expandido["Data"].str["Anyo"].astype("Int64")
    df_expandido["Valor"] = df_expandido["Data"].str["Valor"].astype(float)

    filtro_madrid = df_expandido["Nombre"].str.contains("^Madrid", case=False, na=False)
    filtro_T3unidad = df_expandido["T3_Unidad"].str.strip() == "Euros"
    df_sec_filtrado = df_expandido[filtro_madrid & filtro_T3unidad].copy()

    separacion_nombre = df_sec_filtrado["Nombre"].str.split(".", n=1, expand=True)
    df_sec_filtrado["Seccion madrid"] = separacion_nombre[0].str.strip()
    df_sec_filtrado["Dato base"] = separacion_nombre[1].str.strip()

    indicadores_datobase = ["Dato base. Renta neta media por persona.", "Dato base. Renta neta media por hogar.",]
    filtro_rentas_sec = df_sec_filtrado["Dato base"].isin(indicadores_datobase)
    df_sec_filtrado = df_sec_filtrado[filtro_rentas_sec]
    df_sec_filtrado["Seccion censal"] = df_sec_filtrado["Seccion madrid"].str[-5:]
    

    columnas_drop1 = ["Data", "T3_Escala", "T3_Unidad", "Nombre", "Seccion madrid"]
    df_madrid_seccion = df_sec_filtrado.drop(columns=columnas_drop1).rename(columns={"Fecha": "Año"})

    return df_madrid_seccion
df_madrid_seccion_2015 = procesar_datos_ine(url2015)
df_madrid_seccion_2016 = procesar_datos_ine(url2016)
df_madrid_seccion_2017 = procesar_datos_ine(url2017)
df_madrid_seccion_2018 = procesar_datos_ine(url2018)
df_madrid_seccion_2019 = procesar_datos_ine(url2019)
df_madrid_seccion_2020 = procesar_datos_ine(url2020)
df_madrid_seccion_2021 = procesar_datos_ine(url2021)
df_madrid_seccion_2022 = procesar_datos_ine(url2022)
tablas = [df_madrid_seccion_2015, df_madrid_seccion_2016, df_madrid_seccion_2017, df_madrid_seccion_2018, df_madrid_seccion_2019, df_madrid_seccion_2020, df_madrid_seccion_2021, df_madrid_seccion_2022]
df_madrid_seccion_completo = pd.concat(tablas, axis=0, ignore_index=True)
df_madrid_seccion_completo['Año'].isna().sum()
df_madrid_seccion_completo["tipo"] = df_madrid_seccion_completo["Dato base"].str.contains("hogar").map({True: "hogar", False: "persona"})
df_madrid_seccion_completo = df_madrid_seccion_completo.drop(columns=['COD', 'Dato base'])
df_madrid_seccion_completo = df_madrid_seccion_completo.rename(columns={'Seccion censal': 'COD_SEC_MADRID'})
df_madrid_seccion_completo['COD_SEC_MADRID'] = "28079" + df_madrid_seccion_completo['COD_SEC_MADRID'].astype(str)
df = df_madrid_seccion_completo.reset_index(drop=True).copy()
df["año_pos"] = 2015 + df.index // 4986
df["Año"] = df["Año"].fillna(df["año_pos"]).astype(int)
df = df.drop(columns="año_pos")
renta_sec_madrid = (df.pivot(index=["COD_SEC_MADRID", "Año"], columns="tipo", values="Valor")
           .reset_index().rename(columns={"hogar": "renta_hogar", "persona": "renta_persona"}))
renta_sec_madrid.columns.name = None  # ESTO ES PARA BORRAR EL TITULO 'TIPO' QUE SE GENERA POR EL PIVOT
print(renta_sec_madrid.shape)
renta_sec_madrid.to_csv("../data/clean/renta_seccion.csv", index=False)
alq = pd.read_csv("../data/clean/alquiler.csv", dtype={"COD_SEC_MADRID": str})
rs  = pd.read_csv("../data/clean/renta_seccion.csv", dtype={"COD_SEC_MADRID": str})
rd  = pd.read_csv("../data/clean/renta_distrito.csv", dtype={"COD_DIS_MADRID": str})
dem = pd.read_csv("../data/clean/demografia.csv", dtype={"COD_SEC_MADRID": str})
print(alq.shape, rs.shape, rd.shape, dem.shape)
alq = alq.rename(columns={"COD_SEC_MADRID": "cod_sec", "Año": "año"})
rs  = rs.rename(columns={"COD_SEC_MADRID": "cod_sec", "Año": "año"})
rd  = rd.rename(columns={"COD_DIS_MADRID": "cod_dis", "Año": "año"})
dem = dem.rename(columns={"COD_SEC_MADRID": "cod_sec", "Año": "año"})
codigos = sorted(set(alq["cod_sec"]) | set(rs["cod_sec"]) | set(dem["cod_sec"]))
secciones = pd.DataFrame({"cod_sec": codigos})
secciones["cod_dis"] = secciones["cod_sec"].str[:7]
distritos = pd.DataFrame({"cod_dis": sorted(rd["cod_dis"].unique())})
password = quote_plus(getpass("Contraseña de MySQL: "))
engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/radar_madrid_alquileres")
distritos.to_sql("distritos", engine, if_exists="append", index=False)
secciones.to_sql("secciones", engine, if_exists="append", index=False)
alq.to_sql("alquiler", engine, if_exists="append", index=False, chunksize=2000)
rs.to_sql("renta_seccion", engine, if_exists="append", index=False, chunksize=2000)
rd.to_sql("renta_distrito", engine, if_exists="append", index=False)
dem.to_sql("demografia", engine, if_exists="append", index=False, chunksize=2000)   
















































