import logging
import optparse

import gettext
from gettext import gettext as _
gettext.textdomain('linkmanager-lens')

from linkmanager.db import DataBase

from singlet.lens import SingleScopeLens, IconViewCategory, ListViewCategory

from linkmanager_lens import linkmanager_lensconfig

class LinkmanagerLens(SingleScopeLens):

    class Meta:
        name = 'linkmanager'
        description = 'Linkmanager Lens'
        search_hint = 'Search Linkmanager'
        icon = 'linkmanager.svg'
        search_on_blank=True

    # TODO: Add your categories
    example_category = ListViewCategory("Examples", 'help')

    def search(self, search, results):
        # TODO: Add your search results
        d = DataBase()
        if search == '':
            return
        else:
            search = [tag for tag in search.split(' ') if tag != '']
        links = d.sorted_links(*search)
        c_links = len(links)
        if c_links == 0:
            return
        for link in links:
            results.append(
                link,
                'ubuntu-logo',
                self.example_category,
                "text/html",
                link,
                '...',
                link
            )
