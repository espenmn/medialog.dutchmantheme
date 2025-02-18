def get_items(self):
    language = self.context.Language()
    linked = self.data['linked_folder'] or self.data['select_folder'] or self.get_uid()
    if linked:
        folder = self.context.portal_catalog(UID=linked)
        mappe =  folder[0].getObject()
        folder_path = '/'.join(mappe.getPhysicalPath())
        if mappe.portal_type != 'Collection':
            return self.context.portal_catalog(path={'query': folder_path,}, Language=language  )
        
        query = mappe.query
        query_dict = {q['i']: q['v'] for q in query if 'i' in q and 'v' in q}
        return self.context.portal_catalog(**query_dict) 
 
 
def get_uid(self):
    return self.context.UID()

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
