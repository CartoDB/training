---
layout: default
title: "CartoDB Workshops"
---
#### WELCOME!

Check out the side bar for featured workshop scripts, and the [`img/`](https://github.com/ohasselblad/workshops/tree/master/img) and [`data/`](https://github.com/ohasselblad/workshops/tree/master/data), and [`notes/`](https://github.com/ohasselblad/workshops/tree/master/notes) directories for support images, data hardcopies, and general notes about session audiences.

![Pretty Map](https://raw.githubusercontent.com/ohasselblad/workshops/master/img/alaska/choropleth_map_challenge2.png)

#### CREATING A POST

Start by [creating a new post](http://jekyllrb.com/docs/posts/) one of the categories listed in `_config.yml`. It will appear in the navigation on the left once recompiled. Or use the supplied script to make creating pages easier:

```bash
ruby bin/jekyll-page "Some Page Title" ref
```

* fork the repo and create a branch
* add your materials (guidelines explained below)
* submit a pull request and ask us to merge it with our [live site](ohasselblad.github.io/workshops)!

You can review the [`README`](https://github.com/ohasselblad/workshops/blob/master/README.md) for other links, resources and tips on writing up a post.

Don't forget to include a header at the top of your post!

Like this:

	layout: page
	title: "WDMF"
	subtitle: "Woodstock Digital Media Festival"
	category: intro
	date: 2014-11-07 12:00:00
	author: 'Andrew Hill'
	length: 2
	order: 1


In the above case, the `length` of this workshop is hours long.

If you could like to structure the order of posts in the sidebar menu, you can force a sequence by category by giving it an `order` item in the header.

And choose one of these `category` entries in your header so that the post populates in the sidebar.

```
	* 'intro' = Introductory
	* 'inter' = Intermediate
	* 'adv' = Advanced
	* 'sp' = Special
	* 'tlk' = Talks

```

#### CONTRIBUTING

We'd love to add community-developed workshops to our list of resources and materials.

If you've given a workshop, tutorial, or talk on CartoDB, please fork [this repo](https://github.com/ohasselblad/workshops), add your outline in markdown to the [`_posts/`](https://github.com/ohasselblad/workshops/tree/master/_posts) directory. (just follow one of the existing post templates in that file for format), and submit a pull request.

If you'd rather not deal with Github, please feel free to fill out this [Google Form](https://docs.google.com/forms/d/1aRVYb1gQEii0MjMSXWUtoWlMPmBLO07AEh9zCabiDrA/edit?usp=sharing) and we'll integrate your materials ASAP. Thank you!

#### RESOURCES

* [Pinterest for Maps](http://www.pinterest.com/andrewxhill/interactive-maps/) = sample maps in context, good for images and anecdotes
* [CDB Gallery](https://www.dropbox.com/personal/cdb-gallery) = dropbox repository of mapping images and gifs for presentations
* [CDB Vimeo](https://vimeo.com/vizzuality) = video tutorials and screencasts