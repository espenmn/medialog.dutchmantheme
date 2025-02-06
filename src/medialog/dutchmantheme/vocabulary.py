from zope.interface import directlyProvides
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from plone import api

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('medialog.dutchmantheme')

def format_title(folder):
    return "{}  ...   [ {} ]".format( folder.Title, folder.getURL())



def ShowImagesVocabulary(context):

    images = api.content.find(portal_type='Image', sort_on='sortable_title')

    if images:
        terms = [ SimpleTerm(value=img.UID, token=img.UID, title=img.Title) for img in images ]
    return SimpleVocabulary(terms)

directlyProvides(ShowImagesVocabulary, IVocabularyFactory)



def ShowFoldersVocabulary(context):

    folders = api.content.find(portal_type=['Folder', 'Collection'] , sort_on='sortable_title')

    if folders:
        terms = [ SimpleTerm(value=folder.UID, token=folder.UID, title=format_title(folder)) for folder in folders ]
    return SimpleVocabulary(terms)

directlyProvides(ShowFoldersVocabulary, IVocabularyFactory)
