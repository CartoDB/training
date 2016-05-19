---
layout: page
title: Introduction to Location Intelligence with CartoDB
category: intermediate
date: 2016-05-20
author: 'juanignaciosl@gmail.com'
length: 2
---

* Speaker: Juan Ignacio Sánchez Lara · juanignaciosl@cartodb.com · [@juanignaciosl](http://twitter.com/juanignaciosl)
* May 20th 2016
* [PC16](https://picniccode.es/)· Picnic Code · Valladolid

## [Introduction to Location Intelligence with CartoDB](https://www.gui.uva.es/taller-introduction-to-location-intelligence-with-cartodb/)

## Contents
- [CartoDB presentation](#platform)
- [Editor demo](#editor-demo)
- [PostgreSQL and PostGIS](#sql)
- [Full demo](#full-demo)

----

## CartoDB presentation <a name="presentation"></a>

TODO: link slides

----

## Editor demo<a name="editor-demo"></a>

* Register new account
* Import [Barrios de Valladolid](https://github.com/juanignaciosl/test-data-repository/blob/864b0ddfbd48f453ee9ce024691bf11b48d03dd8/Valladolid/barrios%20valladolid.zip?raw=true)
  * Display table data.
  * Show Pecan.
  * Edit title and annotations, and explain what it is.
  * Change basemap and explain the notion of layers.
  * Add options and try search.
  * Display changed map.
  * Use a filter.
* Import [twitter_t3chfest_reduced.csv](https://github.com/juanignaciosl/test-data-repository/blob/864b0ddfbd48f453ee9ce024691bf11b48d03dd8/twitter_t3chfest_reduced.csv?raw=true)
  * Create animated Torque map with Pecan.
  * Show new wizards.
  * Create new empty layer and geocode. Speak about Dropbox connector.
  * Edit CartoCSS.
  * Publish.

----

## PostgreSQL and PostGIS

TODO: link slides

* Go to table view and filter the query.

```sql
SELECT
  cartodb_id,
  ST_Transform(
    ST_Buffer(the_geom::geography, 100000)::geometry
    ,3857
  ) AS the_geom_webmercator
FROM
  twitter_t3chfest_reduced
```

```sql
SELECT
  ST_MakeLine(a.the_geom_webmercator, b.the_geom_webmercator) AS the_geom_webmercator
FROM
  twitter_t3chfest_reduced a,
  twitter_t3chfest_reduced b
WHERE
    a.cartodb_id != b.cartodb_id
  AND ST_DWithin(
      a.the_geom_webmercator,
      b.the_geom_webmercator,
      15000
    )
```

## Full demo<a name="full-demo"></a>

```sql
SELECT z.*, p.denominacion, replace(p._2015, '.', '')::integer as poblacion FROM zonasestadisticas z inner join  table_01012016pobla_zonasestadist_1986_2016_enero p on z.clave = p.clave where p.clave ~ '[0-9]*' and p._2015 is not null and p._2015 <> ''
```

Getting the stops per area.

```sql
SELECT
  p.cartodb_id,
  p.clave,
  count(*) AS p_count
FROM
  autobus_urbano_paradas a,
  poblacion_2015_zonas p
WHERE
  ST_Intersects(a.the_geom, p.the_geom)
GROUP BY
  p.cartodb_id,
  p.clave
```

Replace choropleth CSS:

```CSS
#poblacion_2015_zonas [ shape_area <= 51296277.9908] {
   polygon-fill: #8A4E8A;
}
#poblacion_2015_zonas [ shape_area <= 183623.9264] {
   polygon-fill: #A05AA0;
}
#poblacion_2015_zonas [ shape_area <= 65630.35375] {
   polygon-fill: #B379B3;
}
#poblacion_2015_zonas [ shape_area <= 42417.14795] {
   polygon-fill: #C08FC0;
}
#poblacion_2015_zonas [ shape_area <= 30620.58055] {
   polygon-fill: #CCA5CC;
}
#poblacion_2015_zonas [ shape_area <= 24426.18045] {
   polygon-fill: #D8BBD8;
}
#poblacion_2015_zonas [ shape_area <= 18082.63345] {
   polygon-fill: #F1E6F1;
}
```

with

```CSS
#poblacion_2015_zonas {
  polygon-fill: ramp([shape_area], 15000, 51296277);
}
```
