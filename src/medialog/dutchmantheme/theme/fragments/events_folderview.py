def get_items(self):
    language = self.context.Language()
    item_count = self.data['item_c']
    linked = self.data['linked_folder'] or self.data['select_folder'] or self.get_uid()
    if linked:
        folder = self.context.portal_catalog(UID=linked)
        mappe =  folder[0].getObject()
        folder_path = '/'.join(mappe.getPhysicalPath())
        from DateTime import DateTime
        date_range = {
            'query': (
                DateTime(),
            ),
            'range': 'min',
        }
        if mappe.portal_type != 'Collection':
            return self.context.portal_catalog(path={'query': folder_path, 'depth': 1}, Language=language, end=date_range, sort_on='start')[:item_count]
        
        query = mappe.query
        query_dict = {q['i']: q['v'] for q in query if 'i' in q and 'v' in q}
        return self.context.portal_catalog(**query_dict)[:item_count]
 
 
    
 

# return self.context.portal_catalog(portal_type='Event', path={'query': folder_path,},  Language=language, end=date_range, sort_on='start')[:item_count]
 

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
