---
layout: page
title: CartoDB at Boston University
subtitle: "CartoDB crash-course for journalists and researchers"
category: introductory
date: 2015-06-17
author: 'Santiago Giraldo Anduaga'
length: 2
---

#Storytelling With Data CartoDB Workshop Boston University

![BU](http://www.bu.edu/creativewriting/files/2009/07/BU-CAS1.jpg)

## Creating your accounts!
Set you up with accounts here, [https://cartodb.com/signup?plan=academy](https://cartodb.com/signup?plan=academy). This will give you a free upgrade to our **University** plan with double the storage space and some neat features!

We also offer free upgrades for IRE members. you can request an IRE account [HERE](https://ire.org/blog/ire-news/2015/03/06/free-upgraded-cartodb-accounts-ire-members/)

##Introduction to CartoDB Editor

* Tour of dashboard
* Maps vs. Datasets
* Public Profile
* Workflow

##Let's Get Started!

On average, Thursdays in Boston are the days with the highest amount of high school and university public events. We want to look at crime rates on these days to infer an appropriate risk assessment.

* Ways of importing data
* Let's make a map!

Let's bring in the crime data by **control+clicking (or right clicking) and selecting 'Copy Link Address'** on [THIS LINK](https://raw.githubusercontent.com/namessanti/boston-data-ws/master/crime_incident_reports_thursday.csv).

We can now paste this link and import the data into CartoDB.

* Table and map view
* Changing data attributes/manipulating data
* Styling data using the GUI
* Torque
* Popup/Hover windows
* Legends
* Basemaps
* Publishing
* CartoCSS Demo (Links at the end!)

##Multi-layered maps

Now Let's see which neighborhoods in Boston have the most crimes.

* Adding a new layer
* Map hierarchy
* Styling multiple layers

Same as before, **right click** and 'copy' [this link](https://github.com/namessanti/boston-data-ws/blob/master/Bos_neighborhoods_new.zip?raw=true) for a Boston neighborhoods Shapefile

##Your First Choropleth!

* Column Join VS Spatial Join
* Spatial join City Council Districts with Rat Sightings
* Visualizing point information in polygons

##Let's get deeper by introducing **SQL**

Navigate back to your dashboard.

Our children's safety is important. So let's compare crimes and Boston Public Schools.

Same as before, **right click** and 'copy' [this link](https://raw.githubusercontent.com/namessanti/boston-data-ws/master/Boston_Public_Schools_2012-2013.csv) for a Boston Public Schools dataset.

We want to find out how many crimes are occuring within 300 meters of each school.

```sql
UPDATE boston_public_schools_2012-2013 SET the_geom = ST_Buffer(the_geom::geography, 300)::geometry
```
* Intro to what's possible with SQL
* Querys
* multi-table manipulation
* Analysis

Now, Let's bring in our crime data from our datasets, and join our tables to **get results!**

* Data table manipulation in the editor
* creating rows and columns

```sql
UPDATE boston_public_schools_2012-2013 SET point_count = (SELECT count(*)
FROM crime_incident_reports_thursday WHERE ST_Intersects(crime_incident_reports_thursday.the_geom, boston_public_schools_2012-2013.the_geom))
```

## Publishing data stories!

With CartoDB it's easy to tell your stories right in the map!

* Labels and annotations
* Layout
* Publishing options
* *Odyssey

###Explore the possibilities behind our powerful APIs using these **CartoDB resources**:

* The [CartoDB Academy](http://academy.cartodb.com/) is great for recapping the basics, starting to use our APIs, and growing your design capabilities

![Academy](http://www.gisuser.com/images/mapacademy.jpg)

* This handy [CartCSS Reference Sheet](http://ebrelsford.github.io/talks/2014/Methods3/week7/materials/cartocss-reference.pdf) is a quick guide for beginners to CartoCSS
* This [blog post](http://blog.cartodb.com/berlin-wall-post/) talks about another CartoDb tool: Odyssey
* This [video and tutorial](http://cartodb.github.io/odyssey.js/documentation/) will quickly help you take your Odyssey.js stories to the next level
* If you have any questions or need any help, I am also available as a resource! Please email me at santiago@cartodb.com

Happy Mapping!
