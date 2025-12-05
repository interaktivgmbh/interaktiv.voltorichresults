from typing import Optional

from Products.GenericSetup.tool import SetupTool
from plone import api
from plone.base.interfaces import INonInstallable
from plone.dexterity.fti import DexterityFTI
from plone.dexterity.interfaces import IDexterityFTI
from zope.interface import implementer


# noinspection PyUnusedLocal
def setup_after(context: Optional[SetupTool]) -> None:
    pass


# noinspection PyUnusedLocal
def uninstall_after(context: Optional[SetupTool]) -> None:
    portal_types = api.portal.get_tool('portal_types')
    behavior_name = 'interaktiv.voltorichresults.richresults'
    for portal_type in portal_types.keys():
        fti: DexterityFTI = portal_types.get(portal_type)
        if IDexterityFTI.providedBy(fti) and behavior_name in fti.behaviors:
            behaviors = tuple(behavior for behavior in fti.behaviors if behavior != behavior_name)
            # noinspection PyProtectedMember
            fti._updateProperty('behaviors', tuple(set(behaviors)))


@implementer(INonInstallable)
class HiddenProfiles(object):

    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'interaktiv.voltorichresults:uninstall',
        ]
