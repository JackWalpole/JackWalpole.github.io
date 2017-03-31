#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jack Walpole'
SITENAME = u'Digging Deeper'
SITEURL = ''

PATH = 'content'
PAGE_PATHS = ['pages']

STATIC_PATHS = ['images']

TIMEZONE = 'GB'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Bristol Earth Sciences', 'http://www.bristol.ac.uk/earthsciences/'),
('My University Page', 'http://www.bristol.ac.uk/earthsciences/people/jack-walpole/index.html'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/jwalpole9'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Added some lines to enable Jupyter blogging
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

IGNORE_FILES = [ '.ipynb_checkpoints' ]