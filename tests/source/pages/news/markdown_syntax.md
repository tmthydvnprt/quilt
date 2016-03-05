title:       Quilt's Markdown Syntax
date:        03/08/2015 1:32 pm
description: An explanation of the markdown syntax specifics used by quilt
author:      tim
categories:  example
tags:        github-flavored-markdown
             markdown
             syntax

# {{title}} <br><small>{{description}}</small>
by {{author}} <small>on {{date}}</small>
{: .h4}
****************************************************************************************************************

[TOC]

<div id="post" markdown="1">
Quilt uses [Python-Markdown](http://pythonhosted.org//Markdown/index.html) as it's `markdown` interpreter. Besides the base syntax rules of original [Markdown](http://daringfireball.net/projects/markdown/), quilt parses extra `markdown` syntax. Extras includes abbreviations, attribute lists, definitions, fenced code, footnotes, tables (with escaped pipes (`\|`) in cells), smart strong (ignore underscores (`_`) in words), newline breaks, list type change, syntax highlighting, checklists, strikethroughs, super/subscript, insert/delete, user input/sample, variables, smalls, bigs, cites, auto wikilinks, and table of contents generation. Inline \(\LaTeX\) and `utf-8` is supported.
{: .lead}

## Syntax Examples:
****************

### Headings
*************

Headings are specified by levels of hashes (`#`). Alternate Headings for H1 and H2 can be created by underlining them with three or more equals (`=`) or hyphens (`-`), respectively.

# H1

```{.example}
# H1
```

## H2

```{.example}
## H2
```

### H3

```{.example}
### H3
```

#### H4

```{.example}
#### H4
```

##### H5

```{.example}
##### H5
```

###### H6

```{.example}
###### H6
```

H1 alternate
============

```{.example}
H1 alternate
============
```

H2 alternate
------------

```{.example}
H2 alternate
------------
```

### Paragraphs & Inline Text
*****************************

Here is one line of **text** _showing_ `inline` styling. Besides italic, bold, and code quilt supports a variety of inline styling:

*italics* with single astrisks (`*`) or underscores (`_`)
**bold** with double astrisks (`**`) or underscores (`__`)
***underlines*** with triple astrisks (`***`) or underscores (`___`)
~~strikethroughs~~ with double tildes (`~~`)
^superscript^ with carets (`^`)
~subscript~ with single tildes (`~`)
--delete-- with double hyphens (`--`)
++insert++ with double pluses (`++`)
---small--- with triple hyphens (`---`)
+++big+++ with triple hyphens (`+++`)
"""cites""" with triple double quotes (`"""`)
==highlight== with double equal signs (`==`)
`inline code` with single/double backticks (`` ` ``)
::user input:: with double colons (`::`)
%variable% with single percent signs (`%`)
:::sample output::: with triple colons (`:::`)
!!text-success|custom span!! with double exclamation marks (`!!`) and a pipe (`|`)
inline μ†ℱ ╋ℯ╳╋ (`μ†ℱ ╋ℯ╳╋`)

```{.example}
Here is one line of **text** _showing_ `inline` styling. Besides italic, bold, and code quilt supports a variety of inline styling:

*italics* with single astrisks (`*`) or underscores (`_`)
**bold** with double astrisks (`**`) or underscores (`__`)
***underlines*** with triple astrisks (`***`) or underscores (`___`)
~~strikethroughs~~ with double tildes (`~~`)
^superscript^ with carets (`^`)
~subscript~ with single tildes (`~`)
--delete-- with double hyphens (`--`)
++insert++ with double pluses (`++`)
---small--- with triple hyphens (`---`)
+++big+++ with triple hyphens (`+++`)
"""cites""" with triple double quotes (`"""`)
==highlight== with double equal signs (`==`)
`inline code` with single/double backticks (`` ` ``)
::user input:: with double colons (`::`)
%variable% with single percent signs (`%`)
:::sample output::: with triple colons (`:::`)
!!text-success|custom span!! with double exclamation marks (`!!`) and a pipe (`|`)
inline μ†ℱ ╋ℯ╳╋ (`μ†ℱ ╋ℯ╳╋`)
```

Multiple lines next to each other will be combined into one paragraph.
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

Lines with a blank line between them will become two paragraphs. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

```{.example}
Multiple lines next to each other will be combined into one paragraph.
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

Lines with a blank line between them will become two paragraphs. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```

Force add blank lines using double percents (`%%`).
%%
This will `<br>` to the output.

```{.example}
Force add blank lines using double percents (`%%`).
%%
This will `<br>` to the output.
```

<p markdown="1" class="alert alert-warning">

`markdown.extensions.nl2br` also adds a `<br>` for each `\n` newline, so `%%` may cause multiple `<br>`s!

</p>

Please not that multiple_underscores_in_a_string will not produce italics (this is helpful for filenames!).

```{.example}
Please not that multiple_underscores_in_a_string will not produce italics (this is helpful for filenames!).
```

> Blockquote paragraphs can
> be created with a greater than
> sign (`>`) before each line.
> > Even nested
> > blockquotes.
>
> A blank line was needed to *unnest* a level.
> ---blockquote examples from """the quilt site"""---

```{.example}
> Blockquote paragraphs can
> be created with a greater than
> sign (`>`) before each line.
> > Even nested
> > blockquotes.
>
> A blank line was needed to *unnest* a level.
> ---blockquote examples from """the quilt site"""---
```

Abbreviations can be used with an inline abbr and an astrisk squared bracket colon (`*[ ]:`) definition somewhere else in the document.

*[abbr]: an abbreviation of abbreviation

```{.example}
Abbreviations can be used with an inline abbr and an astrisk squared bracket colon (`*[ ]:`) definition somewhere else in the document.

*[abbr]: an abbreviation of abbreviation
```

### Lists
**********

Unordered lists can be created with any of the following markers:

* astrisks (`*`)
+ pluses (`+`)
- hyphens (`-`)

```{.example}
* astrisks (`*`)
+ pluses (`+`)
- hyphens (`-`)
```

Ordered lists can be created with:

1. a number
2. a period (`.`)
3. the list item

```{.example}
1. a number
2. a period (`.`)
3. the list item
```

Todo or task lists can be created by adding a square bracket (`[ ]`) checkbox after a hyphen (`-`) marker:

- [x] finished item
- [ ] unfinished item

```{.example}
- [x] finished item
- [ ] unfinished item
```

List items that are separated by blank lines are wrapped with `<p>` tags:

- this is a whole paragraph

- even if it is short

```{.example}
- this is a whole paragraph

- even if it is short
```

Lists can also have some block level styles too (requires item to be indented), like:

-   blockquotes

    > blockquotes in a list

-   code blocks need two indents

        code inside a list

```{.example}  
-   blockquotes

    > blockquotes in a list

-   code blocks need two indents

        code inside a list
```

Markers can be switched from unordered/ordered to create two lists

1. first
2. ordered
3. list

- followed
- by
* one
* ordered
* lists

```{.example}
1. first
2. ordered
3. list

- followed
- by
* one
* ordered
* lists
```

Lists may be nested with indentation

1. an ordered list
2. that contains
    * an unordered list
    * that contains
        1. an ordered list
3. a list may also contain
    - [ ] checkbox
    - [x] lists

```{.example}
1. an ordered list
2. that contains
    * an unordered list
    * that contains
        1. an ordered list
3. a list may also contain
    - [ ] checkbox
    - [x] lists
```


### Links
**********

Create an automatic link, <http://example.com/>, using greater/less than signs (`<>`) that can also be used for <an.email.address@example.com>.  Link cannot be first character on line.

```{.example}
Create an automatic link, <http://example.com/>, using greater/less than signs (`<>`) that can also be used for <an.email.address@example.com>.  Link cannot be first character on line.
```

Specify an [inline link](http://example.com "linky") with square bracket (`[]`) text and parentheses (`()`) url and optional title.

```{.example}
Specify an [inline link](http://example.com "linky") with square bracket (`[]`) text and parentheses (`()`) url and optional title.
```

A [reference link][1] refers to links by an id in square brackets (`[1]`) that is defined somewhere else in the document with `[1]:`

[1]: http://example.com "linky"

```{.example}
A [reference link][1] refers to links by an id in square brackets (`[1]`) that is defined somewhere else in the document with `[1]:`

[1]: http://example.com "linky"
```

Images can by linked with inline or reference using an exclamation mark (`!`) in front of the link.

![alt text](/imgs/icon.png "some relative pathed image"){: .center-block}

```{.example}
![alt text](/imgs/icon.png "some relative pathed image"){: .center-block}
```

A double square bracket (`[[]]`) [[link]] will point to wikipedia

```{.example}
A double square bracket (`[[]]`) [[link]] will point to wikipedia
```


### Code
*********

Inline code is styled with `backticks` (`` ` ``).

```{.example}
Inline code is styled with `backticks` (`` ` ``).
```

    A code block is
    specified by indenting
    each line using
    (4 spaces or a tab)

```{.example}
    A code block is
    specified by indenting
    each line using
    (4 spaces or a tab)
```

A non-indented code block with syntax highlighting may also be specified using *fenced* code where pre formated code is wrapped by three backticks (`` ``` ``) or three tildes (`~~~`) and an optional first line defining the language
```python
def add(a, b):
    """add a and b together"""

    c = a + b

    return c
```

``````{.example}
```python
def add(a, b):
    """add a and b together"""

    c = a + b

    return c
```
``````


### Horizontal Rules
*********************

Horizontal rules are created using three or more astrisks (`*`), hyphens (`-`), or underscores (`_`) (with optional space) on their own line

astrisks

***
* * *

hyphens

---
- - -

underscores

___
_ _ _

```{.example}
astrisks

***
* * *

hyphens

---
- - -

underscores

___
_ _ _
```


### Tables
***********

Tables are build with hyphens (`-`) and pipes (`|`), pipes on the outer right and left are optional.

First Header  | Second Header
--------------|--------------
Content Cell  | Content Cell
Content Cell  | Content Cell

```{.example}
First Header  | Second Header
--------------|--------------
Content Cell  | Content Cell
Content Cell  | Content Cell
```

Right or Left align a column by placing a colon (`:`) on the right or left of the header/cell separator.

First Header  | Second Header
:-------------|-------------:
Content Cell  | Content Cell
Content Cell  | Content Cell

```{.example}
First Header  | Second Header
:-------------|-------------:
Content Cell  | Content Cell
Content Cell  | Content Cell
```

Center align a column by placing colons on both sides of header/cell separator.

First Header  | Second Header
:------------:|:------------:
Content Cell  | Content Cell
Content Cell  | Content Cell


```{.example}
First Header  | Second Header
:------------:|:------------:
Content Cell  | Content Cell
Content Cell  | Content Cell
```

Add attribute lists to the first line after a table.

First Header  | Second Header
:------------:|:------------:
Content Cell  | Content Cell
Content Cell  | Content Cell


{: .table-striped .table-hover .table-condensed}


```{.example}
First Header  | Second Header
:------------:|:------------:
Content Cell  | Content Cell
Content Cell  | Content Cell


{: .table-striped .table-hover .table-condensed}
```


Cells may contain pipes (`|`) if backslash escaped (`\|`).

First Header  | Second Header
:------------:|:------------:
plain \| pipe | `this \| that`
Content Cell  | Content Cell

```{.example}
First Header  | Second Header
:------------:|:------------:
plain \| pipe | `this \| that`
Content Cell  | Content Cell
```


### Definition Lists
*********************

Definition List
:  a list defined by a term followed by a colon (`:`) and the definition of that term

```{.example}
Definition List
:  a list defined by a term followed by a colon (`:`) and the definition of that term
```


### Footnotes
**************

Footnotes can by defined with a square bracket caret number (`[^1]`) [^1] and a `[^1]:` reference somewhere else in the document.  The final location of the footnotes may be set with the `///`@@`footnotes`@@`///` [^2]

[^1]: these are kind of like reference style links
[^2]: otherwise it will be appended to the end of the document.

```{.example}
Footnotes can by defined with a square bracket caret number (`[^1]`) [^1] and a `[^1]:` reference somewhere else in the document.  The final location of the footnotes may be set with the `///`@@`footnotes`@@`///` [^2]

[^1]: these are kind of like reference style links
[^2]: otherwise it will be appended to the end of the document.

///footnotes///
```

///footnotes///


### HTML Capabilities
*********************

Span-level inline HTML <span style="font-size:32px;">*can*</span> be inserted at any point.
Markdown may be used inside span-level inline HTML.

<div class="panel panel-primary">
    <div class="panel-heading">
        <h3 class="panel-title">Block-level inline HTML</h3>
    </div>
    <div class="panel-body">
        <p>Block-level inline HTML is also possible.</p>
        <p>Markdown may <span class="text-danger">*not*</span> be used inside block-level inline HTML</p>
    </div>
</div>

```{.example}
Span-level inline HTML <span style="font-size:32px;">*can*</span> be inserted at any point.
Markdown may be used inside span-level inline HTML.

<div class="panel panel-primary">
    <div class="panel-heading">
        <h3 class="panel-title">Block-level inline HTML</h3>
    </div>
    <div class="panel-body">
        <p>Block-level inline HTML is also possible.</p>
        <p>Markdown may <span class="text-danger">*not*</span> be used inside block-level inline HTML</p>
    </div>
</div>
```

<p markdown="1" class="alert alert-success text-center">
Markdown **may** be wrapped in HTML if the attribute `markdown="1"` is added to the element.
</p>


```{.example}
<p markdown="1" class="alert alert-success text-center">
Markdown **may** be wrapped in HTML if the attribute `markdown="1"` is added to the element.
</p>
```

HTML attributes may be added to markdown by placing an attributes list on the next line (headers and inline go on the same line).
{: #attribute-added .lead}

```{.example}
HTML attributes may be added to markdown by placing an attributes list on the next line (headers have to be on the same line).
{: #attribute-added .lead}
```

### Symbol Shortcuts
********************

Use symbols like `(c)` as shortcuts to certain html entities like (c)

symbol | Character |  `html`
-------|-----------|------------
`(c)`  | (c)       | `&copy;`
`(r)`  | (r)       | `&reg;`
`(tm)` | (tm)      | `&trade;`
`...`  | ...       | `&hellip;`
`--`   | --        | `&ndash;`
`---`  | ---       | `&mdash;`
`+-`   | +-        | `&plusmn;`
`(d)`  | (d)       | `&deg;`
`(o)`  | (o)       | `&deg;`
`1/2`  | 1/2       | `&frac12;`
`1/4`  | 1/4       | `&frac14;`
`3/4`  | 3/4       | `&frac34;`
`(x)`  | (x)       | `&times;`
`(/)`  | (/)       | `&divide;`
`(f)`  | (f)       | `&fnof;`
`(t)`  | (t)       | `&dagger;`
`(tt)` | (tt)      | `&Dagger;`
`(<)`  | (<)       | `&larr;`
`(>)`  | (>)       | `&rarr;`
`(^)`  | (^)       | `&uarr;`
`(v)`  | (v)       | `&darr;`
`(<>)` | (<>)      | `&harr;`
`(oo)` | (oo)      | `&infin;`


``Use symbols like `(c)` as shortcuts to certain html entities like (c)``


```
Use symbols like `(c)` as shortcuts to certain html entities like (c)
```

### \(\LaTeX{}\) Support
****************************

The Lorenz Equations
{: .lead}

$$
    \begin{align}
    \dot{x} & = \sigma(y-x) \\
    \dot{y} & = \rho x - y - xz \\
    \dot{z} & = -\beta z + xy
    \end{align}
$$

The Cauchy-Schwarz Inequality
{: .lead}

$$
    \left( \sum_{k=1}^n a_k b_k \right)^{\!\!2} \leq
    \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
$$

A Cross Product Formula
{: .lead}

$$
    \mathbf{V}_1 \times \mathbf{V}_2 =
    \begin{vmatrix}
    \mathbf{i} & \mathbf{j} & \mathbf{k} \\
    \frac{\partial X}{\partial u} & \frac{\partial Y}{\partial u} & 0 \\
    \frac{\partial X}{\partial v} & \frac{\partial Y}{\partial v} & 0 \\
    \end{vmatrix}
$$

The probability of getting \(k\) heads when flipping \(n\) coins is:
{: .lead}

$$P(E) = {n \choose k} p^k (1-p)^{ n-k}$$

An Identity of Ramanujan
{: .lead}

$$
    \frac{1}{(\sqrt{\phi \sqrt{5}}-\phi) e^{\frac25 \pi}} =
    1+\frac{e^{-2\pi}} {1+\frac{e^{-4\pi}} {1+\frac{e^{-6\pi}}
    {1+\frac{e^{-8\pi}} {1+\ldots} } } }
$$

A Rogers-Ramanujan Identity
{: .lead}

$$
    1 +  \frac{q^2}{(1-q)}+\frac{q^6}{(1-q)(1-q^2)}+\cdots =
    \prod_{j=0}^{\infty}\frac{1}{(1-q^{5j+2})(1-q^{5j+3})},
    \quad\quad \text{for $|q|<1$}.
$$

Maxwell's Equations
{: .lead}

$$
    \begin{align}
    \nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t} & = \frac{4\pi}{c}\vec{\mathbf{j}} \\   \nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \\
    \nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \\
    \nabla \cdot \vec{\mathbf{B}} & = 0
    \end{align}
$$

In-line Mathematics
{: .lead}

Finally, while display equations look good for a page of samples, the ability to mix math and text in a paragraph is also important.  This expression \(\sqrt{3x-1}+(1+x)^2\) is an example of an inline equation.  As you see, MathJax equations can be used this way as well, without unduly disturbing the spacing between lines.

More examples
{: .lead}

$$k_{n+1} = n^2 + k_n^2 - k_{n-1}$$

$$\frac{\frac{1}{x}+\frac{1}{y}}{y-z}$$

$$\cos (2\theta) = \cos^2 \theta - \sin^2 \theta$$

$$\sqrt[n]{1+x+x^2+x^3+\ldots}$$

$$\sum_{i=1}^{10} t_i$$

$$\int_{-\infty}^{\infty} f( x ) e^{2\pi i k} dx$$

$$( a ), [ b ], \{ c \}, | d |, \| e \|, \langle f \rangle, \lfloor g \rfloor, \lceil h \rceil, \ulcorner i \urcorner$$

$$\alpha, A, \beta, B, \gamma, \Gamma, \pi, \Pi, \phi, \varphi, \Phi$$

```
The Lorenz Equations
{: .lead}

$$
    \begin{align}
    \dot{x} & = \sigma(y-x) \\
    \dot{y} & = \rho x - y - xz \\
    \dot{z} & = -\beta z + xy
    \end{align}
$$

The Cauchy-Schwarz Inequality
{: .lead}

$$
    \left( \sum_{k=1}^n a_k b_k \right)^{\!\!2} \leq
    \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
$$

A Cross Product Formula
{: .lead}

$$
    \mathbf{V}_1 \times \mathbf{V}_2 =
    \begin{vmatrix}
    \mathbf{i} & \mathbf{j} & \mathbf{k} \\
    \frac{\partial X}{\partial u} & \frac{\partial Y}{\partial u} & 0 \\
    \frac{\partial X}{\partial v} & \frac{\partial Y}{\partial v} & 0 \\
    \end{vmatrix}
$$

The probability of getting \(k\) heads when flipping \(n\) coins is:
{: .lead}

$$P(E) = {n \choose k} p^k (1-p)^{ n-k}$$

An Identity of Ramanujan
{: .lead}

$$
    \frac{1}{(\sqrt{\phi \sqrt{5}}-\phi) e^{\frac25 \pi}} =
    1+\frac{e^{-2\pi}} {1+\frac{e^{-4\pi}} {1+\frac{e^{-6\pi}}
    {1+\frac{e^{-8\pi}} {1+\ldots} } } }
$$

A Rogers-Ramanujan Identity
{: .lead}

$$
    1 +  \frac{q^2}{(1-q)}+\frac{q^6}{(1-q)(1-q^2)}+\cdots =
    \prod_{j=0}^{\infty}\frac{1}{(1-q^{5j+2})(1-q^{5j+3})},
    \quad\quad \text{for $|q|<1$}.
$$

Maxwell's Equations
{: .lead}

$$
    \begin{align}
    \nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t} & = \frac{4\pi}{c}\vec{\mathbf{j}} \\   \nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \\
    \nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \\
    \nabla \cdot \vec{\mathbf{B}} & = 0
    \end{align}
$$

In-line Mathematics
{: .lead}

Finally, while display equations look good for a page of samples, the ability to mix math and text in a paragraph is also important.  This expression $$\sqrt{3x-1}+(1+x)^2$$ is an example of an inline equation.  As you see, MathJax equations can be used this way as well, without unduly disturbing the spacing between lines.

More examples
{: .lead}

$$k_{n+1} = n^2 + k_n^2 - k_{n-1}$$

$$\frac{\frac{1}{x}+\frac{1}{y}}{y-z}$$

$$\cos (2\theta) = \cos^2 \theta - \sin^2 \theta$$

$$\sqrt[n]{1+x+x^2+x^3+\ldots}$$

$$\sum_{i=1}^{10} t_i$$

$$\int_{-\infty}^{\infty} f( x ) e^{2\pi i k} dx$$

$$( a ), [ b ], \{ c \}, | d |, \| e \|, \langle f \rangle, \lfloor g \rfloor, \lceil h \rceil, \ulcorner i \urcorner$$

$$\alpha, A, \beta, B, \gamma, \Gamma, \pi, \Pi, \phi, \varphi, \Phi$$
```

### Escaping
************

Escape these characters with a backslash (`\`):

+ `\` backslash
+ `` ` `` backtick
+ `*` astrisk
+ `_` underscore
+ `{}` curly braces
+ `[]` square brackets
+ `()` parentheses
+ `#` hash mark
+ `+` plus sign
+ `-` minus sign (hyphen)
+ `.` dot
+ `!` exclamation mark


### Table of Contents
*********************

All headings will be used to generate a table of contents and placed at `[TOC]`. See the [table of contents](#post) at the top of the page.

### Read the Source
********************

Replacing `html` with `md` in the url with load the original markdown source.
{:.lead}

<div class="alert alert-warning">
<h4>Caveats</h4>
<ol>
    <li><code>markdown.extensions.footnotes</code> was edited to allow custom footnote placement.</li>
    <li><code>markdown.extensions.codehilite</code> was edited to allow language and guessed language class.</li>
    <li><code>markdown.extensions.tables</code> was edited to splits row based on more robust <code>regex</code> to ignore escaped backslash (<code>\|</code>).</li>
    <li><code>markdown.extensions.tables</code> was edited to allow attribute lists to be defined on first line after table.</li>
</ol>
</div>

</div>
