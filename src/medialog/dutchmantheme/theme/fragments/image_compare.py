def image1(self):
    item =  self.data['image1'] or self.data['image1b']
    items = self.context.portal_catalog(UID=item)
    return items[0].getObject()

def image2(self):
    item =   self.data['image2'] or self.data['image2b']
    items =self.context.portal_catalog(UID=item)
    return items[0].getObject()

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
