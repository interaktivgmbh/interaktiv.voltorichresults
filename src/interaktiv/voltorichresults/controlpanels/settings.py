from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from interaktiv.voltorichresults import _
from interaktiv.voltorichresults.interfaces import IInteraktivVoltoRichResultsLayer
from interaktiv.voltorichresults.registry.richresults import IRichResultsRegistry
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.restapi.controlpanels import RegistryConfigletPanel
from plone.z3cform import layout
from zope.component import adapter
from zope.interface import Interface


class VoltoRichResultsSettingsForm(RegistryEditForm):
    schema = IRichResultsRegistry
    label = _('trans_richresults_settings')
    description = _('trans_richresults_settings_description')


VoltoRichResultsSettingsView = layout.wrap_form(VoltoRichResultsSettingsForm, ControlPanelFormWrapper)


@adapter(Interface, IInteraktivVoltoRichResultsLayer)
class VoltoRichResultsControlpanel(RegistryConfigletPanel):
    schema = IRichResultsRegistry
    schema_prefix = None
    configlet_id = "voltorichresults_settings"  # needs to be equal to action_id in controlpanel.xml configlet
    configlet_category_id = "Products"
