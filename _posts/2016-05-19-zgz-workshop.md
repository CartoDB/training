---
layout: page
title: Intermediate CartoDB Workshop for MSc GIS & Remote Sensing
category: intermediate
date: 2016-05-10
author: 'Ramiro Aznar'
length: 2h
---

* Speaker: Ramiro Aznar · ramiroaznar@cartodb.com · [@ramiroaznar](http://twitter.com/ramiroaznar)
* May 19th 2016
* MSc GIS & Remote Sensing · Universidad de Zaragoza · Zaragoza

## [http://bit.ly/cdb-zgz-workshop](cdb-zgz-workshop)

## Contents
- [Importing datasets](#import)
- [Getting your data ready](#dataset)
- [Making a map](#map)
- [Going spatial with PostGIS](#postgis)
- [Webmapping apps with CartoDB.js](#cartodbjs)

----

# Intermediate CartoDB Workshop for MSc GIS & Remote Sensing

## 0. Before we start...

* __Import API__ allows to upload new data to CartoDB.
* __SQL API__ allows to interact with CartoDB tables. Query and modify CartoDB tables.
* __Maps API__ allows to visualize the underlying data.

----

>The CartoDB Editor **is a client** of the platform

----

## 1. Importing datasets <a name="import"></a>

### 1. 1. Supported Geospatial Data Files
CartoDB supports the following geospatial data formats to upload vector data*:

* **`Shapefile`**.
* **`KML`**.
* **`KMZ`**.
* **`GeoJSON`****. 
* **`CSV`**.
* **`Spreedsheets`**.
* **`GPX`**.
* **`OSM`**.

*Importing **different geometry types** in the same layer or in a FeatureCollection element (GeoJSON) is not supported. More detailed information [here](http://docs.cartodb.com/cartodb-platform/import-api/geospatial-data-formats/#supported-geospatial-data-formats).
**More detailed information about GeoJSON format [here](http://geojson.org/geojson-spec.html), [here](http://geojsonlint.com/) and [here](http://geojson.io/#map=2/20.0/0.0).

### 1. 2. Common importing errors
* **Dataset too large**:
	* File size limit: 150 Mb (free).
	* Import row limit: 500,000 rows (free).
	* *Solution*: split your dataset into smaller ones, import them into CartoDB and merge them.
<br/>
* **Malformed CSV**:
	* *Solution*: check termination lines, header...
<br/>
* **Encoding**:
	* *Solution*: `Save with Encoding` > `UTF-8 with BOM` in [Sublime Text](https://www.sublimetext.com/).
<br/>
* **Shapefile missing files**:
	* Missing any of the following files within the compressed file will produce an importing error:
		* `.shp`: contains the geometry. REQUIRED.
		* `.shx`: contains the shape index. REQUIRED.
		* `.prj`: contains the projection. REQUIRED.
		* `.dbf`: contains the attributes. REQUIRED.
	* Other auxiliary files such as `.sbn`, `.sbx` or `.shp.xml` are not REQUIRED.
	* *Solution*: make sure to add all required files.
<br/>
* **Duplicated id fields**:
	* *Solution*: check your dataset, remove or rename fields containing the `id` keyword.
<br/>
* **Format not supported**:
	* URLs -that are not points to a file- are not supported by CartoDB. 
	* *Solution*: check for missing url parameters or download the file into your local machine, import it into CartoDB.
<br/>
* **MAYUS extensions not supported**:
	* `example.CSV` is not supported by CartoDB.
	* *Solution*: rename the file.
<br/>

Other importing errors and their codes can be found [here](http://docs.cartodb.com/cartodb-platform/import-api/import-errors/). 

----

## 2. Getting your data ready <a name="dataset"></a>

### 2. 1. Geocoding

If you have a column with longitude coordinates and another with latitude coordinates, CartoDB will automatically detect and covert values into `the_geom`. If this is not the case, CartoDB can help you by turning the named places into best guess of latitude-longitude coordinates:

* **By Lon/Lat Columns**.
* **By City Names**.
* **By Admin. Regions**.
* **By Postal Codes**.
* **By IP Addresses**.
* **By Street Addresses**.

Know more about geocoding in CartoDB:

* In [**this tutorial**](http://docs.cartodb.com/tutorials/how_to_georeference/).
* In [**our Location Data Services website**](https://cartodb.com/location-data-services/geocoding/).
* In our [**documentation**](http://docs.cartodb.com/cartodb-platform/dataservices-api/geocoding-functions/).

### 2. 2. Datasets

* **Populated Places** [`ne_10m_populated_places_simple`]: City and town points.
* **World Borders** [`world_borders`]: World countries borders.
* **Land** [`ne_50m_land`]: World emerged lands.
* **European countries** [`ne_adm0_europe`]: European countries geometries.

### 2. 3. Selecting

* Selecting **all the columns**:

```sql
SELECT
  *
FROM
  ne_10m_populated_places_simple;
```

* Selecting **some columns**:

```sql
SELECT
  cartodb_id,
  name as city,
  adm1name as region,
  adm0name as country,
  pop_max,
  pop_min
FROM 
  ne_10m_populated_places_simple
```

* Selecting **distinc values**:

```sql
SELECT DISTINCT
  adm0name as country
FROM 
  ne_10m_populated_places_simple
```

### 2. 4. Filtering

![filtering](../img/160520-zgz/filtering.png)

* Filtering **numeric fields**:

```sql
SELECT 
  * 
FROM 
  ne_10m_populated_places_simple
WHERE
  pop_max > 5000000;
```

* Filtering **character fields**:

```sql
SELECT 
  *
FROM 
  ne_10m_populated_places_simple
WHERE 
  adm0name ilike 'spain'
```

* Filtering a **range**:

```sql
SELECT 
  *
FROM 
  ne_10m_populated_places_simple
WHERE 
  name in ('Madrid', 'Barcelona')
AND
  adm0name ilike 'spain'
```

* **Combining** character and numeric filters:

```sql
SELECT 
  *
FROM 
  ne_10m_populated_places_simple
WHERE 
  name in ('Madrid', 'Barcelona')
AND
  adm0name ilike 'spain'
AND
  pop_max > 5000000
```

### 2. 5. Others:

* Selecting **aggregated values**:

```sql
SELECT
  count(*) as total_rows
FROM 
  ne_10m_populated_places_simple
```

```sql
SELECT
  sum(pop_max) as total_pop_spain
FROM 
  ne_10m_populated_places_simple
WHERE 
  adm0name ilike 'spain'
```

```sql
SELECT 
  avg(pop_max) as avg_pop_spain
FROM 
  ne_10m_populated_places_simple
WHERE 
  adm0name ilike 'spain'
```

* **Ordering results**:

```sql
SELECT 
  cartodb_id,
  name as city,
  adm1name as region,
  adm0name as country,
  pop_max
FROM 
  ne_10m_populated_places_simple
WHERE 
  adm0name ilike 'spain'
ORDER BY
  pop_max DESC
```

* **Limiting results**:

```sql
SELECT 
  cartodb_id,
  name as city,
  adm1name as region,
  adm0name as country,
  pop_max
FROM 
  ne_10m_populated_places_simple
WHERE 
  adm0name ilike 'spain'
ORDER BY
  pop_max DESC LIMIT 10
```

----


## 3. Making a map <a name="map"></a>

### 3. 0. Before making maps...

----

> CartoDB make maps using **SQL queries**, not tables!

----

### 3. 1. Wizard

[Analyzing your dataset...](http://docs.cartodb.com/cartodb-editor/datasets/#analyzing-your-dataset) In some cases, when you connect a dataset and click on the MAP VIEW for the first time, the Analyzing dataset dialog appears. This analytical tool analyzes the data in each column, predicts how to visualize this data, and offers you snapshots of the visualized maps. You can select one of the possible map styles, or ignore the analyzing dataset suggestions.

* **Simple Map**.
* **Cluster Map**.
* **Category Map**.
* **Bubble Map**.
* **Torque Map**.
* **Heatmap Map**.
* **Torque Cat Map**.
* **Intensity Map**.
* **Density Map**.

* **Choropleth Map**:

Before making a choropleth map, we need to normalize our target column. So we are going to create two new columns with `numeric` as data type: `new_area` and `po_norm`. Finally, run the following SQL queries to update their values:

```sql
UPDATE
  world_borders
SET
  new_area = round(st_area(the_geom)::numeric, 6)
```

```sql
UPDATE
  world_borders
SET
  pop_norm = pop2005 / new_area
```

![choropleth](../img/160520-zgz/choropleth.png)

Know more about chosing the right map to make [here](http://academy.cartodb.com/courses/intermediate-design/which-kind-of-map-should-i-make/).

### 3. 2. Styles

* **Simple Map**:

```css
/** simple visualization */

#world_borders{
  polygon-fill: #FF6600;
  polygon-opacity: 0.7;
  line-color: #FFF;
  line-width: 0.5;
  line-opacity: 1;
}
```

* **Choropleth Map**:

```css
/** choropleth visualization */

#world_borders{
  polygon-fill: #FFFFB2;
  polygon-opacity: 0.8;
  line-color: #FFF;
  line-width: 0.5;
  line-opacity: 1;
}
#world_borders [ pop_norm <= 247992435.530086] {
   polygon-fill: #B10026;
}
#world_borders [ pop_norm <= 4086677.23673585] {
   polygon-fill: #E31A1C;
}
#world_borders [ pop_norm <= 1538732.3943662] {
   polygon-fill: #FC4E2A;
}
#world_borders [ pop_norm <= 923491.374542489] {
   polygon-fill: #FD8D3C;
}
#world_borders [ pop_norm <= 616975.331234902] {
   polygon-fill: #FEB24C;
}
#world_borders [ pop_norm <= 326396.192958792] {
   polygon-fill: #FED976;
}
#world_borders [ pop_norm <= 95044.5589361554] {
   polygon-fill: #FFFFB2;
}
```

* **Category Map**.
* **Bubble Map**.
* **Torque Map**.
* **Heatmap Map**.
* **Torque Cat Map**.
* **Intensity Map**.
* **Density Map**.

Know more about CartoCSS with our [documentation](http://docs.cartodb.com/cartodb-editor/datasets/#analyzing-your-dataset).

### 3. 3. Other elements

* **Basemaps**:

![basemap](../img/160520-zgz/basemap.png)

* **Options**:

![options](../img/160520-zgz/options.png)

* **Legend**:

![legend](../img/160520-zgz/legend.png)

```html
<div class='cartodb-legend choropleth'>	
<div class="legend-title">Total Population</div>
<ul>
	<li class="min">
		95044.56
	</li>
	<li class="max">
		247992435.53
	</li>
	<li class="graph count_441">
	<div class="colors">
	<div class="quartile" style="background-color:#FFFFB2"></div>
	<div class="quartile" style="background-color:#FED976"></div>
	<div class="quartile" style="background-color:#FEB24C"></div>
	<div class="quartile" style="background-color:#FD8D3C"></div>
	<div class="quartile" style="background-color:#FC4E2A"></div>
	<div class="quartile" style="background-color:#E31A1C"></div>
	<div class="quartile" style="background-color:#B10026"></div>
	</div>
	</li>
</ul>
</div>
```

* **Labels**:

![intensity](../img/160520-zgz/labels.png)

```css
#world_borders::labels {
  text-name: [name];
  text-face-name: 'DejaVu Sans Book';
  text-size: 10;
  text-label-position-tolerance: 10;
  text-fill: #000;
  text-halo-fill: #FFF;
  text-halo-radius: 1;
  text-dy: -10;
  text-allow-overlap: true;
  text-placement: point;
  text-placement-type: simple;
}
```

* **Infowindows and tooltip**:

![infowindows](../img/160520-zgz/infowindows.png)

```html
<div class="cartodb-popup v2">
  <a href="#close" class="cartodb-popup-close-button close">x</a>
  <div class="cartodb-popup-content-wrapper">
    <div class="cartodb-popup-content">
      <h4>country</h4>
      <p>{{name}}</p>
      <h4>population</h4>
      <p>{{pop_norm}}</p>
      <h4>area</h4>
      <p>{{new_area}}</p>
    </div>
  </div>
  <div class="cartodb-popup-tip-container"></div>
</div>
```

* **Title, text and images**:

![elements](../img/160520-zgz/elements.png)

### 3. 4. Share your map!

![share](../img/160520-zgz/share.png)

* **Get the link**: [https://team.cartodb.com/u/ramirocartodb/viz/0ba65c92-120b-11e6-9ab2-0e5db1731f59/public_map](https://team.cartodb.com/u/ramirocartodb/viz/0ba65c92-120b-11e6-9ab2-0e5db1731f59/public_map)

* **Embed it**: 

<iframe width="100%" height="520" frameborder="0" src="https://team.cartodb.com/u/ramirocartodb/viz/0ba65c92-120b-11e6-9ab2-0e5db1731f59/embed_map" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

* **CartoDB.js** [vizJSON file*]: https://team.cartodb.com/u/ramirocartodb/api/v2/viz/0ba65c92-120b-11e6-9ab2-0e5db1731f59/viz.json

*BONUS: **[JSONView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc)**, a Google Chrome extension and **[Pretty JSON](https://github.com/dzhibas/SublimePrettyJson)**, a Sublime Text plugin to visualize json files are good resources.

----

## 4. Going spatial with PostGIS <a name="postgis"></a>

### 4. 1. Working with projections

#### 4. 1. 1. `geometry` vs. `geography`
* **`Geometry`** uses a cartesian plane to measure and store features (CRS units):
 
    >The basis for the PostGIS `geometry` type is a plane. The shortest path between two points on the plane is a straight line. That means calculations on geometries (areas, distances, lengths, intersections, etc) can be calculated using cartesian mathematics and straight line vectors.

* **`Geography`** uses a sphere to measure and store features (Meters):
    
    >The basis for the PostGIS `geography` type is a sphere. The shortest path between two points on the sphere is a great circle arc. That means that calculations on geographies (areas, distances, lengths, intersections, etc) must be calculated on the sphere, using more complicated mathematics. For more accurate measurements, the calculations must take the actual spheroidal shape of the world into account, and the mathematics becomes very complicated indeed.

More about the `geography` type can be found [here](http://workshops.boundlessgeo.com/postgis-intro/geography.html) and [here](http://postgis.net/docs/manual-1.5/ch04.html#PostGIS_Geography).

![cart vs sph](http://workshops.boundlessgeo.com/postgis-intro/_images/cartesian_spherical.jpg)

#### 4. 1. 2. `the_geom` and `the_geom_webmercator`
* **`the_geom`** EPSG:4326. Unprojected coordinates in **decimal degrees** (Lon/Lat). WGS84 Spheroid.
* **`the_geom_webmercator`** EPSG:3857. UTM projected coordinates in **meters**. This is a conventional Coordinate Reference System, widely accepted as a 'de facto' standard in webmapping. 

In CartoDB, **the_geom_webmercator column is the one we see represented in the map**. Know more about projections:

* In [this tutorial](http://docs.cartodb.com/tutorials/projections/).
* [Map Projections in Wikipedia](https://en.wikipedia.org/wiki/Map_projection).
* In [this CartoDB blog post](http://blog.cartodb.com/free-your-maps-web-mercator/).

### 4. 2. Changing map projections

* Accessing the **list of default projections** available in CartoDB:

```sql
SELECT 
  * 
FROM 
  spatial_ref_sys
```

![srid](../img/160520-zgz/srid.png)

* Accessing the occult **the_geom_webmercator** field:

```sql
SELECT 
  the_geom_webmercator 
FROM 
  ne_50m_land
```

* **World Robinson** projection (ESPG:54030):

```sql
INSERT INTO spatial_ref_sys
  (srid, auth_name, auth_srid, proj4text, srtext) values (54030, 'EPSG', 54030,
'+proj=robin +datum=WGS84','PROJCS["World_Robinson",
    GEOGCS["GCS_WGS_1984",
        DATUM["WGS_1984",
            SPHEROID["WGS_1984",6378137,298.257223563]],
        PRIMEM["Greenwich",0],
        UNIT["Degree",0.017453292519943295]],
    PROJECTION["Robinson"],
    PARAMETER["False_Easting",0],
    PARAMETER["False_Northing",0],
    PARAMETER["Central_Meridian",0],
    UNIT["Meter",1],
    AUTHORITY["EPSG","54030"]]');
```

```sql
SELECT 
  cartodb_id, ST_Transform(the_geom, 54030) AS the_geom_webmercator
FROM 
  ne_50m_land
```

![robinson](../img/160520-zgz/robinson.png)

*About [`ST_Transform`](http://postgis.net/docs/ST_Transform.html).

### 4. 3. Geoprocessing

* Create a **buffer** from points:

```sql
SELECT
  cartodb_id,
  name,
  ST_Transform(
    ST_Buffer(the_geom::geography, 50000)::geometry
    ,3857
  ) AS the_geom_webmercator
FROM
  populated_places
WHERE
  name ilike 'madrid'
```

![buffer](../img/160520-zgz/buffer.png)

*About [`ST_Buffer`](http://postgis.net/docs/ST_Buffer.html).

* Get the **difference** between two geometries:

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

![difference](../img/160520-zgz/difference.png)

*About [`ST_Difference`](http://postgis.net/docs/ST_Difference.html).

* Know if tow geometries **intersect**:

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

![intersects](../img/160520-zgz/intersects.png)

*About [`ST_Intersects`](http://postgis.net/docs/ST_Intersects.html).

* Know wether a geometry is **within** the given range from another geometry:

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

![dwithin](../img/160520-zgz/dwithin.png)

*About [`ST_DWithin`](http://postgis.net/docs/ST_DWithin.html).

* Create a **straight line** between two points:

```sql
SELECT 
  ST_MakeLine(a.the_geom_webmercator,b.the_geom_webmercator) as the_geom_webmercator 
FROM (SELECT * FROM populated_places
    WHERE name ILIKE 'madrid') as a,
    (SELECT * FROM populated_places
    WHERE name ILIKE 'barcelona'AND adm0name ILIKE 'spain') as b
```

![lines](../img/160520-zgz/lines.png)

*About [`ST_MakeLine`](http://postgis.net/docs/ST_MakeLine.html).

* Create **great circles** between two points:

```sql
SELECT 
  ST_Transform(
  ST_Segmentize(
      ST_Makeline(
        a.the_geom, 
        b.the_geom
      )::geography, 
      100000
  )::geometry,
  3857
  ) as the_geom_webmercator
FROM 
  (SELECT * FROM populated_places
  WHERE name ILIKE 'madrid') as a,
  (SELECT * FROM populated_places
  WHERE name ILIKE 'new york') as b
```

![greatcircles](../img/160520-zgz/greatcircles.png)

*About [Great Circles](http://blog.cartodb.com/jets-and-datelines/).

----

## 5. Webmapping apps with CartoDB.js <a name="cartodbjs"></a>

### 5. 1. CartoDB.js
[CartoDB.js](http://docs.cartodb.com/cartodb-platform/cartodb-js/) is the JavaScript library that allows to create webmapping apps using CartoDB services quickly and efficiently. It's built upon the following components:

* [jQuery](http://jquery.com)
* [Underscore.js](http://underscorejs.org)
* [Backbone.js](http://backbonejs.org/)
* It can use either [Google Maps API](https://developers.google.com/maps/) or [Leaflet](http://leafletjs.com/)

Know more about CartoDB.js [here](http://docs.cartodb.com/cartodb-platform/cartodb-js/) and [here](http://academy.cartodb.com/courses/cartodbjs-ground-up/createvis-vs-createlayer/).

### 5. 2. Create Visualizations and Layers

#### 5. 2. 1. `createVis`

The most basic way to display your map from CartoDB.js involves a call to:

```javascript
cartodb.createVis(div_id, viz_json_url)
```

Couched between the `<script> ... </script>` tags, `createVis` puts a map and CartoDB data layers into the DOM element you specify. In the snippet below we assume that `<div id='map'></div>` placed earlier in an HTML file.

```javascript
window.onload = function() {
  var vizjson = 'link from share panel';
  cartodb.createVis('map', vizjson);
}
```

And that’s it! All you need is that snippet of code, a script block that sources CartoDB.js, and inclusion of the CartoDB.js CSS file. It’s really one of the easiest ways to create a custom map on your webpage. `createVis` also accepts options that you specifiy outside of the CartoDB Editor. They take the form of a [JS object](http://www.w3schools.com/js/js_objects.asp), and can be passed as a third optional argument.

```javascript
var options = {
  center: [40.4000, -3.6833], // Madrid
  zoom: 7,
  scrollwheel: true
};

cartodb.createVis('map', vizjson, options);
```

#### 5. 2. 2. `createLayer`

If you want to exercise more control over the layers and base map, `createLayer` may be the best option for you. You specifiy the base map yourself and load the layer from one or multiple viz.json files. Unlike `createVis`, `createLayer` needs a map object, such as one created by Google Maps or Leaflet. This difference allows for more control of the basemap for the JavaScript/HTML you’re writing.

A basic [Leaflet map](http://leafletjs.com/reference.html#map-class) without your data can be created as follows:

```javascript
window.onload = function() {
  // Choose center and zoom level
  var options = {
    center: [41.8369, -87.6847], // Chicago
    zoom: 7
  }

  // Instantiate map on specified DOM element
  var map_object = new L.Map(dom_id, options);

  // Add a basemap to the map object just created
  L.tileLayer('http://tile.stamen.com/toner/{z}/{x}/{y}.png', {
    attribution: 'Stamen'
  }).addTo(map_object);
}
```

The map we just created doesn’t have any CartoDB data layers yet. If you’re just adding a single layer, you can put your data on top of the basemap from above. If you want to add more, you just repeat the process. We’ll be doing much more with this later. This is the basic snippet to put your data on top of the map you just created. Drop this in below the `L.tileLayer` section.

```javascript
var vizjson = 'link from share panel';
cartodb.createLayer(map_object, vizjson).addTo(map_object);
```

### 5. 3. UI Functions

#### 5. 3. 1. Tooltips

A tooltip is an infowindow that appears when you hover your mouse over a map feature with vis.addOverlay(options). A tooltip appears where the mouse cursor is located on the map.
 
To add a tooltip to a map you need to do two steps:
 
First, define tooltip variable:
  
```javascript
  var tooltip = layer.leafletMap.viz.addOverlay({
            type: 'tooltip',
            layer: layer,
            template: '<div class="cartodb-tooltip-content-wrapper"><p>{{name}}</p></div>', 
            width: 200,
            position: 'bottom|right',
            fields: [{ name: 'name' }]
  });
```
Second, add tooltip to the map:

```javascript
     $('body').append(tooltip.render().el);
```

#### 5. 3. 2. Infowindows

Infowindows provide additional interactivity for your published map, controlled by layer events. It enables interaction and overrides the layer interactivity. A pop-up information window appears when a viewer clicks on a map feature.
  
In order to add the CartoDB.js infowindow you need to add this line within your code:

```javascript
cdb.vis.Vis.addInfowindow(map_object, layer, ['fields']);
```

However, you can create custom infowindows with different tools (`Moustache.js`, HML or `underscore.js`). Whatever choice you use, you would need to create a template first and then add the infowindow with the template. Here we will see how to do it using `Moustache.js`.

[Mustache.js](http://mustache.github.io/) is a `logic-less` logic-template. That means that only tags you create templates that are replaced with a value or series of values, it works by expanding tags in a template using values provided in a hash or object.

Example: Custom infowindow template to display `cartodb_id`:
  
```html
  <script type="infowindow/html" id="infowindow_template">
    <div class="cartodb-popup v2">
  <a href="#close" class="cartodb-popup-close-button close">x</a>
  <div class="cartodb-popup-content-wrapper">
    <div class="cartodb-popup-content">
      <h4>ID</h4>
      <p>{% raw %}{{cartodb_id}}{% endraw %}</p>
    </div>
  </div>
  <div class="cartodb-popup-tip-container"></div>
</div>
</script>
```

Then you can apply the custom infowindow template to the map with:

```javascript
cdb.vis.Vis.addInfowindow(
          map, layer, [columnName],
          {
             infowindowTemplate: $('#infowindow_template').html()
          });
```

#### 5. 3. 3. Legends

In order to add legends with CartoDB.js you would need to define the elemenets and colors of the legend with HTML, then you could use the legend classes of CartoDB.js to create the legends.
  
There is two kind of legend classes:

First, ``cartodb-legend choropleth``, applied in Choropleth maps:

```HTML
<div class='cartodb-legend choropleth'>
    <div class="legend-title">Population</div>
      <ul>
      	<li class="min">
      		1256
      	</li>
      	<li class="max">
      		8300
      	</li>
      	<li class="graph count_441">
      	<div class="colors">
      	<div class="quartile" style="background-color:#FFFFB2"></div>
      	<div class="quartile" style="background-color:#FED976"></div>
      	<div class="quartile" style="background-color:#FEB24C"></div>
      	<div class="quartile" style="background-color:#FD8D3C"></div>
      	<div class="quartile" style="background-color:#FC4E2A"></div>
      	<div class="quartile" style="background-color:#E31A1C"></div>
      	<div class="quartile" style="background-color:#B10026"></div>
      	</div>
      	</li>
      </ul>
  </div>
```

Second, `cartodb-legend category`, applied in simple or category maps:
  	
```HTML
    <div class='cartodb-legend category'>
      <div class="legend-title" style="color:#284a59">Countries</div>
        <ul>
          <li><div class="bullet" style="background-color:#fbb4ae"></div>Spain</li>
          <li><div class="bullet" style="background-color:#ccebc5"></div>Portugal</li>
          <li><div class="bullet" style="background-color:#b3cde3"></div>France</li>    
        </ul>
      </div>
```

### 5. 4. Examples

* Load a visualisation with `createVis()`: [example](http://bl.ocks.org/ramiroaznar/084f63f4200406508467826522dba842), [editor](http://plnkr.co/edit/x6YvoL?p=preview).

* Load SQL+CartoCSS with `createLayer()`: [example](http://bl.ocks.org/jsanz/8ea2c5ef8422c9f9881e2f5132e2f645), [editor](http://plnkr.co/edit/aBFGbAGNwC51U3wOPd70?p=info).

* Add custom infowindow, infobox, tooltip & legend with with `createLayer()`: [example](http://bl.ocks.org/oriolbx/3950e1a9b458a9177f9c).

* Events. Actions on feature click: [example](http://bl.ocks.org/jsanz/1881f68fd76546eda08cafd8fdcf480c), [editor](http://plnkr.co/edit/rLjESjaFzr4m9qrvl4pj?p=preview).

----
