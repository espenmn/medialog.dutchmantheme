def get_items(self):
    data = self.data
    limit = data['limit']
    subjects = data['subjects']
    language = self.context.Language()
    sorton = 'modified'
    if 'sort_on' in data.keys():
        sorton = data['sort_on']

    if subjects:
            return self.context.portal_catalog(portal_type='News Item', Language=language, Subject=subjects, sort_on=sorton, sort_order='descending')[:limit]

    return self.context.portal_catalog(portal_type='News Item', Language=language, sort_on=sorton, sort_order='descending')[:limit]


def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
