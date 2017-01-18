---
layout: page
title: Skanska CARTO Training
category: introductory
date: 2017-01-19
author: 'Daniel M. Sheehan'
length: 4
---

---

<a href="http://www.carto.com/" target='_blank'><center><img src="https://github.com/CartoDB/training/raw/gh-pages/img/170119-skanska-training/logo_CARTO_positive_90.png" ></center></a>

---

* Instructor: Daniel M. Sheehan · danny@carto.com · [@nygeog](http://twitter.com/nygeog)
* January 19th, 2017
* Short url: [http://bit.ly/2ioUffA](http://bit.ly/2ioUffA)
* Full url: [http://cartodb.github.io/training/introductory/skanska-training.html](http://cartodb.github.io/training/introductory/skanska-training.html)
* Full CARTO training materials: [https://github.com/CartoDB/carto-workshop](https://github.com/CartoDB/carto-workshop)

---

<a href="http://www.usa.skanska.com/" target='_blank'><center><img src="http://group.skanska.com/4ae3e3/globalassets/skanskalogo.png"></center></a>

---

#### About Skanska
Skanska is one of the world's leading construction groups. In the U.S., we are a provider of comprehensive construction services and a developer of public-private partnerships. We apply our expertise to everything from small renovations to billion-dollar projects, using a variety of delivery methods.

---

#### Data: 
[http://www.usa.skanska.com/About-Skanska/Our-geographic-markets/](http://www.usa.skanska.com/About-Skanska/Our-geographic-markets/)

#### Style:

Hex color: `#263F6C` _note may not be official hex value_

---

![builder](../img/161105-geoinq-builder/builder.png)
<figcaption>Introduction to CARTO BUILDER</figcaption>

<br>


#### Map Academy, tutorials and other online resources

* [**Map Academy** courses](https://academy.cartodb.com/).
* [**Tutorials**](https://docs.cartodb.com/tutorials/).
* [Other online resources](https://github.com/ramiroaznar/intro-cartodb).

#### Further questions and troubleshooting

* Email to **support@carto.com**.
* Some questions could be already anwered at **[GIS Stack Exchange](http://gis.stackexchange.com/questions/tagged/carto)** `cartodb` tag.

## Contents
* [Making a Skanska Markets Map](#skanska_markets_map)
* [Making a Second Ave Subway Map](#second_ave_subway)

## Skanksa Markets Map
<a name="skanska_markets_map"></a>

Completed Map: [https://team.carto.com/u/sheehan-carto/builder/e72b9e4a-d9b0-11e6-9745-0e05a8b3e3d7/](https://team.carto.com/u/sheehan-carto/builder/e72b9e4a-d9b0-11e6-9745-0e05a8b3e3d7/)

* Setting up an html link to the market website in the **infoWindow**

	<a href="{{website}}" target='_blank'>{{market}} website</a>


## Second Avenue Subway Map
<a name="second_ave_subway"></a>

---
# Below is from other training

## Contents
- [Importing datasets](#import)
- [Getting your data ready](#dataset)
- [Making a map](#map)

----

## 1. Importing datasets <a name="import"></a>

### 1.1 Supported Geospatial Data Files

CartoDB supports the following geospatial data formats to upload vector data*:

* **`Shapefile`**
* **`KML`**
* **`KMZ`**
* **`GeoJSON`***
* **`CSV`**
* **`Spreadsheets`**
* **`GPX`**
* **`OSM`**

Importing **different geometry types** in the same layer or in a FeatureCollection element (GeoJSON) is not supported. More detailed information [here](http://docs.cartodb.com/cartodb-platform/import-api/geospatial-data-formats/#supported-geospatial-data-formats).

[*] More detailed information about GeoJSON format [here](http://geojson.org/geojson-spec.html), [here](http://geojsonlint.com/) and [here](http://geojson.io/#map=2/20.0/0.0).

### 1.2 Common importing errors

* **Dataset too large**:
  * File size limit: 150 Mb (free).
  * Import row limit: 500,000 rows (free).
  * *Solution*: split your dataset into smaller ones, import them into CartoDB and merge them.
* **Malformed CSV**:
  * *Solution*: check termination lines, header...
* **Encoding**:
  * *Solution*: `Save with Encoding` > `UTF-8 with BOM` in [Sublime Text](https://www.sublimetext.com/), any other decent text editor or [iconv](https://en.wikipedia.org/wiki/Iconv).
* **Shapefile missing files**:
  * Missing any of the following files within the compressed file will produce an importing error:
    * `.shp`: contains the geometry. REQUIRED.
    * `.shx`: contains the shape index. REQUIRED.
    * `.prj`: contains the projection. REQUIRED.
    * `.dbf`: contains the attributes. REQUIRED.
  * Other auxiliary files such as `.sbn`, `.sbx` or `.shp.xml` are not REQUIRED.
  * *Solution*: make sure to add all required files.
* **Duplicated id fields**:
  * *Solution*: check your dataset, remove or rename fields containing the `id` keyword.
* **Format not supported**:
  * URLs -that are not points to a file- are not supported by CartoDB.
  * *Solution*: check for missing url parameters or download the file into your local machine, import it into CartoDB.
* **Non supported SRID**:
  * Solution: try to reproject your resources locally to a well known projection like `EPSG:4326`,`EPSG:3857`,`EPSG:25830` and so on.

Other importing errors and their codes can be found [here](http://docs.cartodb.com/cartodb-platform/import-api/import-errors/).

----

## 2. Getting your data ready <a name="dataset"></a>

### 2.1 Geocoding

If you have a column with longitude coordinates and another with latitude coordinates, CartoDB will automatically detect and covert values into `the_geom`. If this is not the case, CartoDB can help you by turning the named places into best guess of latitude-longitude coordinates:

* **By Lon/Lat Columns**.
* **By City Names**.
* **By Admin. Regions**.
* **By Postal Codes**.
* **By IP Addresses**.
* **By Street Addresses**.

Know more about geocoding in CartoDB [here](http://docs.cartodb.com/tutorials/how_to_georeference/).

### 2.2 Datasets

These are the datasets we are going to use on our workshop. You'll find them all on our [Data Library](https://cartodb.com/data-library):

* **Populated Places** [`ne_10m_populated_places_simple`]: City and town points.
* **World Borders** [`world_borders`]: World countries borders.



----



