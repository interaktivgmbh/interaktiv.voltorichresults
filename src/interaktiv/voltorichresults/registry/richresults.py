from interaktiv.voltorichresults import _
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.schema.jsonfield import JSONField
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider


@provider(IFormFieldProvider)
class IRichResultsRegistry(model.Schema):
    richresults_config = JSONField(
        title=_('trans_richresults_config'),
        description=_('trans_richresults_config_description'),
        required=False
    )
