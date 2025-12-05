import json
import unittest

import plone.api as api
from interaktiv.voltorichresults.controlpanels.settings import VoltoRichResultsControlpanel
from interaktiv.voltorichresults.controlpanels.settings import VoltoRichResultsSettingsView
from interaktiv.voltorichresults.registry.richresults import IRichResultsRegistry
from interaktiv.voltorichresults.testing import INTERAKTIV_VOLTO_RICHRESULTS_FUNCTIONAL_TESTING
from plone.app.testing import TEST_USER_ID, setRoles
from plone.restapi.controlpanels import IControlpanel
from zope.component import getMultiAdapter


class TestRichResultsSettingsControlpanel(unittest.TestCase):
    layer = INTERAKTIV_VOLTO_RICHRESULTS_FUNCTIONAL_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Member'])

        self.view: VoltoRichResultsSettingsView = api.content.get_view(
            name='voltorichresults_settings',
            context=self.portal,
            request=self.request
        )

    def test___call____no_params(self):
        # do it
        result = self.view()

        # postcondition
        self.assertIsInstance(result, str)

    def test___call____updates_registry(self):
        # setup
        self.request.form['form.buttons.save'] = 'true'
        richresults_config_data = {
            "selectable_types": {
                'Document': [
                    'MyRichResultType'
                ]
            }
        }
        self.request.form['form.widgets.richresults_config'] = json.dumps(richresults_config_data)

        # do it
        self.view()

        # postcondition
        saved_config_data = api.portal.get_registry_record(
            name='richresults_config',
            interface=IRichResultsRegistry
        )
        self.assertDictEqual(saved_config_data, richresults_config_data)

    def _get_restapi_controlpanel(self, control_panel_name):
        return getMultiAdapter(
            (self.portal, self.request),
            IControlpanel,
            name=control_panel_name
        )

    def test_controlpanel_restapi__get(self):
        # do it
        result = self._get_restapi_controlpanel('voltorichresults_settings')

        # postcondition
        self.assertTrue(isinstance(result, VoltoRichResultsControlpanel))
