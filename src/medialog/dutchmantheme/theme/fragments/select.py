def get_items(self):
    language = self.context.Language()
    linked = self.data['linked_folder']
    folder_path = '/'.join(context.getPhysicalPath())
    content_type = self.data['content_type']
    sort_on = self.data['sort_on']
    sort_order = str(self.data['sort_order'])

    if linked:
        folder_path = self.get_path()

    folder_path.encode('ascii','ignore')

    return self.context.portal_catalog(portal_type=content_type, path={'query': folder_path,}, Language=language, sort_on=sort_on, sort_order=sort_order)

def get_path(self):
    linked = self.data['linked_folder']
    folder = self.context.portal_catalog(UID=linked)
    mappe =  folder[0].getObject()
    return  '/'.join(mappe.getPhysicalPath())

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
