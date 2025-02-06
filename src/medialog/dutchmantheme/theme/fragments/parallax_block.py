def p_image(self):
    item =  self.data['background_image']
    #return item

    items =self.context.portal_catalog(UID=item)
    return items
    #return self.context.portal_catalog(uuid=(self.data['background_image']))


def one_image(self):
    item =  self.data['background_image']
    #return item

    items =self.context.portal_catalog(UID=item)
    return items[0]
    #return self.context.portal_catalog(uuid=(self.data['background_image']))

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
