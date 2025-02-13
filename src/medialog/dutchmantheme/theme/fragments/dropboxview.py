def get_items(self):
    language = self.context.Language()
    linked = self.data['linked_folder']
    if linked:
        folder = self.context.portal_catalog(UID=linked)
        mappe =  folder[0].getObject()
        folder_path = '/'.join(mappe.getPhysicalPath())
        if mappe.portal_type != 'Collection':
            # content_type = self.data['content_type']
            # sort_on = self.data['sort_on']
            # sort_order = str(self.data['sort_order'])
            
            return self.context.portal_catalog(path={'query': folder_path,}, Language=language  )

def get_path(self):
    linked = self.data['linked_folder']
    folder = self.context.portal_catalog(UID=linked)
    mappe =  folder[0].getObject()
    return  '/'.join(mappe.getPhysicalPath())

def list_items(self):
    linked = self.data['linked_folder']
    if linked:
        folder = self.context.portal_catalog(UID=linked)
        if folder[0].portal_type=='Collection':
            return folder[0].getObject()


def get_id(self):
    if self.data['collectionfilter']:
        return 'content-core'
    else:
        return 'fragment-{0}'.format(self.id)


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
