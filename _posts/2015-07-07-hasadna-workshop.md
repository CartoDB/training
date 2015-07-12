---
layout: page
title: Merging Data + Municipal Maps
subtitle: "Hasadna: Meetup at Google Campus"
category: intermediate
date: 2015-07-07
author: 'Aurelia Moser'
length: 2
---

# Hasadna: Pollution Mapping + CartoDB

Aurelia Moser, [CartoDB](http://cartodb.com)
Workshop - Hasadna, IL

**July 6, 2015**

Find this document here:

* Stackedit: <http://tinyurl.com/stack-IL>
* Gist: <http://tinyurl.com/gist-IL>

Find the code checkpoints here:

* Github: <https://github.com/auremoser/hasadna>

# Outline
0. Visualizing Data
1. Introduction to CartoDB
	+ Examples
	+ Tour of the interface
	+ APIs / JS Libs
2. Mapping **Basics**
	+ Setting up accounts!
  	+ Data import
	+ Datasets ([available here](https://github.com/auremoser/hasadna/tree/master/data))
3. Mapping **Data**
	+ Geocoding + SQL/PostGIS
	+ Merging Tables
	+ Customizing UI
4. Building a Map
    + Basics of `VisJson` ([ckpt-1](https://github.com/auremoser/hasadna/tree/master/1-visjson))
	+ Quick map with `CreateVis` ([ckpt-2](https://github.com/auremoser/hasadna/tree/master/2-createVis))
	+ Custom map with `CreateLayer` [(ckpt-3](https://github.com/auremoser/hasadna/tree/master/3-createLayer))
	+ Add SQL/CSS Templates ([ckpt-4](https://github.com/auremoser/hasadna/tree/master/4-sqlcss))
	+ Add Buttons ([ckpt-5](https://github.com/auremoser/hasadna/tree/master/5-buttons))
	+ Infowindows ([ckpt-6](https://github.com/auremoser/hasadna/tree/master/6-info))
  + **BONUS:** Charts ([ckpt-7](https://github.com/auremoser/uofm-2015/tree/master/ckpt-7-chart))
5. Building a Narrative
	+ Case Study: [Air Pollution Map](http://bl.ocks.org/auremoser/2b7f220807ca12d0ac89)
	+ Tell Time/Stories: Odyssey + Torque
	+ Graphs + Charts ([Air Pollution Chart](http://bl.ocks.org/auremoser/6c51769ef05b812690fc))
6. Wrap-Up and Resources


# Visualizing Data
![Types of Visualizations](https://raw.githubusercontent.com/auremoser/images/master/1-vis-types.png)

Source: [The Data Visualization Catalogue](http://www.datavizcatalogue.com/).

### Some samples:

![Time Travel Map](https://raw.githubusercontent.com/auremoser/hasadna/master/img/rainbow.jpg)

Source: [Time Travel Between Counties](http://mdweaver.github.io/times_year/), Carto.JS

![County Chart](https://raw.githubusercontent.com/auremoser/hasadna/master/img/chart.jpg)

Source: [Geogia County Car Crash Counts](http://bl.ocks.org/auremoser/6236a61e5383ab0bc71d), C3.JS

####Some software:

* [**CartoDB**](cartodb.com): light open source library and graphical user interface application for hosting and visualizing geospatial data
* [**ChartJS**](http://www.chartjs.org/): light library for creating charts and graphs

####Some resources:

* [Charting Tools Repository](https://github.com/auremoser/chart-tools)
* [Workshops @ CartoDB](http://cartodb.github.io/training/)
* [Recommended tools for Visualizations](http://selection.datavisualization.ch/)
* [Perception Concerns](https://github.com/tmcw/perception)
* [Gestalt Theory](http://emeeks.github.io/gestaltdataviz/section1.html)
* [Color Brewer](http://colorbrewer2.org/) or [Geocolor](http://geocolor.io/)

![Product](https://raw.githubusercontent.com/auremoser/hasadna/master/img/header.jpg)

## Why Maps?
![Michael's Syrian Refugee visualization](https://raw.githubusercontent.com/auremoser/images/master/syria.jpg)
[Map population by relative density](http://projects.aljazeera.com/2013/syrias-refugees/)

* Maps give you more context than most visualizations.
* They allow you to apply data to a recognizable topography.

# Intro to CartoDB
## Examples
+ [Alcatraz Escape Revisited](http://www.washingtonpost.com/news/morning-mix/wp/2014/12/15/the-alcatraz-escapees-could-have-survived-and-this-interactive-model-proves-it/)
+ [LA Sheriff Election Results](http://graphics.latimes.com/2014-la-sheriff-primary-map/)
+ [Starwars Galaxy Map](http://www.swgalaxymap.com/)
+ [Demonstrations in Brazil](http://blog.cartodb.com/mapping-the-world-ongoing-demonstrations-in-brazil/)
+ [Global Forest Watch](http://www.globalforestwatch.org/map/3/15.00/27.00/ALL/grayscale/loss,forestgain?begin=2001-01-01&end=2013-12-31&threshold=30)
+ [Urban Reviewer](http://www.urbanreviewer.org/#map=12/40.7400/-73.9998&sidebar=plans)

![urban-interface](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/urban.png)

![urban-reviewer](https://raw.githubusercontent.com/auremoser/nicar-test/master/img/urban_reviewer_code_example.png)

## Tour of the interface

![int-data](https://raw.githubusercontent.com/auremoser/nicar-test/master/img/int-data.jpg)
![int-upload](https://raw.githubusercontent.com/auremoser/nicar-test/master/img/int-upload.jpg)
![int-vis](https://raw.githubusercontent.com/auremoser/nicar-test/master/img/int-viz.jpg)
![int-share](https://raw.githubusercontent.com/auremoser/nicar-test/master/img/int-share.jpg)

## APIs / JS Libs
You can read more about the [CartoDB APIs and JS Library here](http://docs.cartodb.com/cartodb-platform.html)

* [CartoJS](http://docs.cartodb.com/cartodb-platform/cartodb-js.html) - JS library for interacting with CartoDB
* [Maps API](http://docs.cartodb.com/cartodb-platform/maps-api.html) - generate public/private maps with data hosted on your CDB account
* [SQL API](http://docs.cartodb.com/cartodb-platform/sql-api.html) - run sql in your code to dynamically filter/request/query your mapped data stored in CartoDB via http calls
* [Import API](http://docs.cartodb.com/cartodb-platform/import-api.html) - push data to your CartoDB Account

## Datasets
You can fork the dataset we'll be working with, and the files for the workshop [here](https://github.com/auremoser/hasadna/tree/master/data). Clone the repo to download.

* Municipality Data (for polygons)
* Pollution Data (for counts and numerical values)

We also have a "Data Library" full of datasets that you can mashup with your own data.

![DataLibrary](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/2-commondata.png)

# Mapping Data
## Getting Geospatial Data

**Geospatial data** is info that ids a geolocation and its characteristic features/frontiers, typically represented by points, lines, polygons, and/or complex geographic features.

### Issues:
+ Comes in multiple formats ([supported formats for CartoDB](http://docs.cartodb.com/cartodb-editor.html#supported-file-formats))
+ Sources uncertain
+ Contains errors
+ etc.

I based most of this demo on my assumptions, because I wanted to make a fast map, because the data didn't have headers, I guessed on which fields corresponded to the pollution counts for transport/electrical/industrial factors contributing to air quality.


## Geocoding + SQL/PostGIS
The most basic SQL statement is:

{% highlight sql %}
SELECT * FROM table_name
{% endhighlight %}

A more detailed query is like this:

{% highlight sql %}
SELECT
  name,
  height,
  age
FROM
  class_list
WHERE
  name = 'Aure'
  AND (
    height > 1.2
    OR
    height < 1.9
  )
{% endhighlight %}

1. `SELECT` is what you're requesting (required)
2. `FROM` is where the data is located (required)
3. `WHERE` is the filter on the data you're requesting (optional)
4. `GROUP BY` and `ORDER BY` are optional additions, you can read more about aggregate/other functions below.

There are two special columns in CartoDB:

1. `the_geom`
2. `the_geom_webmercator`

The first of these is in the units of standard latitude/longitude, while the second is a projection based on the [original Mercator projection](http://en.wikipedia.org/wiki/Mercator_projection) but [optimized for the web](http://en.wikipedia.org/wiki/Web_Mercator).

If you want to run SQL commands and see your map update, make sure to `SELECT` the `the_geom_webmercator` because this is the column that's used for mapping--the other is more of a convenience column since most datasets use lat/long.

You can also do cool things like re-set the projection in SQL. Say you load in your data and want to make sure it's in [ITM (Israeli Transverse Mercator)](http://tx.technion.ac.il/~zvikabh/software/ITM/) or another ESPG, you can do that on the fly.

{% highlight sql %}
SELECT cartodb_id, ST_Transform(the_geom_webmercator,2039) AS the_geom_webmercator FROM aureliamoser.municipalities
{% endhighlight %}

![ITM](https://raw.githubusercontent.com/auremoser/hasadna/master/img/is-proj.jpg)

"municipalities" is my table name, "aureliamoser" is my username I reset the data to the correct projection and can generate a table with it.

## Customizing UI

You have myriad customization options in the in-browser editor.

* `sql` - run sql and postgis functions across your data
* `wizard` - adjust the type, colors and fills in your map
* `infowindow` - create hovers, tooltips with information from your datatables
* `css` - customize the css and style of your map outside the wizard
* `legends` - create keys for your map
* `filters` - filter the data without sql

### Filters & SQL
![filters](https://raw.githubusercontent.com/ohasselblad/workshops/master/img/alaska/filters.png)

Filters are a great way to explore your data. Besides filtering your data, they allow you to see histograms of the distributions, the number of unique entries, or a search box for columns that have a large number of text entries.

### CartoDB Editor

![wizard](https://raw.githubusercontent.com/auremoser/hasadna/master/img/wizard.jpg)

The Editor allows you to select your visualization "type" and customize color palettes, design details, and otherwise set the tone for your map.

## Types of visualizations
+ **Simple** -- most basic visualization
+ **Cluster** -- counts number of points within a certain binned region
+ **Choropleth** -- makes a histogram of your data and gives bins different colors depending on the color ramp chosen
+ **Category** -- color data based on unique category (works best for a handful of unique types)
+ **Bubble** -- size markers based on column values
+ **Intensity** -- colors by density
+ **Density** -- data aggregated by number of points within a hexagon
+ **Torque** -- temporal visualization of data
+ **Heat** -- more fluid map of concentration; ephasis on far over near-view

![heat](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/2-heatmap.png)

Check out [visualization documentation](http://docs.cartodb.com/cartodb-editor.html#wizards) for more.

###_Simple_ Map
The visualization style _simple_ is the default visualization for all maps.

![Simple visualization](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/2-simple.png)

Styles available in the wizard

![Styling options](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/2-simple-wizard.png)

* **Marker Fill:** change the size, color, and opacity of all markers
* **Marker Stroke:** change the width, color, and opacity of every marker's border
* **Composite Operation:** change the color of markers when they overlap
* **Label Text:** Text appearing by a marker (can be from columns)

#### Infowindows/hovers
![Infowindow options](https://raw.githubusercontent.com/auremoser/hasadna/master/img/infowindow.jpg)

+ Select which column data appear in infowindow by toggling column on
+ Customize further by selecting HTML-view

#### Change basemap
Select basemaps from different providers, use custom color, NASA data, MapBox tiles, etc.

![Basemap options](https://raw.githubusercontent.com/ohasselblad/workshops/gh-pages/img/alaska/basemap_options.png)

### Choropleth
Choropleth maps show map elements colored according to where a value associated with the map element falls in a range. It's like a histogram where each bin is colored differently according to a color scale you pick.

**_Quantification_** is an option to pay attention to since it controls how the data is binned into different colors.

* **_Equal interval_** gives bins of equal size across the range,  which means that outliers stand out.

![Equal-Interval](https://raw.githubusercontent.com/auremoser/hasadna/master/img/eqinter.jpg)

* **_Quantile_** bins so that each quantile has approximately the same number of values. This is the default and works for most "normal" data.

![Quant](https://raw.githubusercontent.com/auremoser/hasadna/master/img/quant.jpg)

* **_Jenks_** aims to increase the standard deviation between each group of data while decreasing the standard deviation within each group. In other words, it increases the similarity within a given group in conjunction with the differences from each of the other groups. The Jenks method does this by shuffling data across each group until it detects an optimization.

![Jenks](https://raw.githubusercontent.com/auremoser/hasadna/master/img/jenks.jpg)

* **_Heads/Tails_** breaks can be powerful for data with a long-tail distribution.

![heads](https://raw.githubusercontent.com/auremoser/hasadna/master/img/ht.jpg)

Play around with them and see what works best for your dataset.

### CartoCSS basics
[CartoCSS](https://github.com/mapbox/carto/blob/master/docs/latest.md) is the styling language for our maps.

![CartoCSS screenshot](https://raw.githubusercontent.com/auremoser/hasadna/master/img/cartocss.jpg)

### Legends
...can be easily customized!

![Legend](https://raw.githubusercontent.com/auremoser/hasadna/master/img/legend.jpg)

You have the option of giving it a title, and changing the text for the colors. You can also change the colors manually, or, even better, change the color ramp back in the wizard.

### Navigation
Click on the 90-degree arrow to get back to view your tables/visualizations

![Go back to tables](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/nav.png)

![Navigation for tables](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/dataview.png)

![Navigation for maps](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/mapview.png)

## Merging Tables
Joining and merging tables to make one dataset is a common need. Say you have two datasets related to the same place/map and need to combine them so that they can share the same geometry.

You can do this in SQL [read more here](http://docs.cartodb.com/tutorials/merging_data.html), but CartoDB also has an in-editor button for that.

![mergeButton](https://raw.githubusercontent.com/auremoser/nicar-test/master/img/5-mergeButton.png)

Here is a usecase relative to these datasets:

* when you open the pollution data it has municipality names but geometry
* when you open the municipality data it has geometries and names but not pollution values
* you can load them both into cartodb, and select the "merge tables" button to join them on their mutual `name` column into one unified table
* select `column` or `spatial` join

![joins](https://raw.githubusercontent.com/auremoser/hasadna/master/img/merge-gui.jpg)

* select the columns that you want to join on, in this case, both datasets share a name

![merge](https://raw.githubusercontent.com/auremoser/hasadna/master/img/merge-temp.jpg)

* toggle the columns you want to exist in your new "joined" dataset

![mergGen](https://raw.githubusercontent.com/auremoser/hasadna/master/img/merge-table.jpg)

# Building a Map

Using the data above, you can load in two tables, merge them in the same visualization with the "merge button" or with SQL, and visualize them on the map with the GUI, or pull them into your own applications with the libraries and APIs.

Here's a few steps you can follow, the code it in github (clone and follow along or do go through the steps in your own account).

You will need:
+ datasets from above
+ visjson from your account, you can [reference mine](https://github.com/auremoser/hasadna/blob/master/1-visjson/vis.json) to find yours too.
+ Basic Text Editor
+ Browser

	+ Basics of `VisJson` ([ckpt-1](https://github.com/auremoser/hasadna/tree/master/1-visjson))
	+ Quick map with `CreateVis` ([ckpt-2](https://github.com/auremoser/hasadna/tree/master/2-createVis))
	+ Custom map with `CreateLayer` [(ckpt-3](https://github.com/auremoser/hasadna/tree/master/3-createLayer))
	+ Add SQL/CSS Templates ([ckpt-4](https://github.com/auremoser/hasadna/tree/master/4-sqlcss))
	+ Add Buttons ([ckpt-5](https://github.com/auremoser/hasadna/tree/master/5-buttons))
	+ Infowindows ([ckpt-6](https://github.com/auremoser/hasadna/tree/master/6-info))
  	+ **BONUS:** Charts ([ckpt-7](https://github.com/auremoser/uofm-2015/tree/master/ckpt-7-chart))

### VisJson

The viz.json file is the main source of data for CartoDB JavaScript functions (createVis and createLayer) for creating visualizations in the browser.

![visjson](https://raw.githubusercontent.com/auremoser/hasadna/master/img/1-visjson.jpg)

* Structure of file: JSON
* Defines how to access data: listing servers, subdomains, etc.
* Most important for developers is the `layers` array because it explicitly shows the structure of how visualizations are put together
    * Defines base maps, if applicable, as `layers[0]`
    * CartoDB data layer is `layers[1]`, may consist of multiple sublayers
        * Defines infowindows, which we'll cover in this workshop
        * Defines data accessed by using a SQL statement
        * Defines styling for tile layers, if applicable
        * Defines interactivity (what data shows up on layer events)
        * `layer_name` is the also the name of table where data comes from in the account with key `user_name`

You can view it by opening a text editor and loading the file, or downloading a JSON viewer extension for inbrowser views ([Chrome](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc?hl=en) or [Firefox](https://addons.mozilla.org/en-us/firefox/addon/jsonview/)).

### CreateVis

`createVis` is excellent for creating maps quickly with very little code. There is a lot of customization with it as well. The documentation is [here](http://docs.cartodb.com/cartodb-platform/cartodb-js.html#visualization).

#### Here's a reference point for this section [ckpt-2](https://github.com/auremoser/hasadna/tree/master/2-createVis)


### CreateLayer

`createLayer` is the other main method for bring maps to your browser. One big difference here is that we explicitly expose the SQL and CartoCSS, allowing for easy customization.

The following is the basic createLayer structure (depends on [Leaflet.js](http://leafletjs.com/)):

{% highlight js %}

window.onload = function() {
    var vizjson_url = 'https://team.cartodb.com/u/aureliamoser/api/v2/viz/f1af78c8-23c7-11e5-bff0-0e9d821ea90d/viz.json'; // <-- Paste viz.json URL between quotes

    var options = {
           sql: "SELECT * FROM pollutant_emissions_merge",
           // cartocss: ""
       }

       var sublayers = [];

       // instantiate map object from Leaflet
       var mapObj = new L.Map(map, {  // <-- Replace map_id with your #id for rendering
           center: [31.5000, 34.9000], // Telaviv, IL
           zoom: 8 // zoom projection to adjust starting point zoom
       });


       // add basemap tiles
       L.tileLayer('http://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png', {
           attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
       }).addTo(mapObj);

       // add data tile layers here (if you have multiple layers, you can manipulate them in js here)
       cartodb.createLayer(mapObj,vizjson_url)
           .addTo(mapObj)
           .done(function(layer) {
               console.log("Map successfully created.");
               sublayers[0] = layer.getSubLayer(0);
               sublayers[1] = layer.getSubLayer(1);
               sublayers[1].set(options); // altering the SQL and CartoCSS; see above
               sublayers[1].hide(); // hiding the municipality basic polygons
           })
           .error(function(err) {
               console.log("Map not created: " + err);
           });
    }

{% endhighlight %}

![CreateLayer](https://raw.githubusercontent.com/auremoser/hasadna/master/img/3-createLayer.jpg)

#### Here's a reference point for this section [ckpt-3](https://github.com/auremoser/hasadna/tree/master/3-createLayer)

### Add SQL/CSS Templates

You can create interactive maps that respond to javascript methods a number of ways, we'll be using CSS templates, you can also make SQL templates, you can read documentation on available function magic in the [PostGIS docs](http://postgis.net/docs/) and otherwise just follow along.

* Paste the following CartoCSS structure in the `<head>` section of your webpage.
* This is a pre-configured Choropleth style. You could also create one on the fly by calculating the range in data and creating bins within that range.

{% highlight css %}
<!-- CHOROPLETH CSS -->
    <style type='cartocss/text' id='choropleth'>
      /** choropleth visualization */

      #pollutant_emissions_merge{
        polygon-fill: #FFFFCC;
        polygon-opacity: 0.8;
        line-color: #FFFFFF;
        line-width: 0;
        line-opacity: 1;
      }
      #pollutant_emissions_merge [ industry <= 6590.1] {
         polygon-fill: #253494;
      }
      #pollutant_emissions_merge [ industry <= 1041.9] {
         polygon-fill: #2C7FB8;
      }
      #pollutant_emissions_merge [ industry <= 130.1] {
         polygon-fill: #41B6C4;
      }
      #pollutant_emissions_merge [ industry <= 38.2] {
         polygon-fill: #A1DAB4;
      }
      #pollutant_emissions_merge [ industry <= 15.7] {
         polygon-fill: #FFFFCC;
      }
    </style>
{% endhighlight %}

These two pieces of code are just a jQuery operation that finds the HTML element that has an `id` of `sql` or `cartocss` and extracts the text contained within it.

* add a sublayer reference to your data tile layer function at the end of your js, sublayer 1 is my second layer, zero indexed so I pass it in as "1":

`sublayers[1].set(options); // altering the SQL and CartoCSS; see above`

![SQL](https://raw.githubusercontent.com/auremoser/hasadna/master/img/4-sqlcss.jpg)

#### Here's a reference point for this section: [ckpt-4](https://github.com/auremoser/hasadna/tree/master/4-sqlcss)

## Add Interactivity - Buttons

To add more interactivity, we'll create two buttons to toggle between the `Choropleth` map view and the view that gives a choropleth map. We can easily do this in CartoDB by using the `sublayer.setSQL()` and `sublayer.setCartoCSS()` methods to change the data.

First, create another `<style type="cartocss/text" id="electric">` tag set with the following CartoCSS style. Make sure the `id` is set to `simple`.

* Next, let's create some buttons. Put the following snippet below the `div` with an `id='map'`.

{% highlight html %}
<!-- ADD BUTTONS -->
    <div id="cartocss" class="layer_selector">
        <p><strong>Layers</strong></p>
        <ul>
            <li data="industry">Industrial Pollution</li>
            <li data="electric">Electrical Pollution</li>
        </ul>
    </div>
{% endhighlight %}

{% highlight js %}
function createSelector(layer) {
      var cartocss = "";
      var $options = $(".layer_selector").find("li");
      $options.click(function(e) {
          var $li = $(e.target);
          var selected = $li.attr('data');

          $options.removeClass('selected');
          $li.addClass('selected');

          cartocss = $('#'+selected).text();

          layer[0].setCartoCSS(cartocss);
      });
   }
{% endhighlight %}

Examples:

![quake-sample](https://raw.githubusercontent.com/auremoser/nicar-test/master/img/quakes.png)

+ [JSFiddle with Selectors](http://jsfiddle.net/gh/get/library/pure/CartoDB/academy/tree/master/t/03-cartodbjs-ground-up/lesson-3/jsfiddle_demo_cartocss)
+ [Interactivity tutorial](http://docs.cartodb.com/tutorials/custom_interactivity.html)
+ [Advanced example](http://byndhack.herokuapp.com/)

![buttons](https://raw.githubusercontent.com/auremoser/hasadna/master/img/5-buttons.jpg)

#### Here's a reference point for this section [ckpt-5](https://github.com/auremoser/hasadna/tree/master/5-buttons)

#### Here's a reference point for adding infowindows [ckpt-6](https://github.com/auremoser/hasadna/tree/master/6-info)


# Building Narrative

![Final](https://raw.githubusercontent.com/auremoser/hasadna/master/img/fullMap.jpg)

Outside of the CartoJS library, we have others to help you build dynamic narrative with your data.

## Tell Time + Stories

**Maps that tell Time** - **[Torque](http://docs.cartodb.com/tutorials/introduction_torque.html)**

<iframe src="https://srogers.cartodb.com/viz/337d9194-6458-11e3-85b5-e5e70547d141/embed_map" width="100%" height="500px"></iframe>

1. [Demonstrations in Brazil](http://blog.cartodb.com/mapping-the-world-ongoing-demonstrations-in-brazil/)
2. Tweets that mention [sunrise map](http://cartodb.s3.amazonaws.com/static_vizz/sunrise.html)
3. [Animal migration patterns](http://robbykraft.github.io/AnimalTrack/)
4. [Beyonce Album Release](https://srogers.cartodb.com/viz/337d9194-6458-11e3-85b5-e5e70547d141/embed_map)
5. [Diwali Celebrated](http://bl.ocks.org/anonymous/raw/b9b7c7d6de1c6398e435/)
6. [Ramadan Tweets w/OdysseyJS](http://bl.ocks.org/anonymous/raw/2f1e9a5a74ceeb88e977/)
7. [Alcatraz Escapees](http://www.washingtonpost.com/news/morning-mix/wp/2014/12/15/the-alcatraz-escapees-could-have-survived-and-this-interactive-model-proves-it/?tid=hp_mm&hpid=z3)
8. [Lynching and the Press](http://yale.cartodb.com/u/mdweaver/viz/ffd06ece-8545-11e4-a898-0e018d66dc29/embed_map)

![Twitter Import](http://i.imgur.com/d3GSSYQ.gif)

**Maps that tell Stories** - **[Odyssey JS](http://cartodb.github.io/odyssey.js/index.html)**

1. [Tour of Scotland](http://alasdair.cartodb.com/viz/1332c872-a887-11e4-8c45-0e9d821ea90d/embed_map?zoom=14&center_lat=55.948595&center_lon=-3.199913)
2. [*Al Jazeera*: Israeli-Palestinian Conflict by Tweets](http://stream.aljazeera.com/projects/socialmediaconversation/)
3. [The Sounds of 11M](http://www.cadenaser.com/sonidos-11m/)
4. [Berlin Wall Historic Tour](http://bl.ocks.org/namessanti/raw/d5cf706f68b7c6dce9a3/#3)
5. [Maya Angelou Quotes](http://cartodb.com/v/maya-angelou#6)


## Talk Data in Charts
You can use CartoDB's SQL API to query your data and pull it into any charting library of your choosing.

You can easily wire up a chart of pollution data, [check the code here](http://bl.ocks.org/auremoser/6c51769ef05b812690fc).

![chart](https://raw.githubusercontent.com/auremoser/hasadna/master/img/7-chart.jpg)

Learn more about it [here](http://docs.cartodb.com/tips-and-tricks.html#charts--graphs)!

Here are some examples:

Type | Title | Link/Demo | BlogPost
---- |------ | --------- | ---------
[Chart.js](http://www.chartjs.org/) Bar Graph | Traffic Data| [Aurelia's Block](http://bl.ocks.org/auremoser/af95a29cd76267d3925e)
[Highcharts](http://www.highcharts.com/) | Sensor Data  | [Github](https://github.com/auremoser/VitalSigns-water/) / [Demo](http://auremoser.github.io/VitalSigns-water/)  | [MOW Post](http://blog.cartodb.com/map-of-the-week-pulse-plotting/)
[Highcharts](http://www.highcharts.com/) | Weather Data | [Aurelia's Block](http://bl.ocks.org/auremoser/96b70f6dbcc724ecc973) | [Tutorial](https://stackedit.io/viewer#!provider=gist&gistId=e2d4f0f0b71f258f3ac9&filename=beirut.md)
[Chart.js](http://www.chartjs.org/) Line Graph | Tornado Data  | [Andrew's Block](http://bl.ocks.org/andrewxhill/9134155)
[Plot.ly](https://plot.ly/) | Earthquake Data  | [Plotly Tutorial](https://plot.ly/ipython-notebooks/cartodb/) | [CartoDB Blog](http://blog.cartodb.com/plotly/)

### More
* `sql.execute(SQL command)` to extract data from your account, place into charts, infowindows, etc.
    * Using [Chart.js](http://bl.ocks.org/andrewxhill/9134155)
* `sql.getBounds(SQL command)` to find the bounding box of data returned by SQL command
    * [Porpoise Map](http://robbykraft.github.io/AnimalTrack/)

# Resources
##CartoDB
1. [Map Academy](http://academy.cartodb.com)
    + [CartoDB.js](http://academy.cartodb.com/courses/03-cartodbjs-ground-up/lesson-3.html) -- build a web app to visualize your data, allowing for user interaction
	+ [SQL and PostGIS](http://academy.cartodb.com/courses/04-sql-postgis.html)
2. [CartoDB Tutorials](http://docs.cartodb.com/tutorials.html)
3. [CartoDB Editor Documentation](http://docs.cartodb.com/cartodb-editor.html)
4. [CartoDB APIs](http://docs.cartodb.com/cartodb-platform.html)
5. [Community help on StackExchange](http://gis.stackexchange.com/questions/tagged/cartodb)
6. [CartoDB Map Gallery](http://cartodb.com/gallery/)
7. [CartoDB Bootstrap Template by Chris Wong](https://github.com/chriswhong/cartodb-github-template)

##Visualization
1. [Charting Tools Repository](https://github.com/auremoser/chart-tools)
2. [Workshops @ CartoDB](http://cartodb.github.io/training/)
3. [Recommended tools for Visualizations](http://selection.datavisualization.ch/)
4. [Perception Concerns](https://github.com/tmcw/perception)
5. [Gestalt Theory](http://emeeks.github.io/gestaltdataviz/section1.html)
6. [Color Brewer](http://colorbrewer2.org/) or [Geocolor](http://geocolor.io/)


My contact: [aurelia@cartodb.com](mailto:aurelia@cartodb.com)

If you make a map you're proud of or just want to say hello, connect with me [@auremoser](https://twitter.com/auremoser). And if you have a minute, please give me [feedback on the workshop here](http://go.cartodb.com/we-love-your-feedback).


