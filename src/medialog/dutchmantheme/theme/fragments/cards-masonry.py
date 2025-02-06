def small(self):
    small = self.data['small']
    return 100/small - 2

def medium(self):
    medium = self.data['medium']
    return 100/medium - 2

def large(self):
    large = self.data['large']
    return 100/large - 2

def get_items(self):
    keyword = self.data['keyword']
    if isinstance(u"", str):
        keyword = self.data['keyword'].encode('ascii','ignore')
    language = self.context.Language()
    sorton = 'modified'
    if 'sort_on' in self.data.keys():
        sorton = self.data['sort_on']

    sort_order = 'descending'
    if 'sort_order' in self.data.keys():
        sort_order = str(self.data['sort_order'])

    return self.context.portal_catalog(sort_on=sorton, Language=language, sort_order=sort_order, Subject=keyword)

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return False
