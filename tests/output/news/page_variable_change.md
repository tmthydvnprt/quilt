title:       Page Variable Change
date:        3/9/2015 8:31 am
description: release memo (0.1.1)
author:      tim
categories:  release
tags:        quilt
             python
             release

# {{title}} <br><small>{{description}}</small>
by {{author}} <small>on {{date}}</small>
{: .h4}
****************************************************************************************************************

<div id="post" markdown="1">
The syntax for page variable headers changed from `json`  to `key: value` plaintext. The method follows [MultiMarkdown's metadata](https://github.com/fletcher/MultiMarkdown/wiki/MultiMarkdown-Syntax-Guide#metadata)
{: .lead}

key
:    `[A-Za-z0-9_-]+` from beginning of line until `:`

value
:    a string per line, where multiline values become arrays

notes
:    `key: value` **must** be first (no whitespace before it), and ends at first empty (whitespace-only) line.

For example the page variables of this page are written as
```
title:       Page Variable Change
date:        3/9/2015 8:31 am
description: release memo (0.1.1)
author:      tim
categories:  release
tags:        quilt
             python
             release

```
</div>
