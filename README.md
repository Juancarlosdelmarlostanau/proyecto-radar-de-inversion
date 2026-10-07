TITULO DEL PROYECTO

Radar de inversion residencial  para alquileres en madrid : analisis por seccion censal(2015-2022) y tendencia a 2027

¿donde es mejor invertir en vivienda de alquiler en madrid? "generar un score de atractivo con datos abiertos y un aproyeccion a cinco años"

Pregunta: ¿dónde invertir en alquiler en Madrid?
Tres dimensiones: precio (métricas 1, 2 y 5), capacidad de pago (3 y 4) y demanda (6).
Filtro de calidad: la métrica 7.
Síntesis: el score (8) y la tendencia (9).

SE DESCARGO LOS DATOS DE:
1. xslx de 'Sistema estatal de referencia del precio del alquiler de vivienda' (SERPAVI)
- BD Sistema Estatal Índices de Alquiler de Vivienda (Xlsx. 67.8Mb)
https://www.mivau.gob.es/vivienda/alquila-bien-es-tu-derecho/serpavi

esta informacion muestra el precio y evolucion. Es el nucleo del proyecto : crecimiento y fiabilidad por seccion.

"AQUI DESARROLLAR MIS CRITERIOS DEL LIMPIEZA"
..................................
..................................
..................................
..................................
..................................
..................................

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


HIPOTESIS GENERAL
El atractivo de una zona para invertir en alquiler residencial, no depende solo de su nivel de precio, sino de la combinacion de:
 - crecimiento sostenido del alquiler
 - capacidad de pago de los hogares
 - demanda demografica

Hipótesis específicas
Las secciones con mayor alquiler por m² no son necesariamente las de mayor crecimiento entre 2015 y 2022.
El esfuerzo de alquiler (alquiler anual sobre renta) varía mucho entre secciones, incluso dentro de un mismo distrito.
Las secciones con más población joven y hogares pequeños presentan mayor nivel de alquiler.
Existen secciones con renta alta y esfuerzo moderado (más recorrido) y otras con renta baja y alquiler alto (tensionadas y con más riesgo).
El crecimiento del alquiler cambió de ritmo tras 2020, y ese cambio condiciona la proyección a 2027.
Preguntas de investigación

Sobre precio

¿Cuáles son las secciones y distritos con mayor y menor alquiler por m² en 2022?
¿Dónde creció más el alquiler entre 2015 y 2022, y dónde menos?
¿Cambió el ritmo de crecimiento antes y después de 2020?

Sobre capacidad de pago

¿Qué secciones tienen mayor y menor esfuerzo de alquiler en 2022?
¿Hay zonas donde el alquiler creció más rápido que la renta?

Sobre demanda

¿Dónde se concentra la población joven y los hogares pequeños?
¿Coincide esa demanda con las zonas de mayor alquiler?

Sobre inversión

¿Qué secciones combinan crecimiento, esfuerzo moderado y demanda alta?
¿Qué distritos concentran más secciones atractivas?
¿Cuán dispersos están los precios dentro de cada distrito (percentil 75 frente a 25)?

Sobre el futuro

Si continúa la tendencia, ¿cuál sería el alquiler por distrito en 2027 en un escenario prudente, central y optimista?
¿Qué tan cerca estuvo la proyección de lo realmente observado en 2023 y 2024?
¿Cambia el ranking de distritos atractivos al mirar hacia 2027?
Objetivos
General

Construir un score de atractivo para inversión en alquiler residencial por sección censal en Madrid (2015-2022), e incorporar una tendencia a 2027 por distrito validada con datos posteriores, para producir recomendaciones de inversión.

Específicos
Integrar las tres fuentes en una base de datos relacional con el código de sección como clave común.
Limpiar y validar los datos, documentando fiabilidad (número de contratos), secciones sin dato y problemas de coincidencia entre fuentes.
Calcular indicadores: alquiler por m², crecimiento (por periodos), esfuerzo de alquiler y perfil demográfico.
Construir un score normalizado con pesos justificados.
Visualizar los resultados en mapas por sección y gráficos de ranking por distrito.
Proyectar el alquiler por distrito a 2027 con tres escenarios.
Validar la proyección con el SERPAVI de 2023 y 2024 y reportar su error.
Formular conclusiones accionables: zonas prioritarias, zonas de riesgo y limitaciones.
Prioridad con el tiempo que tienes

Para que no se te complique el viernes, este es el orden de importancia:

Esencial: objetivos 1 a 5 y 8 (el score y las conclusiones).
Extra del jueves, solo si vas holgado: objetivos 6 y 7 (proyección y validación). Aportan mucho al portafolio, pero no deben poner en riesgo lo esencial.
Limitaciones a mencionar desde ya
Datos tributarios con desfase y sin precios de venta (no hay yield).
Seccionado de 2021 aplicado a toda la serie, así que el crecimiento histórico es aproximado.
Solo vivienda colectiva; algunas secciones sin dato.
La proyección parte de 8 años con una ruptura (COVID) y excluye cambios regulatorios o de mercado.
Análisis exploratorio con datos abiertos, no una valoración profesional.



