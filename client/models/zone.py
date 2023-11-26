from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Zone")


@_attrs_define
class Zone:
    """
    Attributes:
        temperature (float):
        snr (float):
        serial (str):
        rssi (float):
        reboot_count (float):
        last_response_date (str):
        last_request_date (str):
        last_active_date (str):
        firmware_version (str):
        current (float):
        configured_length (float):
        bridge_serial (str):
        active (bool):
    """

    temperature: float
    snr: float
    serial: str
    rssi: float
    reboot_count: float
    last_response_date: str
    last_request_date: str
    last_active_date: str
    firmware_version: str
    current: float
    configured_length: float
    bridge_serial: str
    active: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        temperature = self.temperature
        snr = self.snr
        serial = self.serial
        rssi = self.rssi
        reboot_count = self.reboot_count
        last_response_date = self.last_response_date
        last_request_date = self.last_request_date
        last_active_date = self.last_active_date
        firmware_version = self.firmware_version
        current = self.current
        configured_length = self.configured_length
        bridge_serial = self.bridge_serial
        active = self.active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "temperature": temperature,
                "snr": snr,
                "serial": serial,
                "rssi": rssi,
                "rebootCount": reboot_count,
                "lastResponseDate": last_response_date,
                "lastRequestDate": last_request_date,
                "lastActiveDate": last_active_date,
                "firmwareVersion": firmware_version,
                "current": current,
                "configuredLength": configured_length,
                "bridgeSerial": bridge_serial,
                "active": active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        temperature = d.pop("temperature")

        snr = d.pop("snr")

        serial = d.pop("serial")

        rssi = d.pop("rssi")

        reboot_count = d.pop("rebootCount")

        last_response_date = d.pop("lastResponseDate")

        last_request_date = d.pop("lastRequestDate")

        last_active_date = d.pop("lastActiveDate")

        firmware_version = d.pop("firmwareVersion")

        current = d.pop("current")

        configured_length = d.pop("configuredLength")

        bridge_serial = d.pop("bridgeSerial")

        active = d.pop("active")

        zone = cls(
            temperature=temperature,
            snr=snr,
            serial=serial,
            rssi=rssi,
            reboot_count=reboot_count,
            last_response_date=last_response_date,
            last_request_date=last_request_date,
            last_active_date=last_active_date,
            firmware_version=firmware_version,
            current=current,
            configured_length=configured_length,
            bridge_serial=bridge_serial,
            active=active,
        )

        zone.additional_properties = d
        return zone

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
