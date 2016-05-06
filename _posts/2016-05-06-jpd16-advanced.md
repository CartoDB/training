---
layout: page
title: Advanced CartoDB for Data Journalists
category: intermediate
date: 2016-05-06
author: 'Ernesto Martínez'
length: 1.5
---

* Speaker: Ernesto Martínez · ernesto@cartodb.com · [@ernesmb](http://twitter.com/ernesmb)
* May 6th 2016
* [JPD16](http://jpd16.okfn.es/)· IV Jornadas de Periodismo de Datos · Madrid

## [http://bit.ly/adv-cdb-jpd16](http://bit.ly/adv-cdb-jpd16)

## Contents
- [CartoDB as a platform](#platform)
- [PostGIS](#postgis)
- [cartodb.js](#js)

----

## CartoDB as a Platform <a name="platfom"></a>
* __SQL API__ allows to interact with CartoDB tables. Query and modify CartoDB tables
* __Import API__ allows to upload new data to CartoDB
* __Maps API__ allows to visualize the underlying data

----

>The CartoDB Editor **is a client** of the platform

----

## PostGIS <a name="postgis"></a>

### geometry vs. geography data types
  * __Geometry__ uses a cartesian plane to measure and store features. CRS units
    
    >- The basis for the PostGIS geometry type is a plane. 
    - The shortest path between two points on the plane is a straight line. 
    - That means calculations on geometries (areas, distances, lengths, intersections, etc) can be calculated using cartesian mathematics and straight line vectors.

  * __Geography__ uses a sphere to measure and store features. Geographical coordinates
    
    >- The basis for the PostGIS geographic type is a sphere. 
    - The shortest path between two points on the sphere is a great circle arc. 
    - That means that calculations on geographies (areas, distances, lengths, intersections, etc) must be calculated on the sphere, using more complicated mathematics. For more accurate measurements, the calculations must take the actual spheroidal shape of the world into account, and the mathematics becomes very complicated indeed.
  
  ![cart vs sph](http://workshops.boundlessgeo.com/postgis-intro/_images/cartesian_spherical.jpg)

  ![LA-CDG](http://workshops.boundlessgeo.com/postgis-intro/_images/lax_cdg.jpg)

  *Source: [Boundless Postgis intro](http://workshops.boundlessgeo.com/postgis-intro)*

  * [Know more](http://workshops.boundlessgeo.com/postgis-intro/geography.html) about the Geography type
  * [Official PostGIS docs](http://postgis.net/docs/manual-1.5/ch04.html#PostGIS_Geography)

----

> CartoDB make maps using **SQL queries**, not tables!

----

### the_geom vs. the_geom_webmercator

CartoDB tables have **two** `geometry` fields:

  * __the_geom__ EPSG:4326
    - Geographical unprojected coordinates in __decimal degrees__ (Lon/Lat).
    - WGS84 Spheroid.

  * __the_geom_webmercator__ EPSG:3857
    - Spherical Mercator projected coordinates in __meters__. 
    - Widely accepted as a 'de facto' standard in webmapping. 

----

  > In CartoDB, __the_geom_webmercator__ column is the one we see represented in the map. We can use that column with any other CRS using `ST_Transform()` like in this [example](http://bl.ocks.org/ernesmb/eb484b19f26db188c371)

----

Some extra resources: 

* [Map Projections in Wikipedia](https://en.wikipedia.org/wiki/Map_projection)
* [Projections tutorial](http://docs.cartodb.com/tutorials/projections/)
* [Blog post](http://blog.cartodb.com/free-your-maps-web-mercator/) about using other projections in CartoDB

----

### PostGIS Spatial Analysis Queries
We are going to make use of the following datasets, available from CartoDB's Data Library: 

* [ne_50m_land](https://jpd16.cartodb.com/tables/ne_50m_land/public) - Emerged lands
* [ne_adm0_europe](https://jpd16.cartodb.com/tables/ne_adm0_europe/public) - European countries
* [ne_10m_populated_places_simple](https://jpd16.cartodb.com/tables/ne_10m_populated_places_simple) - Populated places in the world

----

>Check __[this visualization](http://cartodb.github.io/labs-cdbfiddle/#https://jpd16.cartodb.com/api/v2/viz/579f83ee-12a6-11e6-9a4a-0ea31932ec1d/viz.json)__ to see the result from each of the queries below

----

#### __ST_Buffer()__ creates a round area with a given radius

```sql
SELECT
  cartodb_id,
  name,
  ST_Transform(
    ST_Buffer(the_geom::geography, 100000)::geometry
    ,3857
  ) AS the_geom_webmercator
FROM
  ne_10m_populated_places_simple
WHERE
  adm0name LIKE 'Spain'  
```

* [ST_Transform](http://postgis.net/docs/ST_Transform.html)
* [ST_Buffer](http://postgis.net/docs/ST_Buffer.html)

#### __ST_Difference()__ calculates the difference between two geometries

```sql
SELECT
  a.cartodb_id,
    ST_Difference(
        a.the_geom_webmercator,
        b.the_geom_webmercator
  ) AS the_geom_webmercator
FROM
  ne_50m_land a,
  ne_adm0_europe b
WHERE
  b.adm0_a3 like 'ESP'
```

* [ST_Difference](http://postgis.net/docs/ST_Difference.html)

#### __ST_Intersects()__ returns `true` if the given two geometries intersects

```sql
SELECT
  a.*
FROM
  ne_10m_populated_places_simple a,
  ne_adm0_europe b
WHERE
  ST_Intersects(
    b.the_geom_webmercator,
    a.the_geom_webmercator
  )
```

* [ST_Intersects](http://postgis.net/docs/ST_Intersects.html)

#### Using __ST_Intersects()__ to get the number of points inside a polygon

Using `GROUP BY`:

```sql
SELECT
  b.cartodb_id,
  b.name,
  b.the_geom_webmercator,
  count(*) AS pp_count,
  sum(a.pop_max) as sum_pop
FROM
  ne_10m_populated_places_simple a,
  ne_adm0_europe b
WHERE
  ST_Intersects(a.the_geom, b.the_geom)
GROUP BY
  b.cartodb_id,
  b.name,
  b.the_geom_webmercator
```

Using `LATERAL`:

```sql
SELECT
  a.cartodb_id,
  a.name,
  a.the_geom_webmercator,
  counts.number_cities,
  to_char(counts.sum_pop,'999,999,999') as sum_pop --decimal separator
FROM
  ne_adm0_europe a
CROSS JOIN LATERAL
  (
    SELECT
      count(*) as number_cities,
      sum(pop_max) as sum_pop
    FROM
      ne_10m_populated_places_simple b
    WHERE
      ST_Intersects(a.the_geom, b.the_geom)
  ) AS counts
```

* [Lateral JOIN](http://blog.heapanalytics.com/postgresqls-powerful-new-join-type-lateral)

#### __ST_DWithin()__ to know wether a geometry is within the given range from another geometry

```sql
SELECT
  a.*
FROM
  ne_10m_populated_places_simple a,
  ne_10m_populated_places_simple b
WHERE
    a.cartodb_id != b.cartodb_id
  AND ST_DWithin(
      a.the_geom_webmercator,
      b.the_geom_webmercator,
      150000
    )
  AND a.adm0name = 'Spain'
  AND b.adm0name = 'Spain'
```

* [ST_DWithin](http://postgis.net/docs/ST_DWithin.html)

#### __ST_DWithin()__ + __ST_MakeLine()__ to connect nearby cities

```sql
SELECT
  ST_MakeLine(a.the_geom_webmercator, b.the_geom_webmercator) AS the_geom_webmercator
FROM
  ne_10m_populated_places_simple a,
  ne_10m_populated_places_simple b
WHERE
    a.cartodb_id != b.cartodb_id
  AND ST_DWithin(
      a.the_geom_webmercator,
      b.the_geom_webmercator,
      150000
    )
  AND a.adm0name = 'Spain'
  AND b.adm0name = 'Spain'
```

* [ST_MakeLine](http://postgis.net/docs/ST_MakeLine.html)

#### Generating Grids with CDB functions

Rectangular grid

```sql
SELECT
  row_number() over () as cartodb_id,
  CDB_RectangleGrid(
    ST_Buffer(the_geom_webmercator,125000),
  250000,
  250000
  ) AS the_geom_webmercator
FROM 
  ne_adm0_europe
WHERE 
  adm0_a3 IN ('ITA','GBR')
```

* [CDB_RectangleGrid](http://docs.cartodb.com/tips-and-tricks/cartodb-functions/#a-rectangle-grid)

Adaptative Hexagonal grid

```sql
WITH grid AS 
(SELECT
  row_number() over () as cartodb_id,
  CDB_HexagonGrid(
    ST_Buffer(the_geom_webmercator, 100000),
    100000
  ) AS the_geom_webmercator
FROM 
  ne_adm0_europe
WHERE 
  adm0_a3 IN ('ESP','ITA'))

SELECT 
  grid.the_geom_webmercator, 
  grid.cartodb_id
FROM
  grid, ne_adm0_europe a
WHERE 
    ST_intersects(grid.the_geom_webmercator, a.the_geom_webmercator)
  AND a.adm0_a3 IN ('ESP','ITA')
```

* [CDB_HexagonGrid](http://docs.cartodb.com/tips-and-tricks/cartodb-functions/#a-hexagon-grid)

#### Extra resources

* [CartoDB Map Academy - SQL and PostGIS](http://academy.cartodb.com/courses/sql-postgis/)

Some CartoDB blogposts about spatial SQL

* [Great arc lines crossing the 'Date Line'](http://blog.cartodb.com/jets-and-datelines/)
* [Looking for the closest geometries](http://blog.cartodb.com/lateral-joins/)
* [About ST_Subdivide](http://blog.cartodb.com/subdivide-all-things/)

----

## Webmaps with CartoDB.js <a name="js"></a>

[CartoDB.js](http://docs.cartodb.com/cartodb-platform/cartodb-js/) is the JavaScript library that allows to create webmapping apps using CartoDB services quickly and efficiently.

It's built upon the following components:

* [jQuery](http://jquery.com)
* [Underscore.js](http://underscorejs.org)
* [Backbone.js](http://backbonejs.org/)
* It can use either [Google Maps API](https://developers.google.com/maps/) or [Leaflet](http://leafletjs.com/)

### Examples

* Load a visualisation with `createVis()`: [example](http://bl.ocks.org/jsanz/78d004e805ea4dbf8397814edc477a89), [editor](http://plnkr.co/edit/plhwv3IQwFxLHBGWodQp?p=preview)

* Load SQL+CartoCSS with `createLayer`: [example](http://bl.ocks.org/jsanz/8ea2c5ef8422c9f9881e2f5132e2f645), [editor](http://plnkr.co/edit/aBFGbAGNwC51U3wOPd70?p=info)

* Events. Actions on feature click: [example](http://bl.ocks.org/jsanz/1881f68fd76546eda08cafd8fdcf480c), [editor](http://plnkr.co/edit/rLjESjaFzr4m9qrvl4pj?p=preview)

* Custom Infowindows: [example](http://bl.ocks.org/jsanz/a0f606c08ec854df3f5e982b3890e188), [editor](http://plnkr.co/edit/CQZL48I1QDfdMZUSH9ve?p=info)

* Custom Tooltip: [example](http://bl.ocks.org/jsanz/cd541c5a61f72e19c1e50c06fb688f40), [editor](http://plnkr.co/edit/3loqq6?p=preview)

* Changing SQL and CartoCSS: [example](http://bl.ocks.org/jsanz/b454ed94c8ab9131dc823166226c18ef), [editor](http://plnkr.co/edit/xqpP5J?p=preview)

* Use a slider to change SQL: [example](http://bl.ocks.org/jsanz/8e3195f2606a22fbfcdd0a117e109fb4), [editor](http://plnkr.co/edit/8HX6Yq?p=preview)

### Some advanced examples

* [Playing with Torque time](http://bl.ocks.org/ernesmb/4939b3751d3be0cdd64b)
* [Aggregating content from clustered features with SQL](http://bl.ocks.org/ernesmb/348b9eed9ee4c7038fd7)
* [Creating a simple layer selector](http://bl.ocks.org/jsanz/6a83dbae9d6e984ca938)
