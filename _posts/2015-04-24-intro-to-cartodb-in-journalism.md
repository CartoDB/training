---
layout: page
title: Introduction to CartoDB for Alaska Journalism
subtitle: "Alaska Press Cub"
category: introductory
date: 2015-04-24
author: 'Andy Eschbacher'
length: 1
---

# Mapping Stories

## Alaska Press Club Conf

### Andy Eschbacher, Map Scientist, CartoDB

### April 24, 2015

![Alaska's Flag](http://upload.wikimedia.org/wikipedia/commons/e/e6/Flag_of_Alaska.svg)

1. Brief introduction to CartoDB
    a. Uses
        1. Journalistic Use Cases
        2. Torque maps, Twitter Connectors
        3. New Stuff: Digital Globe imagery
    b. Brief interface tour
2. Setting up Accounts
3. Importing datasets
4. Choropleth Maps
5. Alaska-friendly projections
6. Things for later

Find this document here: http://bit.ly/cdb-alaskapc

## A quick introduction to CartoDB

We aim to make the creation and sharing of maps as easy as possible. We also want to help you make beautiful, informative maps that make an impact and tell the stories that need to be told. Our beginnings lie in openness and the idea that every dataset has a story waiting to be told. We want to expose more than the lat/long.

Besides our current software stack, we have a lot of cool stuff coming out soon.

### Torque -- animated maps


My favorite: [Map showing tweets that mention sunrise](http://cartodb.s3.amazonaws.com/static_vizz/sunrise.html?title=true&description=true&search=false&shareable=true&cartodb_logo=true&layer_selector=false&legends=false&scrollwheel=true&sublayer_options=1%7C1&sql=&zoom=2&center_lat=22.917922936146045&center_lon=51.328125#)

![tweets mentioning sunrise](http://i.imgur.com/DkXR8eS.gif)

Boston Crime bubbles
[![boston crime in torque](http://i.imgur.com/l4l0Bzr.png)](https://team.cartodb.com/u/andrew/viz/32ff4f28-7e51-11e4-9555-0e853d047bba/public_map)

Alcatraz Escape
[Alcatraz Escape revisited](http://www.washingtonpost.com/news/morning-mix/wp/2014/12/15/the-alcatraz-escapees-could-have-survived-and-this-interactive-model-proves-it/)

### Odyssey -- storytelling with maps

Aurelia's tour of lakes adversely effected by humans

[![Aurelia's Odyssey](http://i.imgur.com/klShR3l.png)](http://bl.ocks.org/auremoser/raw/d2e883314470768a07f8/)

_Source code [here](http://bl.ocks.org/auremoser/d2e883314470768a07f8/)._



### Satellite imagery -- new and exciting for me

Digital Globe

We just partnered with Digital Globe to provide their high resolution, high coverage satellite and aerial imagery of the world available for building maps.

Here are some prototypes we made last week:

![Burning Man](http://cartodb-libs.global.ssl.fastly.net/cartodb.com/assets/img/backgrounds/solutions/digital-globe.dc222e05.jpg)

[![Gigafactory](http://i.imgur.com/y0cmQtA.png)](http://mashable.com/2015/04/17/elon-musk-gigafactory/)

[![Columbia Glacier](http://i.imgur.com/pSxKk2p.png)](https://team.cartodb.com/u/eschbacher/viz/4cd6d042-ea5d-11e4-bcba-0e9d821ea90d/public_map)
High resolution glacier images (to the meter or 30 cm scale) with a good cadence.

## Setting us up for accounts

If you don't have an account, go here to sign up: https://cartodb.com/signup?plan=academy

These are more primo accounts than the normal free accounts.

## Importing data

We can import data several ways. The easiest is dragging the file from your computer and dropping it into the browser window.

![importing data, creating a map](http://i.imgur.com/1BkXZXp.gif)

You can also import by URL or directly through our Data Library where we curate a lot of data that's commonly used.

### Data

| Description  | source  | alaska-specific  |
|---|---|---|
| USGS Earthquakes | [all data](http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv) | -- |
| US Counties  | [all data](http://www2.census.gov/geo/tiger/GENZ2013/cb_2013_us_county_500k.zip)  | [alaska portion](https://www.census.gov/geo/maps-data/data/cbf/cbf_anrc.html)  |
| Populated Places  | [all data](http://common-data.cartodb.com/api/v2/sql?q=SELECT%20*%20FROM%20ne_10m_populated_places_simple&format=geojson&filename=populated_places)  | [alaska portion](http://common-data.cartodb.com/api/v2/sql?q=SELECT%20*%20FROM%20ne_10m_populated_places_simple%20WHERE%20adm1name%20=%20'Alaska'&format=geojson&filename=populated_places)  |


## Exploring different types of maps

Import the dataset on USGS Earthquakes by copying the following link and making a new map:

    http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv

![Make new map](http://i.imgur.com/2ZFS16I.gif)

Experiment with the different visualization options.

## Choropleth maps

Choropleth maps are a common type of map visualization. You see them everywhere from election mapping to ecology visualizations.

Histogram maps are colored based on the value of a number associated with the geographic coordinates. For instance, we could map earthquakes by magnitude and color more intense quakes by a darker red and less intense ones a calmer yellow. This works by making a histogram out of the magnitude data and assigning a color to each bin. Because of our capacity to see differences in colors, hues, etc., seven is usually decided as the upper limit in the number of colors in a choropleth map. There will be a lot of variation on this number.

To get started, import the following data set by creating map like we've done before.

    http://eschbacher.cartodb.com/api/v2/sql?q=SELECT%20*%20FROM%20alaska_template&filename=alaska_template&format=geojson

![choropleth](http://i.imgur.com/9EXHDzo.png)

I left two empty columns in this data table so you can easily customize it later. One column is for numbers, the other is for strings.

## Alaska-friendly projections

We're here in the north, so most projections warp things so they look huge as compared to things nearer the equator. Alaska is not really as large as it appears on a Mercator projection. "Maps lie" is a common refrain in the geo community.

![diptych of two different projections for alaska](http://i.imgur.com/dwmhDFL.png)

Let's re-project Alaska from the standard Mercator Projection to something that doesn't distort it very much. The [Alaska Albers projection](http://epsg.io/3338) is great for this. We do this by copying and pasting the following text and placing it in the SQL text box in the right pane:

{% highlight sql %}
SELECT
  ST_Transform(the_geom_webmercator,3338) AS the_geom_webmercator,
  cartodb_id,
  aland, 
  awater, 
  name, 
  total_area
FROM 
  alaska_template
{% endhighlight %}

## Adding annotations and infowindows


![map with annotations and infowindows](http://i.imgur.com/BuZtmeR.gif)


## Adding another layer

Next choose "Add Layer" in the right pane. Go to "Data File" and enter this URL:

    http://common-data.cartodb.com/api/v2/sql?q=SELECT%20*%20FROM%20ne_10m_populated_places_simple%20WHERE%20adm1name%20=%20'Alaska'&format=geojson&filename=populated_places

This is a dataset of populated places throughout the world filtered for places in Alaska. You can change the filter, or remove it entirely, by deleting all the text from WHERE to the ampersand.

After you have this new layer added, apply this SQL query to project it to our nicer projection:

{% highlight sql %}
SELECT 
  ST_Transform(the_geom_webmercator,3338) the_geom_webmercator, 
  name, 
  cartodb_id 
FROM 
  populated_places
{% endhighlight %}

![multilayer map](http://i.imgur.com/lfe6NB3.png)

There is so, so much more but that's all we have time for today. Please come tomorrow for more!

## Things for Later

I'll keep the template of Alaska counties for download in the same place should you need it at a later date. You can easily fill in the numbers you want for the columns and instantly make a choropleth, category, bubble map, etc. based on the values in that column.

It will always be here:

    http://eschbacher.cartodb.com/api/v2/sql?q=SELECT%20*%20FROM%20alaska_template&filename=alaska_template&format=geojson

Just go to that URL and it should download automatically from your browser.

### Data sources

+ [Census Data](https://www.census.gov/geo/maps-data/data/tiger.html) is oftentimes geocoded
+ [Anchorage Government's](http://www.muni.org/Departments/it/GIS2/Pages/MOAGISData.aspx) data on things related to Anchorage
+ [State of Alaska's trove](http://www.asgdc.state.ak.us/) that I found hard to navigate
+ [Data.gov](http://data.gov) is a huge data portal and there is even an 'Open in CartoDB' button that makes data import easy :)
+ [Natural Earth Data](http://www.naturalearthdata.com/) is a great resource for cultural and geographical data

#### Tips for finding data

Search for the thing you want followed by "shapefile" or "geojson".

For instance, Googling "alaska census shapefile" leads us to the county boundaries identified by the Census Bureau.

"anchorage shapfile" gives lots of good stuff, including the Anchorage government website on "GIS Data &amp; Document Downloads"

### Projecting your data to a nicer Alaska projection

To reproject your data to a nicer projection, you have to run the following SQL query in the SQL tab in the right pane. Hit "Apply Query" and just leave it how you want it.

{% highlight sql %}
SELECT
  ST_Transform(the_geom_webmercator,3338) the_geom_webmercator, -- this reprojects your Alaska geometries
  cartodb_id, -- this column allows your to interact with your map
  column_1, -- change this to whatever column you want to select
  column_2, -- keep selecting columns you want, making sure you use a comma
  column_3  -- the last column you want shouldn't end in a comma
FROM
  table_name -- this is the name of your table that contains your data
{% endhighlight %}

The `--` and what follow it are comments that are ignored when the statement is processed by the database.

## Resources

1. [Map Academy](http://academy.cartodb.com)
    + [Beginner](http://academy.cartodb.com/courses/01-beginners-course.html)
    + [Map design](http://academy.cartodb.com/courses/02-design-for-beginners.html)
    + [CartoDB.js](http://academy.cartodb.com/courses/03-cartodbjs-ground-up/lesson-3.html) -- build a web app to visualize your data, allowing for more user interaction
	+ [SQL and PostGIS](http://academy.cartodb.com/courses/04-sql-postgis.html) -- slice and dice your geospatial data
2. [CartoDB Tutorials](http://docs.cartodb.com/tutorials.html)
3. [CartoDB Editor Documentation](http://docs.cartodb.com/cartodb-editor.html)
4. [CartoDB APIs](http://docs.cartodb.com/cartodb-platform.html)
5. [Community help on StackExchange](http://gis.stackexchange.com/questions/tagged/cartodb)
6. [CartoDB Map Gallery](http://cartodb.com/gallery/)

## Thanks!

The accounts you have now are free for life and you can do so much with them.

If you want fancier accounts, IRE members get a 30% discount.

If you want to trial anything, send me an email and I'll bump you up for a while.

If you make a map, please send it my way! If you want help, let me know :)

Email: eschbacher@cartodb.com
Twitter: [MrEPhysics](https://twitter.com/MrEPhysics)

![State Seal of Alaska](http://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Alaska-StateSeal.svg/1200px-Alaska-StateSeal.svg.png)
_From Wikipedia_