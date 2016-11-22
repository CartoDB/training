---
layout: page
title: QGIS to CARTO BUILDER
subtitle: "UPM"
category: intermediate
date: 2016-11-24
author: 'Ramiro Aznar'
length: 2h
---

---

* Trainers: Ramiro Aznar · ramiroaznar@carto.com · [@ramiroaznar](http://twitter.com/ramiroaznar)
* November 24th, 2016

## [http://bit.ly/161124-qgis-builder](http://bit.ly/161124-qgis-builder)

---

![builder](../img/161105-geoinq-builder/builder.png)
<figcaption>Introduction to CARTO BUILDER</figcaption>

<br>

## Introduction

### Prerequisites

* Laptop,
* A modern browser (Google Chrome would be perfect),
* QGIS installed.

### Resources

You can take a look on those resources if you want to warm up with CARTO:

* [**Learn** guides](https://carto.com/learn/guides).
* BUILDER [**Documentation**](https://carto.com/docs/carto-builder/) & [**FAQs**](https://carto.com/docs/carto-builder/faqs/).
* [`New Features` blog posts](https://carto.com/blog/categories/new-features).
* QGIS Plugin [website](https://plugins.qgis.org/plugins/QgisCartoDB/) & [repo](https://github.com/gkudos/qgis-cartodb).
* [Other online resources](https://github.com/ramiroaznar/intro-cartodb).

### Support

* Email to **support@carto.com**.
* Some questions could be already anwered at **[GIS Stack Exchange](http://gis.stackexchange.com/questions/tagged/carto)** `carto` tag.

### Contents

1. [QGIS to CARTO](#qgis)
* [Setting up](#setting-up)
* [QGIS Plugin installation](#install)
* [Connect your CARTO account to QGIS](#connect)
* [Import CARTO layers](#import)
* [Create a map](#map)

2. [Getting started with BUILDER](#builder)
* [Layers](#layers)
* [Styling](#styling)
* [Widgets](#widgets)
* [Analysis](#analysis)
* [Publish](#publish)

----

## 1. QGIS to CARTO <a name="qgis"></a>

### 1.1. Setting up <a name="setting-up"></a>

* The instructors will provide you a user and passwor to access your account
* Log into your `upm-cartoXX` account going to `https://carto.com/login`

<br>

### 1.2. QGIS Plugin installation <a name="install"></a>

* Open QGIS
* From the `Plugins` menu -> `Manage and Install Plugins`
* Type "CartoDB Plugin".
* Click `Install Plugin`.

<br>

### 1.3. Connect your CARTO account to QGIS <a name="connect"></a>

* From the CartoDB toolbox (located on the QGIS Web Toolbar) or from the Layers Toolbar in QGIS, Click `Add Connection`.
* Select `New` from the *Connection Manager*.
* Go back to CARTO dashboard. 
* Go to your account options (at the top right corner) and copy your API Key.

<br>

![apikey](../img/161124-qgis-builder/apikey.jpg)
<figcaption>CARTO API Key</figcaption>

<br>

* Enter your CARTO account settings: user name and API Key. 
* Click `Save`.

*Note: a more detailed guide can be found [here](https://github.com/gkudos/qgis-cartodb/wiki/Connect-your-CartoDB-Account-to-QGIS).

<br>

### 1.4. Import CARTO layers <a name="import"></a>

* Go back to CARTO dashboard.
* Click on `DATASETS` (at the top left corner).
* Click on `DATA LIBRARY` and search for "populated places" dataset.
* Select `ne_10m_populated_places_simple` and click on `CONNECT DATASET`.
* Go back to QGIS.
* From the CartoDB toolbox, click `Add CartoDB Layer`.
* Select `ne_10m_populated_places_simple` dataset from the list, or search for a table name to filter the list, and click `OK`.

<br>

![qgis](../img/161124-qgis-builder/qgis.png)
<figcaption>CARTO dataset in QGIS</figcaption>

<br>

*Note: a more detailed guide can be found [here](https://github.com/gkudos/qgis-cartodb/wiki/Add-CartoDB--layer-to-Qgis-Project).

<br>

### 1.5. Create a map <a name="map"></a>

* After working with QGIS, you can export your layers into CARTO or create a map.
* From the CartoDB toolbox, click `Create New Map`.
* Type the title and description for your map.
* Click on `Create`.
* Go back to CARTO dashboard.
* Click on `MAPS` (at the top left corner).
* Open the new map you have just created.

<br>

![qgis](../img/161124-qgis-builder/builder-map.png)
<figcaption>CARTO BUILDER main menu</figcaption>

<br>

*Note: a more detailed guide can be found [here](https://github.com/gkudos/qgis-cartodb/wiki/Publish-single-or-multilayer-visualizations#publish-map-on-cartodb).

<hr>

## 2. Getting started with BUILDER <a name="builder"></a>

### 2.1. Layers <a name="layers"></a>

* You can rename the title of this new layer as "Cities".
* Click on the layer to show its components: 
  * **`DATA`**
  * **`ANALYSIS`**
  * **`STYLE`**
  * **`POP-UP`**
  * **`LEGEND`**

<br>

### 2.2. Styling <a name="styling"></a>

* Create a bubble (proportional symbols) map:
  * Click on **`STYLE`**.
  * Click on point-size number.
  * Select **`BY VALUE`**.
  * Select `pop_max` column.

<br>

![dots](../img/161124-qgis-builder/dots.png)
<figcaption>A view of BUILDER bubble map</figcaption>

<br>

* Create a chroropleth map:
  * Click on `marker-fill` column.
  * Select **`BY VALUE`**.
  * Select `pop_max` column (a better cartographic practice would be selecting a normalized field).
  * You can customize your map further changing (and flipping) a different color palette, the number of buckets and quantification method.

<br>

![choropleth](../img/161124-qgis-builder/choropleth.png)
<figcaption>A view of BUILDER bubble & choropleth map</figcaption>

<br>

*To learn more about how this works behind the scenes check out the CartoCSS panel.

<hr>

<br>

### 2.3. Widgets <a name="widgets"></a>

* Set styles as default (orange dots).
* Go back to the main menu.
* Click on the layer.
* Add widgets to "Cities" layer:
  * Click on **`DATA`**.
  * Select `point count` in order to show the number of cities.
  * Select `name` in order to filter by city name.
  * Select `adm0name` in order to filter by country name.
  * Click on **`EDIT`** in order to customize these widgets.

<br>
![widgets](../img/161124-qgis-builder/widgets.png)
<figcaption>A view of BUILDER widgets</figcaption>
<br>

### 2.4. Analysis <a name="analysis"></a>

#### Centroids

* Go back to the main menu.
* Click on `LAYERS`.
* Click on `ADD ANALYSIS` below "Cities" layer.
* Select "Find centroid of geometries" analysis.
* Click on `ADD ANALYSIS`.
* Set paramaters as follows:
  * `CATEGORIZE...`: `adm0name`.
  * `WEIGHTED BY`: `pop_max`.
  * `AGGREGATE...`: `SUM(pop_max)`.

<br>
![centroids](../img/161124-qgis-builder/centroids.png)
<figcaption>A view of BUILDER centroid analysis</figcaption>
<br>

### Connect with lines

* Go back to the main menu.
* Drag and drop out the source layer node.
* Rename `A` node as "Centroids".
* Click on `ADD ANALYSIS` below "Cities" layer.
* Select "Connect with lines" analysis.
* Click on `ADD ANALYSIS`.
* Set paramaters as follows:
  * `TYPE`: `To Source`.
  * `TARGET`: `A1 Centroids`.
  * `CLOSEST`: `All to all`.
  * `GROUP BY`: 
    * `SOURCE COL.`: `adm0name`.
    * `TARGET COL.`: `category`.
* Click on `APPLY`.

<br>
![centroids](../img/161124-qgis-builder/lines.png)
<figcaption>A view of BUILDER connect with lines analysis</figcaption>
<br>

* Finally, edit centroid dots based upon `value` and lines based upon `pop_max`.

*Note: to learn more about connect with lines analysis have a look at this [guide](https://carto.com/learn/guides/analysis/connect-with-lines) and [blogpost](http://ramiroaznar.com/2016/11/12/builder-analysis-insights/).

<br>

### 2.5. Publish <a name="publish"></a>

* Click on **`SHARE`**.
* Set to `LINK` or `PUBLIC`.
* Click on **`PUBLISH`**.
* Now you can share the map as link or embed.

<br>

<iframe width="100%" height="520" frameborder="0" src="https://team.carto.com/u/ramirocartodb/builder/7ace46a2-b0c6-11e6-b13f-0ecd1babdde5/embed" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

<hr>

---
