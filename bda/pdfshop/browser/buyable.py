#from pp.client.plone.compatible import InitializeClass
try:
    from App.class_init import InitializeClass
except ImportError:
    from Globals import InitializeClass

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class HTMLView(BrowserView):
    """ This view renders a HMTL fragment for buyable type """

    template = ViewPageTemplateFile('buyable.pt')

    def __call__(self, *args, **kw):
        return self.template(self.context)

InitializeClass(HTMLView)

