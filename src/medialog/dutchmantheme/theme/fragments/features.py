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
    keyword = self.data['keyword'] 
    language = self.context.Language
    sorton = 'modified'
    sort_order = 'descending'
    if 'sort_order' in data.keys():
        sort_order = str(data['sort_order'])
    if 'sort_on' in data.keys():
        sorton = data['sort_on']
        
    linked = self.data['linked_folder'] 
    if linked:
        folder = self.context.portal_catalog(UID=linked)
        mappe =  folder[0].getObject()
        folder_path = '/'.join(mappe.getPhysicalPath())
        if mappe.portal_type != 'Collection':
            return self.context.portal_catalog(path={'query': folder_path, 'depth': 1}, sort_on=sorton, sort_order=sort_order, Language=language)
        
        query = mappe.query
        query_dict = {q['i']: q['v'] for q in query if 'i' in q and 'v' in q}
        return self.context.portal_catalog(**query_dict) 
    
    if keyword:
        return self.context.portal_catalog(Subject=keyword, sort_on=sorton, sort_order=sort_order, Language=language)
    
    return None
    
def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
