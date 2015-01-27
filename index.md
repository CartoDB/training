---
layout: default
title: "CartoDB Workshops"
---
#### WELCOME!

Check out the side bar for featured workshop scripts, and the [`img/`](https://github.com/ohasselblad/workshops/tree/master/img) and [`data/`](https://github.com/ohasselblad/workshops/tree/master/data), and [`notes/`](https://github.com/ohasselblad/workshops/tree/master/notes) directories for support images, data hardcopies, and general notes about session audiences.

![](https://raw.githubusercontent.com/ohasselblad/workshops/master/img/choropleth_map_challenge2.png)

#### CREATING A POST

Start by [creating a new post](http://jekyllrb.com/docs/posts/) one of the categories listed in `_config.yml`. It will appear in the navigation on the left once recompiled. Or use the supplied script to make creating pages easier:

```bash
ruby bin/jekyll-page "Some Page Title" ref
```

You can review the [`README`](https://github.com/ohasselblad/workshops/blob/master/README.md) for other links, resources and tips on writing up a post.

Don't forget to include a header at the top of your post!

Like this:

```
---
layout: page
title: "WDMF Workshop"
category: ws
date: 2014-11-07 12:00:00
author: 'Andrew Hill'
length: 2
---
```

In the above case, the length of this workshop is {{page.length}} hours long. It was hosted by {{ page.author }} on {{ page.date }}.

#### RESOURCES

* [AxHill's SlideDecks](https://speakerdeck.com/andrewxhill) = good for intro to workshop material
* [Pinterest for Maps](http://www.pinterest.com/andrewxhill/interactive-maps/) = sample maps in context, good for images and anecdotes
* [CDB Gallery](https://www.dropbox.com/personal/cdb-gallery) = dropbox repository of mapping images and gifs for presentations
* [CDB Vimeo](https://vimeo.com/vizzuality) = video tutorials and screencasts