def get_items(self):
    language = self.context.Language()
    linked = self.data['linked_folder']
    folder_path = '/'.join(context.getPhysicalPath())
    content_type = self.data['content_type']
    sort_on = self.data['sort_on']
    sort_order = str(self.data['sort_order'])

    if linked:
        folder_path = self.get_path()

    return self.context.portal_catalog(portal_type=content_type, path={'query': folder_path,}, Language=language, sort_on=sort_on, sort_order=sort_order)

def get_path(self):
    linked = self.data['linked_folder']
    folder = self.context.portal_catalog(UID=linked)
    mappe =  folder[0].getObject()
    return  '/'.join(mappe.getPhysicalPath())

def get_effect(self):
    return self.data['effekt'][:2]

def width100(self):
    bredde = self.data['max_width'] + 100
    return bredde

def width50(self):
    bredde = self.data['max_width'] + 50
    return bredde

def ratio(self):
    bredde = int(self.data['imagewidth'])
    hoyde =  int(self.data['imageheight'])
    return hoyde*100/bredde

def get_css(self):
    return """

    section.hover02.hovercolumn figure img:hover {
    	width: calc(100% + 50px);
    }
    section.hover04.hovercolumn figure img {
    	width: calc(100% + 100px) !important;
      max-width: width: calc(100% + 100px) !important;
    }""" % {  "ratio": self.ratio() }


def get_script(self):
    if self.data['effekt'] == '02 Zoom In 2' or self.data['effekt'] == '04 Zoom Out 2':
        return """$(window).resize(function(){
            $('#fragment-%(s_id)s figure').height( ( $('#fragment-%(s_id)s figure').width()  ) * %(ratio)i / 100) ;
            }).resize();""" % {  "s_id": str(self.id),
                                 "ratio": self.ratio() or None }

    return ""

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True
