title: quilt features+todo
description: see what quilt does

Features+Todo
=============
**Features** are just **todos** with an &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input checked="" type="checkbox"/>!
Unfinished/untested todos are marked with <small>==dev==</small>.
_Questionable_ todos are marked with <small>==???==</small>.
{: .lead}
****************************************************************************************************************
[TOC]

###quilt ---(package\-level)---
***************************************

- [x] command-line interface
- [x] print progress
- [x] passes `pylint`
- [ ] profiled and optimized
- [ ] w3 validator
- [ ] pass user site vars (from `config.json`) to page vars
- [ ] <small>==???==</small> warnings for unused files `css`, `js`, maybe `html`
- [ ] generate blank site
- [ ] 

###QuiltingRoom class ---(site\-level)---
*************************************************

- [x] takes a `source` directory and generates a site
- [x] site wide configuration in `config.json`
- [x] quilts all pages in `pages/` directory
- [x] allow unique `quilt.html` and `patches/` in each directory
- [x] auto includes all resources in `assets/` directory
- [x] css vendor prefixing
    - [x] skip files already containing `-webkit-`, `-moz-`, `-ms-`, or `-o-`
- [x] minimize `css`
    - [x] skip on filenames containing `.min.`
- [x] minimize `js`
    - [x] skip on filenames containing `.min.`
- [x] combine to one `css`
    - [x] only combine top level `js/` files, `js` in deeper down will be included directly
- [x] combine to one `js`
- [x] generate blank index for empty directories
- [x] generate sitemap
- [x] build keyword search index for whole site search (e.g. with `typeahead`)
- [ ] <small>==dev==</small> relative/root path handling
- [x] favicon image creator (with multiple sizes)
- [x] spell checking 
    - [x] user specific correct word list `correct_words.txt`
    - [ ] suggest words for *errors*
- [ ] generate `404.html` page if not found
- [ ] 

###Blog class ---(blog\-level)---
*****************************************

- [x] dynamic _blog_ abilities for pages under `pages/posts/`
- [x] reverse chronological order home page
- [x] category pages
- [x] tag pages
- [x] top sentences (summary <small>==???==</small>) for post links
- [x] rss/atom for blog
- [ ] ~~folder structure is YYYY/MM/DD~~
- [x] hierarchical view from each post, tag or category page
- [x] pagination
- [x] handle, dates, title, authors
- [ ] <small>==dev==</small> handle space in names
- [ ] <small>==dev==</small> handle capitalization
- [ ] add *featured* pages that gathers posts with `featured` pagevar boolean
- [ ] <small>==???==</small> `git` based timestamps for posts
- [ ]

###Quilter class ---(page\-level)---
********************************************

- [x] starts with a `quilt.html` file defining `<patch>` tags
- [x] replace all `<patch id="x">` tags with `patches/x.html` files
- [x] allows page variables with `{ {***}}` braces wrapping
- [ ] <small>==dev==</small> <small>==???==</small> pretty or minimized html
- [x] page file contains `json` header, content (`html` or `.md`), and `script`
- [x] parse `json`
- [x] parse page
- [x] auto `markdown` for files ending in `.md` or `.markdown`
    - [x] markdown original syntax with `markdown` python module
    - [x] markdown syntax extensions:
        - [x] `markdown.extensions.extra` = abbreviations, attribute lists, definitions, fenced code, footnotes, tables, smart strong
        - [x] `markdown.extensions.nl2br` = newlines make `<br>`
        - [x] `markdown.extensions.sane_lists` = new list for list type change
        - [x] `markdown.extensions.codehilite` = syntax highlighting
        - [x] `markdown.extensions.wikilinks` = auto wikipedia linking with `[[.*]]`
        - [x] `markdown.extensions.toc` = auto table of contents with `[toc]`
        - [x] locally defined `ChecklistExtension()` = checkbox in list (`[x]` or `[ ]`)
        - [x] \(\LaTeX\) support
        - [ ]
- [x] copy over original `markdown`
- [x] markdown container wrapping patch
- [x] parse `script`
- [x] fill in blank `alt` and `title` attributes for `a` and `img` tags
- [x] auto remove href anchors without matching ids
- [x] auto remove empty tags
- [x] tag and category links
- [x] insert permalinks for headers
- [x] add markdown source link
- [ ]

<div markdown="1" class="alert alert-warning">

This list is not exhaustive and somewhat of a scratch pad. It is also a *living* list, it may be updated without notice.
{: .lead}

</div>
