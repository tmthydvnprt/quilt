title: quilt docs: Constants
description: Formatable strings and default objects, maybe a list or two.
author: markdoc.py

<ul class="breadcrumb">
<li><a href="index.html">quilt</a></li>
<li><a href="Constants.html">Constants</a></li>
</ul>
****************************************************************************************************************
[TOC]
## __NAME__

Constants - quilt.Constants

## __FILE__

`/Users/timothydavenport/GitHub/quilt/quilt`

## __DESCRIPTION__

Formatable strings and default objects, maybe a list or two.
{: .lead}

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

[nltk](https://www.google.com/#q=python+nltk), [re](https://www.google.com/#q=python+re)
{: .lead}

## __DATA__

__ASSETCOMMENT__
```
/*!
 * ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 * asset %s combined on %s
 * ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 */
```

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

__BG\_ZERO\_RE__
```
background-position:0;
```

__BLOCK\_COMMENT\_RE__
```
/\*(?!\!)(.*?)\*/
```

__CHARSETS2\_RE__
```
^(\s*@charset [^;]+;\s*)+
```

__CHARSETS\_RE__
```
^(.*)(@charset "[^"]*";)
```

__CHECKBOX\_RE__
```
<li>\[([ Xx])\]
```

__CLEAN\_SELECTORS2\_RE__
```
\s+([!{};:>+\(\)\],])
```

__CLEAN\_SELECTORS\_RE__
```
(^|\})([^{]+):([^{]+\{)
```

__CSS\_EXT\_RE__
```
\.css$
```

__CUSTOM\_CLS\_RE__
```
[!]{2}(?P<class>.+?)[|](?P<text>.+?)[!]{2}
```

__DOTSTAR\_RE__
```
.*
```

__EMPTY\_BRACES\_RE__
```
[^}]+{}
```

__ESCAPED\_PAGEVAR\_RE__
```
{ {(.*?)}}
```

__EXTRA\_SPACES\_RE__
```
([!{}:;>+\(\[,])\s+
```

__FIRST\_EMPTY\_LINE\_RE__
```
\n\s*\n
```

__FIRST\_KEY\_RE__
```
[A-Za-z0-9_-]+:
```

__FOUR\_ZEROS\_RE__
```
:0 0 0 0;
```

__GROUP__
```
  <li class="%s-link">
        <h3><a href="%s">%s</a> <span class="badge">%s posts</span></h3>
    </li>

```

__GROUPLINK__
```
<li class="%s"><a href="%s" class="label label-success">%s</a></li>

```

__GROUPLIST__
```
<div class="container">
    <div class="row">
        <div class="col-sm-8 col-sm-offset-2">
            <h1>%s</h1>
            <hr>
            <ul class="%s list-unstyled">
                %s
            </ul>
        </div>
    </div>
</div>

```

__GROUPVARS__
```
title: %s
description: %s
author: %s


```

__JS\_HTML\_PATTERN\_RE__
```
(>tpircs/<.*>tpircs<)?(.*)
```

__KEEP\_COMMENT\_RE__
```
(/\*!.*?\*/)
```

__KEY\_VALUE\_RE__
```
^[ ]{0,3}(?P<key>[A-Za-z0-9_-]+):\s*(?P<value>.*)
```

__LEADING\_ZERO\_DECIMAL\_RE__
```
(:|\s)0+\.(\d+)
```

__LINE\_COMMENT\_RE__
```
^\s*//(?!\!).*$\n
```

__MATHS\_RE__
```
(\$\$|\\\(|\\\[)(.+?)(\$\$|\\\)|\\\])
```

__MD\_INLINE\_TAGS__
```
{'::': 'kbd', '~~': 's', '==': 'mark', '---': 'small', '***': 'u', '+++': 'big', '___': 'u', ':::': 'samp', '%': 'var', '--': 'del', '"""': 'cite', '++': 'ins', '^': 'sup', '~': 'sub'}
```

__MEDIA\_RE__
```
(@media[^{]*[^\s])\(
```

__MISSING\_SEMICOLON\_RE__
```
([^;\}])}
```

__MORE\_THAN\_ONE\_NEWLINE\_RE__
```
\n+
```

__MORE\_THAN\_ONE\_SEMICOLON\_RE__
```
;;+
```

__MORE\_THAN\_ONE\_WHITESPACE\_RE__
```
\s+
```

__MULTIMATCH\_RE__
```
(\:\:|\~\~|\=\=|\-\-\-|\*\*\*|\+\+\+|\_\_\_|\:\:\:|\%|\-\-|\"\"\"|\+\+|\^|\~)(.*?)\2
```

__NO\_NEW\_POSTS__
```
There are no newer posts
```

__NO\_OLD\_POSTS__
```
There are no earlier posts
```

__OPTIONAL\_CARRIAGE\_RETURN\_RE__
```
\r\n?
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

__PLACEHOLDER\_SIZE__
```
64
```

__POST__
```
  <li class="post-link list-group-item">
        <h3 class="list-group-item-heading"><a href="%s">%s</a> <span class="h4">by %s <small>on %s</small></span></h3>
        <hr>
        <p class="lead list-group-item-text">%s <a href="%s">&hellip;continue&hellip;</a></p>
        <ul class="group-list list-inline">
            <li><a href="%s">Tags:</a> </li>
            %s
        </ul>
        <ul class="group-list list-inline">
            <li><a href="%s">Categores:</a> </li>
            %s
        </ul>
    </li>

```

__POSTLIST__
```
<div class="container">
    <div class="row">
        <div class="col-sm-8 col-sm-offset-2">
            <h1>%s</h1>
            <hr>
            <div class="posts list-group">
                %s
            </div>
        </div>
    </div>
</div>

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

__QUILTHEADER__
```
,,,,,,,
;#~#~#; quilt
;~#~#~; source : %s
;#~#~#; time   : %s
'''''''
```

__REPLACE\_TAGS__
```
{'%%': 'br', '@@': 'i'}
```

__REPLACE\_TAGS\_RE__
```
( \%\% | \@\@ )
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

__SELECTORCOLON\_RE__
```
___SELECTORCOLON___
```

__SEMICOLON\_CLOSE\_BRACE\_RE__
```
;}
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

__SPACED\_COLON\_RE__
```
 ?: ?
```

__SPACED\_EQUAL\_RE__
```
 ?= ?
```

__STOPWORDS__
```
set([u'all', u'just', u'being', u'over', u'both', u'through', u'yourselves', u'its', u'before', u'herself', u'had', u'should', u'to', u'only', u'under', u'ours', u'has', u'do', u'them', u'his', u'very', u'they', u'not', u'during', u'now', u'him', u'nor', u'did', u'this', u'she', u'each', u'further', u'where', u'few', u'because', u'doing', u'some', u'are', u'our', u'ourselves', u'out', u'what', u'for', u'while', u'does', u'above', u'between', u't', u'be', u'we', u'who', u'were', u'here', u'hers', u'by', u'on', u'about', u'of', u'against', u's', u'or', u'own', u'into', u'yourself', u'down', u'your', u'from', u'her', u'their', u'there', u'been', u'whom', u'too', u'themselves', u'was', u'until', u'more', u'himself', u'that', u'but', u'don', u'with', u'than', u'those', u'he', u'me', u'myself', u'these', u'up', u'will', u'below', u'can', u'theirs', u'my', u'and', u'then', u'is', u'am', u'it', u'an', u'as', u'itself', u'at', u'have', u'in', u'any', u'if', u'again', u'no', u'when', u'same', u'how', u'other', u'which', u'you', u'after', u'most', u'such', u'why', u'a', u'off', u'i', u'yours', u'so', u'the', u'having', u'once'])
```

__SYMBOLS__
```
{'(v)': '%sdarr;', '(t)': '%sdagger;', '---': '%smdash;', '(oo)': '%sinfin;', '(x)': '%stimes;', '(o)': '%sdeg;', '(r)': '%sreg;', '(tm)': '%strade;', '(c)': '%scopy;', '...': '%shellip;', '1/4': '%sfrac14;', '1/2': '%sfrac12;', '3/4': '%sfrac34;', '(^)': '%suarr;', '(tt)': '%sDagger;', '(<)': '%slarr;', '--': '%sndash;', '+-': '%splusmn;', '(/)': '%sdivide;', '(f)': '%sfnof;', '(>)': '%srarr;', '(<>)': '%sharr;', '(d)': '%sdeg;'}
```

__SYMBOLS\_RE__
```
(\(v\)|\(t\)|\-\-\-|\(oo\)|\(x\)|\(o\)|\(r\)|\(tm\)|\(c\)|\.\.\.|1\/4|1\/2|3\/4|\(\^\)|\(tt\)|\(\<\)|\-\-|\+\-|\(\/\)|\(f\)|\(\>\)|\(\<\>\)|\(d\))
```

__TAG\_CATEGORY__
```
<div class="container">
    <div class="row">
        <div class="col-sm-8 col-sm-offset-2">
            <hr>
            <div class="col-sm-6">%s</div>
            <div class="col-sm-6">%s</div>
        </div>
    </div>
</div>

```

__THREE\_ZEROS\_RE__
```
:0 0 0;
```

__TWO\_ZEROS\_RE__
```
:0 0;
```

__VALUE\_RE__
```
^[ ]{4,}(?P<value>.*)
```

__WORD\_RE__
```
^\w+$
```

__ZERO\_UNITS\_RE__
```
([\s:])(0)(px|em|%|in|cm|mm|pc|pt|ex)
```

__x__
```
(d)
```

