def get_items(self):
    item_count = self.data['item_c']
    language = self.context.Language()
    linked = self.data['linked_folder']
    folder_path = '/'.join(context.getPhysicalPath())
    from DateTime import DateTime
    date_range = {
        'query': (
            DateTime(),
        ),
        'range': 'min',
    }

    if linked:
        folder_path = self.get_path()

    return self.context.portal_catalog(portal_type='Event', path={'query': folder_path,},  Language=language, end=date_range, sort_on='start')[:item_count]

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


def cropped(self):
    if  (self.data['image_width'] and self.data['image_height']):
        return "Cropped"

    return False
