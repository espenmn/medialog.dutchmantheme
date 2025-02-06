def get_items(self):
    linked = self.data['linked_folder'] or self.data['select_folder']
    folder = self.context.portal_catalog(UID=linked)
    return folder[0].getObject()

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return False
