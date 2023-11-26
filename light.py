from __future__ import annotations
from homeassistant.core import HomeAssistant
import logging
from homeassistant.components.light import (ATTR_EFFECT, PLATFORM_SCHEMA, LightEntity, LightEntityFeature, LightEntityDescription)

from .client import Client
from .client.models.status import Status
from .client.models.sequence import Sequence
from .client.models.program import Program
from .client.types import Response
from .client.api.default import get_v1
from .client.api.default import get_v1_sequences
from .client.api.default import post_v_1_zones_zone_id_sequence
from .client.api.default import delete_v_1_zones_zone_id_sequence

_LOGGER = logging.getLogger(__name__)

from .const import DOMAIN
from .const import HUBIP

async def async_setup_entry(
    hass: core.HomeAssistant,
    config_entry: config_entries.ConfigEntry,
    async_add_entities,
):
    config = hass.data[DOMAIN][config_entry.entry_id]
    sdata = None
    client = None
    try:
        everlights_url = "http://" + config[HUBIP]
        client = Client(base_url=everlights_url)
        sdata = get_v1.sync(client=client)
    except Exception:
        _LOGGER.exception("invalid everlights hub ip address or hub is unavailable")
    if sdata == None:
        return
    lights: list[EverlightsLight] = []
    for zone in sdata.zones:
        lights.append(EverlightsLight(client, zone.serial))
    async_add_entities(lights, update_before_add=False)

class EverlightsLight(LightEntity):
    _attr_supported_features = LightEntityFeature.EFFECT

    def __init__(self, client, serial) -> None:
        self._serial = serial
        self._client = client
        self._name = "everlights" + self._serial
        self._avail = True
        self._onoff = False
        self._attr_supported_features |= LightEntityFeature.EFFECT
        self._sequences = get_v1_sequences.sync(client=self._client)
        self._effects: list[str] = []
        for seq in self._sequences:
            self._effects.append(seq.alias)
        self._effects.sort()
        self._effect = self._effects[0]

    @property
    def unique_id(self) -> str:
        return self._serial

    @property
    def name(self) -> str:
        return self._name

    @property
    def icon(self) -> str:
        return "mdi:string-lights"

    @property
    def effect(self) -> str | None:
        return self._effect

    @property
    def effect_list(self) -> list[str] | None:
        return self._effects

    @property
    def available(self) -> bool:
        return self._avail

    @property
    def is_on(self) -> bool:
        return self._onoff

    def update(self) -> None:
        self._sequences = get_v1_sequences.sync(client=self._client)
        self._effects: list[str] = []
        for seq in self._sequences:
            self._effects.append(seq.alias)
        self._effects.sort()
        self._effect = self._effects[0]

    def turn_on(self, **kwargs: Any) -> None:
        if ATTR_EFFECT not in kwargs:
            self._effect = self._sequences[0].alias
        else:
            self._effect = kwargs.get(ATTR_EFFECT, self._sequences[0].alias)
        onseq = None
        for seq in self._sequences:
            if seq.alias == self._effect:
                onseq = seq
                break
        if onseq != None:
            pgm = Program(onseq.pattern, onseq.effects)
            post_v_1_zones_zone_id_sequence.sync(zone_id=self._serial, client=self._client, json_body=pgm)
            self._onoff = True

    def turn_off(self, **kwargs: Any) -> None:
        delete_v_1_zones_zone_id_sequence.sync(zone_id=self._serial, client=self._client)
        self._onoff = False

