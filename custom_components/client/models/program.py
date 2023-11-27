from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.zone_effect import ZoneEffect


T = TypeVar("T", bound="Program")


@_attrs_define
class Program:
    """
    Attributes:
        pattern (List[str]):
        effects (List['ZoneEffect']):
    """

    pattern: List[str]
    effects: List["ZoneEffect"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pattern = self.pattern

        effects = []
        for effects_item_data in self.effects:
            effects_item = effects_item_data.to_dict()

            effects.append(effects_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pattern": pattern,
                "effects": effects,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.zone_effect import ZoneEffect

        d = src_dict.copy()
        pattern = cast(List[str], d.pop("pattern"))

        effects = []
        _effects = d.pop("effects")
        for effects_item_data in _effects:
            effects_item = ZoneEffect.from_dict(effects_item_data)

            effects.append(effects_item)

        program = cls(
            pattern=pattern,
            effects=effects,
        )

        program.additional_properties = d
        return program

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
