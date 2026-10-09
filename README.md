RADAR DE INVERSION RESIDENCIAL EN ALQUILER, MADRID

Análisis del mercado de alquiler residencial de Madrid a nivel de 'sección censal' (2015–2022, con serie de precios hasta 2024), con Python (limpieza y gráficas) y SQL / MySQL(métricas). Proyecto individual del bootcamp de Ironhack.

1. Pregunta de negocio e hipótesis

Un inversor o consultora inmobiliaria necesita saber ¿dónde sube el alquiler y dónde se vuelve difícil de pagar? (a esto se le llama "tensión").


2. HPOTESIS GENERAL: El alquiler crece más rápido que la renta de los hogares, pero la presión sobre las familias se concentra en zonas concretas y no en toda la ciudad. Por eso el análisis se hace por sección censal y no solo por distrito.

3. 6 PREGUNTAS DEL ANALISIS----------------------------------->|--------> METRICAS
    3.1. ¿Cuánto y dónde ha crecido el alquiler?  ------------>|Crecimiento anual compuesto (CAGR) 2015–2019, 2019–2022 y 2015–2022
    3.2. ¿Es homogéneo el mercado dentro de cada distrito?---->|Dispersión (P75 − P25) / mediana por sección; mínimo, máximo y rango por distrito
    3.3. ¿Cuánto pesa el alquiler en el bolsillo?------------->|Esfuerzo de alquiler = alquiler anual / renta neta del hogar (2022)
    3.4. ¿Crece el alquiler más rápido que la renta?---------->|Brecha de crecimiento = CAGR alquiler − CAGR renta (2015–2022)
    3.5. ¿Qué perfil de demanda se asocia a precios altos?---->|Cruce de demografía (hogares unipersonales, edad, tamaño del hogar, mayores de 65) con el alquiler 2022
    3.6. ¿Cómo ha evolucionado cada distrito?----------------->|Serie anual del alquiler ponderado por distrito, 2015–2024

4. RESULTADOS PRINCIPALES
    4.1. El alquiler mediano creció un **3,7 % anual** entre 2015 y 2022: 4,4 % en 2015–2019 y 2,7 % en 2019–2022. El precio de partida no predijo el crecimiento tota (r = −0,08).
    4.2.El alquiler creció **0,94 puntos al año por encima de la renta** (3,75 % frente a 2,81 %). La brecha es positiva en el 80 % de las secciones. Mayor brecha: Retiro (+1,41) y Salamanca (+1,35); Centro es el único distrito negativo.
    4.3. **Esfuerzo mediano de alquiler del 24 %** en 2022. El 38 % de las secciones supera el 25 % y solo el 3 % supera el 30 %. Usera, Centro y Puente de Vallecas pasan del 25 %.
    4.4.En **13 de 21 distritos** el rango interno de precios es mayor que la distancia entre el distrito más caro y el más barato: conviene analizar por sección.
    4.5. A más hogares unipersonales, alquiler más caro (**r = 0,62**). Con más del 45 % de unipersonales, el alquiler es un 51 % más caro que con menos del 25 %. Es correlación, no causalidad.
    4.6. Todos los distritos suben **2015: 7,4–12,9 €/m²; 2024: 10,4–18,6 €/m²**. Salamanca crece más **4,5 % anual** y Barajas, Villa de Vallecas y Hortaleza menos **3,4–3,5 %**.


5. DATOS
Clave de unión: código de sección de 10 dígitos (`28079` + distrito de 2 dígitos + sección de 3 dígitos) y código de distrito de 7 dígitos.
Se guardan siempre como 'texto' para no perder ceros iniciales.

**SERPAVI** ('Sistema estatal de referencia del precio del alquiler de vivienda') Ministerio de Vivienda
- Alquiler mediano y cuartiles (€/m² y por inmueble) y nº de alquileres por sección, 2015–2024
- BD Sistema Estatal Índices de Alquiler de Vivienda (Xlsx. 67.8Mb). se encuentra en la carpeta DATA/RAW
https://www.mivau.gob.es/vivienda/alquila-bien-es-tu-derecho/serpavi
- usando en las Métricas 1, 2, 3, 4, 5 y 6.

**INE, Atlas de Distribución de la Renta**
- Renta neta media del hogar y por persona, por sección y distrito, 2015–2022.
- usando en las Métricas 3 y 4 
- URL, renta para distritos por año en madird, (API)
https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/31097?tip=A&tv=846:
- URL, renta para seccion censal por año en madridd, (API)
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

**INE, indicadores demográficos**
- Edad media, tamaño del hogar, % unipersonales, % mayores de 65, población
- usando en las Métricas 5
- demografia.csv (37 Mb). se encuentra en la carpeta DATA/RAW


6. METODOLOGIA

    6.1.**Limpieza (Python / pandas)**: Unificación de códigos, tipos y nombres de columnas. 
    En la tabla demográfica se conservan solo las filas a nivel de sección: el archivo original mezclaba municipio, distrito y sección.
    6.2.**Carga a MySQL**: Base de datos `radar_madrid_alquileres` con claves primarias (`cod_sec`, `año`) y claves foráneas hacia `secciones` y `distritos`. Carga con pandas `to_sql` (SQLAlchemy y PyMySQL) en modo `append`.
    3. **Métricas en SQL.** Seis consultas en `metricas.sql`, exportadas a texto.
   

7. Decisiones y criterios

- Unidad base: la sección censal: (unas 2.400); el distrito (21) se usa para resumir. Con solo 21 distritos se perdía la variación interna.
- Estadísticos robustos:las comparaciones de crecimiento usan **medianas**; las medias por distrito se usan en las métricas 3, 4 y 5.
- Valores nulos sin imputar: entre el 1,4 % y el 2,2 % según la tabla. Se dejan como nulos y las métricas excluyen esas filas, por lo que el número de secciones varía: 2.357 (métrica 1), 2.420 (métrica 2), 2.396 (métricas 3 y 5) y 2.299 (métrica 4).
- Años de la tabla de renta recuperados: 876 registros sin año se asignaron por posición (`2015 + índice // 4986`), porque el archivo está ordenado por año.


8. Limitaciones

- **Tasas nominales**, sin deflactar con el IPC.(Se muestran los precios reales sin restarles el efecto de la inflacion)
- **Sin precios de compraventa**, por lo que no se calcula la rentabilidad bruta.
- **SERPAVI cubre solo vivienda colectiva** (no unifamiliar) y usa el **seccionado censal de 2021** para todos los años.
- **La renta es la de todos los hogares**, no solo la de los inquilinos. Como los inquilinos suelen ganar menos, el esfuerzo real es probablemente algo mayor.
- Las métricas de demanda son **correlaciones**, no causas: el centro concentra a la vez más hogares unipersonales y precios más altos.
- Los rangos mínimo y máximo por distrito dependen de una sola sección y son sensibles a valores atípicos.
- Se descartó el filtro de población de 18–64 años por cobertura insuficiente (solo 63 secciones con dato).


9. Próximos pasos
- Añadir precios de compraventa para calcular la rentabilidad bruta por sección.
- Deflactar con el IPC.
- Lograr obtener  los datos completos hasta el año 2025, asi poder REALIZAR UNA ESTIMACION AL AÑO 2027
- Extender el método a otras ciudades.


10. Cómo reproducirlo
- Descargar los datos originales de SERPAVI y del INE en `data/raw/`.
- Ejecutar los notebooks de limpieza para generar `data/clean/`.
- Crear la base `radar_madrid_alquileres` en MySQL y ejecutar el script de creación de tablas.
- Ejecutar `carga_sql.ipynb` (requiere `pandas`, `sqlalchemy`, `pymysql`).
- Ejecutar `sql/metricas.sql` en MySQL Workbench.
   
11. Autor

**JUAN CARLOS DEL MAR LOSTANAU** · Arquitecto con estudios en urbanismo · Bootcamp de Data Analytics, Ironhack