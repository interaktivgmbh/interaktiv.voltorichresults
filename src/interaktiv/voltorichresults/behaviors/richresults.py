import json

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
class IRichResults(model.Schema):
    model.fieldset(
        'richresults',
        label=_(_('trans_richresults_fieldset')),
        fields=[
            'richresults',
        ]
    )

    richresults = JSONField(
        title=_('trans_richresults'),
        description=_('trans_richresults_description'),
        schema=json.dumps({
            "$schema": "http://json-schema.org/draft-06/schema#",
            "type": "array",
            "items": {
                "$ref": "#/definitions/RichResult"
            },
            "definitions": {
                "RichResult": {
                    "type": "object",
                    "additionalProperties": True,
                    "properties": {
                        "@context": {
                            "type": "string"
                        },
                        "@type": {
                            "type": "string"
                        }
                    },
                    "required": ["@context", "@type"]
                }
            }
        }),
        required=False
    )

    directives.read_permission(richresults='interaktiv.voltorichresults.manage')
    directives.write_permission(richresults='interaktiv.voltorichresults.manage')


@implementer(IRichResults)
@adapter(IDexterityContent)
class RichResults(object):

    def __init__(self, context):
        self.context = context
