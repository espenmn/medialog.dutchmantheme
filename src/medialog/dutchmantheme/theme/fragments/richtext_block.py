def get_text(self):
    text = self.data['rich_text']
    return text

def background_image(self):
    if self.data['background_image']:
        bi = self.data['background_image']
        items = self.context.portal_catalog(UID=bi)
        return items[0].getURL()
    return ''

def get_url(self):
    if self.data['url']:
        url = self.data['url']
        if url.startswith('${portal_url}'):
            spl_url =  (url.split('/'))[1:]
            url = '/'.join(spl_url)
            context_state = self.context.restrictedTraverse(
                '@@plone_context_state'
            )
            url = '/'.join([
                context_state.canonical_object_url(), url
            ])
        return url
    return ''

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
