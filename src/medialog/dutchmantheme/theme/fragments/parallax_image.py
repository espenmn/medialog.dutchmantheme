def one_image(self):
    item =  self.data['background_image']
    items =self.context.portal_catalog(UID=item)
    return items[0]

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
