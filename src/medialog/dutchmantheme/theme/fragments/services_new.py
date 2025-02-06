def folder_url(self):
	url = self.data['folder_url'].encode('ascii','ignore')
	return url

def item_width(self):
	images = self.data['image_items']
	return (100/images) - 2

def b_point(self):
	min_width = self.data['min_width']
	return (min_width*1.95)

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
