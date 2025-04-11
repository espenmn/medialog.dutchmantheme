
# -*- coding: utf-8 -*-
from medialog.iconpicker.widgets.widget import ColorPickerFieldWidget
from medialog.controlpanel.interfaces import \
    IMedialogControlpanelSettingsProvider
from plone.supermodel import model
from plone.autoform.directives import widget
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope.interface import alsoProvides
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.app.portlets.interfaces import IColumn
from plone.namedfile.field import NamedBlobImage
from zope import interface

_ = MessageFactory('medialog.dutchmantheme')


class IMailColumns(Interface):
    """ Datagrid for contact_info mail
    """

    label = schema.TextLine(
        title=_(u'Navn'),
        required=False,
    )

    email = schema.TextLine(
        title=_(u'E-mail'),
        required=False,
    )


class IMedialogDutchmanthemeLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IBelow(IColumn):
    """here we put the below content portlets
    """

class IAbove(IColumn):
    """here we put the above content portlets
    """

class IRichtextPair(interface.Interface):
    """To be used with the fragments"""
    legend = schema.TextLine(
            title=_('legend', default=u'Tab title'),
    )
    tabtext = schema.TextLine(
            title=_('Text', default=u'Tab text'),
    )

class IMedialogDutchmanThemeSettings(model.Schema):
    """Adds settings to medialog.controlpanel"""

    model.fieldset(
        'Dutchmantheme',
        label=_(u'Dutchmantheme'),
        fields=[
            'style',
            'external_style',
            'rules',
            'load_css',
            'color1',
            'color2',
            'color3',
            'extra_css',
            'jsheading',
            'jsfooter']
    )

    model.fieldset(
        'Theme overrides',
        label=_(u'Theme overrides'),
        fields=[
            'enable_overrides',
            'heading_font',
            'body_font',
            'font_load_url',
            'nav_background',
            'navlink_color',
            'navlink_hover',
            'navlink_visited',
            'footer_background',
            'footer_color',
            'footerlink_color',
            'footerlink_hover',
            'footerlink_visited']
    )

    style = schema.Choice(
        title=_(u'Style'),
        values=['dutchmanblue', 'dutchblue', 'xstyles', 'xxstyles','styles', 'blue'],
        default='dutchmanblue',
        required=False,
    )
    
    jsheading = schema.Text(
        title=_('jsfooter', default=u'Javascript in Head'),
        required=False,
    )
    jsfooter = schema.Text(
        title=_('jsfooter', default=u'Javascript in Footer'),
        required=False,
    )

    external_style = schema.URI(
        title=_(u'External stylesheet'),
        description=_(u'Remember to enable external files  in theming setup'),
        required=False,
    )

    rules = schema.Choice(
        title=_(u'Layout Rules'),
        values=['default', 'default_old', 'spot', 'spot_2', 'head', 'fullmenu_l', 'disabled'],
        required=True,
    )

    load_css = schema.Bool(
        title=_(u'Load CSS? Put it in your theme and disable it here'),
        required=False,
        default=True,
    )

    color1 = schema.TextLine(
        title=_('color1', default=u'Custom Color 1'),
        required=True,
        description=_('help_color',
                      default='Choose Color'),
    )

    color2 = schema.TextLine(
        title=_('color2', default=u'Custom Color 2'),
        required=True,
        description=_('help_color',
                      default='Choose Color'),
    )

    color3 = schema.TextLine(
        title=_('color3', default=u'Custom Color 3'),
        required=True,
        description=_('help_color',
                      default='Choose Color'),
    )

    extra_css = schema.Text(
        title=_('extra_css', default=u'Extra CSS'),
        required=False,
        description=_('help_extra_css'),
    )

    enable_overrides = schema.Bool(
        title=_(u'Enable overrides'),
        required=False,
        default=False,
    )

    heading_font = schema.TextLine(
        title=_(u'Heading font'),
        required=False,
    )

    body_font = schema.TextLine(
        title=_(u'Body font'),
        required=False,
    )

    font_load_url=schema.TextLine(
        title=_(u"Font URL"),
        description=u"For example: https://fonts.googleapis.com/css?family=Montserrat:300,400,600,700&display=swap",
        required=False,
    )

    nav_background = schema.Text(
        title=_('nav_background_color', default=u'Nav background color'),
        description=u"Also affects the seach field",
        required=False,
    )

    navlink_color = schema.Text(
        title=_('navlink_color', default=u'Navlink color'),
        description=u"Also affects the seach field",
        required=False,
    )
    
    navlink_hover = schema.Text(
        title=_('navlin_hover', default=u'Navlink hover'),
        description=u"Also affects the seach field",
        required=False,
    )
    
    navlink_visited = schema.Text(
        title=_('navlin_visited', default=u'Navlink visited text color'),
        required=False,
    )
    
    footer_background = schema.Text(
        title=_('footer_background', default=u'Footer backgroundcolor'),
        required=False,
    )

    footer_color = schema.Text(
        title=_('footer_color', default=u'Footer text color'),
        required=False,
    )

    footerlink_color = schema.Text(
        title=_('footerlink_color', default=u'Footerlink color'),
        required=False,
    )
    footerlink_hover = schema.Text(
        title=_('footerlink_hover', default=u'Footerlink hover'),
        required=False,
    )
    footerlink_visited = schema.Text(
        title=_('footerlink-visited', default=u'Footerlink visited'),
        required=False,
    )

    widget(
        color1=ColorPickerFieldWidget,
        color2=ColorPickerFieldWidget,
        color3=ColorPickerFieldWidget,
        navlink_color=ColorPickerFieldWidget,
        navlink_hover=ColorPickerFieldWidget,
        nav_background=ColorPickerFieldWidget,
        navlink_visited=ColorPickerFieldWidget,
        footer_background=ColorPickerFieldWidget,
        footer_color=ColorPickerFieldWidget,
        footerlink_color=ColorPickerFieldWidget,
        footerlink_hover=ColorPickerFieldWidget,
        footerlink_visited=ColorPickerFieldWidget,
    )

alsoProvides(IMedialogDutchmanThemeSettings, IMedialogControlpanelSettingsProvider)
