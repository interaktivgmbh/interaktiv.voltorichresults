from typing import TypedDict

import plone.api as api
from interaktiv.voltorichresults.registry.richresults import IRichResultsRegistry
from plone.restapi.services import Service


class TRichResultsConfigData(TypedDict):
    selectable_types: dict[str, list[str]]


class RichResultsConfigGet(Service):

    def reply(self) -> TRichResultsConfigData:
        response = self._get_richresults_config()
        return response

    def _get_richresults_config(self) -> TRichResultsConfigData:
        data = api.portal.get_registry_record(
            name='richresults_config',
            interface=IRichResultsRegistry
        )
        if not data:
            return {"selectable_types": {}}

        return data
