title: quilt docs: QuiltingRoom
description: Main module to quilt a static site by stitching html page together
author: markdoc.py

<ul class="breadcrumb">
<li><a href="index.html">quilt</a></li>
<li><a href="QuiltingRoom.html">QuiltingRoom</a></li>
</ul>
****************************************************************************************************************
[TOC]
## __NAME__

QuiltingRoom - quilt.QuiltingRoom

## __FILE__

`/Users/timothydavenport/Documents/notebook/quilt/quilt`

## __DESCRIPTION__

Main module to quilt a static site by stitching html page together
{: .lead}

1. set `source` to users directory containing the [appropriate files](#exampledir) (default output is `quilted_` + `source`)
2. read `config.json` and override [default configuration](#configuration)
3. load quilt file at `quilt.html`
4. load all patch files in `patches/`
5. locate `pages/`, `templates/`, and `assets/` directories
6. if `posts/` exists and configured to build a blog create [`Blog` object]{#Blog}
7. build assets by (+ = optional):
    1. copy `assets/` to output
    2. creating `favicon.ico` +
    3. combine all `css` files into one +
        * auto add vendor prefix +
        * minimize each file +
    4. combine all `js` files into one +
        * minimize each file +
8. go thru pages and stitch together with [`Quilter` object]{#Quilter}
    * if post append page data to `Blog` object
9. add blog Home, Tag and Category pages
10. generate `atom` feed and/or `rss` feed
11. fill directories without `index.html`
12. add `robot.txt`
13. generate `search.json`, a word to url index for `typeahead`
14. generate `sitemap.xml`

## __MODULES__

[PIL](https://www.google.com/#q=python+PIL), [bs4](https://www.google.com/#q=python+bs4), [copy](https://www.google.com/#q=python+copy), [datetime](https://www.google.com/#q=python+datetime), [fnmatch](https://www.google.com/#q=python+fnmatch), [glob](https://www.google.com/#q=python+glob), [json](https://www.google.com/#q=python+json), [os](https://www.google.com/#q=python+os), [shutil](https://www.google.com/#q=python+shutil), [time](https://www.google.com/#q=python+time)
{: .lead}

## __CLASSES__

__builtin__.object
    QuiltingRoom

### class __QuiltingRoom__
> #### description
> ****************
> the quilting room
> 
> 
> #### descriptors
> ****************
> __spellcheck__
> spell check all html files
> 
> __spellcheck__
> spell check all html files
> 
> #### methods
> ****************
> def __analyze\_posts__(_self_'):
> {: .lead}
> > analyze all pages under posts/ and save needed info
> 
> def __build\_assets__(_self_'):
> {: .lead}
> > copy, combine, and minimize assets (all configurable)
> 
> def __build\_word\_dictionary__(_self_'):
> {: .lead}
> > build correct word dictionary for project
> 
> def __combine\_source__(_self, sources=None, source\_name=''_'):
> {: .lead}
> > combine css or js source files
> 
> def __copy\_asset\_directory__(_self_'):
> {: .lead}
> > copy the whole asset directory over to the output directory
> 
> def __create\_favicon\_versions__(_self_'):
> {: .lead}
> > create multiple image versions of icon
> 
> def __generate\_index__(_self_'):
> {: .lead}
> > search for directories without index.html
> 
> def __generate\_robot__(_self_'):
> {: .lead}
> > generate robot.txt in root
> 
> def __generate\_search__(_self_'):
> {: .lead}
> > create reverse word index
> 
> def __generate\_sitemap__(_self_'):
> {: .lead}
> > generates a sitemap for site
> 
> def __get\_output\_files__(_self, match=''_'):
> {: .lead}
> > go thru and find output files
> 
> def __ouput\_path__(_self, filepath='', replacement=''_'):
> {: .lead}
> > get the output directory equivalent
> 
> def __quilt__(_self_'):
> {: .lead}
> > quilt the site
> 
> def __quilt\_pages__(_self, pages, post\_data=None_'):
> {: .lead}
> > loop through pages and quilt them
> 
> def __replace\_or\_minimize\_assets__(_self, soup=None, sources=None, source\_name=''_'):
> {: .lead}
> > replace assets with combined assets and minimize inline assets
> 
> def __spellcheck__(_self_'):
> {: .lead}
> > spell check all html files
>

## __DATA__

__ASSETCOMMENT__
```
/*!
 * ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 * asset %s combined on %s
 * ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 */
```

__BODY\_STRAINER__
```
body|{}
```

__CSS\_EXT\_RE__
```
\.css$
```

__DEFAULT\_CONFIG__
```
{'buildicon': True, 'atomid': 'randomid', 'keywords': [], 'combinejs': True, 'spellcheck': True, 'patches': 'patches', 'title': 'some default title', 'quiltcomment': True, 'combinecss': True, 'priority': '0.5', 'pageobject': True, 'spellignore': ['maths', 'codehilite'], 'local': False, 'correctwords': 'correct_words.txt', 'vendorfycss': True, 'iconsizes': [64, 60, 76, 120, 152], 'categories': [], 'assets': 'assets', 'name': 'some name', 'posts': 'posts', 'copymd': True, 'blogname': 'quilt news', 'pagecomment': True, 'domain': 'some_name.com', 'page_ext': ['*.html', '*.md'], 'quilt': 'quilt.html', 'patchcomment': True, 'minimizecss': True, 'asset_ext': ['*.*'], 'buildsearch': True, 'author': 'you', 'buildatom': True, 'buildrobot': True, 'iconfile': 'icon.png', 'assetcomment': True, 'email': 'you@some_name.com', 'templates': 'templates', 'patch_ext': ['*.html'], 'buildrss': True, 'description': 'default description', 'tags': [], 'template_ext': ['*.html'], 'rssid': 'randomid', 'changefreq': 'monthly', 'pages': 'pages', 'buildindex': True, 'buildsitemap': True, 'minimizejs': True, 'buildblog': True}
```

__HEAD\_STRAINER__
```
head|{}
```

__NO\_NEW\_POSTS__
```
There are no newer posts
```

__NO\_OLD\_POSTS__
```
There are no earlier posts
```

__QUILTHEADER__
```
,,,,,,,
;#~#~#; quilt
;~#~#~; source : %s
;#~#~#; time   : %s
'''''''
```

__ROBOTTXT__
```
# Sitemap location
Sitemap: %s/sitemap.xml

# Allow crawling of all content
User-agent: *
Disallow:

```

__ROOT\_LEVEL\_JS\_EXT\_RE__
```
{{relativepath}}js/.*\.js$
```

__SITEMAP__
```
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
%s
</urlset>
```

__SITEMAPINDEX__
```
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <sitemap>
        <loc>%s</loc>
        <lastmod>%s</lastmod>
    </sitemap>
    <sitemap>
</sitemapindex>
```

__SITEMAPURL__
```
    <url>
        <loc>%s</loc>
        <lastmod>%s</lastmod>
        <changefreq>%s</changefreq>
        <priority>%s</priority>
    </url>

```

