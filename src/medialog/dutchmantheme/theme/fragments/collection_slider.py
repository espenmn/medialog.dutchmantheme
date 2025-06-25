def get_items(self):
    language = self.context.Language()
    linked = self.data['linked_folder'] or self.data['select_folder'] or self.get_uid()
    if linked:
        folder = self.context.portal_catalog(UID=linked)
        mappe =  folder[0].getObject()
        folder_path = '/'.join(mappe.getPhysicalPath())
        if mappe.portal_type != 'Collection':
            sorton = 'modified'
            if 'sort_on' in self.data.keys():
                sorton = self.data['sort_on']
            return self.context.portal_catalog(path={'query': folder_path, 'depth': 1}, sort_on=sorton, Language=language)
        
        query = mappe.query
        query_dict = {q['i']: q['v'] for q in query if 'i' in q and 'v' in q}
        return self.context.portal_catalog(**query_dict) 

 

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return False
