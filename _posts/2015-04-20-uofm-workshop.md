---
layout: page
title: Land Census Maps + Journalism
subtitle: "University of Maryland: Color By Number Cartography"
category: intermediate
date: 2015-04-20
author: 'Aurelia Moser'
length: 2
---


## Color by Number Cartography w/ CartoDB

Aurelia Moser, Map Scientist, [CartoDB](http://cartodb.com)
Workshop - University of Maryland

**April 20, 2015, 1H30**

Find this document here:

* Stackedit: <http://tinyurl.com/md-cdbwkshop>
* Gist: <http://tinyurl.com/md-cdbgist>

Find the code checkpoints here:

* Github: <https://github.com/auremoser/uofm-2015>

![Maryland State Flag from Wikipedia](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/1-mdflag.png)

# Outline
0. Visualizing Data
	+ Why Maps?
1. Introduction to CartoDB
	+ Examples
	+ Tour of the interface
	+ APIs / JS Libs
2. Mapping **Basics**
	+ Setting up accounts!
  	+ Data import
	+ Datasets
3. Mapping **Data**
	+ Getting Geospatial Data
  	+ Data representation in CartoDB (SQL schema)
	+ Geocoding + SQL/PostGIS
	+ Merging Tables
	+ Customizing UI
4. Building a Map
    + Basics of `VisJson` ([ckpt-1](https://github.com/auremoser/uofm-2015/tree/master/ckpt-1-visjson))
	+ Quick map with `CreateVis` ([ckpt-2](https://github.com/auremoser/uofm-2015/tree/master/ckpt-2-createVis))
	+ Custom map with `CreateLayer` [(ckpt-3](https://github.com/auremoser/uofm-2015/tree/master/ckpt-3-createLayer))
	+ Add SQL/CSS Templates ([ckpt-4](https://github.com/auremoser/uofm-2015/tree/master/ckpt-4-sqlcss))
	+ Add Buttons ([ckpt-5](https://github.com/auremoser/uofm-2015/tree/master/ckpt-5-buttons))
	+ Infowindows ([ckpt-6](https://github.com/auremoser/uofm-2015/tree/master/ckpt-6-info))
  + **BONUS:** Charts ([ckpt-5](https://github.com/auremoser/uofm-2015/tree/master/ckpt-7-chart))
5. Building a Narrative
	+ Case Study: [Midwest Downing Map](http://bl.ocks.org/auremoser/f27ed862a4aaf664c31f)
	+ Tell Time/Stories: Odyssey + Torque
	+ Datatelling: Graphs + Charts ([Census County Chart](http://bl.ocks.org/auremoser/9fe84c3f845ea535e7cc))
6. Wrap-Up and Resources

# Visualizing Data
![Types of Visualizations](https://raw.githubusercontent.com/auremoser/images/master/1-vis-types.png)

Source: [The Data Visualization Catalogue](http://www.datavizcatalogue.com/).

![PeriodicTable](https://raw.githubusercontent.com/auremoser/nicar-test/master/img/periodic.png)

Source: [Periodic Table of Visualizations](http://www.visual-literacy.org/periodic_table/periodic_table.html)

####Some terms:

* [**Time-Series**](http://en.wikipedia.org/wiki/Time_series): visualizations that include a temporal component, show change
* [**Thematic Maps**](http://en.wikipedia.org/wiki/Thematic_map): maps related to a body of topics or a subject of discussion
* [**Census Tracts**](http://en.wikipedia.org/wiki/Census_tract): the smallest territorial unit for which population data is available in many countries

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

![Product](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/map-chesepeake.png)

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
* [SQL API](http://docs.cartodb.com/cartodb-platform/sql-api.html) - run sql in your code that dynamically filters/affects/queries your mapped data stored in CartoDB
* [Import API](http://docs.cartodb.com/cartodb-platform/import-api.html) - CRUD files in your CartoDB Account

# Mapping Basics
## Setting Up Accounts
You can setup a _free_ student account today since we're all learning: <https://cartodb.com/signup?plan=academy>

![ire](https://raw.githubusercontent.com/auremoser/nicar-test/master/img/ire.png)

IRE members are eligible for a free upgraded account that includes:

* more space
* private tables ([a Magellan account feature](http://cartodb.com/pricing))
* sync tables

Email cartodb@ire.org with your request for an upgraded account and membership ID, and we'll set you up.

## Data Import
We're going to be building a visualization of land census data in the domestic U.S.

![censusdata](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/1-data.png)

We'll be mapping land tracts according to census information (c. 2014), exploring some choropleth methods and some SQL for manipulating data.

![censusmap](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/1-mapview.png)

**Census Tracts** are subdivisions of land in the USA, the primary purpose of which is to provide a stable set of geographic units for the presentation of statistical data.

![census_tweet](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/2-tweet.png)

* generally have a population size between 1,200 and 8,000 people, with an optimum size of 4,000 people
* usually covers a contiguous area; however, varies on density of settlement
* sometimes split due to population growth or merged as a result of substantial population decline.

![population_growth](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/1-pop.png)


## Datasets
You can fork the dataset we'll be working with, and the files for the workshop here.

Description | Source | Download
---------- | -------- | --------
2014 Census Tracts | [Census.gov](https://www.census.gov/geo/maps-data/data/tiger-line.html)  | [tl_2014_us_tract.zip](ftp://ftp2.census.gov/geo/tiger/TIGER2014/TRACT/)
FIPS Tracts Lookup Table | [US Census Bureau](https://www.census.gov/geo/reference/codes/cou.html)  | [US_FIPS_Codes.xls](www.schooldata.com/pdfs/US_FIPS_Codes.xls)
2014 County Info | [Census.gov](https://www.census.gov/geo/maps-data/data/tiger-line.html)  | [tl_2014_county.zip](ftp://ftp2.census.gov/geo/tiger/TIGER2014/COUNTY/)


** You can also import the data from our "Data Library," all our queries and customizations can be done on the trimmed down library version.

![DataLibrary](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/2-commondata.png)

Select **US Census Tracts** and pull it into you dashboard for manipulation.

# Mapping Data
## Getting Geospatial Data

**Geospatial data** is info that ids a geolocation and its characteristic features/frontiers, typically represented by points, lines, polygons, and/or complex geographic features.

### Issues:
+ Comes in multiple formats ([supported formats for CartoDB](http://docs.cartodb.com/cartodb-editor.html#supported-file-formats))
+ Sources uncertain
+ Contains errors
+ etc.

Downloading the Census Data/FIPS directly requires some finessing.

### Data Check:

* check the source and update date of your data
* remove headers/extra columns (in Excel or Open Refine)
* import the csv/xls/geojson and auto-geocoding via carto
* correct column names to more intelligible terms
* correct datatypes
* do any preliminary sql or filtering that suits

![correctDatatypes](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/2-mergefix.png)

Here is what it might look like when you upload your data:

![Geocoding](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/2-importdia.png)

## Data representation in CartoDB (SQL schema)
The most basic SQL statement is:

{% highlight sql %}
SELECT * FROM table_name
{% endhighlight %}

The * means everything. This means that all rows and columns from the table are given back once the query is run.

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

## Geocoding + SQL/PostGIS
There are two special columns in CartoDB:

1. `the_geom`
2. `the_geom_webmercator`

The first of these is in the units of standard latitude/longitude, while the second is a projection based on the [original Mercator projection](http://en.wikipedia.org/wiki/Mercator_projection) but [optimized for the web](http://en.wikipedia.org/wiki/Web_Mercator).

If you want to run SQL commands and see your map update, make sure to `SELECT` the `the_geom_webmercator` because this is the column that's used for mapping--the other is more of a convenience column since most datasets use lat/long.

This is a SQL statement and you can load it in your visualization tray as a way of querying and exploring your data with immediate visual output. In this case, we are calculating the % of water from your "awater" column that occupies each tract using `ST_Area`, and naming a column for that calculation * 100 to make the number less tiny; more appreciable.

{% highlight sql %}
SELECT *, 100 * awater / ST_Area(the_geom::geography) perc_water FROM tl_2014_census_tracts
{% endhighlight %}

This is a query that adds some more information from the sample, to include percent counts for land as well as a total addition to ensure that the data isn't too skewed (everything adds up to 100%).

![sql](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/2-sqlFact.png)

You can enter queries, apply them, click on "create table from query" in the green field below the column names.

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

### CartoDB Wizard

![wizard](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/3-wizard.png)

The Wizard allows you to select your visualization "type" and customize color palettes, design details, and otherwise set the tone for your map.

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
![Infowindow options](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/3-info.png)

+ Select which column data appear in infowindow by toggling column on
+ Customize further by selecting HTML-view

#### Change basemap
Select basemaps from different providers, use custom color, NASA data, MapBox tiles, etc.

![Basemap options](https://raw.githubusercontent.com/ohasselblad/workshops/gh-pages/img/alaska/basemap_options.png)

### Choropleth
Choropleth maps show map elements colored according to where a value associated with the map element falls in a range. It's like a histogram where each bin is colored differently according to a color scale you pick. Notice the CartoCSS screenshot above.

**_Quantification_** is an option to pay attention to since it controls how the data is binned into different colors.

* **_Equal interval_** gives bins of equal size across the range,  which means that outliers stand out.

![Equal-Interval](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/eqinterval.png)

* **_Quantile_** bins so that each quantile has approximately the same number of values. This is the default and works for most "normal" data.

![Quant](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/quantile.png)

* **_Jenks_** aims to increase the standard deviation between each group of data while decreasing the standard deviation within each group. In other words, it increases the similarity within a given group in conjunction with the differences from each of the other groups. The Jenks method does this by shuffling data across each group until it detects an optimization.

![Jenks](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/jenks.png)

* **_Heads/Tails_** breaks can be powerful for data with a long-tail distribution.

![heads](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/headstails.png)

Play around with them and see what works best for your dataset.

### CartoCSS basics
[CartoCSS](https://github.com/mapbox/carto/blob/master/docs/latest.md) is the styling language for our maps.

![CartoCSS screenshot](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/3-cartocss.png)

### Legends
...can be easily customized!

![Legend](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/3-legend.png)

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

* when you the census tract data from the "Data Library", it has county FIPS codes but no placenames
* [this dataset](https://www.dropbox.com/s/eyq2p1uzg2njifx/ga-counties.kml?dl=0) has placenames and FIPS codes for counties, but no geo spatial data to give it a polygon
* you can load them both into cartodb, and select the "merge tables" button
* select `column` or `spatial` join

![joins](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/4-mergech.png)

* select the columns that you want to join on, in this case, both datasets share a "FIPS" column

![merge](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/4-mergecl.png)

* toggle the columns you want to exist in your new "joined" dataset

![mergGen](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/4-merge.png)


# Building a Map

Once you load your data, you can play with the editor options to see what type of visualization you might light to make.

I started with adding a column called `aâ€“lw` and estimating a value for the amoung of water over land.

![prelimcalc](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/alw.png)

Then I thought I should refine this, to check that the aland and awater values represented half of the land distribution for each tract.

![postlimcalc](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/3-sql2.png)


## Quick map with `CreateVis`
#### Here's a reference point for this section: [ckpt-1](https://github.com/auremoser/uofm-2015/tree/master/ckpt-1-visjson)

You will need:
+ dataset from above
+ visjson from your account, you can [reference mine](https://github.com/auremoser/uofm-2015/tree/master/ckpt-1-visjson/vis.json) to find yours too.
+ Basic Text Editor
+ Browser

#### Running Locally
* You can open HTML files on your hard drive from a browser. Use CMD+O or CTRL+O like you'd do to open a file in any program.
* You can also run a little server by navigating to the folder where you will store your files and running `http-server &`; you have node installed with http-server setup on most macs! if not, no stress, just follow along.

###VisJson

![Share-vizualization](http://i.imgur.com/gVxeNMg.png)

The viz.json file is the main source of data for CartoDB JavaScript functions (createVis and createLayer) for creating visualizations in the browser.

![visjson](https://raw.githubusercontent.com/auremoser/nicar-test/master/img/1-visJson.png)

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


### Creating Basic Visualization in JavaScript

Copy &amp; paste template from [here](https://gist.github.com/auremoser/a57654e18ce06ab396d6).

Overview of template:

1. Included JavaScript libraries and CSS file
2. `map` element
3. `<script>` tags

Create basic visualization using `createVis` by copying and pasting the following either between script tags in your html or by making a file called `[?].js` (I used `main.js` in the template) and referencing it between your script tags:

{% highlight js %}
window.onload = function() {
    var vizjson_url = ''; // <-- Paste viz.json URL between quotes

    cartodb.createVis(map_id, vizjson_url) // <-- Change map_id to 'map'
        .done(function(vis, layers) {
            // do stuff
            console.log("Map successfully created");
        })
        .error(function(err) {
            // report error
            console.log("An error occurred: " + err);
        });
}
{% endhighlight %}

`createVis` is excellent for creating maps quickly with very little code. There is a lot of customization with it as well. The documentation is [here](http://docs.cartodb.com/cartodb-platform/cartodb-js.html#visualization).

**Edit the fields to match your map reload your browser window, your map should work.**

## Custom map with `CreateLayer`
#### Here's a reference point for this section: [ckpt-2](https://github.com/auremoser/uofm-2015/tree/master/ckpt-2-createVis)

![createLayer](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/3.png)

`createLayer` is the other main method for bring maps to your browser.

The following is the basic createLayer structure (depends on [Leaflet.js](http://leafletjs.com/)):

{% highlight js %}

window.onload = function () {
  //
    var vizjson_url = 'https://team.cartodb.com/u/aureliamoser/api/v2/viz/c03a644e-e45a-11e4-9d34-0e0c41326911/viz.json'; // <-- Paste viz.json URL between quotes

   var options = {
       sql: "SELECT * FROM tl_2014_census_tracts",
       // cartocss: ""
   }

   var sublayers = [];

   // instantiate map object from Leaflet
   var mapObj = new L.Map(map, {  // <-- Replace map_id with your #id for rendering
       center: [41.8369, -87.6847], // Chicago, IL
       zoom: 7 // zoom projection to adjust starting point zoom
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
           sublayers[1].hide(); // hiding the traffic data
       })
       .error(function(err) {
           console.log("Map not created: " + err);
       });
}

{% endhighlight %}

One big difference here is that we explicitly expose the SQL and CartoCSS, allowing for easy customization.

![createLayer](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/3.png)

**Edit the fields to match your map reload your browser window, your map should work.**

## Add SQL/CSS Templates
#### Here's a reference point for this section: [ckpt-3](https://github.com/auremoser/uofm-2015/tree/master/ckpt-3-createLayer)

**New goal:** We'll create an interactive map that allows us to toggle between the basic of census tracts and the view of water density in thos tracks.

To accomplish this, we'll crib from the SQL we worked on before.

You can do this a number of ways, we'll be using SQL, you can read documentation on available function magic in the [PostGIS docs](http://postgis.net/docs/) and otherwise just follow along.

Going back to the `createLayer` example we just made:

* Copy the following SQL into your index.html file below the `<style>` tags.

{% highlight sql %}
<script type='sql/text' id='sql'>
      SELECT *, 100 * awater / ST_Area(the_geom::geography) perc_water
      FROM tl_2014_census_tracts
</script>
{% endhighlight %}

* Paste the following CartoCSS structure in the `<head>` section of your webpage.
* This is a pre-configured Choropleth style. You could also create one on the fly by calculating the range in data and creating bins within that range.

{% highlight css %}
<style type='cartocss/text' id='choropleth'>
    /** choropleth visualization */
    #tl_2014_census_tracts{
      polygon-fill: #FFFFCC;
      polygon-opacity: 0.8;
      line-color: #FFF;
      line-width: 0;
      line-opacity: 1;
    }
    #tl_2014_census_tracts [ perc_water <= 100.829766103904] {
       polygon-fill: #253494;
    }
    #tl_2014_census_tracts [ perc_water <= 6.89127773835036] {
       polygon-fill: #2C7FB8;
    }
    #tl_2014_census_tracts [ perc_water <= 1.99990433083773] {
       polygon-fill: #41B6C4;
    }
    #tl_2014_census_tracts [ perc_water <= 0.782021558262898] {
       polygon-fill: #A1DAB4;
    }
    #tl_2014_census_tracts [ perc_water <= 0.258319771503945] {
       polygon-fill: #FFFFCC;
    }
</style>
{% endhighlight %}

* Next replace the string for `sql in the options object with

{% highlight js %}
$("#sql").text(),
{% endhighlight %}

(don't forget the comma!), and the string after `cartocss` with

{% highlight js %}
$("#choropleth").text()
{% endhighlight %}

These two pieces of code are just a jQuery operation that finds the HTML element that has an `id` of `sql` or `cartocss` and extracts the text contained within it.

* add a sublayer reference to your data tile layer function at the end of your js:

`sublayers[0].set(options); // altering the SQL and CartoCSS; see above`

Check [the checkpoint code](https://github.com/auremoser/uofm-2015/tree/master/ckpt-4-sqlcss) here if you're stuck. You can also run the SQL in the tray (not in the your local files) and the the map will populate. The advantage to adding it as a template, is that you can swap it for other SQL or run different queries with different template references locally, and you are not limited to one query option.

![createButtons](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/3.png)

**Reload your browser window, your map should work!**


## Add Interactivity - Buttons
#### Here's a reference point for this section: [ckpt-4](https://github.com/auremoser/uofm-2015/tree/master/ckpt-4-sqlcss)

To add more interactivity, we'll create two buttons to toggle between the `Simple` map view and the view that gives a choropleth map. We can easily do this in CartoDB by using the `sublayer.setSQL()` and `sublayer.setCartoCSS()` methods to change the data.

First, create another `<style type="cartocss/text" id="simple">` tag set with the following CartoCSS style. Make sure the `id` is set to `simple`.

{% highlight css %}
      /** simple visualization */
      #tl_2014_census_tracts{
        polygon-fill: #5CA2D1;
        polygon-opacity: 0.7;
        line-color: #FFF;
        line-width: 0.25;
        line-opacity: 1;
      }
{% endhighlight %}

* Next, let's create some buttons. Put the following snippet below the `div` with an `id='map'`.

{% highlight html %}
<div id="cartocss" class="layer_selector">
        <p>Layers</p>
        <ul>
            <li data="choropleth">Water Density Choropleth</li>
            <li data="simple">Simple County Map</li>
        </ul>
</div>
{% endhighlight %}

* Wire up the buttons with click events:

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

![sqlcss](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/5.png)

Examples:

![quake-sample](https://raw.githubusercontent.com/auremoser/nicar-test/master/img/quakes.png)

+ [JSFiddle with Selectors](http://jsfiddle.net/gh/get/library/pure/CartoDB/academy/tree/master/t/03-cartodbjs-ground-up/lesson-3/jsfiddle_demo_cartocss)
+ [Interactivity tutorial](http://docs.cartodb.com/tutorials/custom_interactivity.html)
+ [Advanced example](http://byndhack.herokuapp.com/)


## Infowindows + More
#### Here's a reference point for this section [ckpt-5](https://github.com/auremoser/uofm-2015/tree/master/ckpt-5-buttons)

### Adding infowindows in Editor
You can enable hover infowindows in your editor, that will port to your map and give you some choropleth context.

* customization in html/css
* all data in your table is available to you to populate the tooltips

### Adding infowindows in JS
* HTML templates
    * Handlebar notation
    * Customizing display of information
    * Pulling in images

{% highlight html %}
<script type="infowindow/html" id="infowindow_template">
<div class="cartodb-tooltip-content-wrapper">
  <div class="cartodb-tooltip-content">
    <h4>Tract:</h4>
    <p>{{name}}</p>
    <h4>% Water/Tract Area:</h4>
    <p>{{perc_water}}</p>
  </div>
</div>
</script>
{% endhighlight %}

Then add this to the `options`:
{% highlight js %}
interactivity: 'cartodb_id, name, perc_water'
{% endhighlight %}

After `sublayers[0].set(...)`, add this:

{% highlight js %}
sublayers[0].infowindow.set('template', $('#infowindow_template').html());
{% endhighlight %}

* Click events
    * On hover
    * On click

You can build on this, or checkout the demo block here to view the result of your work with some limited interactivity!

### Final project here: [Downing Census Map](http://bl.ocks.org/auremoser/f27ed862a4aaf664c31f)

![info](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/6.png)

# Building Narrative
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

You can easily wire up a chart of census track water density, [check the code here](http://bl.ocks.org/auremoser/9fe84c3f845ea535e7cc).

![downing-chart](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/7.png)

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

##Data
1. [Functional street classification DC](http://opendata.dc.gov/datasets/99d13287b85240b89bd46b2aa89e1acf_48)
2. [Open Data DC Transportation](http://opendata.dc.gov/datasets?keyword=transportation)
3. [High Accident Intersection map ughhh pdf](http://ddot.dc.gov/sites/default/files/dc/sites/ddot/publication/attachments/publication_map_high_accident_intersection_09_ddot.pdf)
Current 311 map:
![311](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/ezrimap.png)
4. [NHTSA Crash Data for Maryland](http://www-fars.nhtsa.dot.gov/States/StatesCrashesAndAllVictims.aspx)
5. [DC GIS Data](http://dcatlas.dcgis.dc.gov/catalog/results.asp?pretype=All&alpha=T)
6. [2030 Proposed Rapid Bus Routes](http://opendata.dc.gov/datasets/99d13287b85240b89bd46b2aa89e1acf_28)
7. [DC Service Requests](http://opendata.dc.gov/datasets/8311590ecf2c4de294c1556c48c2837c_1)
8. [Streetlight Locations](http://opendata.dc.gov/datasets/99d13287b85240b89bd46b2aa89e1acf_90)
9. [Traffic Volume (2006)](http://opendata.dc.gov/datasets/99d13287b85240b89bd46b2aa89e1acf_64)
10. [Transportation Study Areas](http://opendata.dc.gov/datasets/99d13287b85240b89bd46b2aa89e1acf_310)
11. [Council of Governments Traffic Analysis Zones](http://dcatlas.dcgis.dc.gov/catalog/results.asp?pretype=All&pretype_info=&alpha=T&page=2&pagesize=10)

##Visualization
1. [Charting Tools Repository](https://github.com/auremoser/chart-tools)
2. [Workshops @ CartoDB](http://cartodb.github.io/training/)
3. [Recommended tools for Visualizations](http://selection.datavisualization.ch/)
4. [Perception Concerns](https://github.com/tmcw/perception)
5. [Gestalt Theory](http://emeeks.github.io/gestaltdataviz/section1.html)
6. [Color Brewer](http://colorbrewer2.org/) or [Geocolor](http://geocolor.io/)


My contact: [aurelia@cartodb.com](mailto:aurelia@cartodb.com)

If you make a map you're proud of or just want to say hello, connect with me [@auremoser](https://twitter.com/auremoser)

![MD-Seal](https://raw.githubusercontent.com/auremoser/uofm-2015/master/img/z-mdcoatofarms.png)