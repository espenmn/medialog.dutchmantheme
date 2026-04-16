def item_url(self):
    item = load_item(self)
    return item.getURL()

def load_item(self):
    item =  self.data['content_item']
    items =self.context.portal_catalog(UID=item)
    return items[0]

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True

def border_radius(self):
    return self.data.get('border_radius') or None
    # return self.data['border_radius'] or None 
