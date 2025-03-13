def folder_url(self):
	url = self.data['folder_url']
	return url

def item_width(self):
	images = self.data['image_items']
	return (100/images) - 1

def get_folder(self):
    language = self.context.Language()
    folder_path = self.folder_url()
    the_folder = self.context.portal_catalog(path={'query': folder_path, 'depth': 1}, Language=language)
    return the_folder[0].getObject() 

def get_items(self):
    language = self.context.Language()
    folder_path = self.folder_url()
    return self.context.portal_catalog(path={'query': folder_path, 'depth': 1}, Language=language)
    
def color1(self):
    return self.data['color1']

def color2(self):
    return self.data['color2']

def color3(self):
    return self.data['color3']

def color4(self):
    return self.data['color4']

def css_file(self):
    return self.data['css_file']

def image_items(self):
    return self.data['image_items']
 
def min_width(self):
    return self.data['min_width']

def image_size(self):
    return self.data['image_size']

def button(self):
    return self.data['button']

def get_folder_title(self):
    folder = self.get_folder()
    return folder.Title()

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
