def one_link(self):
    item =  self.data['link']
    #return item

    items =self.context.portal_catalog(UID=item)
    if items:
        return items[0].getObject()
    return None
    #return self.context.portal_catalog(uuid=(self.data['background_image']))

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
