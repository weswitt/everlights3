from __future__ import annotations

import logging
from typing import Any
import ipaddress

import voluptuous as vol
import homeassistant.helpers.config_validation as cv

from homeassistant import config_entries, exceptions
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .const import HUBIP

_LOGGER = logging.getLogger(__name__)

DATA_SCHEMA = vol.Schema(
    {
        vol.Required(HUBIP): cv.string
    }
)


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            try:
                ip_object = ipaddress.ip_address(user_input[HUBIP])
                return self.async_create_entry(title="everlights", data=user_input)
            except ValueError:
                errors["base"] = "cannot connect"
            except CannotConnect:
                errors["base"] = "cannot connect"
            except InvalidHost:
                errors["base"] = "invalid host"
            except Exception:
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA, errors=errors
        )

class CannotConnect(exceptions.HomeAssistantError):
    """Error to indicate we cannot connect."""

class InvalidHost(exceptions.HomeAssistantError):
    """Error to indicate there is an invalid hostname."""

