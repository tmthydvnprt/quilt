"""
quilt.Constants

Formatable strings and default objects, maybe a list or two.
{: .lead}

"""

import re
import nltk

# english stop words
STOPWORDS = set(nltk.corpus.stopwords.words('english'))
#PUNCTUATION = set(list(string.punctuation) + ['\''])

# compiled general regex
WORD_RE = re.compile(r'^\w+$')
#ALPHA_RE = re.compile(r'^[a-zA-Z_]+$')
DOTSTAR_RE = re.compile(r'.*')
#PUNCT_RE = re.compile(r'[!#"%$\'&)(+*\-,/.;:=<?>@\[\]\\_\^`{}|~]+')
#NUM_RE = re.compile(r'[0-9]+')
#UNI_ESCAPE_RE = re.compile(r'x[0-9]+[A-Za-z]')
#HEX_RE = re.compile(r'[\\0&]?x|U+[A-Fa-f0-9]+;?')

# compiled regex to split page files into page variables, html, script
FIRST_KEY_RE = re.compile(r'[A-Za-z0-9_-]+:')
FIRST_EMPTY_LINE_RE = re.compile(r'\n\s*\n')
JS_HTML_PATTERN_RE = re.compile(r'(>tpircs/<.*>tpircs<)?(.*)', re.DOTALL)
KEY_VALUE_RE = re.compile(r'^[ ]{0,3}(?P<key>[A-Za-z0-9_-]+):\s*(?P<value>.*)')
VALUE_RE = re.compile(r'^[ ]{4,}(?P<value>.*)')

# compiled "handlebar" pagevars
PAGEVAR_RE = re.compile(r'{{(.*?)}}')
ESCAPED_PAGEVAR_RE = re.compile(r'{ {(.*?)}}')
PAGEVAR_SEARCH_RE = re.compile(r'(.*?){ ?{(.*?)}}(.*?)')

# compiled regex for assets
CSS_EXT_RE = re.compile(r"\.css$")
ROOT_LEVEL_JS_EXT_RE = re.compile(r"{{relativepath}}js/.*\.js$")

# compiled regex for minimization
BLOCK_COMMENT_RE = re.compile(r'/\*(?!\!)(.*?)\*/', re.DOTALL)
LINE_COMMENT_RE = re.compile(r'^\s*//(?!\!).*$\n', re.MULTILINE)
KEEP_COMMENT_RE = re.compile(r'(/\*!.*?\*/)', re.DOTALL)
OPTIONAL_CARRIAGE_RETURN_RE = re.compile(r'\r\n?')
MORE_THAN_ONE_NEWLINE_RE = re.compile(r'\n+', re.MULTILINE)
MORE_THAN_ONE_WHITESPACE_RE = re.compile(r'\s+')
SPACED_EQUAL_RE = re.compile(r' ?= ?')
SPACED_COLON_RE = re.compile(r' ?: ?')
CLEAN_SELECTORS_RE = re.compile(r'(^|\})([^{]+):([^{]+\{)')
CLEAN_SELECTORS2_RE = re.compile(r'\s+([!{};:>+\(\)\],])')
SELECTORCOLON_RE = re.compile(r'___SELECTORCOLON___')
CHARSETS_RE = re.compile(r'^(.*)(@charset "[^"]*";)')
CHARSETS2_RE = re.compile(r'^(\s*@charset [^;]+;\s*)+')
MEDIA_RE = re.compile(r'(@media[^{]*[^\s])\(')
EXTRA_SPACES_RE = re.compile(r'([!{}:;>+\(\[,])\s+')
MISSING_SEMICOLON_RE = re.compile(r'([^;\}])}')
ZERO_UNITS_RE = re.compile(r'([\s:])(0)(px|em|%|in|cm|mm|pc|pt|ex)')
FOUR_ZEROS_RE = re.compile(r':0 0 0 0;')
THREE_ZEROS_RE = re.compile(r':0 0 0;')
TWO_ZEROS_RE = re.compile(r':0 0;')
BG_ZERO_RE = re.compile(r'background-position:0;')
LEADING_ZERO_DECIMAL_RE = re.compile(r'(:|\s)0+\.(\d+)')
MORE_THAN_ONE_SEMICOLON_RE = re.compile(r';;+')
SEMICOLON_CLOSE_BRACE_RE = re.compile(r';}')
EMPTY_BRACES_RE = re.compile(r'[^}]+{}')

# tags for markdown inline match
MD_INLINE_TAGS = {
    '***' : 'u',
    '___' : 'u',
    '"""' : 'cite',
    ':::' : 'samp',
    '+++' : 'big',
    '---' : 'small',
    '::'  : 'kbd',
    '++'  : 'ins',
    '--'  : 'del',
    '=='  : 'mark',
    '~~'  : 's',
    '~'   : 'sub',
    '%'   : 'var',
    '^'   : 'sup'
}
# tags for simple replacement
REPLACE_TAGS = {
    '%%' : 'br',
    '@@' : 'i'
}
# symbol html replacement
SYMBOLS = {
    '(c)'       : '%scopy;',
    '(r)'       : '%sreg;',
    '(tm)'      : '%strade;',
    '...'       : '%shellip;',
    '--'        : '%sndash;',
    '---'       : '%smdash;',
    '+-'        : '%splusmn;',
    '(d)'       : '%sdeg;',
    '(o)'       : '%sdeg;',
    '1/2'       : '%sfrac12;',
    '1/4'       : '%sfrac14;',
    '3/4'       : '%sfrac34;',
    '(x)'       : '%stimes;',
    '(/)'       : '%sdivide;',
    '(f)'       : '%sfnof;',
    '(t)'       : '%sdagger;',
    '(tt)'      : '%sDagger;',
    '(<)'       : '%slarr;',
    '(>)'       : '%srarr;',
    '(^)'       : '%suarr;',
    '(v)'       : '%sdarr;',
    '(<>)'      : '%sharr;',
    '(oo)'      : '%sinfin;'
}

# match [x], [X] or [ ] in list item for checkbox
CHECKBOX_RE = r'<li>\[([ Xx])\]'
# match !! class | text !!
CUSTOM_CLS_RE = r'[!]{2}(?P<class>.+?)[|](?P<text>.+?)[!]{2}'
# match double %% @@
REPLACE_TAGS_RE = r'( {} )'.format(r' | '.join([re.escape(x) for x in REPLACE_TAGS.keys()]))
# $$...$$ \(...\) \[...\]
MATHS_RE = r'(\$\$|\\\(|\\\[)(.+?)(\$\$|\\\)|\\\])'
# match *** ___ """ ::: +++ --- :: ++ -- == ~~ ~ %
MULTIMATCH_RE = r'({})(.*?)\2'.format(r'|'.join([re.escape(x) for x in MD_INLINE_TAGS.keys()]))
# match for symbols
SYMBOLS_RE = r'({})'.format(r'|'.join([re.escape(x) for x in SYMBOLS.keys()]))

# quilting logo, yeah!
QUILTHEADER = """,,,,,,,
;#~#~#; quilt
;~#~#~; source : %s
;#~#~#; time   : %s
'''''''"""
# comment put in head if config["quiltcomment"] is True
QUILTCOMMENT = """
    -- """ + "~"*64 + """
    -- Page stitched together with quilt.py
    -- url            : %s
    -- quilted on     : %s
    -- stitching took : %s s
%s
    -- """ + "~"*64 + """
"""
# comment put between asset source if config["assetcomment"] is True
ASSETCOMMENT = """/*!
 * """ + "~"*64 + """
 * asset %s combined on %s
 * """ + "~"*64 + """
 */"""
# comment to put between patches
PATCHCOMMENT = """quilted %s patch"""
# script to add with page object in js
PAGEOBJ = """
<script>
pagevars = %s;
</script>"""

# size of random placeholder for minimize code
PLACEHOLDER_SIZE = 64
# sitemap strings
SITEMAPINDEX = """<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <sitemap>
        <loc>%s</loc>
        <lastmod>%s</lastmod>
    </sitemap>
    <sitemap>
</sitemapindex>"""
SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
%s
</urlset>"""
SITEMAPURL = """    <url>
        <loc>%s</loc>
        <lastmod>%s</lastmod>
        <changefreq>%s</changefreq>
        <priority>%s</priority>
    </url>
"""
# atom xml strings
ATOMXML = """<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
    <title>%s Feed</title>
    <subtitle>%s</subtitle>
    <link href="%s/feed/" rel="self"/>
    <link href="%s"/>
    <id>%s</id>
    <updated>%s</updated>
    %s
</feed>"""
ATOMENTRY = """    <entry>
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
"""
# rss xml strings
RSSXML = """<?xml version="1.0" encoding="utf-8"?>
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
</rss>"""
RSSITEM = """   <item>
        <title>%s</title>
        <link>%s</link>
        <guid>%s</guid>
        <pubDate>%s</pubDate>
        <description>%s</description>
    </item>
"""
# post link strings
POSTLIST = """<div class="container">
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
"""
POST = """  <li class="post-link list-group-item">
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
"""
NO_NEW_POSTS = "There are no newer posts"
NO_OLD_POSTS = "There are no earlier posts"
# post link strings
GROUPLIST = """<div class="container">
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
"""
GROUP = """  <li class="%s-link">
        <h3><a href="%s">%s</a> <span class="badge">%s posts</span></h3>
    </li>
"""
GROUPLINK = """<li class="%s"><a href="%s" class="label label-success">%s</a></li>
"""
TAG_CATEGORY = """<div class="container">
    <div class="row">
        <div class="col-sm-8 col-sm-offset-2">
            <hr>
            <div class="col-sm-6">%s</div>
            <div class="col-sm-6">%s</div>
        </div>
    </div>
</div>
"""
GROUPVARS = """title: %s
description: %s
author: %s

"""
# robot.txt string
ROBOTTXT = """# Sitemap location
Sitemap: %s/sitemap.xml

# Allow crawling of all content
User-agent: *
Disallow:
"""
