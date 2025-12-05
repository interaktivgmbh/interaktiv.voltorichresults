import unittest

from interaktiv.voltorichresults.behaviors.richresults import IRichResults
from interaktiv.voltorichresults.testing import INTERAKTIV_VOLTO_RICHRESULTS_FUNCTIONAL_TESTING
from interaktiv.voltorichresults.vocabularies.richresults_contenttypes import RichResultsContentTypesFactory
from plone.app.testing import TEST_USER_ID, setRoles


class TestRichResultsContenttypesVocabulary(unittest.TestCase):
    layer = INTERAKTIV_VOLTO_RICHRESULTS_FUNCTIONAL_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager', 'Site Administrator'])

    def test_richresults_contenttypes(self):
        # do it
        result = RichResultsContentTypesFactory(context=self.portal)

        # postcondition
        term_values = [term.value for term in result._terms]
        self.assertIn('Document', term_values)

        document_term = result.getTerm('Document')
        self.assertEqual(document_term.value, 'Document')
        self.assertEqual(document_term.token, 'Document')
        self.assertEqual(document_term.title, 'Page')
