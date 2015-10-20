from __future__ import absolute_import

from confpages.loaders import Loader, Page


class BaseLoader(Loader):
    """The base page loader."""

    content = '''
<!DOCTYPE html>
<html>
  <head>
    <title>{title}</title>
  </head>
  <body>
    <p>This is the content from the {loader_name}.</p>
  </body>
</html>
'''

    def get_page(self, name, only_api_url=False):
        """Retrieve the page object."""
        page = Page(name)
        if not only_api_url:
            page.title = name.capitalize()
            page.content = self.content.format(
                title=page.title,
                loader_name=self.__class__.__name__
            )
        return page


class LoaderA(BaseLoader):
    """The page loader A."""


class LoaderB(BaseLoader):
    """The page loader B."""


loader_a = LoaderA()
loader_b = LoaderB()
