---
layout: page
title: Making an Election Map
subtitle: "Alaska Press Club"
category: introductory
date: 2015-04-25
author: 'Andy Eschbacher'
length: 1
---

# Making an election map

### Andy Eschbacher, Map Scientist, CartoDB

### April 25, 2015

## A quick introduction to CartoDB

We aim to make the creation and sharing of maps as easy as possible. We also want to help you make beautiful, informative maps that make an impact and tell the stories that need to be told. Our beginnings lie in openness and the idea that every dataset has a story waiting to be told. We want to expose more than the lat/long.

## Today's goal -- make this map

<iframe width='100%' height='520' frameborder='0' src='https://andye.cartodb.com/viz/60e214be-eb8b-11e4-8c14-0e0c41326911/embed_map' allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

## Cool stuff coming out

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

These are more primo accounts than the normal free accounts. If you have a free account already but not the more primo one, send me an email and I'll bump you up.

## Let's make an election map!

### The data -- 2014 General Election, Alaska House

Alaska Board of Elections publishes data on election results, however it's not in a convenient format. I simplified it for our purposes here.

I got the data from the November 4th, 2014 General Elections [here](http://www.elections.alaska.gov/results/14GENR/). Like most data released by government organizations, it took some work getting it in to a useable form. I added the geographical data from information I received from an Alaska GIS employee.

Steps I took to get this dataset into a usable form:

1. Contact Alaska government official to get house districting data
2. Get election results data from Alaska Elections results
3. Parse that data heavily
4. Combined the two datasets with the best pieces of both
5. Make a map!

You can grab my [data directly](https://andye.cartodb.com/tables/alaska_house_election_results_2014_geometry_fi/public), but to reduce bandwidth it's so much easier to copy the following link and pasting it into the importer at CartoDB:

{% highlight html %}
http://andye.cartodb.com/api/v2/sql?q=SELECT%20*%20FROM%20public.alaska_house_election_results_2014_geometry_fi&format=geojson&filename=alaska_house_election_2014
{% endhighlight %}

### Map after import

After your data is imported, find Alaska and you should see something like this:

![First import showing alaska](http://i.imgur.com/hsT84YY.png)

You can style your map using the 'wizard' in the pane on the right-hand side of the browser window.

This map has a polygon of the house districts for each candidate, whether they won or not, so there are multiple overlapping polygons. For our map today, we'll display a map of the winners color-coded by party.


### Filtering out the winners

To do this, first we have to filter out the all the candidates that lost. We do this by clicking on the 'filters' tab. Once there, select the column 'win' and then deselect `false` so that only the winners are displayed.

Your filter tab should look like this afterwords:

![Filter to only show winners](http://i.imgur.com/tAB6uF3.png)

If you look at your data table, you'll see that only the winners are displayed. The map will look more or less the same, but now if we apply different styles to it we'll notice the data visualized much more clearly.

### Adding map labels

Next, let's add some labels to each of the districts so they are clearly identifiable.

We can do this by clicking on the "Label Text" in the pane window.

![Label text screencap](http://i.imgur.com/JTFb7Nx.png)

To avoid clutter, I selected `false` after "Label Overlap" and increased the font size to 16.

My map looks like this:

![labeled districts](http://i.imgur.com/7KR0Kij.png)

### Category map on winners

Now that we have our map in place, let's style it by which party won in a district.

We can do this by selecting "Category" in the visualization wizard. Once there, select "party" to give the districts different colors based on the party that won.

You'll get a map that looks like this:

![basic election map](http://i.imgur.com/cn5asWI.png)

The colors aren't very traditional, let's change them to the typical colors for parties by going to the wizard and selecting the colors you prefer. I'm selecting blue for DEM, red for REP, and green for NA.

![Changing colors](http://i.imgur.com/9HfbTlG.png)

### Getting back our labels

Go back to the "simple" visualization you did before, click on the CSS tab, and copy the block that has the labels... or paste the following at the bottom of the text box that's labeled CSS:

{% highlight css %}
#alaska_house_election_2014::labels {
  text-name: [district];
  text-face-name: 'DejaVu Sans Book';
  text-size: 16;
  text-label-position-tolerance: 10;
  text-fill: #000;
  text-halo-fill: #FFF;
  text-halo-radius: 1;
  text-dy: -10;
  text-allow-overlap: false;
  text-placement: point;
  text-placement-type: simple;
}
{% endhighlight %}

You should now have the labels back on your map.

### Infowindows

Try clicking on any of the districts and you'll see a mostly empty pop up window. Click on "Select Fields" and the pane on the right will open up. Toggle on any of the info you want displayed for all of your districts.

![infowindows](http://i.imgur.com/fXtUZPq.png)

### Adding an annotation

Annotations are a great tool to highlight specific information about your maps. They zoom and pan with the user.

![annotation](http://i.imgur.com/yJ6Bx5I.gif)

### Adding a title or linking your data

Let's add a title which includes a link to the original data.

Your final map should look similar to the map at the top of this page.

## Resources to help you make maps 
1. [Map Academy](http://academy.cartodb.com) is a site I run
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

The accounts you have now are **free for life** and you can do so much with them. For most things, these accounts are good enough.

If you want fancier accounts, IRE members get a 30% discount. If you make a map, please send it my way! If you want help, let me know :)

Email: eschbacher@cartodb.com
Twitter: [@MrEPhysics](https://twitter.com/MrEPhysics)
