##Welcome, Contributor!

If you've given a workshop, tutorial, or talk on CartoDB, we'd love to host your materials one our Workshops site!

## About

This repo contains workshops on CartoDB and affiliated mapping talks [blog.cartodb.com](http://cartodb.com/). The blog of CartoDB is built on top of [Jekyll](http://jekyllrb.com/), a simple content management system for static sites.


## Process
Please fork [this repo](https://github.com/ohasselblad/workshops), add your workshop outline in markdown to the [`_posts/`](https://github.com/ohasselblad/workshops/tree/master/_posts) directory. (just follow one of the existing post templates in that file for format), and submit a pull request.

If you'd rather not deal with Github, please feel free to fill out this [Google Form](https://docs.google.com/forms/d/1aRVYb1gQEii0MjMSXWUtoWlMPmBLO07AEh9zCabiDrA/edit?usp=sharing) and we'll integrate your materials ASAP.

There are more details below if you want to submit materials. Thank you!

If you have any questions feel free to chat us on Gitter:

[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/ohasselblad/workshops)

====
##GENERAL
If you'd rather contribute via github, here's a short guide to doing that.
Sometimes understanding the mental model of git can be tough, so, check out these tools for practicing before you contribute.

* [Github in 15 minutes](https://try.github.io/levels/1/challenges/1)
* [D3 Visual Git Sandbox](http://onlywei.github.io/explain-git-with-d3/#deletebranches)
* [Mental Model of Git branching](http://nvie.com/posts/a-successful-git-branching-model/)


## DEVELOP

### How to install

The workshops repo uses [Jekyll](http://jekyllrb.com/). You'll need a Ruby and a Node.js version installed, and you can follow these [quick instructions](http://jekyllrb.com/docs/installation/) to do that.

Basically:

```
gem install jekyll
```

### Run locally

Once you fork the repo on github, navigate to where you currently are storing it on your machine in Terminal.

You'll likely use two commands, but there are more in the Jekyll docs [here](http://jekyllrb.com/docs/usage/)

For when you want to run the Jekyll blog locally to view changes:

```
jekyll serve
# => A development server will run at http://localhost:4000/
# Auto-regeneration: enabled. Use `--no-watch` to disable.
```

For when you have added and saved content and want to test it and add it to the `./_site` folder:

```
$ jekyll build
# => The current folder will be generated into ./_site
```

A tab in your browser will open and direct you to [http://localhost:9000/](http://localhost:9000/), it will track changes to rebuild and reload your browser so you can see your modifications.


## WRITE

Much of our recommendations and some details about syntax in jekyll came from our [blog post guidelines](https://github.com/CartoDB/blog/wiki/Blog-post-guidelines). But here are some specific instructions for the Workshops repo.

Start by [creating a new post](http://jekyllrb.com/docs/posts/) for one of the categories listed in `_config.yml` (also bulleted below). It will appear in the navigation on the left once recompiled. You can copy the format for one of the other posts and just edit the header configurations (date, title, category) and body content to suit your needs.

Save it with a title.md that matches the other posts, but with your date + title:

`YYYY-MM-DD-title.md`

###Guide to Git
* fork the repo and create a branch
* add your materials (guidelines explained below)
* submit a pull request and ask us to merge it with our [live site](ohasselblad.github.io/workshops)!

You can review the [`README`](https://github.com/ohasselblad/workshops/blob/master/README.md) for other links, resources and tips on writing up a post.

### Header
Don't forget to include a header at the top of your post!

Like this:
{% highlight yaml %}
layout: page
title: "WDMF"
subtitle: "Woodstock Digital Media Festival"
category: intro
date: 2014-11-07 12:00:00
author: 'Andrew Hill'
length: 2
order: 1
{% endhighlight %}

In the above case, the `length` of this workshop is hours long.

If you could like to structure the order of posts in the sidebar menu, you can force a sequence by category by giving it an `order` item in the header.

And choose one of these `category` entries in your header so that the post populates in the sidebar.

* 'intro' = Introductory
* 'inter' = Intermediate
* 'adv' = Advanced
* 'sp' = Special
* 'talk' = Talks
* 'video' = Videos

## DEPLOY

When creating a **Pull Request** (PR), please tag `@` a team member (@auremoser, @ohasselblad) to review them. Once the Pull Request has been reviewed, it can be merged to the `master` branch for deployment.

New features should be tested locally! So your reviewer can do that to make sure a setup is k

### Merging Pull Requests

**Double-check** that the name includes the right date, it should match the day you are merging on, not the day it was written!
