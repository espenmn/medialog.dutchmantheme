from zope.interface import implements, Interface
#, Attribute
from Products.Five import BrowserView
from plone.dexterity.interfaces import IDexterityContent
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api

import re


# -*- coding: utf-8 -*-
from plone.app.contenttypes.utils import DEFAULT_TYPES
from plone.dexterity.interfaces import IDexterityFTI
from Products.CMFCore.utils import getToolByName
from zope.component import queryUtility
from zope.component.hooks import getSite


class IAzView(BrowserView):
    """collection view"""

    def __init__(self, context, request):
        self.context = context
        self.request = request


class IChangelayoutView(BrowserView):
    """change layout from a to b"""


    def __init__(self, context, request):
        self.context = context
        self.request = request



    def fix_map_cordinates(self):
        #every image that does not have a proper name should be renamed
        import pdb; pdb.set_trace()
        items = api.content.find(Type='MapLocation')
        a = 0
        for item in items:
            #obj = item.getObject()
            obj = item.getObject()
            old_cordinates = item.old_cordinates()
            long = eval(old_cordinates)[0]
            lat =  eval(old_cordinates)[1]
            #obj.coordinates     = "POINT({0} {1})".format.(long, lat)
            ICoordinates.coordinates = "POINT({0} {1})".format(long, lat)
            #obj.new_coordinates = "POINT({0} {1})".format.(long, lat)
            #Might as well reindex everything, it is migrated after all…
            obj.reindexObject()
            #import pdb; pdb.set_trace()

            #obj.reindexObject(idxs=['Title'])
            a = a + 1

        return a

    def hide_images(self):
        #every image that does not have a proper name should be hidden
        items = api.content.find(Type='Image')
        a = 0
        for item in items:
            #itempath = '/langs-kaiene/ymse-bilder/copy2_of_FergeSelbakLisleby.JPG'
            obj = item.getObject()
            if len(obj.Title()) == 0:
                if obj.exclude_from_nav == False:
                    a = a + 1
                    obj.exclude_from_nav = True
                    obj.reindexObject(idxs=['exclude_from_nav'])
        return a

    def folder_prev_next(self):
        #enabel prev next for all folders
        items = api.content.find(Type='Folder')
        a = 0
        for item in items:
            obj = item.getObject()
            if obj.nextPreviousEnabled == False:
                a = a + 1
            #import pdb; pdb.set_trace()
            obj.nextPreviousEnabled = True
            obj.reindexObject(idxs=['nextPreviousEnabled'])
        return a


    def x_dosomething(self):
        fra = 'folder_leadimage_view'
        til = 'summary_view'
        antall = 0
        items = api.content.find(layout=fra)
        for i in items:
            antall = antall + 1
            i.setLayout(til)
            obj = i.getObject()
            obj.setLayout(til)
            obj.reindexObject(idxs=['layout'])
        return antall


    def add_titles(self):
        #every image that does not have a proper name should be renamed
        items = api.content.find(Type='Image')
        a = 0
        for item in items:
            #obj = item.getObject()
            if len(item.Title) == 0:
                obj = item.getObject()
                #import pdb; pdb.set_trace()
                line = item.id
                try:
                    line = obj.image.filename
                except:
                    line = item.id
                line = re.sub('.jpg','', line)
                line = re.sub('.JPG','', line)
                line = re.sub('DS','Ds', line)
                line = line.title()
                line = re.sub(r"\B([A-Z])", r" \1", line)
                line = re.sub('Ds','DS', line)
                line = re.sub('\.',  r' ', line)
                #line = re.sub('.([0-9])',  r' \1', line)
                item.Title = line
                obj.setTitle(line)
                obj.reindexObject(idxs=['Title'])
                a = a + 1

        return a




    def set_image_size(self):
        #every image that does not have a proper name should be renamed
        a = 0
        items = api.content.find(Type='Image')
        for item in items:
            obj = item.getObject()
            import pdb; pdb.set_trace()
            if obj.leadsize == 'large':
                obj.leadsize = 'larger'
                obj.reindexObject(idxs=['leadsize'])
                a = a + 1

        return a


    def fix_titles(self):
        #every image that does not have a proper name should be renamed
        a = 0
        change_text = { 'Mms': 'MMS',
                    'Lms': 'LMS',
                    'Iii': 'III',
                    'Ii': 'II',
                    'Hms': 'HMS',
                    'Tc': 'TC',
                    'Nss': 'NSS'
                  }

        items = api.content.find(Type='Image')
        for item in items:
            obj = item.getObject()
            for key, value in change_text.items():
                if key in item.Title:
                    #import pdb; pdb.set_trace()
                    line = item.Title
                    line = re.sub(key, value, line)
                    item.Title = line
                    obj.setTitle(line)
                    #print (line)
                    obj.reindexObject(idxs=['Title'])
                    a = a + 1

        return a
