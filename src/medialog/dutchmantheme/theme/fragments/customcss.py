def glyphicon(self):
    return """
    <script type="text/javascript" src="++resource++medialog.iconpicker/bootstrap-iconpicker/js/iconset/iconset-glyphicon.min.js"></script>
    """


def medialogfont(self):
    return """
    <link rel="stylesheet" href="++resource++medialog.iconpicker/icon-fonts/medialogfont/css/medialogfont.css"/>
    <script type="text/javascript" src="++resource++medialog.iconpicker/bootstrap-iconpicker/js/iconset/iconset-medialogfont.js"></script>
    """

def iconpickerfont(self):
    return """
    <link rel="stylesheet" href="++resource++medialog.iconpicker/icon-fonts/iconpickerfont/style.css"/>
    <script type="text/javascript" src="++resource++medialog.iconpicker/bootstrap-iconpicker/js/iconset/iconset-iconpickerfont.js"></script>
    """

def fontawesome(self):
    return """
    <script type="text/javascript" src="++resource++medialog.iconpicker/bootstrap-iconpicker/js/iconset/iconset-fontawesome-4.2.0.js"></script>
    <link rel="stylesheet" href="++resource++medialog.iconpicker/icon-fonts/font-awesome-4.2.0/css/font-awesome.min.css"/>
    """

def mapicon(self):
    return """
    <link rel="stylesheet" href="++resource++medialog.iconpicker/icon-fonts/map-icons-2.1.0/css/map-icons.min.css"/>
    <script type="text/javascript" src="++resource++medialog.iconpicker/bootstrap-iconpicker/js/iconset/iconset-mapicon-2.1.0.min.js"></script>
    """

def typicon(self):
    return """
    <link rel="stylesheet" href="++resource++medialog.iconpicker/icon-fonts/typicons-2.0.6/css/typicons.min.css"/>
    <script type="text/javascript" src="++resource++medialog.iconpicker/bootstrap-iconpicker/js/iconset/iconset-typicon-2.0.6.min.js"></script>
    """

def ionicon(self):
   return """
    <link rel="stylesheet" href="++resource++medialog.iconpicker/icon-fonts/ionicons-1.5.2/css/ionicons.min.css"/>
    <script type="text/javascript" src="++resource++medialog.iconpicker/bootstrap-iconpicker/js/iconset/iconset-ionicon-1.5.2.min.js"></script>
   """

def weathericon(self):
    return """
    <link rel="stylesheet" href="++resource++medialog.iconpicker/icon-fonts/weather-icons-1.2.0/css/weather-icons.min.css"/>
    <script type="text/javascript" src="++resource++medialog.iconpicker/bootstrap-iconpicker/js/iconset/iconset-weathericon-1.2.0.min.js"></script>
    """

def octicon(self):
    return """
    <link rel="stylesheet" href="++resource++medialog.iconpicker/icon-fonts/octicons-2.1.2/css/octicons.min.css"/>
    <script type="text/javascript" src="++resource++medialog.iconpicker/bootstrap-iconpicker/js/iconset/iconset-octicon-2.1.2.min.js"></script>
    """

def elusiveicon(self):
    return """
    <link rel="stylesheet" href="++resource++medialog.iconpicker/icon-fonts/elusive-icons-2.0.0/css/elusive-icons.min.css"/>
    <script type="text/javascript" src="++resource++medialog.iconpicker/bootstrap-iconpicker/js/iconset/iconset-elusiveicon-2.0.0.min.js"></script>
    """

def lineawesome(self):
    return """
    <script type="text/javascript" src="++resource++medialog.iconpicker/bootstrap-iconpicker/js/iconset/iconset-lineawesome.js"></script>
    <link rel="stylesheet" href="++resource++medialog.iconpicker/icon-fonts/line-awesome/css/line-awesome.css"/>
    """

def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return True


def xtra_css(self):
    return self.context.portal_registry['medialog.dutchmantheme.interfaces.IMedialogDutchmanThemeSettings.extra_css']

def ext_css(self):
    return self.context.portal_registry['medialog.dutchmantheme.interfaces.IMedialogDutchmanThemeSettings.external_style']

def cssfile(self):
    return self.context.portal_registry['medialog.dutchmantheme.interfaces.IMedialogDutchmanThemeSettings.style']
    
def color1(self):              
    return str(self.context.portal_registry['medialog.dutchmantheme.interfaces.IMedialogDutchmanThemeSettings.color1'])
    
def color2(self): 
    return str(self.context.portal_registry['medialog.dutchmantheme.interfaces.IMedialogDutchmanThemeSettings.color2'])

def color3(self):
    return str(self.context.portal_registry['medialog.dutchmantheme.interfaces.IMedialogDutchmanThemeSettings.color3'])

def iconset(self):
    return str(self.context.portal_registry['medialog.iconpicker.interfaces.IIconPickerSettings.iconset'])

def font_load_url(self):          
    return str(self.context.portal_registry['medialog.dutchmantheme.interfaces.IMedialogDutchmanThemeSettings.font_load_url'])

def override(self):  
    return self.context.portal_registry['medialog.dutchmantheme.interfaces.IMedialogDutchmanThemeSettings.enable_overrides']

def navlink_color(self):      
    return  str(self.context.portal_registry['medialog.dutchmantheme.interfaces.IMedialogDutchmanThemeSettings.navlink_color'])
                   
def body_font(self):          
    return str(self.context.portal_registry['medialog.dutchmantheme.interfaces.IMedialogDutchmanThemeSettings.body_font'])
                    
def heading_font(self):       
    return str(self.context.portal_registry['medialog.dutchmantheme.interfaces.IMedialogDutchmanThemeSettings.heading_font'])
                    
def nav_background(self):     
    return str(self.context.portal_registry['medialog.dutchmantheme.interfaces.IMedialogDutchmanThemeSettings.nav_background'])
                    
def navlink_hover(self):      
    return str(self.context.portal_registry['medialog.dutchmantheme.interfaces.IMedialogDutchmanThemeSettings.navlink_hover'])
                    
def navlink_visited(self):    
    return str(self.context.portal_registry['medialog.dutchmantheme.interfaces.IMedialogDutchmanThemeSettings.navlink_visited'])
                    
def footer_background(self):  
    return str(self.context.portal_registry['medialog.dutchmantheme.interfaces.IMedialogDutchmanThemeSettings.footer_background'])
                    
def footerlink_color(self):   
    return str(self.context.portal_registry['medialog.dutchmantheme.interfaces.IMedialogDutchmanThemeSettings.footerlink_color'])
                    
def footer_color(self):   
    return str(self.context.portal_registry['medialog.dutchmantheme.interfaces.IMedialogDutchmanThemeSettings.footer_color'])
                    
def footerlink_hover(self):   
    return str(self.context.portal_registry['medialog.dutchmantheme.interfaces.IMedialogDutchmanThemeSettings.footerlink_hover'])
                    
def footerlink_visited(self):  
    return str(self.context.portal_registry['medialog.dutchmantheme.interfaces.IMedialogDutchmanThemeSettings.footerlink_visited'])
