# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from plone import api
import os
#from plone.app.textfield.value import RichTextValue
from plone.namedfile.file import NamedBlobImage
from zope.interface import noLongerProvides
from zope.interface import alsoProvides
from medialog.controlpanel.interfaces import \
    IMedialogControlpanelSettingsProvider
from medialog.dutchmantheme.interfaces import IMedialogDutchmanThemeSettings


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "medialog.dutchmantheme:uninstall",
        ]

    def getNonInstallableProducts(self):
        """Hide the upgrades package from site-creation and quickinstaller."""
        return ["medialog.dutchmantheme.upgrades"]



def post_install(context):
    """add favicons etc"""
    portal = api.portal.get()
    _create_content(portal)
    alsoProvides(IMedialogDutchmanThemeSettings, IMedialogControlpanelSettingsProvider)

def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
    noLongerProvides(IMedialogDutchmanThemeSettings, IMedialogControlpanelSettingsProvider)

def upgrade(context):
    """Upgradel script"""
    # Do something at the end of the uninstallation of this package.
    pass

def _create_content(portal):
    """Lets create the icons and the user can customize them"""
    titles = [
        'favicon.png',
        'apple-touch-icon-57x57-precomposed.png',
        'apple-touch-icon-72x72-precomposed.png',
        'apple-touch-icon-114x114-precomposed.png',
        'apple-touch-icon-144x144-precomposed.png',
        'apple-touch-icon-precomposed.png',
        'apple-touch-icon.png'
        ]

    for i_image in titles:
        if not portal.get(i_image, False):
            icon_image = api.content.create(
                type='Image',
                container=portal,
                id=i_image,
                title=i_image,
            )

            icon_image.image = load_image(i_image)


def load_image(i_image):
    filename = os.path.join(os.path.dirname(__file__), 'theme',
                            i_image)

    #https://community.plone.org/t/python-3-plone-api-read-blob-image/8978

    return NamedBlobImage(
        data=open(filename, 'rb').read(),
        filename=u'{0}'.format(i_image)
    )
