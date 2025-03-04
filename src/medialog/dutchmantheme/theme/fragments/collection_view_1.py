def get_items(self):
    language = self.context.Language()
    linked = self.data['linked_folder'] or self.data['select_folder'] or self.get_uid()
    if linked:
        folder = self.context.portal_catalog(UID=linked)
        mappe =  folder[0].getObject()
        folder_path = '/'.join(mappe.getPhysicalPath())
        if mappe.portal_type != 'Collection':
            return self.context.portal_catalog(path={'query': folder_path, 'depth': 1}, Language=language)
        
        query = mappe.query
        query_dict = {q['i']: q['v'] for q in query if 'i' in q and 'v' in q}
        return self.context.portal_catalog(**query_dict) 
 

def ctype(self):
    if 'ctype' in self.data.keys():
        return self.data['ctype']
    return True

def csubject(self):
    if 'csubject' in self.data.keys():
        return self.data['csubject']
    return None

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True

def get_id(self):
    if self.data['collectionfilter']:
        return 'content-core'
    else:
        return 'fragment-{0}'.format(self.id)

def max_chars(self):
    return self.data.max_chars or 1000