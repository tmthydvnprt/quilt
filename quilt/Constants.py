"""
quilt.Constants

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
FIRST_KEY_RE = re.compile(r'[A-Za-z0-9_-]+[ \t]*:')
FIRST_EMPTY_LINE_RE = re.compile(r'\n\s*\n')
JS_HTML_PATTERN_RE = re.compile(r'(>tpircs/<.*>tpircs<)?(.*)', re.DOTALL)
KEY_VALUE_RE = re.compile(r'^[ ]{0,3}(?P<key>[A-Za-z0-9_-]+)[ \t]*:\s*(?P<value>.*)')
VALUE_RE = re.compile(r'^[ ]{4,}(?P<value>.*)')

# compiled regex for finding true
TRUE_RE = re.compile(r'[Tt]rue')

# compiled "handlebar" pagevars
PAGEVAR_RE = re.compile(r'{{(.*?)}}')
ESCAPED_PAGEVAR_RE = re.compile(r'{ {(.*?)}}')

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

# compiled regex for text analysis
WHITESPACE_RE = re.compile(r'\s')
EXT_LINK = re.compile(r'((?:[Ff]|[Hh][Tt])[Tt][Pp][Ss]?://[^>]*)')

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
# ignore these files when building sitemap
SITEMAP_IGNORE = {'sourcehash.pkl', 'sitemapindex.xml', 'sitemap.xml'}
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
QUILTHEADER = """,,,,,,, quilt %s
;#~#~#; source : %s
;~#~#~; branch : %s
;#~#~#; hash   : %s
''''''' time   : %s
"""
# comment put in head if config["quiltcomment"] is True
QUILTCOMMENT = """
""" + "~"*64 + """
Page stitched together with quilt:
quilt          : %s
url            : %s
quilted on     : %s
source branch  : %s
source hash    : %s
stitching took : %s s%s
""" + "~"*64 + """
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

PAGEVARS_TO_PRINT = '''author
categories
copydate
copyrighter
date
description
directory
disable_last
disable_next
domain
email
keywords
last_post
last_title
latestpostlink
markdownlink
name
next_post
next_title
page_path
relativepath
tags
title
url
post-length
post-characters
post-lines
post-words
post-symbols
post-numbers
post-diversity
post-sentences
post-questions
post-extlinks
post-intlinks
post-anchors
post-images
post-headers'''.split('\n')

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
NO_NEW_POSTS = "There are no newer posts"
NO_OLD_POSTS = "There are no earlier posts"

GROUPLINK = """<li class="%s"><a href="%s" class="group-link">%s</a></li>
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
GROUP_SINGLE_NAME = {
    'tags'      : 'tag',
    'categories': 'category',
    'featured'  : 'featured'
}
GROUP_VERBS = {
    'tags'      : 'tagged with',
    'categories': 'categorized in',
    'featured'  : 'featured'
}

# robot.txt string
ROBOTTXT = """# Sitemap location
Sitemap: %s/sitemap.xml

# Allow crawling of all content
User-agent: *
Disallow:
"""
