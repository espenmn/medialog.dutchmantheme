def get_images(self):
    imagelist = self.data['imagelist']
    image_items = self.context.portal_catalog(UID=imagelist)
    return image_items

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
