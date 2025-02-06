def css_class(self):
    card_items = int(self.data['card_items'])
    return (12/card_items)

def get_items(self):
 card_items = int(self.data['card_items'])
 keyword = self.data['keyword']
 if isinstance(u"", str):
     keyword.encode('ascii','ignore')

 language = self.context.Language()
 return self.context.portal_catalog(sort_on='modified', Language=language, sort_order='ascending', Subject=keyword)[:card_items]

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
