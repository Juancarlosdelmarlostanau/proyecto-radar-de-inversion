TITULO DEL PROYECTO

Radar de inversion residencial  para alquileres en madrid : analisis por seccion censal(2015-2022) y tendencia a 2027

¿donde es mejor invertir en vivienda de alquiler en madrid? "generar un score de atractivo con datos abiertos y un aproyeccion a cinco años"

HIPOTESIS GENERAL
Entre 2015 y 2022, el atractivo de una sección de Madrid para invertir en alquiler no dependió de su nivel de precio, sino de la combinación de crecimiento del alquiler, capacidad de pago de los hogares y perfil demográfico de la demanda. El análisis por sección revela oportunidades y riesgos que el distrito oculta, y la tendencia 2015-2022 permite estimar, con incertidumbre, el alquiler hacia 2027.

PREGUNTAS
1. ¿Las secciones más caras son las que más crecieron?
2. Dispersión intradistrital: (P75 − P25) / mediana por sección, y variación entre secciones de cada distrito
3. Esfuerzo de alquiler: alquiler mensual del inmueble × 12 / renta neta del hogar
4. Brecha de crecimiento: crecimiento del alquiler menos crecimiento de la renta del hogar
5. Índice de perfil de demanda: % de 18 a 64, edad media, tamaño del hogar y % hogares unipersonales, relacionado con nivel y crecimiento
6. Proyección por distrito en tres escenarios, validada con el error frente a 2023-2024

METRICAS
1. Crecimiento anual compuesto del alquiler (2015-2019, 2019-2022 y total), comparado con el nivel de partida (SERPAVI)
2. ¿Cuánto varía el alquiler dentro de un mismo distrito frente a entre distritos?                            (SERPAVI + distrito (de los 7 primeros dígitos del código))
3. ¿Dónde pueden pagar los hogares el alquiler?                                                               (SERPAVI + renta por sección)
4. ¿Dónde creció el alquiler más rápido que la renta?                                                         (SERPAVI + renta por sección)
5. ¿Coincide el perfil demográfico de demanda con los alquileres altos o crecientes?                          (Demografía + SERPAVI)
6. ¿Qué distritos tendrán más alquiler en 2027 y qué tan fiable es esa estimación?                            (SERPAVI agregado (ponderado por número de alquileres))



SE DESCARGO LOS DATOS DE:
1. xslx de 'Sistema estatal de referencia del precio del alquiler de vivienda' (SERPAVI)
- BD Sistema Estatal Índices de Alquiler de Vivienda (Xlsx. 67.8Mb)
https://www.mivau.gob.es/vivienda/alquila-bien-es-tu-derecho/serpavi

esta informacion muestra el precio y evolucion. Es el nucleo del proyecto : crecimiento y fiabilidad por seccion.

Existen en total 2399 nulos  en un total de 173382 celdas que equivalen al 1.44% aproximadamente.
Que se dejaron sin imputar (sin rellenar con ceros, medias ni interpolaciones) para no inventar datos.

el DF_final se llama df_alquileres_madrid
df_alquileres_madrid tiene las columnas llamandas: con los años (2015-2022) VC:VIVIENDA COLECTIVA
-BI_ALVHEPCO_TVC = RECUENTO DE CONTRATOS DE ALQUILER´, ES LA MEDIDA PARA FIABILIDAD
-ALQM2_LV_M_VC   = NIVEL DE ALQUILER
-ALQM2_LV_25_VC  = PARA LA DISPERSION
-ALQM2_LV_75_VC  = PARA DISPERSION
-ALQTBID12_M_VC =  PARA EL ESFUERZO DE ALQUILER
-ALQTBID12_25_VC = PARA RANGOS EN LOS ESCENARIOS
-ALQTBID12_75_VC = PARA RANGOS EN LOS ESCENARIOS     
-COD_SEC_MADRID = ES MI IDENTIFICADOR UNIVERSAL


2. API: INE (API publica JSON): Muestra la capacidad de pago. Permite calcular el esfuerzo de alquiler
-El esfuerzo de un alquiler se calcula dividiendo el coste anual o mensual del arrendamiento entre la renta neta disponible, multiplicando el resultado por 100, para sacar un porcentaje. este porcentaje si es < 30% : esfuerzo saludable ; 30%< esfuerzo <40% : esfuerzo moderado; >40% : sobreesfuerzo crito o riesgo financiero elevado.

-renta neta media por hogar
-renta neta media por persona

ESTE URL  ES LA RENTA POR distrito, hay que filtrar 2015-2022
https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=846:

aqui estan por seccion censal por año, hay que filtrar

url2015: 'https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20150101:20150101'
url2016: 'https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20160101:20160101'
url2017: 'https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20170101:20170101'
url2018: 'https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20180101:20180101'
url2019: 'https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20190101:20190101'
url2020: 'https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20200101:20200101'
url2021: 'https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20210101:20210101'
url2022: 'https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20220101:20220101'

Cómo leer estos nombres:
CPRO, LITPRO: código y nombre de provincia.
CUMUN, LITMUN: código y nombre de municipio (Madrid es 28079)
CUSEC: código de la sección censal. Tiene 10 dígitos: 5 del municipio + 2 del distrito + 3 de la sección.
El resto: un indicador + un año al final. 
Por ejemplo, ALQM2_LV_M_VC_24 sería alquiler en €/m² al mes (ALQM2)mediana (M; 25 y 75 son los percentiles), vivienda colectiva (VC; VU es unifamiliar) y año 2024 (_24)

3. ARCHIVO CSV :INE, indicadores demograficos del Atlas
Estructura de  edad, tamaño de hogares, poblacion.
-Estos datos nos muestran la demanda potencial, Identifica zonas con poblacion joven y hogares pequeños, tipicos del alquiler

el 18-64 mide población en edad de trabajar, no población joven, y los nulos (2,2% en renta y demografía, 1,4% en SERPAVI) se dejan sin imputar.

"AQUI DESARROLLAR MIS CRITERIOS DEL LIMPIEZA"
..................................
..................................
..................................
..................................
..................................
..................................

4. SI ES QUE TENGO TIEMPO......
ARCHIVOS SHAPEFILE DE SECCIONES CENSALES
ME APORTA DE MANERA GRAFICA(MAPAS) LIMITES GEOGRAFICOS



ME FALTA HACER MAS EL README








