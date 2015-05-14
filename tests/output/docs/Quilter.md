title: quilt docs: Quilter
description: Object to stitch a page based on quilt
author: markdoc.py

<ul class="breadcrumb">
<li><a href="index.html">quilt</a></li>
<li><a href="Quilter.html">Quilter</a></li>
</ul>
****************************************************************************************************************
[TOC]
## __NAME__

Quilter - quilt.Quilter

## __FILE__

`/Users/timothydavenport/GitHub/quilt/quilt`

## __DESCRIPTION__

Object to stitch a page based on quilt
{: .lead}

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

[bs4](https://www.google.com/#q=python+bs4), [copy](https://www.google.com/#q=python+copy), [json](https://www.google.com/#q=python+json), [math](https://www.google.com/#q=python+math), [os](https://www.google.com/#q=python+os), [shutil](https://www.google.com/#q=python+shutil), [time](https://www.google.com/#q=python+time)
{: .lead}

## __FUNCTIONS__

def __add\_suffix__(_filepath='', suffix=''_'):
{: .lead}
> add suffix to file name

def __parse\_pagevars__(_var\_str=''_'):
{: .lead}
> parse page var string

## __CLASSES__

__builtin__.object
    Quilter

### class __Quilter__
> #### description
> ****************
> page quilter object
> 
> 
> #### descriptors
> ****************
> __write__
> write it out
> 
> __write__
> write it out
> 
> #### methods
> ****************
> def __add\_page\_comments__(_self_'):
> {: .lead}
> > create a page key value pair
> 
> def __clean\_html__(_self_'):
> {: .lead}
> > clean html, post process html
> 
> def __parse\_page__(_self, page_'):
> {: .lead}
> > parses page into vars, html, and scripts7.487 s
> 
> def __remove\_empty__(_self_'):
> {: .lead}
> > remove empty tags
> 
> def __replace\_patches__(_self_'):
> {: .lead}
> > replace all patches in quilt with patch files
> 
> def __replace\_variables__(_self_'):
> {: .lead}
> > replace {{}} page variables (re based replacement)
> 
> def __stitch__(_self_'):
> {: .lead}
> > generate the page
> 
> def __write__(_self, pretty=False_'):
> {: .lead}
> > write it out
>

## __DATA__

__BODY\_STRAINER__
```
body|{}
```

__DEBUG\_FILE__
```

```

__DOTSTAR\_RE__
```
.*
```

__ESCAPED\_PAGEVAR\_RE__
```
{ {(.*?)}}
```

__FIRST\_EMPTY\_LINE\_RE__
```
\n\s*\n
```

__FIRST\_KEY\_RE__
```
[A-Za-z0-9_-]+:
```

__HEAD\_STRAINER__
```
head|{}
```

__JS\_HTML\_PATTERN\_RE__
```
(>tpircs/<.*>tpircs<)?(.*)
```

__KEY\_VALUE\_RE__
```
^[ ]{0,3}(?P<key>[A-Za-z0-9_-]+):\s*(?P<value>.*)
```

__MD__
```
<markdown.Markdown object at 0x1091bfe10>
```

__NO\_EMPTY\_TAGS__
```
['section', 'article', 'header', 'footer', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hgroup', 'nav', 'aside', 'div', 'main', 'p', 'pre', 'bockquote', 'ol', 'ul', 'li', 'a', 'abbr', 'cite', 'code', 'b', 'strong', 'em', 's', 'q', 'small', 'samp', 'u', 'time', 'var', 'sup', 'sub', 'kdb', 'mark', 'dl', 'dt', 'dd', 'table', 'thead', 'td', 'tr', 'th', 'tbody', 'tfooter']
```

__PAGEOBJ__
```

<script>
pagevars = %s;
</script>
```

__PAGEVAR\_RE__
```
{{(.*?)}}
```

__PATCHCOMMENT__
```
quilted %s patch
```

__QUILTCOMMENT__
```

    -- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    -- Page stitched together with quilt.py
    -- url            : %s
    -- quilted on     : %s
    -- stitching took : %s s
%s
    -- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

```

__VALUE\_RE__
```
^[ ]{4,}(?P<value>.*)
```

