def get_items(self):
    linked = self.data['linked_folder'] or self.data['select_folder']
    if linked:
        folder = self.context.portal_catalog(UID=linked)
        return folder[0].getObject()
    return self.context

def get_margin(self):
    image_width = self.data['image_width']
    return image_width /20

def get_width(self):
    image_width = self.data['image_width']
    max_images = self.data['max_images']
    return image_width * 1.10 * max_images

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
