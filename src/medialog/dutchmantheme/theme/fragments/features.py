def family_css(self):
    #return css_family_class, like fa, wi
    iconset = self.iconset()
    if iconset == 'glyphicon':
         return 'glyphicon'
    if iconset == 'mapicon':
        return 'map-icons'
    if iconset == 'typicon':
        return 'typcn'
    if iconset == 'ionicon':
        return 'ionicons'
    if iconset == 'weathericon':
        return 'wi'
    if iconset == 'octicon' :
        return 'octicon'
    if iconset == 'elusiveicon':
        return 'el-icon'
    if iconset == 'medialogfont':
        return 'medialogfont'
    if iconset == 'iconpickerfont':
        return 'iconpickerfont'
    if iconset == 'lineawsome':
        return 'linewsome'

    return 'fa'

def iconset(self):
    """Returns current iconset name This is also used for loading the resources below"""
    return self.context.portal_registry['medialog.iconpicker.interfaces.IIconPickerSettings.iconset']


def get_items(self):
    data = self.data
    keyword = data['keyword']
    if isinstance(u"", str):
        keyword.encode('ascii','ignore')
    sorton = 'modified'
    sort_order = 'descending'
    if 'sort_order' in data.keys():
        sort_order = str(data['sort_order'])
    if 'sort_on' in data.keys():
        sorton = data['sort_on']
    language = self.context.Language
    return self.context.portal_catalog(Subject=keyword, sort_on=sorton, sort_order=sort_order, Language=language)

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
