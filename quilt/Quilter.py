"""
quilt.Quilter

Object to stitch a page based on quilt
{: .lead}

1. use [quilt file](#quiltfile) to create quilt
2. replace all [patch files](#patchfile) by matching `patch#id` tags in quilt with a `patch/id.html` file
3. parses [page file](#pagefile) using the following format:
    1. `key: value` page variable *header* (optional)
        * key = `[A-Za-z0-9_-]+` until `:`, value = a string per line (mulitlines become array) until next key
        * page variable section ends with first empty (whitespace-only) line
    2. `html` or `markdown` page content
    3. `<script>` page script (optional)
4. set [page variables](#pagevars), overriding default site variables
5. add page content to quilt (auto processing [`markdown` page](#pagefilemd) if file ends with `.md` or `.markdown`)
6. add page script to the end of quilt
7. replace all brace variables, `{ {.*}}`, in content with page or site variables
8. if page is under `posts/` directory, `tags` and `categories` variables are linked and appended to page content
9. fill in blank `alt` attributes for `<a>` and `<img>` tags

"""

import os
import bs4
import json
import copy
import time
import math
import shutil
from collections import defaultdict

from quilt.Constants import JS_HTML_PATTERN_RE, FIRST_KEY_RE, FIRST_EMPTY_LINE_RE, KEY_VALUE_RE, VALUE_RE
from quilt.Constants import PAGEVAR_RE, ESCAPED_PAGEVAR_RE
from quilt.Constants import PATCHCOMMENT, QUILTCOMMENT, PAGEOBJ, DOTSTAR_RE
from quilt.Util import write_file, relative_path, group_links, minimize_js, NO_EMPTY_TAGS
from quilt.Util import  HEAD_STRAINER, BODY_STRAINER
from quilt.Markdown import MD

DEBUG_FILE = ''

def add_suffix(filepath='', suffix=''):
    """add suffix to file name"""
    dirname = os.path.dirname(filepath)
    filename, ext = os.path.splitext(os.path.basename(filepath))
    new_name = os.path.join(dirname, filename + suffix + ext)
    print 'debuging:', new_name
    return new_name

#@profile
def parse_pagevars(var_str=''):
    """parse page var string"""

    page_vars = defaultdict(list)
    key = None
    value = None
    if var_str:
        # parse key, value pairs from each line
        for line in var_str.split('\n'):
            key_value = KEY_VALUE_RE.match(line)
            if key_value:
                key = key_value.group('key').strip()
                value = key_value.group('value').strip()
                page_vars[key].append(value)
            else:
                another_value = VALUE_RE.match(line)
                if another_value and key:
                    page_vars[key].append(another_value.group('value').strip())

#    70                                               # reduce singleton arrays to string
#    71       117          108      0.9      8.9      for key, value in page_vars.items():
#    72        94           70      0.7      5.8          if len(value) == 1:
#    73        86           65      0.8      5.4              page_vars[key] = value[0]
# 243
#    # reduce singleton arrays to string
#    for key, value in page_vars.items():
#        if len(value) == 1:
#            page_vars[key] = value[0]
    # reduce singleton arrays to string
    page_vars = {key: value[0] for key, value in page_vars.items() if len(value) == 1}

    return page_vars

class Quilter(object):
    """page quilter object"""

    #@profile
    def __init__(self, page_file='', quilt='', patches=None, page='', config=None, overrides=None, wrap=''):
        """create quilter"""

        # set settings
        self.config = config
        self.post = self.config["buildblog"] and os.path.join(os.path.basename(self.config["posts"]), "") in page_file

        # set pagevars, handling some special cases
        self.pagevars = copy.deepcopy(self.config["page_defaults"])
        self.pagevars.update({
            "rootpath" : self.config["output"],
            "relativepath" : relative_path(page_file, self.config["pages"]),
            "source" : page_file,
            "output" : page_file.replace(self.config["pages"], self.config["output"]).replace('.md', '.html'),
            "markdownlink" : page_file.replace(self.config["pages"], self.config["output"]),
            "directory" : os.path.basename(os.path.dirname(page_file))
        })
        if self.config["local"]:
            self.pagevars["url"] = self.pagevars["output"]
        else:
            self.pagevars["url"] = self.pagevars["output"].replace(self.pagevars["rootpath"], self.pagevars["domain"])

        # update pagevars
        if overrides:
            self.pagevars.update(overrides)

        # set control
        self.control = {
            "do_debug"    : self.pagevars["output"] == DEBUG_FILE,
            "do_markdown" : page_file[-3:] == '.md',
            "wrap"        : wrap or page_file[-3:] == '.md'
        }

        # parse html and build soup
        self.soup = bs4.BeautifulSoup(quilt, "lxml")

        # build patches
        self.patches = copy.deepcopy(patches)

        # process page file
        self.parse_page(page)

        # keep track of processing time
        self.start = time.time()

    #@profile
    def parse_page(self, page):
        """parses page into vars, content, and scripts7.487 s"""

        if self.control["do_debug"]:
            write_file(add_suffix(DEBUG_FILE, '_original-page'), page.encode('utf-8'))

        # parse variables, content, and scripts
        if FIRST_KEY_RE.match(page.split('\n', 1)[0]):
            page_vars, page_html = FIRST_EMPTY_LINE_RE.split(page, 1)
        else:
            page_vars, page_html = None, page
        page_js, page_html = JS_HTML_PATTERN_RE.match(page_html[::-1]).groups()
        page_html = page_html[::-1]
        page_js = page_js[::-1] if page_js else None

        # update pagevars with page var json
        if page_vars:
            self.pagevars.update(parse_pagevars(page_vars))

        if self.control["do_debug"]:
            write_file(add_suffix(DEBUG_FILE, 'parsed-page'), page_html.encode('utf-8'))

        # handle markdown if necessary
        if self.control["do_markdown"]:

            page_html_md = MD.reset().convert(page_html)

            if self.control["do_debug"]:
                write_file(add_suffix(DEBUG_FILE, '_markdown-output'), page_html_md.encode('utf-8'))

            page_html = page_html_md.replace("<code> ", "<code>").replace(" </code>", "</code>")

        if self.control["wrap"] and self.patches["markdown"]:
            page_html = self.patches["markdown"].replace("{{markdown}}", page_html)

        # set page html
        self.patches["page"] = page_html

        # append page script to quilt
        if page_js:
            self.patches["scripts"] = '\n'.join((self.patches["scripts"], page_js))
        # add page variables to object
        if self.config["pageobject"]:
            page_obj = json.dumps(self.pagevars, indent=4, separators=(',', ': '), sort_keys=True)
            if self.config["minimizejs"]:
                page_obj = minimize_js(page_obj)
            self.patches["scripts"] = '\n'.join((PAGEOBJ % (page_obj), self.patches["scripts"]))

        if self.control["do_debug"]:
            write_file(add_suffix(DEBUG_FILE, '_markdown-wrapped'), page_html.encode('utf-8'))

        return self

    #@profile
    def replace_patches(self):
        """replace all patches in quilt with patch files"""

        # replace head (special case of patch)
        head = bs4.BeautifulSoup(self.patches["head"], "lxml", parse_only=HEAD_STRAINER).head
        self.soup.html.head.replace_with(head)
        if self.pagevars["patchcomment"]:
            self.soup.html.insert(0, self.soup.new_string("quilted head patch", bs4.Comment))
            self.soup.html.insert(0, '\n')

        # replace all other patches, recursively
        patch_tags = self.soup.find_all("patch")
        while len(patch_tags) > 0:
            for patch in patch_tags:
                if patch["id"] in self.patches:

                    if patch["id"] == "scripts":
                        patch_soup = bs4.BeautifulSoup(
                            self.patches[patch["id"]].encode('utf-8'),
                            "lxml",
                            parse_only=HEAD_STRAINER
                        )
                    else:
                        patch_soup = bs4.BeautifulSoup(
                            self.patches[patch["id"]].encode('utf-8'),
                            "lxml",
                            parse_only=BODY_STRAINER
                        )

                    if self.control["do_debug"]:
                        write_file(
                            add_suffix(DEBUG_FILE, '_'+patch["id"]+'-html'),
                            self.patches[patch["id"]].encode('utf-8')
                        )
                        write_file(
                            add_suffix(DEBUG_FILE, '_'+patch["id"]+'-soup'),
                            patch_soup.encode('utf-8', formatter='html')
                        )

                    if patch["id"] == "scripts":
                        patch.append('\n')
                        patch.append(patch_soup.head)
                        patch.head.unwrap()
                    else:
                        patch.append('\n')
                        patch.append(patch_soup.body)
                        patch.body.unwrap()

                    # auto add patch id for replaced element id
                    patch.contents[1].attrs["id"] = patch["id"]
                    # add patch comment if necessary
                    if self.pagevars["patchcomment"]:
                        patch.insert(0, self.soup.new_string(PATCHCOMMENT % (patch["id"]), bs4.Comment))
                        patch.insert(0, '\n')
                    patch.unwrap()

                    if self.control["do_debug"]:
                        write_file(add_suffix(DEBUG_FILE, '_added-'+patch["id"]), self.soup.encode('utf-8', formatter='html'))

                else:
                    patch.decompose()

                if self.control["do_debug"]:
                    write_file(add_suffix(DEBUG_FILE, 'replaced_patches'), self.soup.encode('utf-8', formatter='html'))

            # check for new patches (see if patch had nested patches)
            patch_tags = self.soup.find_all("patch")

        return self

    #@profile
    def replace_variables(self):
        """replace {{}} page variables (re based replacement) 3.93589"""

        html = self.soup.encode('utf-8', formatter='html')
        page_vars = list(set(PAGEVAR_RE.findall(html)))

        if self.control["do_debug"]:
            write_file(add_suffix(DEBUG_FILE, 'replacing_vars'), html)

        if self.post:
            self.pagevars["tag_list"] = group_links(self.pagevars, "tags")
            self.pagevars["category_list"] = group_links(self.pagevars, "categories")

        # replace all page_vars, recursivley
        while len(page_vars) > 0:
            for page_var in page_vars:
                pagevar_brace = "{{" + page_var + "}}"
                if page_var in self.pagevars:
                    variable = self.pagevars[page_var]
                    if isinstance(variable, list):
                        variable = ','.join(variable)
                    html = html.replace(pagevar_brace, str(variable))
                else:
                    html = html.replace(pagevar_brace, "not found")
            # check for new page variables (see if variable had nested variable)
            page_vars = list(set(PAGEVAR_RE.findall(html)))

            escaped_page_vars = list(set(ESCAPED_PAGEVAR_RE.findall(html)))
            for escaped_page_var in escaped_page_vars:
                html = html.replace("{ {" + escaped_page_var + "}}", "{{" + escaped_page_var + "}}")

        if self.control["do_debug"]:
            write_file(add_suffix(DEBUG_FILE, 'replaced_vars'), html)

        self.soup = bs4.BeautifulSoup(html, "lxml")

        if self.control["do_debug"]:
            write_file(add_suffix(DEBUG_FILE, 'replaced_vars_soup'), self.soup.encode('utf-8', formatter='html'))

        return self

#    @profile
#    def replace_vars_in_string(self, html=''):
#
#        page_vars = list(set(PAGEVAR_RE.findall(html)))
#
#        while len(page_vars) > 0:
#            for page_var in page_vars:
#                pagevar_brace = "{{" + page_var + "}}"
#                if page_var in self.pagevars:
#                    variable = self.pagevars[page_var]
#                    if type(variable) is list:
#                        variable = ','.join(variable)
#                    html = html.replace(pagevar_brace, str(variable))
#                else:
#                    html = html.replace(pagevar_brace, "not found")
#            # check for new page variables (see if variable had nested variable)
#            page_vars = list(set(PAGEVAR_RE.findall(html)))
#
#            for escaped_page_var in list(set(ESCAPED_PAGEVAR_RE.findall(html))):
#                html = html.replace("{ {" + escaped_page_var + "}}", "{{" + escaped_page_var + "}}")
#
#        return html
#
#    @profile
#    def replace_variables(self):
#        """replace {{}} page variables (re based replacement) 3.93589"""
#
#        if self.post:
#            self.pagevars["tag_list"] = group_links(self.pagevars, "tags")
#            self.pagevars["category_list"] = group_links(self.pagevars, "categories")
#
#        for tag in self.soup.find_all(href=PAGEVAR_SEARCH_RE):
#            tag.attrs["href"] = self.replace_vars_in_string(tag["href"])
#
#        for tag in self.soup.find_all(content=PAGEVAR_SEARCH_RE):
#            tag.attrs["content"] = self.replace_vars_in_string(tag["content"])
#
#        for tag in self.soup.find_all(src=PAGEVAR_SEARCH_RE):
#            tag.attrs["src"] = self.replace_vars_in_string(tag["src"])
#
#        for tag in [x.find_parent() for x in self.soup.find_all(text=PAGEVAR_SEARCH_RE)]:
#            html = tag.encode('utf-8', formatter='html')
#            html = self.replace_vars_in_string(html)
#            new_tag = bs4.BeautifulSoup(html, "lxml", parse_only=bs4.SoupStrainer(tag.name)).contents[0]
#
#            if tag.parent is not None:
#                tag.replace_with(new_tag)
#            else:
#                tag.append(new_tag)
#
#
#        if self.control["do_debug"]:
#            write_file(add_suffix(DEBUG_FILE, 'replaced_vars_soup'), self.soup.encode('utf-8', formatter='html'))
#
#        return self

    #@profile
    def add_page_comments(self):
        """create a page key value pair"""

        etime = time.time() - self.start

        if self.pagevars["pagecomment"]:
            max_key_len = str(max([len(x) for x in self.pagevars.keys()])+1)
            keyval_line = '{{:>{}}} : {{}}'.format(max_key_len)
            keyvalpair = [keyval_line.format(k, v) for k, v in sorted(self.pagevars.items())]
            pagevar_comment = '    -- quilt pagevars :\n    --     ' + '\n    --    '.join(keyvalpair)
        else:
            pagevar_comment = ''

        if self.pagevars["quiltcomment"]:
            quilt_comment = QUILTCOMMENT % (
                self.pagevars["url"],
                self.pagevars["date"],
                math.floor(1000*etime)/1000,
                pagevar_comment
            )
        else:
            quilt_comment = pagevar_comment

        self.soup.head.insert(0, self.soup.new_string(quilt_comment, bs4.Comment))
        self.soup.head.insert(0, '\n')

        return self

    #@profile
    def stitch(self):
        """generate the page"""

        self.replace_patches()
        self.replace_variables()
        self.add_page_comments()

        return self

    def clean_document(self):
        """check, clean, standardize document"""

        # make sure doctype is set
        doctype = [x for x in self.soup.contents if isinstance(x, bs4.Doctype)]
        if not doctype:
            self.soup.insert(0, bs4.Doctype('html'))

        # make sure language is set
        self.soup.html["lang"] = self.soup.html.get("lang") or "en"

        # make sure certain metas are set
        viewport_meta = self.soup.head.find("meta", viewport=True)
        if not viewport_meta:
            viewport_meta_tag = self.soup.new_tag('meta')
            viewport_meta_tag["name"] = "viewport"
            viewport_meta_tag["content"] = "width=device-width, initial-scale=1"
            self.soup.head.insert(0, viewport_meta_tag)
            self.soup.head.insert(0, '\n')

        http_equiv_meta = self.soup.head.find("meta", attrs={"http-equiv": DOTSTAR_RE})
        if not http_equiv_meta:
            http_equiv_meta_tag = self.soup.new_tag('meta')
            http_equiv_meta_tag["http-equiv"] = "X-UA-Compatible"
            http_equiv_meta_tag["content"] = "ie=edge"
            self.soup.head.insert(0, http_equiv_meta_tag)
            self.soup.head.insert(0, '\n')

        charset_meta = self.soup.head.find("meta", attrs={"charset": DOTSTAR_RE})
        if not charset_meta:
            charset_meta_tag = self.soup.new_tag('meta')
            charset_meta_tag["charset"] = "utf-8"
            self.soup.head.insert(0, charset_meta_tag)
            self.soup.head.insert(0, '\n')

        return self

    def clean_tags(self):
        """check, clean, standardize tags"""

        # make sure as have clean hrefs and alts/titles
        for a_tag in self.soup.find_all("a"):
            a_tag.attrs["href"] = a_tag.attrs.get("href") or "#"
            a_tag.attrs["alt"] = a_tag.attrs.get("alt") or a_tag.get_text()
            a_tag.attrs["title"] = a_tag.attrs.get("title") or a_tag.get_text()

        # make sure imgs have clear src and alt/tiles
        for img_tag in self.soup.find_all("img"):
            if "src" in img_tag.attrs:
                img_tag.attrs["alt"] = img_tag.attrs.get("alt") or img_tag.attrs["src"]
                img_tag.attrs["title"] = img_tag.attrs.get("title") or img_tag.attrs["src"]

        # make sure css links have href and proper rel and type
        for link_tag in self.soup.find_all("link"):
            if "href" not in link_tag.attrs:
                link_tag.decompose()
            elif len(link_tag.attrs["href"]) > 4 and link_tag.attrs["href"][-4:] == '.css':
                link_tag.attrs["rel"] = "stylesheet"
                link_tag.attrs["type"] = "text/css"

        # make sure js scripts have src and proper rel and type
        for script_tag in self.soup.find_all("script"):
            if len(script_tag.contents) == 0 and "src" not in script_tag.attrs:
                script_tag.decompose()
            else:
                script_tag.attrs["rel"] = script_tag.attrs.get("rel") or "javascript"
                script_tag.attrs["type"] = script_tag.attrs.get("type") or "text/javascript"

        # add .table to <table>
        for table in self.soup.find_all("table"):
            table.attrs["class"] = ['table'] + table.attrs["class"] if "class" in table.attrs else 'table'

        return self

    def remove_empty_tags(self):
        """remove empty tags"""

        for tag in self.soup.body.find_all(NO_EMPTY_TAGS):
            if not tag.contents:
                tag.decompose()

        return self

    #@profile
    def clean_html(self):
        """clean html, post process html"""

        self.clean_document()
        self.clean_tags()
        self.remove_empty_tags()

        return self

    #@profile
    def write(self, pretty=False):
        """write it out"""

        page_string = self.soup.prettify(formatter='html') if pretty else self.soup.encode('utf-8', formatter='html')
        write_file(self.pagevars["output"], page_string)
        if self.config["copymd"] and os.path.isfile(self.pagevars["source"]):
            shutil.copyfile(self.pagevars["source"], self.pagevars["output"].replace('.html', '.md'))

        return self
