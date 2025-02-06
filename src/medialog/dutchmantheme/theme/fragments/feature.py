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

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
