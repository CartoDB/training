---
layout: page
title: "Deep Dive: CartoDB JS"
subtitle: "CartoDB.js Deep-Dive"
category: advanced
date: 2014-12-16 12:00:00
author: 'Andy Eschbacher'
length: 3
---

## CartoDB.js Deep Dive

### CartoDB's JavaScript API
Examples:

+ [Global Forest Watch](http://www.globalforestwatch.org/map/3/15.00/27.00/ALL/grayscale/loss,forestgain?begin=2001-01-01&end=2013-12-31&threshold=30)
+ [Urban Reviewer](http://www.urbanreviewer.org/#map=12/40.7400/-73.9998&sidebar=plans)

Table names:

+ `census_neighborhood_demographics_2010`
+ `traffic_accidents`
+ The viz.json for the [Visualization Andrew created](http://partners.cartodb.com/api/v2/viz/5060b5e6-8092-11e4-b44f-0e853d047bba/viz.json) or use the one from your account or use one from [my account](http://andye.cartodb.com/api/v2/viz/2b04388c-8131-11e4-9030-0e4fddd5de28/viz.json)

## Going from CartoDB Editor --> CartoDB.js

![Share vizualization](http://i.imgur.com/gVxeNMg.png)

### **viz.json** in depth

The viz.json file is the main source of data for CartoDB JavaScript functions (createVis and createLayer) for creating visualizations in the browser.

Either open in a simple text editor or download a JSON viewer extension for [Chrome](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc?hl=en) or [Firefox](https://addons.mozilla.org/en-us/firefox/addon/jsonview/) to view it in the browser.

![Screenshot of viz.json file](http://i.imgur.com/VyJXjcy.png)

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

### What you need

+ Basic text editor
+ Browser

You can open HTML files on your hard drive from a browser. Use CMD+O or CTRL+O like you'd do to open a file in any program.

### Creating Basic Visualization in JavaScript

Copy &amp; paste template from [here](https://gist.github.com/ohasselblad/af5c4171e8b19363ee82).

Overview of template:

1. Included JavaScript libraries and CSS file
2. `map` element
3. `<script>` tags

Create basic visualization using createVis (docs here) by copying and pasting the following:

{% highlight javascript %}
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

createVis is excellent for creating maps quickly with very little code. There is a lot of customization with it as well. The documentation is [here](http://docs.cartodb.com/cartodb-platform/cartodb-js.html#visualization).

\* **Reload your browser window, your map should work.** \*

### createLayer and basic Leaflet.js
createLayer is the other main method for bring maps to your browser.

The following is the basic createLayer structure (depends on [Leaflet.js](http://leafletjs.com/)):

{% highlight javascript %}
window.onload = function() {
   var layerSource = ''; // <-- same viz.json as before

   var sublayerOptions = {
       sql: "SELECT * FROM census_neighborhood_demographics_2010",
       cartocss: "#census_neighborhood_demographics_2010{polygon-fill:#FF6600;}"
   }

   var sublayers;

   // Instantiate map object from Leaflet
   var mapObj = new L.Map(map_id, {  // <-- Replace map_id with 'map'
       center: [39.7392, -104.9847], // Denver, Colorado
       zoom: 11
   });

   // Add basemap tiles
   L.tileLayer('http://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png', {
       attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
   }).addTo(mapObj);

   // Add data tile layer
   cartodb.createLayer(map_object,layerSource) // <-- Replace map_object with mapObj
       .addTo(mapObj)
       .done(function(layer) {
           console.log("Map successfully created.");
           sublayers[0] = layer.getSubLayer(0);
           sublayers[1] = layer.getSubLayer(1);
           sublayers[0].set(sublayerOptions); // Here we're altering the SQL and CartoCSS of only the neighborhoods
           sublayers[1].hide(); // And hiding the traffic data
       })
       .error(function(err) {
           console.log("Map not created: " + err);
       });
}
{% endhighlight %}

One big difference here is that we explicitly expose the SQL and CartoCSS, allowing for easy customization.

![createLayer image](http://i.imgur.com/0rPSAJn.png)

**Reload your browser window, your map should work**

### Changing SQL on the fly

#### Spatial join of crashes in neighborhoods

**New goal:** We'll create an interactive map that allows us to toggle between the basic view and the view of crashes per neighborhood per capita.

To accomplish this, we need to know how many crashes happened per neighborhood, then divide that number by the population of the neighborhood. We could do a simple SQL JOIN if our data tables both contained the neighborhood name. This is less computationally intensive. To have more fun, we can instead use geospatial functions to find out how many points are inside of a shape. The function is called `ST_Intersects` (link to [documentation](http://postgis.net/docs/ST_Intersects.html)) and is part of the PostGIS extension to PostgreSQL.

Going back to the createLayer example we just created:

* Copy the following SQL command and place it below the `<style>` tags you just created.
{% highlight sql %}
<script type='sql/text' id='sql'>
SELECT
  cartodb_id, the_geom,
  the_geom_webmercator,
  nbrhd_name,
  (
    SELECT
      count(*)
    FROM
      traffic_accidents
    WHERE
      ST_Intersects(
          traffic_accidents.the_geom,
          census_neighborhood_demographics_2010.the_geom
      )
  ) / population AS accidents_per_capita
FROM
  census_neighborhood_demographics_2010
</script>
{% endhighlight %}

* Paste the following CartoCSS structure in the `<head>` section of your webpage.
    This is a pre-configured Choropleth style. You could also create one on the fly by calculating the range in data and creating bins within that range.

{% highlight css %}
<style type='cartocss/text' id='choropleth'>
/** choropleth visualization */

#census_neighborhood_demographics_2010{
  polygon-fill: #FFFFB2;
  polygon-opacity: 0.8;
  line-color: #FFF;
  line-width: 1;
  line-opacity: 1;
}
#census_neighborhood_demographics_2010 [ accidents_per_capita <= 1.40425531914894] {
   polygon-fill: #B10026;
}
#census_neighborhood_demographics_2010 [ accidents_per_capita <= 0.351046698872786] {
   polygon-fill: #E31A1C;
}
#census_neighborhood_demographics_2010 [ accidents_per_capita <= 0.19941348973607] {
   polygon-fill: #FC4E2A;
}
#census_neighborhood_demographics_2010 [ accidents_per_capita <= 0.164257555847569] {
   polygon-fill: #FD8D3C;
}
#census_neighborhood_demographics_2010 [ accidents_per_capita <= 0.115582743077914] {
   polygon-fill: #FEB24C;
}
#census_neighborhood_demographics_2010 [ accidents_per_capita <= 0.101583384741929] {
   polygon-fill: #FED976;
}
#census_neighborhood_demographics_2010 [ accidents_per_capita <= 0.077445490289527] {
   polygon-fill: #FFFFB2;
}
</style>
{% endhighlight %}

3. Next, replace the string for `sql` in the sublayerOptions object with

{% highlight javascript %}
$("#sql").text(),
{% endhighlight %}

(don't forget the comma!), and the string after `cartocss` with

{% highlight javascript %}
$("#choropleth").text()
{% endhighlight %}

These two pieces of code are just a jQuery operation that finds the HTML element that has an `id` of `sql` or `cartocss` and extracts the text contained within it.

**Reload your browser window, your map should work**

### Adding interactivity to your map

To add more interactivity, we'll create two buttons to toggle between the `Simple` map view and the view that gives a choropleth map. We can easily do this in CartoDB by using the `sublayer.setSQL()` and `sublayer.setCartoCSS()` methods to change the data

Preview lesson product for next CartoDB.js lesson.

First, create another `<style type="cartocss/text" id="simple">` tag set with the following CartoCSS style. Make sure the `id` is set to `simple`

{% highlight css %}
/** simple visualization */

#census_neighborhood_demographics_2010{
  polygon-fill: #FF6600;
  polygon-opacity: 0.7;
  line-color: #FFF;
  line-width: 1;
  line-opacity: 1;
}
{% endhighlight %}

* Next, let's create some buttons. Put the following snippet below the `div` with an `id='map'`.
{% highlight html %}
<div class="layer_selector">
    <p>Visualization Selector</p>
    <ul>
        <li data="choropleth">Color by accidents per neighborhood per capita</li>
        <li data="simple">Reset CartoCSS</li>
    </ul>
</div>
{% endhighlight %}

* Wire up the buttons with click events:
{% highlight javascript %}
// Create layer selector
function createSelector(layer) {
   var cartocss = "";
   var $options = $(".layer_selector").find("li");
   $options.click(function(e) {
       var $li = $(e.target);
       var selected = $li.attr('data');

       $options.removeClass('selected');
       $li.addClass('selected');

       cartocss = $('#'+selected).text();

       layer.setCartoCSS(cartocss);
   });
}
{% endhighlight %}

![Basic selectors](http://i.imgur.com/Y8voITB.png)

Helpful examples
+ [Interactivity tutorial](http://docs.cartodb.com/tutorials/custom_interactivity.html)
+ [Advanced example](http://byndhack.herokuapp.com/)

### Interactivity

#### Adding infowindows to your map

* HTML templates
    * Handlebar notation
    * Customizing display of information
    * Pulling in images

{% highlight html %}
<script type="infowindow/html" id="infowindow_template">
  <div class="cartodb-popup">
    <a href="#close" class="cartodb-popup-close-button close">x</a>
     <div class="cartodb-popup-content-wrapper">
       <div class="cartodb-popup-header">
         <img style="width: 100%" src="http://cartodb.com/assets/logos/logos_full_cartodb_light-5ef5e4ff558f4f8d178ab2c8faa231c1.png"></src>
       </div>
       <div class="cartodb-popup-content">
         <!-- content.data contains the field info -->
         <h4>Neighborhood: </h4>
         <p>{{content.data.nbrhd_name}}</p>
       </div>
     </div>
     <div class="cartodb-popup-tip-container"></div>
  </div>
</script>
{% endhighlight %}

Then add this to the `sublayerOptions`:
{% highlight javascript %}
interactivity: 'cartodb_id, nbrhd_name'
{% endhighlight %}

After `sublayer[0].set(...)`, add this:

{% highlight javascript %}
sublayers[0].infowindow.set('template', $('#infowindow_template').html());
{% endhighlight %}

* Click events
    * On hover
    * On click

### So much more
* `sql.execute(SQL command)` to extract data from your account, place into charts, infowindows, etc.
    * Using [Chart.js](http://bl.ocks.org/andrewxhill/9134155)
* `sql.getBounds(SQL command)` to find the bounding box of data returned by SQL command
    * [EcoHack from a few weeks ago](http://robbykraft.github.io/AnimalTrack/)

### More
* Where to get more information
    * [Documentation](http://docs.cartodb.com/cartodb-platform/cartodb-js.html)
    * [Map Academy on CartoDB.js](http://academy.cartodb.com/courses/03-cartodbjs-ground-up.html)
    * [CartoDB tutorials](http://docs.cartodb.com/tutorials.html)
    * Examples by [Andrew Hill](bl.ocks.org/andrewxhill) and [Javier Santanta](http://bl.ocks.org/javisantana)

* Want lessons, tutorials, courses that aren't currently offered? Let me know: eschbacher@cartodb.com or @MrEPhysics
