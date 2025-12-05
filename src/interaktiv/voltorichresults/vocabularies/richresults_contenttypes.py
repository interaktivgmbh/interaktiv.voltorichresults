import plone.api as api
from zope.i18n import translate
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


@provider(IVocabularyFactory)
def RichResultsContentTypesFactory(context):
    richresults_behavior = 'interaktiv.voltorichresults.richresults'
    types_tool = api.portal.get_tool('portal_types')
    richresults_ftis = [
        types_tool[fti_id] for fti_id in types_tool
        if richresults_behavior in getattr(types_tool[fti_id], 'behaviors', tuple())]

    terms = [
        # Value, Token, Title
        SimpleVocabulary.createTerm(
            fti.id,
            fti.id,
            context.translate(fti.Title(), domain='plone')
        ) for fti in richresults_ftis
    ]

    return SimpleVocabulary(terms)
