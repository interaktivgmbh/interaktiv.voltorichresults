import unittest

import plone.api as api
from interaktiv.voltorichresults.registry.richresults import IRichResultsRegistry
from interaktiv.voltorichresults.services.richresults_config.get import RichResultsConfigGet
from interaktiv.voltorichresults.testing import INTERAKTIV_VOLTO_RICHRESULTS_FUNCTIONAL_TESTING
from plone.app.testing import TEST_USER_ID, setRoles


class TestRichResultsConfigGet(unittest.TestCase):
    layer = INTERAKTIV_VOLTO_RICHRESULTS_FUNCTIONAL_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager', 'Site Administrator'])

        self.service = RichResultsConfigGet()
        self.service.context = self.portal
        self.service.request = self.request

    def test_richresults_config__reply__no_config(self):
        # do it
        result = self.service.reply()

        # postcondition
        expecxted_result = {'selectable_types': {}}
        self.assertDictEqual(result, expecxted_result)

    def test_richresults_config__reply__with_config(self):
        # setup
        data = {
            'selectable_types': {
                'Document': [
                    'Organization'
                ]
            }
        }
        api.portal.set_registry_record(
            name='richresults_config',
            value=data,
            interface=IRichResultsRegistry
        )

        # do it
        result = self.service.reply()

        # postcondition
        self.assertDictEqual(result, data)
