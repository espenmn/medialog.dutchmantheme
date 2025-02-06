def folder_url(self):
	url = self.data['folder_url'].encode('ascii','ignore')
	return url

def item_width(self):
	images = self.data['image_items']
	return (100/images) - 1

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
