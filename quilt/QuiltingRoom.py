"""
quilt.QuiltingRoom

Main module to quilt a static site by stitching html page together
{: .lead}

1. set `source` to users directory containing the [appropriate files](#exampledir) (default output is `quilted_` + `source`)
2. read `config.json` and override [default configuration](#configuration)
3. load quilt file at `quilt.html`
4. load all patch files in `patches/`
5. locate `pages/`, `templates/`, and `assets/` directories
6. if `posts/` exists and configured to build a blog create [`Blog` object]{#Blog}
7. build assets by (+ = optional):
    1. copy `assets/` to output
    2. creating `favicon.ico` +
    3. combine all `css` files into one +
        * auto add vendor prefix +
        * minimize each file +
    4. combine all `js` files into one +
        * minimize each file +
8. go thru pages and stitch together with [`Quilter` object]{#Quilter}
    * if post append page data to `Blog` object
9. add blog Home, Tag and Category pages
10. generate `atom` feed and/or `rss` feed
11. fill directories without `index.html`
12. add `robot.txt`
13. generate `search.json`, a word to url index for `typeahead`
14. generate `sitemap.xml`

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

import os
import bs4
import json
import copy
import glob
import time
import shutil
import pickle
import fnmatch
import hashlib
import datetime
import PIL.Image
import subprocess

import quilt
from quilt.Blog import Blog
from quilt.Quilter import Quilter
from quilt.Util import DEFAULT_CONFIG, time_since, read_file, write_file, load_files, get_file_names, get_dir_hash
from quilt.Util import find_hrefsrc, filter_external_url, minimize_css, minimize_js, prefix_vendor_css
from quilt.Util import path_link_list, top_sentences, get_just_words, get_keywords, spell_check, analyze_post, ProgressBar
from quilt.Util import reverse_chronological_order, check_local_quilt, get_group, make_group_links
from quilt.Util import  HEAD_STRAINER, BODY_STRAINER
from quilt.Constants import QUILTHEADER, ASSETCOMMENT, ROBOTTXT, SITEMAPINDEX, SITEMAP, SITEMAPURL
from quilt.Constants import NO_NEW_POSTS, NO_OLD_POSTS, CSS_EXT_RE, ROOT_LEVEL_JS_EXT_RE

class QuiltingRoom(object):
    """the quilting room"""

    #@profile
    def __init__(self, source='', output=''):
        """setup the quilting room"""

        # default configuration
        self.config = copy.copy(DEFAULT_CONFIG)

        # runtime
        __date = datetime.datetime.now().replace(microsecond=0)
        __utc = datetime.datetime.utcnow().replace(microsecond=0)
        __delta = __date - __utc
        __hh, __mm = divmod((__delta.days * 24*60*60 + __delta.seconds + 30) // 60, 60)
        self.config["quiltversion"] = quilt.__version__
        self.config["date"] = __date
        self.config["now"] = {
            "iso"	    : "%s%+03d:%02d" % (__date.isoformat(), __hh, __mm),
            "wkday"	    : __date.strftime('%a'),
            "wkdaylong" : __date.strftime('%A'),
            "date"	    : __date.strftime('%d'),
            "month"	    : __date.strftime('%b'),
            "monthlong" : __date.strftime('%B'),
            "monnum"	: __date.strftime('%m'),
            "year"	    : __date.strftime('%y'),
            "yearlong"  : __date.strftime('%Y'),
            "fulldate"  : __date.strftime('%x'),
            "isodate"   : __date.strftime('%Y-%m-%d'),
            "datetime"  : __date.strftime('%m/%d/%Y %I:%M %p')
        }

        # set runtime variables
        output = output or os.path.dirname(self.source) + '/quilted_' + os.path.basename(self.source)
        self.source = source
        # self.finaloutput = output
        self.output = output
        # self.output = output + '_' + hashlib.sha1(output + str(__date)).hexdigest()[:7]

        # read in configuration
        config_options = json.loads(read_file(os.path.join(self.source, 'config.json')))
        self.config.update(config_options)

        # set full filenames
        self.config["output"] = self.output
        self.config["quilt"] = os.path.join(self.source, self.config["quilt"])
        self.config["assets"] = os.path.join(self.source, self.config["assets"])
        self.config["patches"] = os.path.join(self.source, self.config["patches"])
        self.config["posts"] = os.path.join(self.source, self.config["pages"], self.config["posts"])
        self.config["pages"] = os.path.join(self.source, self.config["pages"])
        self.config["templates"] = os.path.join(self.source, self.config["templates"])
        self.config["correctwords"] = os.path.join(self.source, self.config["correctwords"])

        # get quilt git repo info
        repo = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.git')
        try:
            self.config["quilthash"] = subprocess.check_output('git -C {} rev-parse HEAD'.format(repo), shell=True).strip()
        except:
            self.config["quilthash"] = ''
        try:
            self.config["quiltbranch"] = subprocess.check_output('git -C {} rev-parse --abbrev-ref HEAD'.format(repo), shell=True).strip()
        except:
            self.config["quiltbranch"] = ''

        # get source git repo info
        if (self.config["git"]):
            repo = os.path.join(self.source, self.config["git"], '.git')
            try:
                self.config["hash"] = subprocess.check_output('git -C {} rev-parse HEAD'.format(repo), shell=True).strip()
            except:
                self.config["hash"] = ''
            try:
                self.config["branch"] = subprocess.check_output('git -C {} rev-parse --abbrev-ref HEAD'.format(repo), shell=True).strip()
            except:
                self.config["branch"] = ''
        else:
            self.config["hash"] = ''
            self.config["branch"] = ''

        # load quilt pattern
        self.quilt_pattern = read_file(self.config["quilt"])

        # load patches
        self.patches = load_files(self.config["patches"], self.config["patch_ext"])

        # find pages, templates, assets
        self.files = {
            "pages" : get_file_names(self.config["pages"], self.config["page_ext"]),
            "templates" : get_file_names(self.config["templates"], self.config["template_ext"]),
            "assets" : get_file_names(self.config["assets"], self.config["asset_ext"])
        }
        self.files["posts"] = {x for x in self.files["pages"] if self.config["posts"] in x}
        self.files["pages"] = {x for x in self.files["pages"] if self.config["posts"] not in x}

        # set quilting page defaults
        self.config["page_defaults"] = {
            # internal variables used by quilt (auto-generated, but may be used in content)
            # -----------------------------------------------------------------------------------
            "url"           : "",                            # absolure url of page
            "relativepath"  : "",                            # relative path of page
            "rootpath"      : "",                            # absolute path of output directory
            "source"        : "",                            # absolute local path of page source
            "output"        : "",                            # absolute local path of page output
            "domain"        : self.config["domain"],         # site domain
            "directory"     : "/",                           # parent directory
            "patchcomment"  : self.config["patchcomment"],   # print comment showing patch source
            "quiltcomment"  : self.config["quiltcomment"],   # print quilt comment in header
            "pagecomment"   : self.config["pagecomment"],    # print page var comment in header
            "latestpostlink": "",                            # filename of latest post
            "page_path"     : "",                            # breadcrumb path of post
            "next_post"     : "",                            # url of next post
            "next_title"    : "",                            # title of next post
            "disable_next"  : "disabled",                    # set if last post
            "last_post"     : "",                            # url of previous post
            "last_title"    : "",                            # title of last post
            "disable_last"  : "disabled",                    # set if first post
            "branch"        : self.config["branch"],         # the current branch if source it a git repo
            "hash"          : self.config["hash"],           # the current commit if source is a git repo
            "quiltversion"  : self.config["quiltversion"],   # the version of quilt being used
            "quiltbranch"   : self.config["quiltbranch"],    # the branch of quilt being used
            "quilthash"     : self.config["quilthash"],      # the commit of quilt being used
            # content page variables (intended to be overriden)
            # -----------------------------------------------------------------------------------
            "name"          : self.config["name"],           # site/project name
            "title"         : self.config["title"],          # page title
            "blogtitle"     : self.config["blogtitle"],      # name of blog
            "blogsubtitle"  : self.config["blogsubtitle"],   # subtitle or description for blog
            "author"        : self.config["author"],         # page author
            'email'         : self.config["email"],          # page email
            "description"   : self.config["description"],    # page description
            "categories"    : self.config["categories"],     # page categories (for pages in posts/)
            "tags"          : self.config["tags"],           # page tags (for pages in posts/)
            "keywords"      : self.config["keywords"],       # page keywords = tags + categories
            "date"          : self.config["now"]["fulldate"],# created date (useful for posts/)
            "copydate"      : self.config["copydate"],       # copyright dates (auto extend to now)
            "copyrighter"   : self.config["copyrighter"]     # copyright owner
        }

        # extend copyright date
        if self.config["page_defaults"]["copydate"] < int(self.config["now"]["yearlong"]):
            self.config["page_defaults"]["copydate"] = '{}&ndash;{}'.format(self.config["page_defaults"]["copydate"], self.config["now"]["yearlong"])

        # add user variables (keys not found in DEFAULT_CONFIG)
        for key, val in self.config.items():
            if not key in DEFAULT_CONFIG:
                self.config["page_defaults"][key] = val

        # start blog
        if self.config["buildblog"]:
            self.blog = Blog(self.config["blogtitle"], self.source, self.output, self.quilt_pattern, self.patches, self.config)
        else:
            self.blog = None

        # processes all template files
        self.patches["templates"] = '\n'.join([read_file(template) for template in self.files["templates"]])

    #@profile
    def ouput_path(self, filepath='', replacement=''):
        """get the output directory equivalent"""

        replacement = replacement or self.source
        return os.path.dirname(filepath).replace(replacement, self.output)

    #@profile
    def create_favicon_versions(self):
        """create multiple image versions of icon"""

        icon_file = os.path.join(self.config["assets"], self.config["images"], self.config['iconfile'])
        imgs_path = os.path.join(self.output, self.config["images"])

        if os.path.exists(icon_file):
            print 'creating icons from:\t', icon_file
            print 'creating icons in:\t', imgs_path, '\n'
            # create favicon from icon
            icon_img = PIL.Image.open(icon_file)
            default_size = self.config["iconsizes"][0]
            png_info = icon_img.info
            width, _ = icon_img.size
            ico = icon_img.resize((default_size, default_size), PIL.Image.ANTIALIAS)
            ico.save(os.path.join(imgs_path, 'favicon.png'), **png_info)
            os.rename(os.path.join(imgs_path, 'favicon.png'), os.path.join(imgs_path, 'favicon.ico'))

            # create multiple size
            for size in self.config["iconsizes"]:
                filt = PIL.Image.BICUBIC if size > width else PIL.Image.ANTIALIAS
                img = icon_img.resize((size, size), filt)
                fname, ext = os.path.splitext(self.config['iconfile'])
                img.save(os.path.join(imgs_path, '%s_%sx%s%s' % (fname, str(size), str(size), ext)), **png_info)
        else:
            print 'creating icons from :\t', 'missing icon file, could not create', '\n'
        return self

    #@profile
    def copy_asset_directory(self):
        """copy the whole asset directory over to the output directory"""

        # assetdirs = glob.glob(os.path.join(self.config["assets"], "*/"))
        # for assetdir in assetdirs:
            # dirname = os.path.basename(assetdir[:-1])
            # shutil.copytree(assetdir, os.path.join(self.output, dirname))
        shutil.copytree(self.config["assets"], self.output)

        return self

    #@profile
    def replace_or_minimize_assets(self, soup=None, sources=None, source_name=''):
        """replace assets with combined assets and minimize inline assets"""

        # determine tags and attributes to replace
        asset_tag = "link" if source_name.endswith(".css") else "script"
        asset_attr = "href" if asset_tag == "link" else "src"
        asset_found = False
        # search soup for asset
        for tag in soup.find_all(asset_tag):
            # minimize inline js
            if asset_tag == 'script' and len(tag.contents) > 0 and self.config["minimizejs"]:
                tag.string = minimize_js(tag.string)
            # remove asset if in list of sources to remove
            if asset_attr in tag.attrs and tag.attrs[asset_attr] in sources:
                asset_found = True
                tag.decompose()
        # if any asset was found, add the combined source
        if asset_found:
            combined_asset = soup.new_tag(asset_tag)
            combined_asset.attrs[asset_attr] = '{{relativepath}}%s' % (source_name)
            if asset_tag == "link":
                soup.head.append(combined_asset)
            else:
                soup.head.insert(0, combined_asset)

        return self

    #@profile
    def combine_source(self, sources=None, source_name=''):
        """combine css or js source files"""
        file_type = os.path.splitext(source_name)[1]
        combined_source = []
        for source_file in sources:
            # read source
            source = read_file(source_file.replace("{{relativepath}}", self.config["assets"]+'/'))
            # prefix css
            if file_type == '.css' and self.config["vendorfycss"]:
                source = prefix_vendor_css(source)
            # minimize css or js
            if '.min' not in source_file:
                if file_type == '.css' and self.config["minimizecss"]:
                    source = minimize_css(source)
                if file_type == '.js' and self.config["minimizejs"]:
                    source = minimize_js(source)

            # append comment and append source to combined file
            if self.config["assetcomment"]:
                combined_source.append(ASSETCOMMENT % (os.path.basename(source_file), self.config["now"]["iso"]))
            combined_source.append(source)

        # dump it to disk
        combined_src = '\n'.join(combined_source).strip()
        write_file(os.path.join(self.output, source_name), combined_src.encode('utf-8'))

        return self

    #@profile
    def build_assets(self):
        """copy, combine, and minimize assets (all configurable)"""

        # copy asset directories to output
        self.copy_asset_directory()

        # create favicon
        if self.config['buildicon']:
            self.create_favicon_versions()

        # make soup
        head_soup = bs4.BeautifulSoup(self.patches["head"], "lxml", parse_only=HEAD_STRAINER)
        script_soup = bs4.BeautifulSoup(self.patches["scripts"], "lxml", parse_only=HEAD_STRAINER)

        if self.config["combinecss"]:
            # find assets
            css_files = find_hrefsrc(head_soup, "link", CSS_EXT_RE)
            # make sure asset is local
            css_files = filter_external_url(css_files, self.config["domain"])
            # build combined name
            css_name = 'css/%s.css' % ('_'.join([os.path.splitext(os.path.basename(css))[0] for css in css_files]))
            # replace combined asset name
            if css_files:
                self.replace_or_minimize_assets(head_soup, css_files, css_name)
            # combine asset sources (+ minimize)
            self.combine_source(css_files, css_name)
            print 'combined css files:\t', ' '.join([os.path.basename(x) for x in css_files])
            print 'into one css file :\t', css_name, '\n'

        if self.config["combinejs"]:
            # find assets
            js_files = find_hrefsrc(head_soup, "script", ROOT_LEVEL_JS_EXT_RE)
            js_files += find_hrefsrc(script_soup, "script", ROOT_LEVEL_JS_EXT_RE)
            # make sure asset is local
            js_files = filter_external_url(js_files, self.config["domain"])
            # build combined name
            js_name = 'js/%s.js' % ('_'.join([os.path.splitext(os.path.basename(js))[0] for js in js_files]))
            # replace combined asset name
            if js_files:
                self.replace_or_minimize_assets(head_soup, js_files, js_name)
                self.replace_or_minimize_assets(script_soup, js_files, js_name)
            # combine asset sources (+ minimize)
            self.combine_source(js_files, js_name)
            print 'combined js files:\t', ' '.join([os.path.basename(x) for x in js_files])
            print 'into one js file :\t', js_name, '\n'

        # put head and script soups back into patches
        self.patches["head"] = unicode(head_soup.head)
        self.patches["scripts"] = ''.join([unicode(scripts) for scripts in script_soup.head.contents])

        return self

    #@profile
    def generate_index(self):
        """search for directories without index.html"""

        # get list of no-index directories
        no_index_dirs = [xd for xd, _, xf in os.walk(self.output) if len(fnmatch.filter(xf, 'index.html')) == 0]
        no_index_dirs = [x for x in no_index_dirs if 'mathjax' not in x]

        # add blank index.html to those directories
        for no_index_dir in no_index_dirs:
            page = os.path.join(no_index_dir, "index.html")

            # process page
            overrides = {
                "title" : "%s directory index" % (os.path.basename(no_index_dir)),
                "directory" : os.path.basename(no_index_dir),
                "description" : "blank index page of %s directory" % (os.path.basename(no_index_dir)),
                "keywords" : "index"
            }

            # stitch the page together
            qultr = Quilter(page, self.quilt_pattern, self.patches, self.patches["index"], self.config, overrides)
            qultr.stitch()
            qultr.clean_html()
            qultr.remove_empty()
            qultr.write()
            del qultr

        return self

    #@profile
    def generate_sitemap(self):
        """generates a sitemap for site"""

        # get list of files
        output_locs = []
        for dirpath, _, files in os.walk(self.output):
            for outputfile in files:
                loc = os.path.join(dirpath, outputfile).replace(self.output, self.config["domain"])
                output_locs.append(loc)

        # add to sitemap
        sitemapurls = [SITEMAPURL % (
            'http://' + output_loc,
            self.config["now"]["iso"],
            self.config["changefreq"],
            self.config["priority"]
        ) for output_loc in output_locs]

        # output sitemap & sitemap index
        sitemap = SITEMAP % ("".join(sitemapurls))
        sitemapindex = SITEMAPINDEX % (
            'http://' + os.path.join(self.config["domain"], "sitemap.xml"),
            self.config["now"]["iso"]
        )
        write_file(os.path.join(self.output, "sitemap.xml"), sitemap)
        write_file(os.path.join(self.output, "sitemapindex.xml"), sitemapindex)

        return self

    #@profile
    def generate_robot(self):
        """generate robot.txt in root"""

        robot = ROBOTTXT % ('http://' + self.config["domain"])
        write_file(os.path.join(self.output, 'robots.txt'), robot)

        return self

    #@profile
    def get_output_files(self, match=''):
        """go thru and find output files"""

        output_locs = []
        for dirpath, _, files in os.walk(self.output):
            for outputfile in files:
                if outputfile.endswith(match):
                    file_loc = os.path.join(dirpath, outputfile)
                    file_url = file_loc if self.config["local"] else file_loc.replace(self.output, self.config["domain"])
                    output_locs.append((file_loc, file_url))
        return output_locs

    #@profile
    def generate_search(self):
        """create reverse word index"""

        # get words used in all of output files
        word_url_list = []
        for page_loc, page_url in self.get_output_files('.html'):
            # read page
            page_text = read_file(page_loc)
            # add indexed keywords
            soup = bs4.BeautifulSoup(page_text)
            content = soup.find(id="page") or soup.body
            words = get_keywords(content.get_text())
            word_url_list.extend([(word, page_url) for word in words])

        # create keyword json
        search = json.dumps([{'val':k[0], 'url':k[1]} for k in word_url_list])
        write_file(os.path.join(self.output, 'search.json'), search)

        return self

    #@profile
    def build_word_dictionary(self):
        """build correct word dictionary for project"""

        # correctly spelled english words
        word_text = read_file(os.path.join(os.path.dirname(__file__), 'words.txt'))
        modern_word_text = read_file(os.path.join(os.path.dirname(__file__), 'modern_words.txt'))
        correct_words = {x.lower() for x in word_text.split('\n') + modern_word_text.split('\n')}

        # add all words in the quilt source
        for source_file in glob.glob(os.path.join(os.path.dirname(__file__), '*.py')):
            source = read_file(source_file)
            correct_words.update({x.lower() for x in get_just_words(source)})

        # update user words
        if os.path.exists(self.config["correctwords"]):
            user_words_text = read_file(self.config["correctwords"])
            user_words = {x.lower() for x in user_words_text.split('\n')}
            correct_words.update(user_words)
        # add empty string and space
        correct_words.update({'', ' '})

        return correct_words

    #@profile
    def spellcheck(self):
        """spell check all html files"""

        print 'checking for potential spelling errors:'

        correct_words = self.build_word_dictionary()

        # check spelling errors for html output file
        output_files = self.get_output_files('.html')
        progbar = ProgressBar(len(output_files))

        spelling_errors = []
        for i, (page_loc, _) in enumerate(output_files):

            progbar.animate(i + 1)

            # read page, make sure BeautifulSoup separate words around <br>s with space
            page_text = read_file(page_loc).replace('<br/>', ' <br/>')
            # get text and spell check
            soup = bs4.BeautifulSoup(page_text, "lxml", parse_only=BODY_STRAINER)
            for ignore in soup(['script', 'code', 'pre']):
                ignore.extract()
            for ignore in soup.find_all(True, self.config["spellignore"]):
                ignore.extract()
            page_text = soup.body.get_text()
            errors = spell_check(page_text, correct_words)
            if errors:
                error_text = '%s:\n\t%s\n' % (page_loc, '\n\t'.join([x for x in errors]))
                spelling_errors.append(error_text)

        if spelling_errors:
            print '\n\nPossible spelling Errors:\n\n', '\n'.join(spelling_errors)
        else:
            print '\n\n', 'No errors found!'

        return self

    #@profile
    def quilt_pages(self, pages, post_data=None):
        """loop through pages and quilt them"""

        if post_data:
            print '\n', 'building posts:'
        else:
            print '\n', 'quilting pages:'
        progbar = ProgressBar(len(pages))

        # quilt all the pages
        for i, page in enumerate(pages):

            progbar.animate(i + 1)

            # read page
            page_text = read_file(page)

            # check for directory quilt and directory patches?
            quilt, patches = check_local_quilt(page, self.quilt_pattern, self.patches, self.config)

            # stitch the page together
            qultr = Quilter(page, quilt, patches, page_text, self.config)

            if post_data:
                qultr.pagevars["page_path"] = path_link_list(page.replace(self.config["pages"], ''), post_data[i]["title"])
                qultr.pagevars["next_post"] = post_data[i-1]["url"] if i > 0 else "#"
                qultr.pagevars["next_title"] = post_data[i-1]["title"] if i > 0 else NO_NEW_POSTS
                qultr.pagevars["disable_next"] = "" if i > 0 else "disabled"
                qultr.pagevars["last_post"] = post_data[i+1]["url"] if i < len(post_data)-1 else "#"
                qultr.pagevars["last_title"] = post_data[i+1]["title"] if i < len(post_data)-1 else NO_OLD_POSTS
                qultr.pagevars["disable_last"] = "" if i < len(post_data)-1 else "disabled"

            qultr.stitch()
            qultr.clean_html()
            qultr.remove_empty()
            qultr.write()
            del qultr

    #@profile
    def analyze_posts(self):
        """analyze all pages under posts/ and save needed info"""

        print 'analyzing posts:'
        progbar = ProgressBar(len(self.files["posts"]))

        all_tags = set()
        all_featured = set()
        all_categories = set()

        # quilt all the posts
        for i, page in enumerate(self.files["posts"]):

            progbar.animate(i + 1)

            # read page
            page_text = read_file(page)

            # check for directory quilt and directory patches?
            quilt, patches = check_local_quilt(page, self.quilt_pattern, self.patches, self.config)

            # stitch the page together
            qultr = Quilter(page, quilt, patches, page_text, self.config)
            qultr.stitch()

            # keep track of the post
            post = copy.deepcopy(qultr.pagevars)

            # analyze the post text and structure
            post_data = analyze_post(qultr.soup.find(id="post"), self.config['domain'])
            post.update(post_data)

            # keep track of groups

            if 'featured' in post.keys() and post['featured']:
                all_featured.update([(post['url'], post['title'], post['description'])])
            all_tags.update(get_group(post, 'tags'))
            all_categories.update(get_group(post, 'categories'))

            # store it
            self.blog.append(post)
            del qultr

        # add "global view" of blog to pagevars
        latest_post = os.path.splitext(os.path.basename(reverse_chronological_order(self.blog.posts)[0]["url"]))[0]
        self.config["page_defaults"]["latestpostlink"] = latest_post
        self.config["page_defaults"]["all_category_list"] = make_group_links(all_categories, self.blog.posts[0], 'categories')
        self.config["page_defaults"]["all_tag_list"] = make_group_links(all_tags, self.blog.posts[0], 'tags')
        self.config["page_defaults"]["all_featured_list"] = '\n'.join([
            '<li><h5><a href="%s">%s</a><br><small>%s</small></h5></li>' % (url, title, description)
                for (url, title, description) in all_featured
        ])

        return self

    #@profile
    def quilt(self):
        """quilt the site"""

        # get current time
        __t0 = time.time()

        # read in last source hashes
        lastsourcehash = {}
        sourcehash_path = os.path.join(self.output, 'sourcehash.pkl')
        if os.path.exists(sourcehash_path):
            with open(sourcehash_path, 'r') as f:
                lastsourcehash = pickle.load(f)

        # calculate current source hashes
        sourcehash = get_dir_hash(self.source)
        # assume no files changed for the moment
        self.fileschanged = {k: False for k in sourcehash.keys()}
        # create boolean of change status for each file
        for k in self.fileschanged.keys():
            # if the file is new
            if k not in lastsourcehash:
                self.fileschanged[k] = True
            # if the file is old but with new checksum
            elif sourcehash[k] != lastsourcehash[k]:
                self.fileschanged[k] = True

        # display console output
        print QUILTHEADER % (
            '(v{}, {}, {})'.format(self.config["quiltversion"], self.config["quiltbranch"], self.config["quilthash"]),
            self.source,
            self.config["branch"],
            self.config["hash"],
            self.config["date"]
        )

        # if the source has changed, begin quilting
        if sourcehash != lastsourcehash:

            # destroy last version
            if os.path.isdir(self.output):
                shutil.rmtree(self.output)

            # dislpay loaded patches and templates
            print '\n', \
            'loaded patches:', '\t' + '  '.join(self.patches.keys()), '\n' \
            'loaded templates:', '\t' + '  '.join([os.path.splitext(os.path.basename(x))[0] for x in self.files["templates"]]), '\n'

            # quilt all the assets
            self.build_assets()
            print 'quilting time: %s' % (time_since(__t0))

            # setup pages output directories
            folders = [self.ouput_path(b, self.config["pages"]) for b in self.files["pages"]]
            folders += [self.ouput_path(b, self.config["pages"]) for b in self.files["posts"]]
            for folder in folders:
                if not os.path.isdir(folder):
                    os.makedirs(folder)

            # analyze all the posts
            if self.config["buildblog"]:
                self.analyze_posts()
                print 'quilting time: %s' % (time_since(__t0))

            # quilt all the pages
            self.quilt_pages(self.files["pages"])
            print 'quilting time: %s' % (time_since(__t0))

            # quilt all the post pages
            if self.config["buildblog"]:
                posts = reverse_chronological_order(self.blog.posts)
                self.quilt_pages([post["source"] for post in posts], posts)
                print 'quilting time: %s' % (time_since(__t0))

            # build the posts and blog
            adds = []
            if self.config["buildblog"]:
                self.blog.generate_blog_home()
                adds.append('blog')
                print 'quilting time: %s' % (time_since(__t0))
                self.blog.generate_featured()
                adds.append('featured')
                print 'quilting time: %s' % (time_since(__t0))
                self.blog.generate_group_pages("tags")
                adds.append('tags')
                print 'quilting time: %s' % (time_since(__t0))
                self.blog.generate_group_pages("categories")
                adds.append('categories')
                print 'quilting time: %s' % (time_since(__t0))

            # add site files
            if self.config["buildblog"] and self.config["buildatom"]:
                adds.append('atom')
                self.blog.generate_atom()
                print 'quilting time: %s' % (time_since(__t0))
            if self.config["buildblog"] and self.config["buildrss"]:
                adds.append('rss')
                self.blog.generate_rss()
                print 'rss quilting time: %s' % (time_since(__t0))
            if self.config["buildindex"]:
                adds.append('indexes')
                self.generate_index()
                print 'index quilting time: %s' % (time_since(__t0))
            if self.config["buildrobot"]:
                adds.append('robot.txt')
                self.generate_robot()
                print 'quilting time: %s' % (time_since(__t0))
            if self.config["buildsearch"]:
                adds.append('search.json')
                self.generate_search()
                print 'search quilting time: %s' % (time_since(__t0))
            if self.config["buildsitemap"]:
                adds.append('sitemap')
                self.generate_sitemap()
                print 'quilting time: %s' % (time_since(__t0))

            print '\n\nadding:\t', ' '.join(adds)
            print '\n', 'quilting is finished!', '\n'

            if self.config["spellcheck"]:
                self.spellcheck()
            print 'quilting time: %s' % (time_since(__t0))

            # write out current source hashes
            with open(sourcehash_path, 'w') as f:
                pickle.dump(sourcehash, f)
        else:
            print '\nSource files have not changed. Nothing to quilt.'

        return self
