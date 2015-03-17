---
layout: page
title: Humanitarian Aid Maps
subtitle: "Haiti Humanitarian Project"
category: intermediate
date: 2015-02-04 12:00:00
author: 'Aurelia Moser'
length: 3
---

Aurelia Moser, Map Scientist, [CartoDB](http://cartodb.com)
Workshop - Yale
February 4, 2015

Find this document here:
[http://bit.ly/1At1cQQ](http://bit.ly/1At1cQQ)

[Gist](https://gist.github.com/cedbafd367aabf8fe188.git)

![Haiti Flag from wikipedia](http://upload.wikimedia.org/wikipedia/commons/5/56/Flag_of_Haiti.svg)

## Outline
1. Introduction to CartoDB
	+ Intro to the interface
	+ Examples
	+ Tour of the interface
2. Mapping Workshop
	+ Setting up accounts!
    + Data import
	+ Choropleth, Category, Intensity Maps
	+ Basic map styling
	+ Column data types
	+ Torque -- temporal maps
	+ Sharing visualizations
4. Dealing with Data
    + Getting Data
	+ What is geospatial data?
    + Data representation in CartoDB (SQL schema)
	+ Geocoding
	+ SQL/PostGIS
6. Carto.js
    + CartoJS: What it looks like (HTML/CSS/JS)
	+ Examples!
7. Odyssey.js
   + Brief Intro on authoring narratives with maps
   + Hands-on
8. Wrap Up
   + Resources
   + Onward!

### Later reference
You can find this document in [my GitHub Account](https://gist.github.com/cedbafd367aabf8fe188.git).

1. [Demonstrations in Brazil](http://blog.cartodb.com/mapping-the-world-ongoing-demonstrations-in-brazil/)
2. [Violence in Africa](http://team.cartodb.com/u/santiagoa/viz/bd69bca0-7449-11e4-88e4-0e018d66dc29/public_map)
3. [NGO Aid Map](http://ngoaidmap.org/)

<iframe src="http://team.cartodb.com/u/santiagoa/viz/bd69bca0-7449-11e4-88e4-0e018d66dc29/embed_map" width="600px" height="400px"></iframe>

## Tour of the interface
### Data Import
Basic Data Import
![Data import dialog](https://raw.githubusercontent.com/ohasselblad/workshops/master/img/common/data_import_dialog.png)
Most major formats for storing data: Excel Spreadsheets, CSV files, Shapefiles, KML (Google Earth), etc. [See complete list here.](http://docs.cartodb.com/cartodb-editor.html#supported-data-formats)

1. Import by URL! Super handy when in a workshop and you don't want to overwhelm the bandwidth
2. Select file from your HD
3. [Common Data](http://docs.cartodb.com/cartodb-editor.html#common-data) contains useful datasets for everyday use (admin regions, USGS earthquake data, ports and their locations, and many more)

Integration with **Google Drive** and **Dropbox**.

**Twitter** firehose access for [Enterprise](http://cartodb.com/enterprise) accounts.
<iframe src="http://srogers.cartodb.com/viz/81916204-c392-11e3-bcbf-0e230854a1cb/embed_map" width="600px" height="400px"></iframe>

### Data tables in CartoDB
Schema or column names
![Column names](https://raw.githubusercontent.com/ohasselblad/workshops/master/img/common/column_names.png)

### Filters & SQL
![Filters](https://raw.githubusercontent.com/ohasselblad/workshops/master/img/alaska/filters.png)
Filters are a great way to explore your data. Besides filtering your data, they allow you to see histograms of the distributions, the number of unique entries, or a search box for columns that have a large number of text entries.

#### Types of visualizations

+ **Simple** -- most basic visualization
+ **Cluster** -- counts number of points within a certain binned region
+ **Choropleth** -- makes a histogram of your data and gives bins different colors depending on the color ramp chosen
+ **Category** -- color data based on unique category (works best for a handful of unique types)
+ **Bubble** -- size markers based on column values
+ **Intensity** -- colors by density
+ **Density** -- data aggregated by number of points within a hexagon
+ **Torque** -- temporal visualization of data

Check out [visualization documentation](http://docs.cartodb.com/cartodb-editor.html#wizards) for more.

### _Simple_ Map
The visualization style _simple_ is the default visualization for all maps.
![Simple visualization](https://raw.githubusercontent.com/ohasselblad/workshops/gh-pages/img/yale/simple_visualization.png)

Styles available in the wizard
![Styling options](https://raw.githubusercontent.com/ohasselblad/workshops/gh-pages/img/alaska/styling_options.png)

**Marker Fill:** change the size, color, and opacity of all markers
**Marker Stroke:** change the width, color, and opacity of every marker's border
**Composite Operation:** change the color of markers when they overlap
**Label Text:** Text appearing by a marker (can be from columns)

#### Infowindows/hovers
![Infowindow options](https://raw.githubusercontent.com/ohasselblad/workshops/master/img/alaska/infowindow_options.png)

+ Select which column data appear in infowindow by toggling column on
+ Customize further by selecting

#### Change basemap
Select basemaps from different providers, use custom color, NASA data, MapBox tiles, etc.
![Basemap options](https://raw.githubusercontent.com/ohasselblad/workshops/gh-pages/img/alaska/basemap_options.png)

### Choropleth
Choropleth maps show map elements colored according to where a value associated with the map element falls in a range. It's like a histogram where each bin is colored differently according to a color scale you pick. Notice the CartoCSS screenshot above.

_Quantification_ is an option to pay attention to since it controls how the data is binned into different colors. _Equal interval_ gives bins of equal size across the range,  which means that outliers stand out. _Quantile_ bins so that each quantile has approximately the same number of values.

#### CartoCSS basics
[CartoCSS](https://github.com/mapbox/carto/blob/master/docs/latest.md) is the styling language for our maps.

![CartoCSS screenshot](https://raw.githubusercontent.com/ohasselblad/workshops/gh-pages/img/alaska/cartocss.png)

#### Legends
Can be easily customized
![Legend](https://raw.githubusercontent.com/ohasselblad/workshops/gh-pages/img/alaska/legend.png)

You have the option of giving it a title, and changing the text for the colors. You can also change the colors manually, or, even better, change the color ramp back in the wizard. If you want to explore other color ramps, check out [Color Brewer](http://colorbrewer2.org/) for some very well thought out color schemes.

### Torque maps

CartoDB created a fully zoomable map that changes over time.

Some examples

1. World Cup tweets saturate [this map](http://cartodb.com/v/worldcup/match/?TC=x&vis=30acae6a-0a51-11e4-8918-0e73339ffa50&h=t&t=Germany,B40903%7CArgentina,5CA2D1&m=7%2F13%2F2014%2016:00:00%20GMT,7%2F12%2F2014%2018:35:00GMT&g=147%7C#/2/7.7/56.8/0)
2. Tweets that mention [sunrise map](http://cartodb.s3.amazonaws.com/static_vizz/sunrise.html)
3. [Animal migration patterns](http://robbykraft.github.io/AnimalTrack/)

### Last few things
#### Navigating back to your tables or visualization
Click on the 90-degree arrow to get back to view your tables/visualizations
![go back to tables](https://raw.githubusercontent.com/ohasselblad/workshops/gh-pages/img/common/back_to_tables_arrow.png)

#### Navigating in general
![Navigation bar](https://raw.githubusercontent.com/ohasselblad/workshops/gh-pages/img/common/navigation_bar.png)

## Mapping
**Let's make maps!**
Make sure you already have an account setup: https://cartodb.com/signup?plan=academy

### Data Import
Import a new dataset by copying the link (not downloading) and pasting it into the import window in your CartoDB account:

**USGS reported seismic activity (earthquakes)**
http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv

### _Simple_ Map

#### Challenge #1
Using the styles in simple, try to recreate the visualization below. It's similar to an intensity map that shows where earthquakes are occurring in largest numbers. Play with styles to your preference.

![Styling options](https://raw.githubusercontent.com/ohasselblad/workshops/master/img/alaska/styling_options.png)

### Choropleth Map

More on quantification [here](http://blog.cartographica.com/blog/2010/8/16/gis-data-classifications-in-cartographica.html).

#### Challenge #2
Make a choropleth map
Next select _choropleth_ from the Vizualization wizard. By default it will select `depth`. Select the `mag` column (which means magnitude or power of the earthquake).

Notice that there are lots of US-based earthquakes that are fairly weak -- so perhaps filtering for earthquakes above 3.0 will give a better visualization of our data.

_hint_: notice that a filter was used
![Choropleth map](https://raw.githubusercontent.com/ohasselblad/workshops/master/img/alaska/choropleth_map_challenge2.png)

### Category Map

#### Challenge #3

Try to recreate this map using *category*. `net` is the column to categorize by...

![Category challenge](https://raw.githubusercontent.com/ohasselblad/workshops/master/img/alaska/category_map_challenge3.png)

### Multilayer map
Three basic types of data appear on a map.

+ Point data -- like we saw for the earthquakes
+ Line data -- like flight paths, can be seen in [this example](http://andye.cartodb.com/viz/93141b9a-784e-11e4-9f55-0e853d047bba/public_map)
+ Polygon data -- like the shapes of states

#### Challenge #4 -- Create a multilayer visualization
Go back to your dashboard and click on _Common Data_. Find _Administrative Regions_, then click on _USA States_.

Or download Haiti's admin districts [here](http://www.gadm.org/country).

After the data imports into your account, click on the large **+** on the panel on the right side of the page.

![multilayer visualization](https://raw.githubusercontent.com/ohasselblad/workshops/master/img/alaska/multilayer_map.png)

Select the earthquake dataset. It's default name on import is `all_month`. Then hit **Add layer**.

![Add additional layer](https://raw.githubusercontent.com/ohasselblad/workshops/master/img/alaska/add_additional_layer.png)

Name your visualization something like "First multilayer visualization."

You can customize each layer just as you would customize a single layer.

Try to create a map that looks like this:

![Multilayer map](https://raw.githubusercontent.com/ohasselblad/workshops/gh-pages/img/yale/multi_layer_vis.png)


####  Challenge #5 -- Create a basic torque map
Create a torque map and select the time column of the earthquake data

#### Multilayer example
Multilayer tool developed by The Daily Beast on [Abortion Clinic Access](http://www.thedailybeast.com/articles/2013/01/22/interactive-map-america-s-abortion-clinics.html).

## Working with Data Workshop
### Data is messy

+ Comes in multiple formats
+ Sources uncertain
+ Contains errors
+ etc.

### What is Geospatial Data?
**Geospatial data** is into that ids a geolocation and its characteristic features/frontiers, typically represented by points, lines, polygons, and/or complex geographic features.

### Getting Data
Data sets we could use:

1. [Number of NGOs](http://ngoaidmap.org/p/data-quality)
2. [GDP Data for Haiti](http://data.worldbank.org/country/haiti)
3. [World Bank index data](http://data.worldbank.org/country/haiti)
4. [OECD Database of Econ Stats](http://stats.oecd.org/Index.aspx?DataSetCode=TABLE1)
5. [World Bank Indicators - Health](http://data.worldbank.org/topic/health)

### Data Representation in CartoDB (SQL schema)
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
4. `GROUP BY` and `ORDER BY` are optional additions, you can read more about aggregate/other functions below

### Geocoding
####Consider the Geom
There are two special columns in CartoDB:

1. `the_geom`
2. `the_geom_webmercator`

The first of these is in the units of standard latitude/longitude, while the second is a projection based on the [original Mercator projection](http://en.wikipedia.org/wiki/Mercator_projection) but [optimized for the web](http://en.wikipedia.org/wiki/Web_Mercator).

If you want to run SQL commands and see your map update, make sure to `SELECT` the `the_geom_webmercator` because this is the column that's used for mapping--the other is more of a convenience column since most datasets use lat/long.

#### Example (if time)
1. Go back to your tables view (by clicking on the little arrow in the upper lefthand corner of your browser window)
2. import a new table called `usa_counties` into your account by pasting the following link into the import box: `http://andye.cartodb.com/api/v2/sql?q=SELECT%20*%20FROM%20usa_counties&filename=usa_counties&format=csv`
3. Rename the table to `usa_counties` by clicking on table name in the upper left-hand corner of your browser window, like the image below.
![Change table name](https://raw.githubusercontent.com/ohasselblad/workshops/master/img/alaska/change_table_name.png)

_Pro tip_: this is a call using our SQL API and is a great way to access your data. More at our [SQL API page](http://docs.cartodb.com/cartodb-platform/sql-api.html).

### SQL/PostGIS

This is a SQL statement and you'll note it in your visualization tray as a way of querying and exploring your data with immediate visual output.

{% highlight sql %}
SELECT * FROM earthquakes_all_month WHERE (mag >= 0.2975 AND mag < 3.17)
{% endhighlight %}

You can enter queries, apply them, click on "create table from query" in the green field below the column names.

![create table](https://raw.githubusercontent.com/ohasselblad/workshops/gh-pages/img/alaska/create_table.png)

You'll also note that your sql query box populated when you filtere; the two features serve similar functions serve similar functions, but the filters give you a nice gui for manipulating data, and require less-fluency in query langs.

## CartoDB.js

[CartoDB.js](http://docs.cartodb.com/cartodb-platform/cartodb-js.html) is our JavaScript API -- a way to make maps using JavaScript.

### What it looks like
![Three pieces to JavaScript maps](https://raw.githubusercontent.com/ohasselblad/workshops/master/img/alaska/three_pieces_to_js_map.png)

The [example above](http://jsfiddle.net/gh/get/library/pure/CartoDB/academy/tree/master/t/03-cartodbjs-ground-up/lesson-3/jsfiddle_demo_cartocss) use HTML, CSS, and JavaScript to make a map appear on a webpage.

Check out our [Map Academy course on CartoDB.js](http://academy.cartodb.com/courses/03-cartodbjs-ground-up.html) if you want to learn more.


### Extensibility

Use CartoDB.js with other JavaScript libraries to make powerful web map apps.

Check out [Urban Reviewer](http://www.urbanreviewer.org/).

If you take a look at the source code, there are a dozen libraries linked:
![Urban Reviewer source code](https://raw.githubusercontent.com/ohasselblad/workshops/gh-pages/img/alaska/urban_reviewer_code_example.png)

### Examples!
[Illustreets](http://illustreets.co.uk/) shows standard of living information across England to amazing detail. There are millions of data points, each can be interacted with to give graphs, summaries, etc.

[Metrologic](http://auremoser.github.io/metrologic/) weather based transport recs based on the forecast.io api


## Torque -- spatio-temporal maps

Requirements:

1. Info in `the_geom`
2. A time column (numeric or date type)

Topical Temporal Examples:

1. [Super Bowl 49](http://blog.cartodb.com/superbowl-forty-nine/)
2. [Boston Crime](https://team.cartodb.com/u/andrew/viz/32ff4f28-7e51-11e4-9555-0e853d047bba/embed_map)
3. [Beyonce Album Release](https://srogers.cartodb.com/viz/337d9194-6458-11e3-85b5-e5e70547d141/embed_map)

<iframe src="http://team.cartodb.com/u/andrew/viz/1e90fefa-ab11-11e4-8b14-0e4fddd5de28/embed_map" width="600px" height="400px"></iframe>

## Odyssey -- building narratives with your geospatial data

[Home page](http://cartodb.github.io/odyssey.js/index.html)

Huge revamp coming next week!

Example maps:

1. [Tour of Scotland](http://alasdair.cartodb.com/viz/1332c872-a887-11e4-8c45-0e9d821ea90d/embed_map?zoom=14&center_lat=55.948595&center_lon=-3.199913)
2. [HMS Beagle](http://bl.ocks.org/anonymous/raw/7d67c4ef3348192da613/?__hstc=26280290.ab5f76548b8f08714a4e4c6c33f587e7.1421332770627.1422923447351.1422937868002.39&__hssc=26280290.1.1422937868002&__hsfp=144419593)
3. [*Al Jazeera*: Israeli-Palestinian Conflict by Tweets](http://stream.aljazeera.com/projects/socialmediaconversation/)
4. [The Sounds of 11M](http://www.cadenaser.com/sonidos-11m/)


### Getting started!
Go to the [Sandbox](http://cartodb.github.io/odyssey.js/sandbox/sandbox.html).

Brief tour of the interface.
You follow [Markdown Syntax](http://daringfireball.net/projects/markdown/syntax) to populate a post.

You can read more in the [documentation](http://cartodb.github.io/odyssey.js/documentation/).

We'll check out the inbrowser beta.


## Resources

1. [Map Academy](http://academy.cartodb.com)
    + [CartoDB.js](http://academy.cartodb.com/courses/03-cartodbjs-ground-up/lesson-3.html) -- build a web app to visualize your data, allowing for user interaction
	+ [SQL and PostGIS](http://academy.cartodb.com/courses/04-sql-postgis.html)
2. [CartoDB Tutorials](http://docs.cartodb.com/tutorials.html)
3. [CartoDB Editor Documentation](http://docs.cartodb.com/cartodb-editor.html)
4. [CartoDB APIs](http://docs.cartodb.com/cartodb-platform.html)
5. [Community help on StackExchange](http://gis.stackexchange.com/questions/tagged/cartodb)
6. [CartoDB Map Gallery](http://cartodb.com/gallery/)

My contact: [aurelia@cartodb.com](mailto:aurelia@cartodb.com)

If you make a map you're proud of or just want to say hello, connect with me [@auremoser](https://twitter.com/auremoser)


