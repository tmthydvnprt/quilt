title:       Quilt: A python based static site html stitcher.
date:        3/1/2015 3:15 pm
description: initial development release (0.1.0)
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
A `python` based static site `html` _stitcher_.
{: .lead}

Description
:  Generate a static site via `python` from content-only `.html` and `.md` pages that are _stitched_ together  along with patch (e.g. `nav.html`, `footer.html`) files onto a main site `quilt.html` file.  

Code Examples
 : Quilt a site located at `path/to/site/source/files`.
```
:::python
from quilt.Quilting import QuiltingRoom

q = QuiltingRoom('path/to/site/source/files')
q.quilt()
```
</div>
