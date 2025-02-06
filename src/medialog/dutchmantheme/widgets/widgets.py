import zope.component
import zope.interface
import zope.schema.interfaces

from z3c.form import interfaces
from z3c.form import widget
from z3c.form.browser import text
from Products.CMFPlone.utils import get_portal

from plone import api

class IPickerWidget(interfaces.IWidget):
    """Picker widget."""


@zope.interface.implementer_only(IPickerWidget)
class PickerWidget(text.TextWidget):
    """Picker Widget"""

    def items(self):
        return api.content.find(portal_type='Image')

@zope.interface.implementer(interfaces.IFieldWidget)
def PickerFieldWidget(field, request):
    """IFieldWidget factory for PickerWidget."""
    return widget.FieldWidget(field, PickerWidget(request))




class IFolderPickerWidget(interfaces.IWidget):
    """Folder Picker widget."""


@zope.interface.implementer_only(IFolderPickerWidget)
class FolderPickerWidget(text.TextWidget):
    """Folder Picker Widget"""

    def items(self):
        return api.content.find(portal_type=['Folder', 'Collection'])

@zope.interface.implementer(interfaces.IFieldWidget)
def FolderPickerFieldWidget(field, request):
    """IFieldWidget factory for FolderPickerWidget."""
    return widget.FieldWidget(field, FolderPickerWidget(request))
