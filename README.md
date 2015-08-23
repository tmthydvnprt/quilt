Quilt
=====

What is quilt? — another static site generator
----------------------------------------------
Generate a static site via python from content-only html and markdown pages that are stitched together along with patch (e.g. nav.html, footer.html) files onto a main site quilt.html file. http://tmthydvnprt.github.io/quilt

### Why?
Cause there's a bunch of other static site generators already!

#### Because I wanted...
1. specific features
2. something I didn't see in others
3. to improve python fluency
4. homegrown customization

### Notable features
- [x] focus on page content, site features (head, navbar, footer) are written & stored separately
- [x] write content in <mark>`html` or `markdown`</mark>
- [x] extensible markdown for custom needs
- [x] <mark>LaTeX Support</mark>
- [x] unique template overrides in each directory
- [x] automatically fill `alt`/`img` attributes, and remove empty tags
- [x] automatically vendorize, minimize, & combine `css` and `js` files
- [x] automatically create certain files (`robot.txt`, `sitemap.xml`, multiple sized favicons, etc.)
- [x] provide some dynamic blogy abilities (reverse chronology, tags, categories)
- [x] create atom/rss feeds
- [x] index the text of final site for searching (e.g. with typeahead)
- [ ] <mark>potential for `nltk` integration</mark>
- [x] spell checking
- [x] Check out all the features and what's coming up on the features+todo page.
- [ ] <mark>parallel processing</mark>
- [ ] `git` integration (pull modify dates from repo commits)
- [ ] *any ideas?*
- [ ]

Check out all the features and what's coming up on the [features+todo](http://tmthydvnprt.com/quilt/features_todo.html) page

### Want an example?
This [site](http://tmthydvnprt.github.io/quilt) was stitched with quilt! Download or inspect the [source](https://github.com/tmthydvnprt/quilt/tree/master/tests).

### Want to learn more?
Get an overview on the [about(readme)](http://tmthydvnprt.com/quilt/readme.html) page, or read the [documentation](http://tmthydvnprt.com/quilt/docs/index.html).
