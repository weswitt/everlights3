from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.event_occurrences import EventOccurrences
    from ..models.event_sequence import EventSequence


T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """
    Attributes:
        zone_serials (List[str]):
        sequences (List['EventSequence']):
        occurrences (List['EventOccurrences']):
        last_changed (str):
        id (str):
        group (str):
        flags (List[str]):
        alias (str):
        account_id (str):
    """

    zone_serials: List[str]
    sequences: List["EventSequence"]
    occurrences: List["EventOccurrences"]
    last_changed: str
    id: str
    group: str
    flags: List[str]
    alias: str
    account_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        zone_serials = self.zone_serials

        sequences = []
        for sequences_item_data in self.sequences:
            sequences_item = sequences_item_data.to_dict()

            sequences.append(sequences_item)

        occurrences = []
        for occurrences_item_data in self.occurrences:
            occurrences_item = occurrences_item_data.to_dict()

            occurrences.append(occurrences_item)

        last_changed = self.last_changed
        id = self.id
        group = self.group
        flags = self.flags

        alias = self.alias
        account_id = self.account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "zoneSerials": zone_serials,
                "sequences": sequences,
                "occurrences": occurrences,
                "lastChanged": last_changed,
                "id": id,
                "group": group,
                "flags": flags,
                "alias": alias,
                "accountId": account_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event_occurrences import EventOccurrences
        from ..models.event_sequence import EventSequence

        d = src_dict.copy()
        zone_serials = cast(List[str], d.pop("zoneSerials"))

        sequences = []
        _sequences = d.pop("sequences")
        for sequences_item_data in _sequences:
            sequences_item = EventSequence.from_dict(sequences_item_data)

            sequences.append(sequences_item)

        occurrences = []
        _occurrences = d.pop("occurrences")
        for occurrences_item_data in _occurrences:
            occurrences_item = EventOccurrences.from_dict(occurrences_item_data)

            occurrences.append(occurrences_item)

        last_changed = d.pop("lastChanged")

        id = d.pop("id")

        group = d.pop("group")

        flags = cast(List[str], d.pop("flags"))

        alias = d.pop("alias")

        account_id = d.pop("accountId")

        event = cls(
            zone_serials=zone_serials,
            sequences=sequences,
            occurrences=occurrences,
            last_changed=last_changed,
            id=id,
            group=group,
            flags=flags,
            alias=alias,
            account_id=account_id,
        )

        event.additional_properties = d
        return event

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
