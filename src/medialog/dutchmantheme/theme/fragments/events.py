def get_items(self):
    item_count = self.data['item_c']
    language = self.context.Language()
    keyword = self.get_keyword()
    from DateTime import DateTime
    date_range = {
        'query': (
            DateTime(),
        ),
        'range': 'min',
    }

    if keyword:
        return  self.context.portal_catalog(portal_type='Event', end=date_range, Language=language, Subject=keyword, sort_on='start')[:item_count]

    return self.context.portal_catalog(portal_type='Event', end=date_range, Language=language, sort_on='start')[:item_count]

def get_keyword(self):
    keyword = self.data['keyword']
    if isinstance(u"", str):
        keyword.encode('ascii','ignore')
    return [s for s in keyword]

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True


def cropped(self):
    if  (self.data['image_width'] and self.data['image_height']):
        return "Cropped"

    return False
