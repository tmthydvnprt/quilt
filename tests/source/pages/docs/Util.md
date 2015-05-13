title: quilt docs: Util
description: Utility functions
author: markdoc.py

<ul class="breadcrumb">
<li><a href="index.html">quilt</a></li>
<li><a href="Util.html">Util</a></li>
</ul>
****************************************************************************************************************
[TOC]
## __NAME__

Util - quilt.Util

## __FILE__

`/Users/timothydavenport/GitHub/quilt/quilt`

## __DESCRIPTION__

Utility functions
{: .lead}

Helper functions used all over, but don't belong anywhere.

project    : quilt
version    : 0.1.0
status     : development
modifydate : 2015-05-12 06:43:00 -0700
createdate : 2015-04-28 06:02:00 -0700
website    : https://github.com/tmthydvnprt/quilt
author     : tmthydvnprt
email      : tmthydvnprt@users.noreply.github.com
maintainer : tmthydvnprt
license    : MIT
copyright  : Copyright 2015, quilt
credits    :

## __MODULES__

[bs4](https://www.google.com/#q=python+bs4), [codecs](https://www.google.com/#q=python+codecs), [copy](https://www.google.com/#q=python+copy), [dt](https://www.google.com/#q=python+dt), [fnmatch](https://www.google.com/#q=python+fnmatch), [nltk](https://www.google.com/#q=python+nltk), [os](https://www.google.com/#q=python+os), [random](https://www.google.com/#q=python+random), [string](https://www.google.com/#q=python+string), [sys](https://www.google.com/#q=python+sys), [urlparse](https://www.google.com/#q=python+urlparse)
{: .lead}

## __FUNCTIONS__

def __check\_local\_quilt__(_page='', quilt\_pattern=None, default\_patches=None, config=None_'):
{: .lead}
> check for directory quilt and directory patches?

def __chronological\_order__(_posts=None_'):
{: .lead}
> sort posts in reverse chronological order

def __filter\_external\_url__(_urls=None, domain=''_'):
{: .lead}
> filter file list for external assets

def __find\_hrefsrc__(_soup, tag\_name='', re\_pattern=None_'):
{: .lead}
> search a soup for pattern in href or src of tag

def __get\_file\_names__(_source='', extensions=''_'):
{: .lead}
> get all file names matching

def __get\_just\_words__(_text=''_'):
{: .lead}
> tokenize text, punctuation remove and lowercased

def __get\_keywords__(_text=''_'):
{: .lead}
> find keywords

def __group\_links__(_pagevars=None, name=''_'):
{: .lead}
> place tag and category links

def __load\_files__(_source='', extensions=''_'):
{: .lead}
> load all files matching

def __minimize\_css__(_css=''_'):
{: .lead}
> minimize css file ported from https://github.com/isaacs/cssmin/blob/master/rules.txt

def __minimize\_js__(_js=''_'):
{: .lead}
> minimize js file

def __parse\_css\_blocks__(_css=''_'):
{: .lead}
> parse css string into css blocks {...}

def __path\_link\_list__(_path\_string='', file\_name=''_'):
{: .lead}
> create lists of links for each level in a path

def __prefix\_vendor\_css__(_css=''_'):
{: .lead}
> add vendor prefix to css string, if prefixes already exist return original css

def __random\_placeholder__(_size=64_'):
{: .lead}
> return a random string of numbers and digits

def __read\_file__(_file\_path='', encoding='utf-8'_'):
{: .lead}
> read a file into a string. assumes utf-8 encoding.

def __relative\_path__(_filepath='', rootpath=''_'):
{: .lead}
> get relative path between a root and file

def __reverse\_chronological\_order__(_posts=None_'):
{: .lead}
> sort posts in reverse chronological order

def __spell\_check__(_text='', correct\_words=None_'):
{: .lead}
> spell checking, ignores non-ascii words, and numbers

def __summarize\_text__(_text='', sentence\_number=4_'):
{: .lead}
> summarizes a text

def __top\_sentences__(_text='', sentence\_number=4, max\_chars=200_'):
{: .lead}
> return top sentences or max number of words

def __unparse\_css\_blocks__(_blocks=None_'):
{: .lead}
> unparse css blocks back into a css string

def __vendorfy\_at\_prefix__(_blck=None, at\_prefix=None_'):
{: .lead}
> handle at prefix rules

def __vendorfy\_block__(_blck=None_'):
{: .lead}
> handle block

def __vendorfy\_block\_list__(_blck=None_'):
{: .lead}
> handle block

def __vendorfy\_css__(_block=None_'):
{: .lead}
> adds vendor prefixes to a block of css

def __write\_file__(_file\_path='', data=''_'):
{: .lead}
> write a file from a string. ~~string is utf encoded before~~

## __CLASSES__

__builtin__.object
    ProgressBar

### class __ProgressBar__
> #### description
> ****************
> implements a comand-line progress bar
> 
> 
> #### descriptors
> ****************
> __update\_iteration__
> increment progress
> 
> __update\_iteration__
> increment progress
> 
> #### methods
> ****************
> def __animate__(_self, iterate_'):
> {: .lead}
> > animate progress
> 
> def __update\_iteration__(_self, elapsed\_iter_'):
> {: .lead}
> > increment progress
>

## __DATA__

__AT\_RULES__
```
['keyframes']
```

__BG\_ZERO\_RE__
```
background-position:0;
```

__BLOCK\_COMMENT\_RE__
```
/\*(?!\!)(.*?)\*/
```

__BODY\_STRAINER__
```
body|{}
```

__CHARSETS2\_RE__
```
^(\s*@charset [^;]+;\s*)+
```

__CHARSETS\_RE__
```
^(.*)(@charset "[^"]*";)
```

__CLEAN\_SELECTORS2\_RE__
```
\s+([!{};:>+\(\)\],])
```

__CLEAN\_SELECTORS\_RE__
```
(^|\})([^{]+):([^{]+\{)
```

__DEFAULT\_CONFIG__
```
{'copyrighter': 'you', 'buildicon': True, 'atomid': 'randomid', 'keywords': [], 'combinejs': True, 'spellcheck': True, 'patches': 'patches', 'title': 'some default title', 'quiltcomment': True, 'combinecss': True, 'priority': '0.5', 'pageobject': True, 'local': False, 'correctwords': 'correct_words.txt', 'copydate': 2015, 'vendorfycss': True, 'iconsizes': [64, 60, 76, 120, 152], 'assets': 'assets', 'categories': [], 'spellignore': ['maths', 'codehilite'], 'name': 'some name', 'posts': 'posts', 'copymd': True, 'blogname': 'quilt news', 'pagecomment': True, 'domain': 'some_name.com', 'page_ext': ['*.html', '*.md'], 'quilt': 'quilt.html', 'patchcomment': True, 'minimizecss': True, 'images': 'imgs', 'asset_ext': ['*.*'], 'buildsearch': True, 'author': 'you', 'buildatom': True, 'buildrobot': True, 'iconfile': 'icon.png', 'assetcomment': True, 'email': 'you@some_name.com', 'templates': 'templates', 'patch_ext': ['*.html'], 'buildrss': True, 'description': 'default description', 'tags': [], 'template_ext': ['*.html'], 'rssid': 'randomid', 'changefreq': 'monthly', 'pages': 'pages', 'buildindex': True, 'buildsitemap': True, 'minimizejs': True, 'buildblog': True}
```

__EMPTY\_BRACES\_RE__
```
[^}]+{}
```

__EXTRA\_SPACES\_RE__
```
([!{}:;>+\(\[,])\s+
```

__FOUR\_ZEROS\_RE__
```
:0 0 0 0;
```

__GROUPLINK__
```
<li class="%s"><a href="%s" class="label label-success">%s</a></li>

```

__HEAD\_STRAINER__
```
head|{}
```

__KEEP\_COMMENT\_RE__
```
(/\*!.*?\*/)
```

__LEADING\_ZERO\_DECIMAL\_RE__
```
(:|\s)0+\.(\d+)
```

__LINE\_COMMENT\_RE__
```
^\s*//(?!\!).*$\n
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

__NO\_EMPTY\_TAGS__
```
['section', 'article', 'header', 'footer', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hgroup', 'nav', 'aside', 'div', 'main', 'p', 'pre', 'bockquote', 'ol', 'ul', 'li', 'a', 'abbr', 'cite', 'code', 'b', 'strong', 'em', 's', 'q', 'small', 'samp', 'u', 'time', 'var', 'sup', 'sub', 'kdb', 'mark', 'dl', 'dt', 'dd', 'table', 'thead', 'td', 'tr', 'th', 'tbody', 'tfooter']
```

__OPTIONAL\_CARRIAGE\_RETURN\_RE__
```
\r\n?
```

__PLACEHOLDER\_SIZE__
```
64
```

__PREFIXES__
```
['transform', 'transition', 'animation', 'perspective', 'padding-start', 'padding-end']
```

__SELECTORCOLON\_RE__
```
___SELECTORCOLON___
```

__SEMICOLON\_CLOSE\_BRACE\_RE__
```
;}
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

__THREE\_ZEROS\_RE__
```
:0 0 0;
```

__TWO\_ZEROS\_RE__
```
:0 0;
```

__VENDORS__
```
['-webkit-', '-moz-', '-ms-', '-o-']
```

__WORD\_RE__
```
^\w+$
```

__ZERO\_UNITS\_RE__
```
([\s:])(0)(px|em|%|in|cm|mm|pc|pt|ex)
```

