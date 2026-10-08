USE radar_madrid_alquileres;

-- 1. Crecimiento anual compuesto del alquiler

SELECT alquiler_2015.cod_sec,
  ROUND((POWER(alquiler_2019.eur_m2_media / alquiler_2015.eur_m2_media, 1/4) - 1)*100, 2) AS crecimiento_anual_2015_2019_pct,
  ROUND((POWER(alquiler_2022.eur_m2_media / alquiler_2019.eur_m2_media, 1/3) - 1)*100, 2) AS crecimiento_anual_2019_2022_pct,
  ROUND((POWER(alquiler_2022.eur_m2_media / alquiler_2015.eur_m2_media, 1/7) - 1)*100, 2) AS crecimiento_anual_2015_2022_pct,
  ROUND(alquiler_2015.eur_m2_media, 2) AS alquiler_mediano_eur_m2_2015,
  ROUND(alquiler_2022.eur_m2_media, 2) AS alquiler_mediano_eur_m2_2022
FROM alquiler AS alquiler_2015
JOIN alquiler AS alquiler_2019 ON alquiler_2019.cod_sec = alquiler_2015.cod_sec AND alquiler_2019.año = 2019
JOIN alquiler AS alquiler_2022 ON alquiler_2022.cod_sec = alquiler_2015.cod_sec AND alquiler_2022.año = 2022
WHERE alquiler_2015.año = 2015
  AND alquiler_2015.eur_m2_media IS NOT NULL
  AND alquiler_2019.eur_m2_media IS NOT NULL
  AND alquiler_2022.eur_m2_media IS NOT NULL
   LIMIT 1000000;

-- 2a. Dispersion del alquiler(2022)

SELECT cod_sec,
  ROUND((eur_m2_p75 - eur_m2_p25) / eur_m2_media * 100, 1) AS dispersion_alquiler_2022_pct
FROM alquiler
WHERE año = 2022 AND eur_m2_media IS NOT NULL
 LIMIT 1000000;

-- 2b. Variación dentro de cada distrito(2022)
SELECT secciones.cod_dis,
  COUNT(*) AS n_secciones,
  ROUND(MIN(alquiler.eur_m2_media), 2) AS alquiler_minimo_eur_m2,
  ROUND(AVG(alquiler.eur_m2_media), 2) AS alquiler_promedio_eur_m2,
  ROUND(MAX(alquiler.eur_m2_media), 2) AS alquiler_maximo_eur_m2,
  ROUND(MAX(alquiler.eur_m2_media) - MIN(alquiler.eur_m2_media), 2) AS rango_alquiler_eur_m2
FROM alquiler
JOIN secciones ON secciones.cod_sec = alquiler.cod_sec
WHERE alquiler.año = 2022 AND alquiler.eur_m2_media IS NOT NULL
GROUP BY secciones.cod_dis
ORDER BY rango_alquiler_eur_m2 DESC
 LIMIT 1000000;

-- 3.Esfuerzo de alquiler(2022)

SELECT alquiler.cod_sec, secciones.cod_dis,
  ROUND(alquiler.alq_inmueble_media * 12 / renta_seccion.renta_hogar * 100, 1) AS esfuerzo_alquiler_2022_pct,
  alquiler.n_alquileres
FROM alquiler
JOIN renta_seccion ON renta_seccion.cod_sec = alquiler.cod_sec AND renta_seccion.año = alquiler.año
JOIN secciones ON secciones.cod_sec = alquiler.cod_sec
WHERE alquiler.año = 2022
  AND alquiler.alq_inmueble_media IS NOT NULL
  AND renta_seccion.renta_hogar IS NOT NULL
   LIMIT 1000000;


-- 4 Brecha de crecimiento (alquiler menos renta, 2015-2022)

SELECT alquiler_2015.cod_sec, secciones.cod_dis,
  ROUND((POWER(alquiler_2022.alq_inmueble_media / alquiler_2015.alq_inmueble_media, 1/7) - 1) * 100, 2) AS crecimiento_anual_alquiler_2015_2022_pct,
  ROUND((POWER(renta_2022.renta_hogar / renta_2015.renta_hogar, 1/7) - 1) * 100, 2) AS crecimiento_anual_renta_2015_2022_pct,
  ROUND(((POWER(alquiler_2022.alq_inmueble_media / alquiler_2015.alq_inmueble_media, 1/7) - 1)
       - (POWER(renta_2022.renta_hogar / renta_2015.renta_hogar, 1/7) - 1)) * 100, 2) AS brecha_crecimiento_pct
FROM alquiler AS alquiler_2015
JOIN alquiler AS alquiler_2022 ON alquiler_2022.cod_sec = alquiler_2015.cod_sec AND alquiler_2022.año = 2022
JOIN renta_seccion AS renta_2015 ON renta_2015.cod_sec = alquiler_2015.cod_sec AND renta_2015.año = 2015
JOIN renta_seccion AS renta_2022 ON renta_2022.cod_sec = alquiler_2015.cod_sec AND renta_2022.año = 2022
JOIN secciones ON secciones.cod_sec = alquiler_2015.cod_sec
WHERE alquiler_2015.año = 2015
  AND alquiler_2015.alq_inmueble_media IS NOT NULL AND alquiler_2022.alq_inmueble_media IS NOT NULL
  AND renta_2015.renta_hogar IS NOT NULL AND renta_2022.renta_hogar IS NOT NULL
   LIMIT 1000000;


-- 5 Perfil de demanda cruzado con el alquiler 2022

SELECT demografia.cod_sec, secciones.cod_dis,
  ROUND(demografia.edad_media, 1) AS edad_media,
  ROUND(demografia.tam_hogar, 1) AS tam_hogar,
  ROUND(demografia.pct_unipersonal, 1) AS pct_unipersonal,
  ROUND(demografia.pct_65mas, 1) AS pct_65mas,
  demografia.poblacion,
  ROUND(alquiler.eur_m2_media, 2) AS eur_m2_media,
  alquiler.n_alquileres
FROM demografia
JOIN secciones ON secciones.cod_sec = demografia.cod_sec
LEFT JOIN alquiler ON alquiler.cod_sec = demografia.cod_sec AND alquiler.año = demografia.año
WHERE demografia.año = 2022
 LIMIT 1000000;

-- 6 Serie anual por distrito (2015-2024)

SELECT secciones.cod_dis, alquiler.año,
  ROUND(SUM(alquiler.eur_m2_media * alquiler.n_alquileres) / SUM(alquiler.n_alquileres), 2) AS alquiler_ponderado_eur_m2
FROM alquiler
JOIN secciones ON secciones.cod_sec = alquiler.cod_sec
WHERE alquiler.eur_m2_media IS NOT NULL AND alquiler.n_alquileres IS NOT NULL
GROUP BY secciones.cod_dis, alquiler.año
ORDER BY secciones.cod_dis, alquiler.año
 LIMIT 1000000;








