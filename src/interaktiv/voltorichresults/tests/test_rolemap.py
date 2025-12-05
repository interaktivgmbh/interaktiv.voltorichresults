import unittest

import plone.api as api
from interaktiv.voltorichresults.testing import INTERAKTIV_VOLTO_RICHRESULTS_INTEGRATION_TESTING
from plone.app.testing import TEST_USER_ID, setRoles


class TestSetupRoleMap(unittest.TestCase):
    layer = INTERAKTIV_VOLTO_RICHRESULTS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Member'])

    def test_role_permissions__configure(self):
        with api.env.adopt_roles(roles=['Manager']):
            self.assertTrue(api.user.has_permission('InteraktivVoltoRichResults: Configure'))
        with api.env.adopt_roles(roles=['Site Administrator']):
            self.assertTrue(api.user.has_permission('InteraktivVoltoRichResults: Configure'))
        with api.env.adopt_roles(roles=['Editor']):
            self.assertFalse(api.user.has_permission('InteraktivVoltoRichResults: Configure'))
        with api.env.adopt_roles(roles=['Owner']):
            self.assertFalse(api.user.has_permission('InteraktivVoltoRichResults: Configure'))
        with api.env.adopt_roles(roles=['Member']):
            self.assertFalse(api.user.has_permission('InteraktivVoltoRichResults: Configure'))

    def test_role_permissions__manage(self):
        with api.env.adopt_roles(roles=['Manager']):
            self.assertTrue(api.user.has_permission('InteraktivVoltoRichResults: Manage'))
        with api.env.adopt_roles(roles=['Site Administrator']):
            self.assertTrue(api.user.has_permission('InteraktivVoltoRichResults: Manage'))
        with api.env.adopt_roles(roles=['Editor']):
            self.assertTrue(api.user.has_permission('InteraktivVoltoRichResults: Manage'))
        with api.env.adopt_roles(roles=['Owner']):
            self.assertTrue(api.user.has_permission('InteraktivVoltoRichResults: Manage'))
        with api.env.adopt_roles(roles=['Member']):
            self.assertFalse(api.user.has_permission('InteraktivVoltoRichResults: Manage'))
