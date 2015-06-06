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
from quilt.Util import write_file, group_links, reverse_chronological_order, check_local_quilt
from quilt.Constants import ATOMENTRY, ATOMXML
from quilt.Constants import RSSITEM, RSSXML
from quilt.Constants import POST, POSTLIST
from quilt.Constants import GROUP, GROUPLIST, GROUPVARS

#@profile
def create_post_list(name, posts=None, offset=''):
    """create list html from posts"""

    postlist = []
    for post in posts:
        post_url = offset + os.path.basename(post['url'])
        postlist.append(POST % (
            post_url,
            post['title'],
            post['author'],
            post['date'],
            post['summary'].encode('utf8'),
            post_url,
            os.path.join(os.path.dirname(post["url"]), 'tags', 'index.html'),
            group_links(post, "tags"),
            os.path.join(os.path.dirname(post["url"]), 'categories', 'index.html'),
            group_links(post, "categories")
        ))
    return POSTLIST % (name, ''.join(postlist))

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

    #@profile
    def append(self, post=None):
        """append a post to the blog"""

        self.posts.append(post)
        return self

    #@profile
    def generate_blog_home(self):
        """generate blog index page"""

        # generate reverse chronological order of first x posts
        page_html = GROUPVARS % (
            self.name,
            self.name,
            "quilt"
        )
        page_html = ''.join((page_html, create_post_list(self.name, reverse_chronological_order(self.posts))))

        # stitch blog home page
        page = os.path.join(self.config["posts"], "index.html")

        # check for directory quilt and directory patches?
        quilt, patches = check_local_quilt(page, self.quilt_pattern, self.patches, self.config)

        # stitch the page together
        qultr = Quilter(page, quilt, patches, page_html, self.config)
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
            post_groups = post[name] if isinstance(post[name], list) else [post[name]]
            for group in post_groups:
                groups[group].append(post)
        return groups

    #@profile
    def generate_group_pages(self, name=''):
        """generate tag or category page"""

        # make group folder
        os.makedirs(os.path.join(self.config["posts"], name).replace(self.config["pages"], self.output))

        # create group -> page look up table
        groups = self.group_by(name)

        # create page for each group
        for group, posts in groups.items():
            page_html = create_post_list('%s Posts' % (group.title()), reverse_chronological_order(posts), '../')

            # stitch blog home page
            page = os.path.join(self.config["posts"], name, "%s.html" % group)

            # check for directory quilt and directory patches?
            quilt, patches = check_local_quilt(os.path.dirname(page), self.quilt_pattern, self.patches, self.config)

            # stitch the page together
            qultr = Quilter(page, quilt, patches, page_html, self.config)
            qultr.stitch()
            qultr.clean_html()
            qultr.remove_empty()
            qultr.write()
            del qultr

        # create index of groups
        grouplist = ''.join([GROUP % (name, "%s.html" % (group), group, len(posts)) for group, posts in groups.items()])
        page_html = GROUPLIST % (name.title(), name, grouplist)

        # stitch blog home page
        page = os.path.join(self.config["posts"], name, "index.html")

        # check for directory quilt and directory patches?
        quilt, patches = check_local_quilt(os.path.dirname(page), self.quilt_pattern, self.patches, self.config)
            
        # stitch the page together
        qultr = Quilter(page, quilt, patches, page_html, self.config)
        qultr.stitch()
        qultr.clean_html()
        qultr.remove_empty()
        qultr.write()
        del qultr

        return self

    #@profile
    def generate_atom(self):
        """generate atom xml"""

        # generate an atom entry for each blog page
        entries = [ATOMENTRY % (
            post['title'],
            post['url'],
            post['url'],
            self.config['atomid'],
            post['date'],
            post['summary'].encode('utf8'),
            post['content'].encode('utf8'),
            post['author'],
            post['email']
        ) for post in self.posts]

        # generate the atom xml file
        atom_xml = ATOMXML % (
            self.config["name"],
            self.config["posts"],
            self.config["domain"],
            self.config["domain"],
            self.config["atomid"],
            self.config["now"]["iso"],
            ''.join(entries)
        )

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

        # generate an rss item for each blog page
        items = [RSSITEM % (
            post['title'],
            post['url'],
            self.config['atomid'],
            post['date'],
            post['summary'].encode('utf8')
        ) for post in self.posts]

        # generate the rss xml file
        rss_xml = RSSXML % (
            self.config['name'],
            self.config['posts'],
            self.config['domain'],
            self.config['rssid'],
            self.config["now"]["iso"],
            self.config["now"]["iso"],
            self.config['author'],
            ''.join(items)
        )

        feed_path = os.path.join(self.output, 'feed')
        # make feed/ if need be
        if not os.path.exists(feed_path):
            os.makedirs(feed_path)

        # output new atom files
        write_file(os.path.join(feed_path, 'rss.xml'), rss_xml)
        write_file(os.path.join(feed_path, 'feed.rss'), rss_xml)

        return self
