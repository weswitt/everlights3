from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.zone import Zone


T = TypeVar("T", bound="Status")


@_attrs_define
class Status:
    """
    Attributes:
        zones (List['Zone']):
        time_offset (float):
        server_reachable (bool):
        serial (str):
        reboot_count (float):
        radio_firmware_version (str):
        last_checkin_date (str):
        last_active_date (str):
        hardware_version (str):
        firmware_version (str):
        ssid (Union[Unset, str]):
        local_ip (Union[Unset, str]):
    """

    zones: List["Zone"]
    time_offset: float
    server_reachable: bool
    serial: str
    reboot_count: float
    radio_firmware_version: str
    last_checkin_date: str
    last_active_date: str
    hardware_version: str
    firmware_version: str
    ssid: Union[Unset, str] = UNSET
    local_ip: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        zones = []
        for zones_item_data in self.zones:
            zones_item = zones_item_data.to_dict()

            zones.append(zones_item)

        time_offset = self.time_offset
        server_reachable = self.server_reachable
        serial = self.serial
        reboot_count = self.reboot_count
        radio_firmware_version = self.radio_firmware_version
        last_checkin_date = self.last_checkin_date
        last_active_date = self.last_active_date
        hardware_version = self.hardware_version
        firmware_version = self.firmware_version
        ssid = self.ssid
        local_ip = self.local_ip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "zones": zones,
                "timeOffset": time_offset,
                "serverReachable": server_reachable,
                "serial": serial,
                "rebootCount": reboot_count,
                "radioFirmwareVersion": radio_firmware_version,
                "lastCheckinDate": last_checkin_date,
                "lastActiveDate": last_active_date,
                "hardwareVersion": hardware_version,
                "firmwareVersion": firmware_version,
            }
        )
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if local_ip is not UNSET:
            field_dict["localIP"] = local_ip

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.zone import Zone

        d = src_dict.copy()
        zones = []
        _zones = d.pop("zones")
        for zones_item_data in _zones:
            zones_item = Zone.from_dict(zones_item_data)

            zones.append(zones_item)

        time_offset = d.pop("timeOffset")

        server_reachable = d.pop("serverReachable")

        serial = d.pop("serial")

        reboot_count = d.pop("rebootCount")

        radio_firmware_version = d.pop("radioFirmwareVersion")

        last_checkin_date = d.pop("lastCheckinDate")

        last_active_date = d.pop("lastActiveDate")

        hardware_version = d.pop("hardwareVersion")

        firmware_version = d.pop("firmwareVersion")

        ssid = d.pop("ssid", UNSET)

        local_ip = d.pop("localIP", UNSET)

        status = cls(
            zones=zones,
            time_offset=time_offset,
            server_reachable=server_reachable,
            serial=serial,
            reboot_count=reboot_count,
            radio_firmware_version=radio_firmware_version,
            last_checkin_date=last_checkin_date,
            last_active_date=last_active_date,
            hardware_version=hardware_version,
            firmware_version=firmware_version,
            ssid=ssid,
            local_ip=local_ip,
        )

        status.additional_properties = d
        return status

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
