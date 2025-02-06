def titlestructure(self):
    data = self.data
    header =  data['header']
    title = data['titletext']
    return "<%s>%s</%s>""" % (header, title, header)

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
