from plone.app.testing import (
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE,
    PloneSandboxLayer,
)
from plone.testing import Layer
from plone.testing.zope import WSGI_SERVER_FIXTURE


class InteraktivVoltoRichResultsLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import interaktiv.voltorichresults
        self.loadZCML(package=interaktiv.voltorichresults)

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'interaktiv.voltorichresults:default')


INTERAKTIV_VOLTO_RICHRESULTS_FIXTURE: Layer = InteraktivVoltoRichResultsLayer()
INTERAKTIV_VOLTO_RICHRESULTS_INTEGRATION_TESTING: Layer = IntegrationTesting(
    bases=(INTERAKTIV_VOLTO_RICHRESULTS_FIXTURE,),
    name='InteraktivVoltoRichResultsLayer:Integration'
)
INTERAKTIV_VOLTO_RICHRESULTS_FUNCTIONAL_TESTING: Layer = FunctionalTesting(
    bases=(INTERAKTIV_VOLTO_RICHRESULTS_FIXTURE, WSGI_SERVER_FIXTURE),
    name='InteraktivVoltoRichResultsLayer:Functional'
)
