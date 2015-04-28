Quilt
=============

A `python` based static site `html` _stitcher_.


Description
-----------

Generate a static site via `python` from content-only `.html` and `.md` pages that are _stitched_ together along with patch (e.g. `nav.html`, `footer.html`) files onto a main site `quilt.html` file.


Code Examples
-------------

Assuming the [directory structure](#exampledir) is set up correctly, quilting is quite easy. Quilt a site located at `path/to/site/source/files` from inside python.
```python
from quilt.QuiltingRoom import QuiltingRoom

q = QuiltingRoom('path/to/site/source/files')
q.quilt()
```

The project also includes a `__main__.py` to execute from command-line.
```shell
machine:~ user$ python quilt path/to/site/source/files
```


Installation
------------

TBD, just run from a directory at the moment.


How it works
-------------

### QuiltingRoom class *(site-level)*
Used to _*quilt*_ a whole site together.

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

#### Example directory structure

#### Source

- `site_files/`
    - `config.json`
    - `quilt.html`
    - `assets/`
        - `css/`
            - `site.css`
            - `bootstrap.css`
            - ...
        - `js/`
            - `site.js`
            - `jquery.js`
            - ...
        - `imgs/`
            - `favicon.png`
            - `icon.png`
        - `fonts/`
            - ...
    - `pages/`
        - `index.html`
        - `about.html`
        - `blog/`
            - `post1.md`
            - `post2.html`
            - ...
        - ...
    - `patches/`
        - `head.html`
        - `nav.html`
        - `footer.html`
        - `scripts.html`
        - `markdown.html` (html wrapper) [^1]
        - `index.html` (no index dir/) [^2]
        - `page.html` (default blank page)

#### Output

- `quilted_site_files/`
    - `index.html` 
    - `about.html`
    - `blog/`
        - `post1.html` 
        - `post2.html`    
        - ...    
    - `sitemap.xml` 
    - `sitemapindex.xml` 
    - ...  
    - `css/` 
        - `site.css`     
        - `bootstrap.css`    
        - ...    
    - `js/`  
        - `site.js`       
        - `jquery.js`    
        - ...   
    - `imgs/`
        - `favicon.png` 
        - `icon.png` 
    - `fonts/` 
        - ...

[^1]: special case patch, not used in `quilt.html`, used to wrap all `markdown` content.
[^2]: special case patch, not used in `quilt.html`, used for directories without an `index.html` file.

#### Default Quilting Configuration:

```python
# default config, overridden by config.json in source directory
DEFAULT_CONFIG = {
    # project variables
    # -----------------------------------------------------------------------------------
    "name"        : "some name",            # site or project name
    "domain"      : "some_name.com",        # site domain
    "title"       : "some default title",   # default page title
    "author"      : "you",                  # site author
    "email"       : "you@some_name.com",    # site author's email
    "description" : "default description",  # default page description
    "keywords"    : [],                     # default page keywords
    "categories"  : [],                     # page categories
    "tags"        : [],                     # page tags
    "changefreq"  : "monthly",              # sitemap changefreq
    "priority"    : 0.5,                    # sitemap priority
    "blogname"    : "quilt news",           # atom id
    "atomid"      : "randomid",             # atom id
    "rssid"       : "randomid",             # rss id
    # configuration
    # -----------------------------------------------------------------------------------
    "local"       : False,                  # use local disk paths as urls (dev)
    "patchcomment": True,                   # comment identifying patch
    "quiltcomment": True,                   # head comment with page info
    "assetcomment": True,                   # comment asset source when combining
    "pagecomment" : True,                   # put page variables in head comment
    "pageobject"  : True,                   # put page variables in js object
    "copymd"      : True,                   # copy original markdown to output
    "combinecss"  : True,                   # combine all `css` into one
    "combinejs"   : True,                   # combine all `js` into one
    "vendorfycss" : True,                   # auto add vendor prefixes
    "minimizecss" : True,                   # minimize `css`
    "minimizejs"  : True,                   # minimize `js`
    "buildindex"  : True,                   # add `index.html` to directories w/o it
    "buildrobot"  : True,                   # add robot.txt
    "buildsearch" : True,                   # build words to url index (for `typeahead`)
    "buildsitemap": True,                   # create sitemap
    "buildblog"   : True,                   # add blog abilities to `posts/` directory
    "buildatom"   : True,                   # create atom feed
    "buildrss"    : True,                   # create rss feed
    "buildicon"   : True,                   # create favicon
    "iconsizes"   : [64, 60, 76, 120, 152], # image sizes to create
    "spellignore" : ["maths", "codehilite"],# classes to ignore spelling
    # file and directory names
    # -----------------------------------------------------------------------------------
    "quilt"       : "quilt.html",           # name of quilt file
    "patches"     : "patches",              # patches directory
    "pages"       : "pages",                # pages directory
    "templates"   : "templates",            # templates directory
    "assets"      : "assets",               # assets directory
    "posts"       : "posts",                # post directory in `pages/` directory
    "iconfile"    : "icon.png",             # image for favicon
    # file types
    # -----------------------------------------------------------------------------------
    "patch_ext"   : ["*.html"],             # allowable patch extension
    "page_ext"    : ["*.html", "*.md"],     # allowable page extension
    "template_ext": ["*.html"],             # allowable template extension
    "asset_ext"   : ["*.*"]                 # allowable resource extension
}
```

###Quilter class *(page-level)*
Used to _*stitch*_ one page together with a quilt file, patch files, and a page file.

1. use [quilt file](#quiltfile) to create quilt
2. replace all [patch files](#patchfile) by matching `patch#id` tags in quilt with a `patch/id.html` file
3. parses [page file](#pagefile) using the following format:
    1. `key: value` page variable *header* (optional)
        * key = `[A-Za-z0-9_-]+` until `:`, value = a string per line (mulitlines become array) until next key
        * page variable section ends with first empty (whitespace-only) line
    2. `html` or `markdown` page content
    3. `<script>` page script (optional)
4. set [page variables](#pagevars), overriding default site variables
5. add page content to quilt (auto processing [`markdown` page](#pagefilemd) if file ends with `.md` or `.markdown`)
6. add page script to the end of quilt
7. replace all brace variables, `{ {.*}}`, in content with page or site variables
8. if page is under `posts/` directory, `tags` and `categories` variables are linked and appended to page content
9. fill in blank `alt` attributes for `<a>` and `<img>` tags

#### Page Variables:

```python
# set quilting page defaults
page_defaults = {
    # internal variables used by quilt (auto-generated, but may be used in content)
    # -----------------------------------------------------------------------------------
    "url"          : "",                       # absolure url of page
    "relativepath" : "",                       # relative path of page
    "rootpath"     : "",                       # absolute path of output directory
    "source"       : "",                       # absolute local path of page source
    "output"       : "",                       # absolute local path of page output
    "domain"       : config["domain"],         # site domain
    "directory"    : "/",                      # parent directory
    "patchcomment" : config["patchcomment"],   # print comment showing patch source
    "quiltcomment" : config["quiltcomment"],   # print quilt comment in header
    "pagecomment"  : config["pagecomment"],    # print page var comment in header
    "latestpost"   : "",                       # filename of latest post
    "page_path"    : "",                       # breadcrumb path of post
    "next_post"    : "",                       # url of next post
    "next_title"   : "",                       # title of next post
    "disable_next" : "disabled",               # set if last post
    "last_post"    : "",                       # url of previous post
    "last_title"   : "",                       # title of last post
    "disable_last" : "disabled",               # set if first post 
    # content page variables (intended to be overriden)
    # -----------------------------------------------------------------------------------
    "name"         : config["name"],           # site/project name
    "title"        : config["name"],           # page title
    "author"       : config["author"],         # page author
    'email'        : config["email"],          # page email
    "description"  : config["description"],    # page description
    "categories"   : config["categories"],     # page categories (for pages in posts/)
    "tags"         : config["tags"],           # page tags (for pages in posts/)
    "keywords"     : [],                       # page keywords = tags + categories
    "date"         : config["now"]["fulldate"] # created date (useful for posts/)
}
```

##### Example quilt file (`quilt.html`):

```html
<!doctype html>
<html>
    <head></head>
    <body>
        <patch id="nav"></patch>
        <patch id="page"></patch>
        <patch id="footer"></patch>
        <patch id="templates"></patch>
        <patch id="scripts"></patch>
    </body>
</html>
```

##### Example patch file (`head.html`):

```html
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <title>{ {title}}</title>

    <meta name="author" content="{ {author}}">
    <meta name="description" content="{ {description}}">
    <meta name="keywords" content="{ {keywords}}">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="favicon" href="apple-touch-icon.png">
    <link rel="apple-touch-icon" href="apple-touch-icon.png">

    <link rel="stylesheet" href="{ {relativepath}}css/bootstrap.css">
    <link rel="stylesheet" href="{ {relativepath}}css/quilt.css">
    <link rel="stylesheet" href="{ {relativepath}}css/colorful.css">

</head>
```

##### Example page file (`index.html`):

```shell
title: quilt project example index.html
description: an example page file with pagevar header, page html, & page script
author: haha
name: this is already defined in a sites variables, this will override it...
uniquepagevar: make a page variable

```
```html
<div id="page" class="container-fluid">
    <div class="jumbotron text-center">
        <h1>{ {name}}</h1>
        <p>
            A <code>python</code> based static site <code>html</code> <em>stitcher</em>.
        </p>
        { {uniquepagevar}}
    </div>
</div>
```
```html
<script>
/* unique to this page, NOT inserted with patch#page but appended after global scripts */
alert('page script');
</script>
```

##### Example page file (`index.md`):

```
:::shell
title: quilt project example index.html
description: an example page file with pagevar header, page html, & page script
author: haha
name: this is already defined in a sites variables, this will override it...
uniquepagevar: make a page variable

```
```markdown
{{name}}
=========

A `python` based static site `html` _stitcher_.
--------------------------------------------------
```
```html
<script>
/* unique to this page, NOT inserted with patch#page but appended after global scripts */
alert('page script');
</script>
```

###Blog class *(blog-level)*
Used to add dynamic *blog* abilities to `posts/` directory under `pages/`

1. set `source` to `posts/` along with unique or default quilt and patches
2. as [`QuiltingRoom`](#QuiltingRoom) loops over pages append page data from [`Quilter`](#Quilter) to `Blog`
3. create list of posts in reverse chronological order
4. create group pages for tags and/or categories:
    1. create page that list all groups (e.g. list all tags)
    2. create page for each group with list of associated posts in reverse chronological order
5. generate `atom` feed and/or `rss` feed


Todo
----

- [x] mostly finished ;)
- [ ] always improvable :)

See [feature+todo]({{relativepath}}features_todo.html).


History
-------
...

License
-------

### MIT
