def editmode(self):
    form = self.request.form

    if '_layouteditor' in form:
        return True

    if 'disabled' in self.data:
        return self.data['disabled'] is False

    return True

def folder_url(self):
    return self.data.get('folder_url', '')

def item_width(self):
    images = self.data.get('image_items', 1)
    return (100 / images) - 1

def b_point(self):
    min_width = self.data.get('min_width', 0)
    return min_width * 1.95


def color1(self):
    return self.data.get('color1')


def color2(self):
    return self.data.get('color2')


def color3(self):
    return self.data.get('color3')


def color4(self):
    return self.data.get('color4')


def css_file(self):
    return self.data.get('css_file')


def image_items(self):
    return self.data.get('image_items')


def min_width(self):
    return self.data.get('min_width')


def image_size(self):
    return self.data.get('image_size')


def button(self):
    return self.data.get('button')


def get_folder(self):
    language = self.context.Language()
    portal = self.context.portal_url.getPortalObject()
    portal_path = '/'.join(portal.getPhysicalPath())

    folder_url = self.data.get('folder_url', '')

    if portal_path:
        folder_path = f"{portal_path}/{folder_url}"
    else:
        folder_path = folder_url

    results = self.context.portal_catalog(
        path={'query': folder_path, 'depth': 0},
        Language=language
    )

    if results:
        return results[0].getObject()

    return None


def test_path(self):
    portal = self.context.portal_url.getPortalObject()
    portal_path = '/'.join(portal.getPhysicalPath())
    
    if portal_path: 
        folder_path = f'{portal_path}/{self.folder_url}'
    else:
        folder_path = self.folder_url
        
    return folder_path

def get_items(self):
    language = self.context.Language()
    portal = self.context.portal_url.getPortalObject()
    portal_path = '/'.join(portal.getPhysicalPath())
    
    if portal_path: 
        folder_path = f'{portal_path}/{self.data['folder_url']}'
    else:
        folder_path = self.data['folder_url']
        
    return self.context.portal_catalog(path={'query': folder_path, 'depth': 1}, Language=language)


def get_folder_title(self):
    folder = self.get_folder()

    if folder:
        return folder.Title()

    return ""