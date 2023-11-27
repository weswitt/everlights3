from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EventSequence")


@_attrs_define
class EventSequence:
    """
    Attributes:
        sequence_id (str):
        duration (float):
    """

    sequence_id: str
    duration: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sequence_id = self.sequence_id
        duration = self.duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sequenceId": sequence_id,
                "duration": duration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sequence_id = d.pop("sequenceId")

        duration = d.pop("duration")

        event_sequence = cls(
            sequence_id=sequence_id,
            duration=duration,
        )

        event_sequence.additional_properties = d
        return event_sequence

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
