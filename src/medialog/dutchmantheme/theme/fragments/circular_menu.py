def get_item_image(self):
    linked = self.data['linked_folder'] or self.data['select_folder']
    if linked:
        folder = self.context.portal_catalog(UID=linked)
        return folder[0]
    return self.context

def get_items(self):
    linked = self.data['linked_folder'] or self.data['select_folder']
    radius = self.data['radius']
    standard_icon = self.data['iconfield']

    if linked:
        folder = self.context.portal_catalog(UID=linked)
        items = folder[0].getObject().items()
    else:
        items = self.context.items()

    item_count = len(items)
    rotation = (2 *math.pi)/item_count

    rotate_list = []

    for index, item in enumerate(items):
        real_index = index + 1
        turner = real_index * rotation
        x = radius * math.sin(turner)
        y = radius * math.cos(turner)
        item1 = item[1]
        iconfield = standard_icon
        if hasattr(item1,'iconfield'):
            iconfield = item1.iconfield
        rotate_list.append({'item': item,
                            'index': index,
                            'iconfield': iconfield,
                            'rotation': turner,
                            'title': item[0],
                            'obj': item1.absolute_url_path(),
                            'x':x,
                            'y':y}
        )

    return rotate_list


def get_height(self):
    radius = self.data['radius']
    return radius * 2 + 144

def get_radius(self):
    return self.data['radius']

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
    return False
