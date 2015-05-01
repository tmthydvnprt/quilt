"""
quilt.Util

Utility functions
{: .lead}

Helper functions used all over, but don't belong anywhere.

"""

import os
import sys
import bs4
import copy
import nltk
import numpy as np
import string
import codecs
import fnmatch
import urlparse
import datetime as dt

from quilt.Constants import STOPWORDS, PLACEHOLDER_SIZE # , PUNCTUATION, NUM_RE, PUNCT_RE, UNI_ESCAPE_RE, HEX_RE
from quilt.Constants import BLOCK_COMMENT_RE, LINE_COMMENT_RE, KEEP_COMMENT_RE, OPTIONAL_CARRIAGE_RETURN_RE
from quilt.Constants import MORE_THAN_ONE_NEWLINE_RE, MORE_THAN_ONE_WHITESPACE_RE, SPACED_EQUAL_RE, SPACED_COLON_RE
from quilt.Constants import CLEAN_SELECTORS_RE, CLEAN_SELECTORS2_RE, SELECTORCOLON_RE, CHARSETS_RE, CHARSETS2_RE
from quilt.Constants import MEDIA_RE, EXTRA_SPACES_RE, MISSING_SEMICOLON_RE, ZERO_UNITS_RE, FOUR_ZEROS_RE
from quilt.Constants import THREE_ZEROS_RE, TWO_ZEROS_RE, BG_ZERO_RE, LEADING_ZERO_DECIMAL_RE
from quilt.Constants import MORE_THAN_ONE_SEMICOLON_RE, SEMICOLON_CLOSE_BRACE_RE, EMPTY_BRACES_RE
from quilt.Constants import GROUPLINK, WORD_RE

# default config, overridden by config.json in source directory
DEFAULT_CONFIG = {
    # project variables
    # -----------------------------------------------------------------------------------
    "name"        : "some name",            # site or project name
    "domain"      : "some_name.com",        # site domain
    "title"       : "some default title",   # default page title
    "author"      : "you",                  # site author
    "email"       : "you@some_name.com",    # site author's email
    "description" : "default description",  # default page description
    "keywords"    : [],                     # default page keywords
    "categories"  : [],                     # page categories
    "tags"        : [],                     # page tags
    "changefreq"  : "monthly",              # sitemap changefreq
    "priority"    : "0.5",                  # sitemap priority
    "blogname"    : "quilt news",           # atom id
    "atomid"      : "randomid",             # atom id
    "rssid"       : "randomid",             # rss id
    "copydate"    : dt.datetime.now().year, # copyright dates (auto extend to now)
    "copyrighter" : "you",                  # copyright owner
    # configuration
    # -----------------------------------------------------------------------------------
    "local"       : False,                  # use local disk paths as urls (dev)
    "patchcomment": True,                   # comment identifying patch
    "quiltcomment": True,                   # head comment with page info
    "assetcomment": True,                   # comment asset source when combining
    "pagecomment" : True,                   # put page variables in head comment
    "pageobject"  : True,                   # put page variables in js object
    "copymd"      : True,                   # copy original markdown to output
    "combinecss"  : True,                   # combine all `css` into one
    "combinejs"   : True,                   # combine all `js` into one
    "vendorfycss" : True,                   # auto add vendor prefixes
    "minimizecss" : True,                   # minimize `css`
    "minimizejs"  : True,                   # minimize `js`
    "buildindex"  : True,                   # add `index.html` to directories w/o it
    "buildrobot"  : True,                   # add robot.txt
    "buildsearch" : True,                   # build words to url index (for `typeahead`)
    "buildsitemap": True,                   # create sitemap
    "buildblog"   : True,                   # add blog abilities to `posts/` directory
    "buildatom"   : True,                   # create atom feed
    "buildrss"    : True,                   # create rss feed
    "buildicon"   : True,                   # create favicon
    "iconsizes"   : [64, 60, 76, 120, 152], # image sizes to create
    "spellcheck"  : True,                   # spell check after quilting
    "spellignore" : ["maths", "codehilite"],# classes to ignore spelling
    # file and directory names
    # -----------------------------------------------------------------------------------
    "quilt"       : "quilt.html",           # name of quilt file
    "patches"     : "patches",              # patches directory
    "pages"       : "pages",                # pages directory
    "templates"   : "templates",            # templates directory
    "assets"      : "assets",               # assets directory
    "posts"       : "posts",                # post directory in `pages/` directory
    "feed"        : "feed",                 # post directory in `pages/` directory
    "images"      : "imgs",                 # image directory in `assets/` directory
    "iconfile"    : "icon.png",             # image for favicon
    "correctwords": "correct_words.txt",    # correctly spelled unique user words
    # file types
    # -----------------------------------------------------------------------------------
    "patch_ext"   : ["*.html"],             # allowable patch extension
    "page_ext"    : ["*.html", "*.md"],     # allowable page extension
    "template_ext": ["*.html"],             # allowable template extension
    "asset_ext"   : ["*.*"]                 # allowable resource extension
}

VENDORS = ['-webkit-', '-moz-', '-ms-', '-o-']
PREFIXES = ['transform', 'transition', 'animation', 'perspective', 'padding-start', 'padding-end']
AT_RULES = ['keyframes']

NO_EMPTY_TAGS = [
    'section', 'article', 'header', 'footer', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hgroup', 'nav', 'aside', 'div',
    'main', 'p', 'pre', 'bockquote', 'ol', 'ul', 'li', 'a', 'abbr', 'cite', 'code', 'b', 'strong', 'em', 's', 'q',
    'small', 'samp', 'u', 'time', 'var', 'sup', 'sub', 'kdb', 'mark', 'dl', 'dt', 'dd', 'table', 'thead', 'td', 'tr',
    'th', 'tbody', 'tfooter'
]

HEAD_STRAINER = bs4.SoupStrainer("head")
BODY_STRAINER = bs4.SoupStrainer("body")

A_LINK_SET = {'a', 'link'}
STRING_POPULATION = np.array(list(string.uppercase + string.lowercase + string.digits))

#@profile
def read_file(file_path='', encoding='utf-8'):
    """read a file into a string. assumes utf-8 encoding."""
    if os.path.exists(file_path):
        fid = codecs.open(file_path, mode='r', encoding=encoding)
        source = fid.read()
        fid.close()
    else:
        source = ''
    return source

#@profile
def write_file(file_path='', data=''):
    """write a file from a string. ~~string is utf encoded before~~"""
    fid = codecs.open(file_path, 'w')
    fid.write(data)
    fid.close()

##@profile
#def load_files(source='', extensions=''):
#    """load all files matching 0.002274 """
#    loaded_files = {}
#    for dirpath, _, files in os.walk(source):
#        for ext in extensions:
#            for f in fnmatch.filter(files, ext):
#                loaded_files[os.path.splitext(f)[0]] = read_file(os.path.join(dirpath, f))
#    return loaded_files
#@profile
def load_files(source='', extensions=''):
    """load all files matching 0.002274 """
    return {os.path.splitext(f)[0]: read_file(os.path.join(dirpath, f)) \
            for dirpath, _, files in os.walk(source) \
                for ext in extensions \
                    for f in fnmatch.filter(files, ext)}

#@profile
def check_local_quilt(page='', quilt_pattern=None, default_patches=None, config=None):
    """check for directory quilt and directory patches?"""

    # check for directory quilt?
    dir_quilt = os.path.join(os.path.dirname(page), os.path.basename(config['quilt']))
    if os.path.exists(dir_quilt):
        dir_quilt_text = read_file(dir_quilt)
        quilt = dir_quilt_text
    else:
        quilt = quilt_pattern

    # check for directory patches?
    patches = copy.deepcopy(default_patches)
    dir_patch = os.path.join(os.path.dirname(page), os.path.basename(config['patches']))
    if os.path.exists(dir_patch):
        dir_patches = load_files(dir_patch, config['patch_ext'])
        patches.update(dir_patches)

    return (quilt, patches)

##@profile
#def get_file_names(source='', extensions=''):
#    """get all file names matching"""
#
#    file_names = set()
#    for dirpath, _, files in os.walk(source):
#        if os.path.basename(dirpath) != 'patches':
#            for ext in extensions:
#                for f in fnmatch.filter(files, ext):
#                    if f != 'quilt.html':
#                        file_names.update([os.path.join(dirpath, f)])
#
#    return file_names

#@profile
def get_file_names(source='', extensions=''):
    """get all file names matching 0.008896 """
    return {os.path.join(dirpath, f) \
            for dirpath, _, files in os.walk(source) if os.path.basename(dirpath) != 'patches' \
                for ext in extensions \
                    for f in fnmatch.filter(files, ext) if f != 'quilt.html'}

#@profile
def relative_path(filepath='', rootpath=''):
    """get relative path between a root and file"""

    relpath = os.path.dirname(filepath.replace(rootpath, ''))
    relcount = relpath.count('/') if relpath != '/' else relpath.count('/') - 1
    return '../' * relcount

#@profile
def find_hrefsrc(soup, tag_name='', re_pattern=None):
    """search a soup for pattern in href or src of tag"""

    attr = 'href' if tag_name in A_LINK_SET else 'src'
    tags = soup.find_all(tag_name)
    url = [tag.attrs[attr] for tag in tags if attr in tag.attrs and re_pattern.findall(tag.attrs[attr])]

    return url

#@profile
def path_link_list(path_string='', file_name=''):
    """create lists of links for each level in a path"""

    post_paths = path_string.split('/')[1:]
    path_list = []
    for j, post_path in enumerate(post_paths):
        if j == len(post_paths)-1:
            path_list.append('<li class="active">' + file_name + '</li>')
        else:
            url = '../' * (len(post_paths)-2-j) + 'index.html'
            path_list.append('<li><a href="%s">%s</a></li>' % (url, post_path))

    return '\n'.join(path_list)

#@profile
def filter_external_url(urls=None, domain=''):
    """filter file list for external assets"""
    return [url for url in urls if domain in urlparse.urlparse(url).netloc or urlparse.urlparse(url).netloc == '']

#@profile
def random_placeholder(size=PLACEHOLDER_SIZE):
    """return a random string of numbers and digits 0.00515 """
    return ''.join(np.random.choice(STRING_POPULATION, size=size))
#    return ''.join(random.SystemRandom().choice(STRING_POPULATION) for _ in xrange(size))

#@profile
def minimize_js(js=''):
    """minimize js file"""

    # remove carriage returns
    js = OPTIONAL_CARRIAGE_RETURN_RE.sub(r'\n', js)
    # remove comment blocks, everything between /* and */ and //, unless it has ! as first character....
    js = BLOCK_COMMENT_RE.sub(r'', js)
    js = LINE_COMMENT_RE.sub(r'', js)

    # remove and store /*! ...*/ comments
    saved_comments = {}
    for comment in KEEP_COMMENT_RE.findall(js):
        placeholder = random_placeholder()
        js = js.replace(comment, placeholder)
        saved_comments[placeholder] = comment

    # normalize equals
    js = SPACED_EQUAL_RE.sub(r'=', js)
    # normalize colons
    js = SPACED_COLON_RE.sub(r':', js)

    # normalize whitespace
    js = MORE_THAN_ONE_WHITESPACE_RE.sub(r' ', js)
    js = MORE_THAN_ONE_NEWLINE_RE.sub(r'', js)

    # replace /*! ...*/ comments
    for placeholder, comment in saved_comments.items():
        js = js.replace(placeholder, '\n'+ comment +'\n')

    # Trim the final string (for any leading or trailing white spaces)
    js = js.strip()

    return js

#@profile
def minimize_css(css=''):
    """minimize css file ported from https://github.com/isaacs/cssmin/blob/master/rules.txt"""

    # remove carriage returns
    css = OPTIONAL_CARRIAGE_RETURN_RE.sub(r'\n', css)

    # remove comment blocks, everything between /* and */ and //, unless it has ! as first character....
    css = BLOCK_COMMENT_RE.sub(r'', css)

    # remove and store /*! ...*/ comments
    saved_comments = {}
    for comment in KEEP_COMMENT_RE.findall(css):
        placeholder = random_placeholder()
        css = css.replace(comment, placeholder)
        saved_comments[placeholder] = comment

    # normalize whitespace
    css = MORE_THAN_ONE_WHITESPACE_RE.sub(r' ', css)

    # Remove the spaces before the things that should not have spaces before them.
    # But, be careful not to turn "p :link {...}" into "p:link{...}"
    # Swap out any selector colons with a token, and then swap back.
    css = CLEAN_SELECTORS_RE.sub(r'\1\2___SELECTORCOLON___\3', css)
    css = CLEAN_SELECTORS2_RE.sub(r'\1', css)
    css = SELECTORCOLON_RE.sub(r':', css)

    # If there is a @charset, then only allow one, and push to the top of the file.
    css = CHARSETS_RE.sub(r'\2\1', css)
    css = CHARSETS2_RE.sub(r'\1', css)

    # Put the space back in some cases, to support stuff like
    # @media screen and (-webkit-min-device-pixel-ratio:0){
    # where @media screen and(-webkit-...){ would fail.
    css = MEDIA_RE.sub(r'\1 (', css)

    # Remove the spaces after the things that should not have spaces after them.
    css = EXTRA_SPACES_RE.sub(r'\1', css)

    # Add the semicolon where it's missing. This is no longer necessary,
    # and will be removed later, but it makes a few of the next rules simpler.
    css = MISSING_SEMICOLON_RE.sub(r'\1;}', css)

    # Replace 0(px,em,%) with 0.
    css = ZERO_UNITS_RE.sub(r'\1\2', css)

    # Replace 0 0 0 0; with 0.
    css = FOUR_ZEROS_RE.sub(r':0;', css)
    css = THREE_ZEROS_RE.sub(r':0;', css)
    css = TWO_ZEROS_RE.sub(r':0;', css)

    # Replace background-position:0; with background-position:0 0;
    # since we just broke that with the last bit.
    css = BG_ZERO_RE.sub(r'background-position:0 0;', css)

    # Replace 0.6 to .6, but only when preceded by : or a white-space
    css = LEADING_ZERO_DECIMAL_RE.sub(r'\1.\2', css)

    # 	# Shorten colors from rgb(51,102,153) to #336699
    # 	# This makes it more likely that it'll get further compressed in the next step.
    # 	each 'rgb\(([0-9]{1,3})(,[0-9]{1,3}){2}\)'
    # 		replace '([0-9]{1,3})'/' hex('\1')
    # 		replace 'rgb\(([A-F0-9]{6})\)' '#\1'
    # 	end

    # 	# normalize #aBc to #ABC.  These will be in groups of either 3 or 6
    # 	css = re.sub('#([a-fA-F0-9]{3}){1,2}', uppercase('\0'), css)

    # Shorten colors from #AABBCC to #ABC. Note that we want to make sure
    # the color is not preceded by either ", " or =. Indeed, the property
    #	 filter: chroma(color="#FFFFFF");
    # would become
    #	 filter: chroma(color="#FFF");
    # which makes the filter break in IE.
    # 	css = re.sub('([^"\'=\s])(\s*)([0-9A-F])\3([0-9A-F])\4([0-9A-F])\5', '\1\2\3\4\5', css)

    # Replace multiple semi-colons in a row by a single one
    # See SF bug #1980989
    css = MORE_THAN_ONE_SEMICOLON_RE.sub(r';', css)

    # Remove the final semicolons
    css = SEMICOLON_CLOSE_BRACE_RE.sub(r'}', css)

    # Remove empty rules.
    css = EMPTY_BRACES_RE.sub(r'', css)

    # replace /*! ...*/ comments
    for placeholder, comment in saved_comments.items():
        css = css.replace(placeholder, '\n'+ comment +'\n')

    # Trim the final string (for any leading or trailing white spaces)
    css = css.strip()

    return css

#Total time: 0.017315 s
#Function: parse_css_blocks at line 352
#
#Line #      Hits         Time  Per Hit   % Time  Line Contents
#==============================================================
#   352                                           #@profile
#   353                                           def parse_css_blocks(css=''):
#   354                                               """parse css string into css blocks {...}"""
#   355
#   356         2            1      0.5      0.0      temp = ''
#   357         2            0      0.0      0.0      block = []
#   358         2            0      0.0      0.0      stack = []
#   359      8576         3690      0.4     21.3      for c in css:
#   360      8574         4439      0.5     25.6          if c == '{':
#   361       106          125      1.2      0.7              stack.append([temp, []])
#   362       106           45      0.4      0.3              temp = ''
#   363      8468         4303      0.5     24.9          elif c == '}':
#   364       106           48      0.5      0.3              if not stack[-1][-1]:
#   365       106           55      0.5      0.3                  stack[-1][-1] = temp
#   366       106           32      0.3      0.2                  temp = ''
#   367       106           55      0.5      0.3              if len(stack) > 1:
#   368                                                           t = stack.pop()
#   369                                                           stack[-1][-1].append(t)
#   370                                                       else:
#   371       106          136      1.3      0.8                  block.append(stack.pop())
#   372                                                   else:
#   373      8362         4385      0.5     25.3              temp += c
#   374         2            1      0.5      0.0      return block

#@profile
def parse_css_blocks(css=''):
    """parse css string into css blocks {...} 0.017315 """

    temp = []
    block = []
    stack = []
    for c in css:
        if c == '{':
            stack.append([''.join(temp), []])
            temp = []
        elif c == '}':
            if not stack[-1][-1]:
                stack[-1][-1] = ''.join(temp)
                temp = []
            if len(stack) > 1:
                t = stack.pop()
                stack[-1][-1].append(t)
            else:
                block.append(stack.pop())
        else:
            temp.append(c)
    return block

#@profile
def vendorfy_at_prefix(blck=None, at_prefix=None):
    """handle @prefix rules"""

    b0vender = []
    b1vender = []
    for vendor in VENDORS:
        b1vender = []
        for b in blck[1]:
            b11vender = []
            for props in b[1].split(';'):
                prefix = [p for p in PREFIXES if p in props]
                if prefix:
                    b11vender.append(props.replace(prefix[0], vendor+prefix[0]))
                else:
                    b11vender.append(props)
            b1vender.append([b[0], ';'.join(b11vender)])
        b0vender.append([blck[0].replace(at_prefix[0], vendor+at_prefix[0]), b1vender])
    b0vender.append(blck)

    return b0vender

#@profile
def vendorfy_block_list(blck=None):
    """handle block"""

    b1vender = []
    for b in blck[1]:
        b11vender = []
        for props in b[1].split(';'):
            prefix = [p for p in PREFIXES if p in props]
            if prefix:
                for vendor in VENDORS:
                    b11vender.append(props.replace(prefix[0], vendor+prefix[0]))
                b11vender.append(props)
            else:
                b11vender.append(props)
        b1vender.append([b[0], ';'.join(b11vender)])
    return b1vender

#@profile
def vendorfy_block(blck=None):
    """handle block"""

    b1vender = []
    for props in blck[1].split(';'):
        prefix = [p for p in PREFIXES if p in props]
        if prefix:
            for vendor in VENDORS:
                b1vender.append(props.replace(prefix[0], vendor+prefix[0]))
            b1vender.append(props)
        else:
            b1vender.append(props)
    return ';'.join(b1vender)

#@profile
def vendorfy_css(block=None):
    """adds vendor prefixes to a block of css"""

    for i, blck in enumerate(block):
        if isinstance(blck[1], list):
            at_prefix = [a for a in AT_RULES if a in blck[0]]
            if at_prefix:
                block[i] = (vendorfy_at_prefix(blck, at_prefix))
            else:
                block[i][1] = vendorfy_block_list(blck)
        else:
            block[i][1] = vendorfy_block(blck)
    return block

##@profile
#def unparse_css_blocks(blocks=None):
#    """unparse css blocks back into a css string"""
#
#    css = []
#    for block in blocks:
#        if all([isinstance(blck, list) for blck in block]):
#            for blck in block:
#                css.append('%s {%s}' % (blck[0], unparse_css_blocks(blck[1])))
#        elif any([isinstance(blck, list) for blck in block]):
#            css.append('%s {%s}' % (block[0], unparse_css_blocks(block[1])))
#        else:
#            css.append('%s {%s}' % (block[0], block[1]))
#    return ''.join(css)

#@profile
def unparse_css_blocks(blocks=None):
    """unparse css blocks back into a css string"""

    css = []
    for block in blocks:
        if all([isinstance(blck, list) for blck in block]):
            for blck in block:
                css.append(blck[0] + ' {' + unparse_css_blocks(blck[1]) +'}')
        elif any([isinstance(blck, list) for blck in block]):
            css.append(block[0] + ' {' + unparse_css_blocks(block[1]) +'}')
        else:
            css.append(block[0] + ' {' + block[1] +'}')
    return ''.join(css)

#@profile
def prefix_vendor_css(css=''):
    """add vendor prefix to css string, if prefixes already exist return original css"""
    if any(x in css for x in VENDORS):
        return css
    else:
        return unparse_css_blocks(vendorfy_css(parse_css_blocks(css)))

#@profile
def group_links(pagevars=None, name=''):
    """place tag and category links"""
    linklist = ''
    if pagevars[name]:
        groups = pagevars[name] if isinstance(pagevars[name], list) else [pagevars[name]]
        dirname = os.path.join(os.path.dirname(pagevars["url"]), name)
        linklist = '\n'.join([GROUPLINK % (name, os.path.join(dirname, x + '.html'), x) for x in groups])
    return linklist

#@profile
def top_sentences(text='', sentence_number=4, max_chars=200):
    """return top sentences or max number of words"""

    sents = nltk.sent_tokenize(text[:max_chars])
    top_sents = ' '.join(sents[:sentence_number])
    return top_sents
#    return ''.join(text.split()[:max_chars])

#@profile
def summarize_text(text='', sentence_number=4):
    """summarizes a text"""

    summary = []
    sents = nltk.sent_tokenize(text)
    lower_sents = [s.lower() for s in sents]
    words = nltk.wordpunct_tokenize(text)
    lower_words = [w.lower() for w in words]
    lower_words = [w for w in lower_words if w not in STOPWORDS and WORD_RE.match(w)]
    word_freqs = nltk.FreqDist(lower_words)
    common_words = [wf[0] for wf in word_freqs.items()[:100]]

    for common_word in common_words:
        if len(summary) < sentence_number:
            for lower_sent, sent in zip(lower_sents, sents):
                if sent not in summary and common_word in lower_sent:
                    summary.append(sent)
                    break
        else:
            break

    return ' '.join(summary)

#@profile
def reverse_chronological_order(posts=None):
    """sort posts in reverse chronological order"""
    return sorted(posts, key=lambda x: dt.datetime.strptime(x['date'], '%m/%d/%Y %I:%M %p'), reverse=True)

#@profile
def chronological_order(posts=None):
    """sort posts in reverse chronological order"""
    return sorted(posts, key=lambda x: dt.datetime.strptime(x['date'], '%m/%d/%Y %I:%M %p'), reverse=False)

#@profile
def get_just_words(text=''):
    """tokenize text, punctuation remove and lowercased"""
    return {w.encode('ascii', 'ignore').lower() for w in set(nltk.wordpunct_tokenize(text)) if w.isalpha()}

#@profile
def get_keywords(text=''):
    """find keywords"""
    return get_just_words(text).difference(STOPWORDS)

##@profile
#def spell_check(text='', correct_words=None):
#    """spell checking, ignores non-ascii words, and numbers 0.015568 """
#
#    lower_words = get_just_words(text)
#    check_words = {x.encode('ascii', 'ignore') for x in lower_words}
#    word_errors = check_words.difference(correct_words)
#@profile
def spell_check(text='', correct_words=None):
    """spell checking, ignores non-ascii words, and numbers 0.015568 0.01145 """
    return get_just_words(text).difference(correct_words)

class ProgressBar(object):
    """implements a comand-line progress bar"""

    def __init__(self, iterations):
        """create a progress bar"""
        self.iterations = iterations
        self.prog_bar = '[]'
        self.fill_char = '*'
        self.width = 40
        self.__update_amount(0)

    def animate(self, iterate):
        """animate progress"""
        print '\r' + str(self),
        sys.stdout.flush()
        self.update_iteration(iterate + 1)
        return self

    def update_iteration(self, elapsed_iter):
        """increment progress"""
        self.__update_amount((elapsed_iter / float(self.iterations)) * 100.0)
        self.prog_bar = '%s %s of %s complete' % (self.prog_bar, elapsed_iter, self.iterations)
        return self

    def __update_amount(self, new_amount):
        """update amout of progress"""
        percent_done = int(round((new_amount / 100.0) * 100.0))
        all_full = self.width - 2
        num_hashes = int(round((percent_done / 100.0) * all_full))
        self.prog_bar = '[' + self.fill_char * num_hashes + ' ' * (all_full - num_hashes) + ']'
        pct_place = (len(self.prog_bar) // 2) - len(str(percent_done))
        pct_string = str(percent_done) + '%'
        self.prog_bar = ''.join((self.prog_bar[0:pct_place], pct_string, self.prog_bar[pct_place + len(pct_string):]))
        return self

    def __str__(self):
        """string representation"""
        return str(self.prog_bar)
