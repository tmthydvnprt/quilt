title: quilt docs: Blog
description: Provide blog capabilities for static site
author: markdoc.py

<ul class="breadcrumb">
<li><a href="index.html">quilt</a></li>
<li><a href="Blog.html">Blog</a></li>
</ul>
****************************************************************************************************************
[TOC]
## __NAME__

Blog - quilt.Blog

## __FILE__

`/Users/timothydavenport/GitHub/quilt/quilt`

## __DESCRIPTION__

Provide blog capabilities for static site
{: .lead}

1. set `source` to `posts/` along with unique or default quilt and patches
2. as [`QuiltingRoom`](#QuiltingRoom) loops over pages append page data from [`Quilter`](#Quilter) to `Blog`
3. create list of posts in reverse chronological order
4. create group pages for tags and/or categories:
    1. create page that list all groups (e.g. list all tags)
    2. create page for each group with list of associated posts in reverse chronological order
5. generate `atom` feed and/or `rss` feed

project    : quilt
version    : 0.1.1
status     : development
modifydate : 2015-05-13 07:09:00 -0700
createdate : 2015-04-28 06:02:00 -0700
website    : https://github.com/tmthydvnprt/quilt
author     : tmthydvnprt
email      : tmthydvnprt@users.noreply.github.com
maintainer : tmthydvnprt
license    : MIT
copyright  : Copyright 2015, quilt
credits    :

## __MODULES__

[os](https://www.google.com/#q=python+os)
{: .lead}

## __FUNCTIONS__

def __create\_post\_list__(_posts=None, post\_list\_template='', offset=''_'):
{: .lead}
> create list html from posts

## __CLASSES__

__builtin__.object
    Blog

### class __Blog__
> #### description
> ****************
> blog object
> 
> 
> #### descriptors
> ****************
> __group\_by__
> create group dictionary
> 
> __group\_by__
> create group dictionary
> 
> #### methods
> ****************
> def __append__(_self, post=None_'):
> {: .lead}
> > append a post to the blog
> 
> def __generate\_atom__(_self_'):
> {: .lead}
> > generate atom xml
> 
> def __generate\_blog\_home__(_self_'):
> {: .lead}
> > generate blog index page
> 
> def __generate\_featured__(_self_'):
> {: .lead}
> > generate featured posts
> 
> def __generate\_group\_pages__(_self, name=''_'):
> {: .lead}
> > generate tag or category page
> 
> def __generate\_rss__(_self_'):
> {: .lead}
> > geneate rss xml
> 
> def __group\_by__(_self, name=''_'):
> {: .lead}
> > create group dictionary
>

## __DATA__

__ATOMENTRY__
```
    <entry>
        <title>%s<title>
        <link href="%s"/>
        <link rel="alternate" type="text/html" href="%s"/>
        <id>%s</id>
        <updated>%s</updated>
        <summary>%s</summary>
        <content type="xhtml">
            <div xmlns="http://www.w3.org/1999/xhtml">
                <p>%s</p>
            </div>
        </content>
        <author>
            <name>%s</name>
            <email>%s</email>
        </author>
    </entry>

```

__ATOMXML__
```
<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
    <title>%s Feed</title>
    <subtitle>%s</subtitle>
    <link href="%s/feed/" rel="self"/>
    <link href="%s"/>
    <id>%s</id>
    <updated>%s</updated>
    %s
</feed>
```

__GROUPVARS__
```
title: %s
description: %s
author: %s


```

__GROUP\_SINGLE\_NAME__
```
{'featured': 'featured', 'categories': 'category', 'tags': 'tag'}
```

__GROUP\_VERBS__
```
{'featured': 'featured', 'categories': 'categorized in', 'tags': 'tagged with'}
```

__RSSITEM__
```
   <item>
        <title>%s</title>
        <link>%s</link>
        <guid>%s</guid>
        <pubDate>%s</pubDate>
        <description>%s</description>
    </item>

```

__RSSXML__
```
<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
    <channel>
        <title>%s Feed</title>
        <description>%s</description>
        <link>%s</link>
        <id>%s</id>
        <language>en-us</language>
        <lastBuildDate>%s</lastBuildDate>
        <pubDate>%s</pubDate>
        <managingEditor>%s</managingEditor>
        %s
    </channel>
</rss>
```

