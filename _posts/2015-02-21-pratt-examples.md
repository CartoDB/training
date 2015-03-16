---
layout: page
title: Styling and Map Examples
subtitle: "Pratt Ongoing Projects Workshop"
category: intermediate
date: 2015-02-21 12:00:00
author: 'Santiago Giraldo Anduaga'
length: 2
---

# Intermediate Styling and Features in CartoDB
**Personal Projects Workshop**

_This workshop is designed to leave a lot of flexible space to work on personal projects, tackle challenges, and achieve a safe project-need-specific learning experience with the help of experts._

## About me:

* [Map Science &amp; Community Intern at CartoDB](http://cartodb.com/team)
* [@namessanti on Twitter](http://twitter.com/namessanti)
* [Creative Director for Cohabitation Strategies](http://www.moma.org/visit/calendar/exhibitions/1438)

Today we will explore various intermediate methods and features using the CartoDB UI and our JavaScript API CartoDB.js by exploring specific map examples and how the outcome is achieved.

## Diving in -- CartoDB Editor

#### Check out this map:

<iframe width='100%' height='520' frameborder='0' src='http://team.cartodb.com/u/santiagoa/viz/4a39c7f8-b6ce-11e4-9da5-0e853d047bba/embed_map' allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

A few things to note about the map:

* The data was scraped using the [Kimono API builder](https://www.kimonolabs.com).
* The title and text boxes were made using the 'add element' icon on the top right of the editor.

![Add Element]({{site.baseurl}}/img/pratt//element_button.png)

* Here you can also add annotations. Check out this ["After The Fall"](http://cdb.io/1yjVagF) map to see how they can be used.
* This map has no basemap, but uses another data layer as the base. You can change your base maps, add your own images, or remove the base map using the "base map selector" in the lower left corner of the editor.

![Basemaps]({{site.baseurl}}/img/common/basemap_options.png)

* The stylings of the map was done entirely in [CartoCSS](https://github.com/mapbox/carto/blob/master/docs/latest.md)
* The Torque animation elements are clickable. This is not a functionality available in Torque at the moment but you can duplicate the same layer, make it transparent on top of your animation, and style the infowindows accordingly
* There is a header image embedded into the infowindows on click

**Let's take a moment to check out what this map looks like in the data table and in the editor.**

Take this time to ask questions about style, technique, or anything else that may come to mind regarding your own project or how I achieved certain elements in the map.

### What's next?

#### Check out this map:
<iframe width='100%' height='520' frameborder='0' src='http://team.cartodb.com/u/santiagoa/viz/f0bc0d82-6f86-11e4-8b0a-0e018d66dc29/embed_map' allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

This map combines multiple layers, and many of the features were created using the built in "Add feature" function

![Add Feature]({{site.baseurl}}/img/pratt/add_feature.png)

+ Create a new layer in your project and experiment with making new features.
+ Take a look at what they look like in the data table. You can add columns with information to these spatial features in order to generate your own styles, categories, or info windows.

### Realtime Maps

#### Check out this map:
<iframe width='100%' height='520' frameborder='0' src='http://team.cartodb.com/u/santiagoa/viz/f29910f6-a59a-11e4-bf9a-0e0c41326911/embed_map' allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

* It updates every hour to let you know where storms have been reported and where there they're headed.
This is done by importing data from a URL.
* real-time sync is available only in paid accounts (unless you contact us as and you're doing something super awesome).
* This map also contains a custom legend created using the built in HTML editor.

![HTML Editor]({{site.baseurl}}/img/pratt/custom_legend.png)

**Let's take another moment for questions and to tackle challenges. While I understand not everyone is HTML-savvy, a quick tutorial on [Codecademy](http://www.codecademy.com/learn) will get you going in no time : )**

##CartoDB.js

###Check out [this](http://namessanti.github.io/crime_map_site/) map.

* The data was styled in the CartoDB Editor, then the viz.json file was pulled out using the 'share' button in the upper right hand corner.

![share]({{site.baseurl}}/img/common/share.png)

* CartoDB.js was used to create a layer selector, and toggle map legends, which were also created in the JavaScript

Feel free to check out our [documentation](http://docs.cartodb.com/cartodb-platform/cartodb-js.html) about CartoDB.js to get started coding your own maps


Here are some examples of additional data stories:

* [Walmart Nation](http://cdb.io/113rw46)
* [Violence in Africa: October 2014](http://cdb.io/1yYw8Ux)

**Don't be afraid to explore the possibilities behind the User Interface, APIs, and cartodb.js using these _resources_:**

* The [CartoDB Academy](http://academy.cartodb.com/) is great for recapping the basics, starting to use our APIs, and growing your design capabilities
* This handy [CartoCSS Reference Sheet](http://ebrelsford.github.io/talks/2014/Methods3/week7/materials/cartocss-reference.pdf) is a quick guide for beginners to CartoCSS
* If you have any questions or need any help, I am also available as a resource! Please email me at santiago@cartodb.com

## Data

[geox4.neocities.org/](http://geox4.neocities.org/) is a a great resource for accessing data across the web. It is organized into the following sections: International Resources, US-based Resources, and NYC-based Resources. **Remember - shapefiles (.shp) must be zipped with all the files before importing to CartoDB.**

The [NYC Open Data Portal](https://nycopendata.socrata.com/) is a place where you can search for and download data about NYC. Simply click on "Export" at the top right when a data set is open to download the data as a shapefile or CSV.

**Happy Mapping!**
