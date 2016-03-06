title: quilt docs: Markdown
description: Custom Markdown Extensions
author: markdoc.py

<ul class="breadcrumb">
<li><a href="index.html">quilt</a></li>
<li><a href="markdown.html">Markdown</a></li>
</ul>
****************************************************************************************************************
[TOC]
## __NAME__

Markdown - Markdown

## __FILE__

`/Users/timothydavenport/GitHub/quilt/quilt`

## __DESCRIPTION__

Custom Markdown Extensions
{: .lead}

Adds both included and custom extensions to `Python-Markdown` :
1. 'markdown.extensions.extra'
2. 'markdown.extensions.nl2br'
3. 'markdown.extensions.sane_lists'
4. 'markdown.extensions.codehilite'
5. 'markdown.extensions.wikilinks'
6. 'markdown.extensions.toc'
7. ChecklistExtension()
8. SuperscriptExtension()
9. StrikethroughExtension()
10. SubscriptExtension()
11. SmallExtension()
12. DeleteExtension()
13. InsertExtension()
14. CiteExtension()
15. HighlightExtension()
16. CustomSpanClassExtension()
17. BlankLineExtension()
18. 'markdown.extensions.footnotes'
19. AetherExtension()

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

[etree](https://www.google.com/#q=python+etree), [markdown](https://www.google.com/#q=python+markdown), [re](https://www.google.com/#q=python+re), [sys](https://www.google.com/#q=python+sys)
{: .lead}

## __FUNCTIONS__

def __convert\_checkbox__(_match=None_'):
{: .lead}
> handle checkbox logic

## __CLASSES__

markdown.extensions.Extension(__builtin__.object)
    ChecklistExtension
    CustomSpanExtension
    MathExtension
    MultiExtension
    ReplaceTagsExtension
    SymbolExtension
markdown.inlinepatterns.Pattern(__builtin__.object)
    CustomSpanPattern
    MultiPattern
    ReplacePattern
    SymbolPattern
markdown.inlinepatterns.SimpleTagPattern(markdown.inlinepatterns.Pattern)
    MathsPattern
markdown.postprocessors.Postprocessor(markdown.util.Processor)
    ChecklistPostprocessor

### class __ChecklistExtension__
> #### description
> ****************
> adds checkbox to markdown list (e.g. [x] checked or [ ] unchecked)
> 
> 
> #### methods
> ****************
> def __extendMarkdown__(_self, md, md\_globals_'):
> {: .lead}
> > Modifies inline patterns.
> 
### class __ChecklistPostprocessor__
> #### description
> ****************
> post process to add checklist class to list element
> 
> 
> #### methods
> ****************
> def __run__(_self, html_'):
> {: .lead}
> > post process
> 
### class __CustomSpanExtension__
> #### description
> ****************
> Adds custom span extension to Markdown class
> 
> 
> #### methods
> ****************
> def __extendMarkdown__(_self, md, md\_globals_'):
> {: .lead}
> > Modifies inline patterns.
> 
### class __CustomSpanPattern__
> #### description
> ****************
> custom span pattern
> 
> 
> #### methods
> ****************
> def __handleMatch__(_self, matched_'):
> {: .lead}
> > handle matched inline pattern
> 
### class __MathExtension__
> #### description
> ****************
> create mathjax extension
> 
> 
> #### methods
> ****************
> def __extendMarkdown__(_self, md, md\_globals_'):
> {: .lead}
> > Modifies inline patterns
> 
### class __MathsPattern__
> #### description
> ****************
> match LaTeX math patterns
> 
> 
> #### methods
> ****************
> def __handleMatch__(_self, m_'):
> {: .lead}
> > replace match with span.maths
> 
### class __MultiExtension__
> #### description
> ****************
> extension: multiple matches
> 
> 
> #### methods
> ****************
> def __extendMarkdown__(_self, md, md\_globals_'):
> {: .lead}
> > Modifies inline patterns.
> 
### class __MultiPattern__
> #### description
> ****************
> match multiple patterns
> 
> 
> #### methods
> ****************
> def __handleMatch__(_self, m_'):
> {: .lead}
> > handle matched inline pattern
> 
### class __ReplacePattern__
> #### description
> ****************
> match multiple patterns
> 
> 
> #### methods
> ****************
> def __handleMatch__(_self, m_'):
> {: .lead}
> > handle matched inline pattern
> 
### class __ReplaceTagsExtension__
> #### description
> ****************
> Adds line break extension to Markdown class.
> 
> 
> #### methods
> ****************
> def __extendMarkdown__(_self, md, md\_globals_'):
> {: .lead}
> > Modifies inline patterns.
> 
### class __SymbolExtension__
> #### description
> ****************
> pre process to add checklist class to list element
> 
> 
> #### methods
> ****************
> def __extendMarkdown__(_self, md, md\_globals_'):
> {: .lead}
> > Modifies inline patterns
> 
### class __SymbolPattern__
> #### description
> ****************
> match symbols and replace html entities
> 
> 
> #### methods
> ****************
> def __handleMatch__(_self, m_'):
> {: .lead}
> > replace match with span.symbol
>

## __DATA__

__AMP\_SUBSTITUTE__
```
amp
```

__CHECKBOX\_RE__
```
<li>\[([ Xx])\]
```

__CUSTOM\_CLS\_RE__
```
[!]{2}(?P<class>.+?)[|](?P<text>.+?)[!]{2}
```

__MATHS\_RE__
```
(\$\$|\\\(|\\\[)(.+?)(\$\$|\\\)|\\\])
```

__MD__
```
<markdown.Markdown object at 0x108a5aed0>
```

__MD\_EXT__
```
['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', 'markdown.extensions.codehilite', 'markdown.extensions.wikilinks', 'markdown.extensions.toc', <Markdown.ChecklistExtension object at 0x108a5ad10>, <Markdown.CustomSpanExtension object at 0x108a5ad90>, <Markdown.ReplaceTagsExtension object at 0x108a5add0>, 'markdown.extensions.footnotes', <Markdown.SymbolExtension object at 0x108a5ae10>, <Markdown.MultiExtension object at 0x108a5ae50>, <Markdown.MathExtension object at 0x108a5ae90>]
```

__MD\_EXT\_CONFIG__
```
{'markdown.extensions.wikilinks': {'end_url': '', 'base_url': 'http://en.wikipedia.org/wiki/'}, 'markdown.extensions.codehilite': {'use_pygments': False, 'guess_lang': True}, 'markdown.extensions.toc': {'permalink': u'\x02amp\x03sect;'}, 'markdown.extensions.footnotes': {'PLACE_MARKER': '///footnotes///'}}
```

__MD\_INLINE\_TAGS__
```
{'::': 'kbd', '~~': 's', '==': 'mark', '---': 'small', '***': 'u', '+++': 'big', '___': 'u', ':::': 'samp', '%': 'var', '--': 'del', '"""': 'cite', '++': 'ins', '^': 'sup', '~': 'sub'}
```

__MULTIMATCH\_RE__
```
(\:\:|\~\~|\=\=|\-\-\-|\*\*\*|\+\+\+|\_\_\_|\:\:\:|\%|\-\-|\"\"\"|\+\+|\^|\~)(.*?)\2
```

__REPLACE\_TAGS__
```
{'%%': 'br', '@@': 'i'}
```

__REPLACE\_TAGS\_RE__
```
( \%\% | \@\@ )
```

__SYMBOLS__
```
{'(v)': '%sdarr;', '(t)': '%sdagger;', '---': '%smdash;', '(oo)': '%sinfin;', '(x)': '%stimes;', '(o)': '%sdeg;', '(r)': '%sreg;', '(tm)': '%strade;', '(c)': '%scopy;', '...': '%shellip;', '1/4': '%sfrac14;', '1/2': '%sfrac12;', '3/4': '%sfrac34;', '(^)': '%suarr;', '(tt)': '%sDagger;', '(<)': '%slarr;', '--': '%sndash;', '+-': '%splusmn;', '(/)': '%sdivide;', '(f)': '%sfnof;', '(>)': '%srarr;', '(<>)': '%sharr;', '(d)': '%sdeg;'}
```

__SYMBOLS\_RE__
```
(\(v\)|\(t\)|\-\-\-|\(oo\)|\(x\)|\(o\)|\(r\)|\(tm\)|\(c\)|\.\.\.|1\/4|1\/2|3\/4|\(\^\)|\(tt\)|\(\<\)|\-\-|\+\-|\(\/\)|\(f\)|\(\>\)|\(\<\>\)|\(d\))
```

