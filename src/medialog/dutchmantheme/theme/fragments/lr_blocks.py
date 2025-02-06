def get_allitems(self):
    linked = self.data['linked_folder']

    if linked:
        folder = self.context.portal_catalog(UID=linked)
        return folder[0].getObject()

    selected = self.data['select_folder']

    if selected:
        folder = self.context.portal_catalog(UID=selected)
        return folder[0].getObject()

    return None

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
