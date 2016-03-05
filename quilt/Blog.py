"""
quilt.Blog

Provide blog capabilities for static site
{: .lead}

1. set `source` to `posts/` along with unique or default quilt and patches
2. as [`QuiltingRoom`](#QuiltingRoom) loops over pages append page data from [`Quilter`](#Quilter) to `Blog`
3. create list of posts in reverse chronological order
4. create group pages for tags and/or categories:
    1. create page that list all groups (e.g. list all tags)
    2. create page for each group with list of associated posts in reverse chronological order
5. generate `atom` feed and/or `rss` feed

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
from collections import defaultdict

from quilt.Quilter import Quilter
from quilt.Util import write_file, group_links, reverse_chronological_order, handlebar_replace, check_local_quilt
from quilt.Constants import ATOMENTRY, ATOMXML, GROUP_SINGLE_NAME, GROUP_VERBS
from quilt.Constants import RSSITEM, RSSXML
from quilt.Constants import GROUPVARS

#@profile
def create_post_list(posts=None, post_list_template='', offset=''):
    """create list html from posts"""

    postlist = []
    for post in posts:
        post_url = offset + os.path.basename(post['url'])
        postvars = {
            'url'          : post_url,
            'title'        : post['title'],
            'author'       : post['author'],
            'date'         : post['date'],
            'summary'      : post['summary'],
            'tag_link'     : os.path.join(os.path.dirname(post["url"]), 'tags', 'index.html'),
            'tag_list'     : group_links(post, "tags"),
            'category_link': os.path.join(os.path.dirname(post["url"]), 'categories', 'index.html'),
            'category_list': group_links(post, "categories")
        }
        postlist.append(handlebar_replace(post_list_template, postvars))
    return '\n'.join(postlist)

class Blog(object):
    """blog object"""

    #@profile
    def __init__(self, name='', source='', output='', quilt_pattern=None, patches=None, config=None):
        """create a blog"""

        self.name = name
        self.source = source
        self.output = output
        self.config = config
        self.quilt_pattern = quilt_pattern
        self.patches = patches
        self.posts = []
        self.fileschanged = {}

    #@profile
    def append(self, post=None):
        """append a post to the blog"""

        self.posts.append(post)
        return self

    #@profile
    def generate_blog_home(self):
        """generate blog index page"""

        # only redo index if any post has changed
        if any([self.fileschanged[x["source"]] for x in self.posts]):
            # stitch blog home page
            page = os.path.join(self.config["posts"], "index.html")

            # check for directory quilt and directory patches?
            quilt, patches = check_local_quilt(page, self.quilt_pattern, self.patches, self.config)

            # use index patch as starting point
            page_html = GROUPVARS % (
                self.name,
                self.name,
                self.config["author"]
            )
            page_html += patches["index"]

            # stitch the page together
            qultr = Quilter(page, quilt, patches, page_html, self.config)

            # update pagevars with special blog variables
            qultr.pagevars["latest_post"] = reverse_chronological_order(self.posts)[0]["content"]
            # generate reverse chronological order of first x posts
            qultr.pagevars["postitems"] = create_post_list(reverse_chronological_order(self.posts), patches['post_item'])

            qultr.stitch()
            qultr.clean_html()
            qultr.remove_empty()
            qultr.write()
            del qultr

        return self

    #@profile
    def group_by(self, name=''):
        """create group dictionary"""

        groups = defaultdict(list)
        for post in self.posts:
            post_groups = []
            if self.fileschanged[post["source"]] and name in post.keys():
                post_groups = post[name] if isinstance(post[name], list) else [post[name]]
            for group in post_groups:
                groups[group].append(post)
        return groups

    def generate_featured(self):
        """generate featured posts"""

        # only redo featured if any post has changed
        if any([self.fileschanged[x["source"]] for x in self.posts]):
            name = 'featured'

            # make group folder
            os.makedirs(os.path.join(self.config["posts"], name).replace(self.config["pages"], self.output))

            # create group -> page look up table
            groups = self.group_by(name)

            group = name
            posts = groups[True]

            # stitch blog home page
            page = os.path.join(self.config["posts"], name, "index.html")

            # check for directory quilt and directory patches?
            quilt, patches = check_local_quilt(os.path.dirname(page), self.quilt_pattern, self.patches, self.config)

            # use category or tag patch as page
            page_html = GROUPVARS % (
                'Featured Posts',
                'Cherry Picked Posts',
                self.config["author"]
            )
            page_html += patches['group']

            # stitch the page together
            qultr = Quilter(page, quilt, patches, page_html, self.config)

            # update pagevars with list of group posts
            qultr.pagevars["postitems"] = create_post_list(reverse_chronological_order(posts), patches['post_item'], '../')
            qultr.pagevars["group"] = ''
            qultr.pagevars["grouptype"] = group.title()

            qultr.stitch()
            qultr.clean_html()
            qultr.remove_empty()
            qultr.write()
            del qultr

    #@profile
    def generate_group_pages(self, name=''):
        """generate tag or category page"""

        singular_name = GROUP_SINGLE_NAME[name]
        verb =  GROUP_VERBS[name]

        # make group folder
        os.makedirs(os.path.join(self.config["posts"], name).replace(self.config["pages"], self.output))

        # create group -> page look up table
        groups = self.group_by(name)

        group_reduce_data = {}

        # create page for each group
        for group, posts in groups.items():

            # reduce all post-data for each group
            if group not in group_reduce_data.keys():
                group_reduce_data[group] = {}
            for post in posts:
                for postvar in post.keys():
                    if 'post-' in postvar:
                        if postvar not in group_reduce_data[group].keys():
                            group_reduce_data[group][postvar] = 0
                        group_reduce_data[group][postvar] += post[postvar]

            # stitch group page
            page = os.path.join(self.config["posts"], name, "%s.html" % group.lower())

            # check for directory quilt and directory patches?
            quilt, patches = check_local_quilt(os.path.dirname(page), self.quilt_pattern, self.patches, self.config)

            # use category or tag patch as page
            page_html = GROUPVARS % (
                '%s > %s' % (singular_name.title(), group.title()),
                'Posts %s %s' % (verb, group.title()),
                self.config["author"]
            )
            page_html += patches['group']

            # stitch the page together
            qultr = Quilter(page, quilt, patches, page_html, self.config)

            # update pagevars with list of group posts
            qultr.pagevars["postitems"] = create_post_list(reverse_chronological_order(posts), patches['post_item'], '../')
            qultr.pagevars["group"] = group.title()
            qultr.pagevars["grouptype"] = singular_name.title()

            qultr.stitch()
            qultr.clean_html()
            qultr.remove_empty()
            qultr.write()
            del qultr

        # stitch group home page
        if groups:
            page = os.path.join(self.config["posts"], name, "index.html")

            # check for directory quilt and directory patches?
            quilt, patches = check_local_quilt(os.path.dirname(page), self.quilt_pattern, self.patches, self.config)

            # use categories or tags patch as page
            page_html = GROUPVARS % (
                name.title(),
                name.title(),
                self.config["author"]
            )
            page_html += patches['groups']

            # stitch the page together
            qultr = Quilter(page, quilt, patches, page_html, self.config)

            # update pagevars with list of groups
            groupitems = []
            for group, posts in groups.items():
                groupvars = {
                    'grouptype' : name.title(),
                    'grouplink' : "%s.html" % group.lower(),
                    'group'     : group.title(),
                    'post-count': len(posts)
                }
                groupvars.update(group_reduce_data[group])
                groupitems.append(handlebar_replace(patches['group_item'], groupvars))

            qultr.pagevars["grouptype"] = name.title()
            qultr.pagevars["groupitems"] = '\n'.join(groupitems)

            qultr.stitch()
            qultr.clean_html()
            qultr.remove_empty()
            qultr.write()
            del qultr

        return self

    #@profile
    def generate_atom(self):
        """generate atom xml"""

        # only redo atom if any post has changed
        if any([self.fileschanged[x["source"]] for x in self.posts]):
            # generate an atom entry for each blog page
            entries = [ATOMENTRY % (
                post['title'],
                post['url'],
                post['url'],
                self.config['atomid'],
                post['date'],
                post['summary'], #.encode('utf8'),
                post['content'], #.encode('utf8'),
                post['author'],
                post['email']
            ) for post in self.posts]

            # generate the atom xml file
            atom_xml = (ATOMXML % (
                self.config["name"],
                self.config["posts"],
                self.config["domain"],
                self.config["domain"],
                self.config["atomid"],
                self.config["now"]["iso"],
                ''.join(entries)
            )).encode('utf8')

            feed_path = os.path.join(self.output, 'feed')
            # make feed/ if need be
            if not os.path.exists(feed_path):
                os.makedirs(feed_path)

            # output new atom files
            write_file(os.path.join(feed_path, 'atom.xml'), atom_xml)
            write_file(os.path.join(feed_path, 'feed.atom'), atom_xml)

        return self

    #@profile
    def generate_rss(self):
        """geneate rss xml"""

        # only redo rss if any post has changed
        if any([self.fileschanged[x["source"]] for x in self.posts]):
            # generate an rss item for each blog page
            items = [RSSITEM % (
                post['title'],
                post['url'],
                self.config['atomid'],
                post['date'],
                post['summary'], #.encode('utf8')
            ) for post in self.posts]

            # generate the rss xml file
            rss_xml = (RSSXML % (
                self.config['name'],
                self.config['posts'],
                self.config['domain'],
                self.config['rssid'],
                self.config["now"]["iso"],
                self.config["now"]["iso"],
                self.config['author'],
                ''.join(items)
            )).encode('utf8')

            feed_path = os.path.join(self.output, 'feed')
            # make feed/ if need be
            if not os.path.exists(feed_path):
                os.makedirs(feed_path)

            # output new atom files
            write_file(os.path.join(feed_path, 'rss.xml'), rss_xml)
            write_file(os.path.join(feed_path, 'feed.rss'), rss_xml)

        return self
