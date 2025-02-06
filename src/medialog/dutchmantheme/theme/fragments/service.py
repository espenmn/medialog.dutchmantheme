def get_item(self):
    item =  self.data['link'].encode('ascii')
    items =self.context.portal_catalog(UID=item)
    return items[0]

def item_url(self):
    item =  self.data['link']
    items =self.context.portal_catalog(UID=item)
    return items[0].getURL()

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
