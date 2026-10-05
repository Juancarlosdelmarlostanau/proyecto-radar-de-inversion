RADAR DE INVERSION RESIDENCIAL POR DISTRITO EN MADRID CAPITAL
SE QUIERE INVERTIR en vivienda en madrid, ¿ en que distritos y porque?


SE DESCARGO LOS DATOS DE:
xslx de 'Sistema estatal de referencia del precio del alquiler de vivienda' (SERPAVI)
- BD Sistema Estatal Índices de Alquiler de Vivienda (Xlsx. 67.8Mb)
https://www.mivau.gob.es/vivienda/alquila-bien-es-tu-derecho/serpavi

Las siguientes medidas son para el subconjunto de estudio del alquiler: bienes inmuebles con ingresos por arrendamiento para vivienda habitual (excluidos arrendamientoa a parientes).
--> La denominación del campo se marca al final con "_AA" para señalar el año
Nota: Este archivo 2026-03_09_bd_SERPAVI_2011-2024 - DEFINITIVO WEB_v2.xlsx únicamente incluye la corrección en la fecha de referencia del seccionado censal del INE utilizado (2021) en esta hoja de Metadatos (08/07/2026).

Cómo leer estos nombres:
CPRO, LITPRO: código y nombre de provincia.
CUMUN, LITMUN: código y nombre de municipio (Madrid es 28079)
CUSEC: código de la sección censal. Tiene 10 dígitos: 5 del municipio + 2 del distrito + 3 de la sección.
El resto: un indicador + un año al final. Por ejemplo, ALQM2_LV_M_VC_24 sería alquiler en €/m² al mes (ALQM2), mediana (M; 25 y 75 son los percentiles), vivienda colectiva (VC; VU es unifamiliar) y año 2024 (_24). Es una lectura probable por el patrón, confírmala en la hoja "Metadatos", que debe traer el diccionario.
BI_ALVHEPCO_TVC_11 parece un conteo de contratos (muestra), pero no lo doy por hecho: búscalo en Metadatos, porque lo necesitamos para saber qué secciones tienen datos fiables.




informacion grafica:
-Secciones censales (enlace a un fichero zip)
-son archivos .shape


API:
INE (API publica JSON: renta, poblacion, indice de precios de vivienda)
-renta neta media por hogar, representa el poder adquisitivo real

aqui esta por distrito, hay que filtrar 2015-2022
https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=846:

aqui estan por seccion censal por año, hay que filtrar

url2015: https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20150101:20150101
url2016: https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20160101:20160101
url2017: https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20170101:20170101
url2018: https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20180101:20180101
url2019: https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20190101:20190101
url2020: https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20200101:20200101
url2021: https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20210101:20210101
url2022: https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=847:&date=20220101:20220101