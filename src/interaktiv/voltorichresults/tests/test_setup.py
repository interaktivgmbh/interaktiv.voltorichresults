import unittest
from interaktiv.voltorichresults.behaviors.richresults import IRichResults
from interaktiv.voltorichresults.interfaces import IInteraktivVoltoRichResultsLayer
from interaktiv.voltorichresults.testing import INTERAKTIV_VOLTO_RICHRESULTS_INTEGRATION_TESTING

from plone.app.testing import TEST_USER_ID, setRoles
from plone.base.utils import get_installer
from plone.browserlayer import utils


class TestSetup(unittest.TestCase):
    layer = INTERAKTIV_VOLTO_RICHRESULTS_INTEGRATION_TESTING
    product_name = 'interaktiv.voltorichresults'

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager', 'Site Administrator'])

    def is_product_installed(self, product_name):
        installer = get_installer(self.portal, self.request)
        return installer.is_product_installed(product_name)

    def test_product_installed(self):
        # post condition
        self.assertTrue(self.is_product_installed(self.product_name))

    def test_browserlayer(self):
        # post condition
        self.assertIn(
            IInteraktivVoltoRichResultsLayer,
            utils.registered_layers()
        )

    def test_richresults_behavior_added(self):
        # setup
        behavior = 'interaktiv.voltorichresults.richresults'
        fti = self.portal.portal_types['Document']

        # postcondition
        self.assertIn(behavior, fti.behaviors)

    def test_controlpanel_registered(self):
        # setup
        controlpanel = self.portal.portal_controlpanel

        # postcondition
        action_ids = [a.getAction(self.portal)['id'] for a in controlpanel.listActions()]
        self.assertIn('voltorichresults_settings', action_ids)

    def test_controlpanel_in_products_category(self):
        # setup
        controlpanel = self.portal.portal_controlpanel

        # postcondition
        actions = [a for a in controlpanel.listActions() if a.getAction(self.portal)['id'] == 'voltorichresults_settings']
        self.assertEqual(len(actions), 1)
        self.assertEqual(actions[0].category, 'Products')


class TestUninstall(unittest.TestCase):
    layer = INTERAKTIV_VOLTO_RICHRESULTS_INTEGRATION_TESTING
    product_name = 'interaktiv.voltorichresults'

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager', 'Site Administrator'])

        installer = get_installer(self.portal, self.request)
        installer.uninstall_product(self.product_name)

    def test_product_uninstalled(self):
        installer = get_installer(self.portal, self.request)
        self.assertFalse(installer.is_product_installed(self.product_name))

    def test_browserlayer_removed(self):
        self.assertNotIn(IInteraktivVoltoRichResultsLayer, utils.registered_layers())

    def test_richresults_behavior_removed(self):
        # setup
        behavior = 'interaktiv.voltorichresults.richresults'
        fti = self.portal.portal_types['Document']

        # postcondition
        self.assertNotIn(behavior, fti.behaviors)

    def test_controlpanel_removed(self):
        # setup
        controlpanel = self.portal.portal_controlpanel

        # postcondition
        action_ids = [a.getAction(self.portal)['id'] for a in controlpanel.listActions()]
        self.assertNotIn('voltorichresults_settings', action_ids)
