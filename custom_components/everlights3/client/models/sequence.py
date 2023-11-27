from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.zone_effect import ZoneEffect


T = TypeVar("T", bound="Sequence")


@_attrs_define
class Sequence:
    """
    Attributes:
        pattern (List[str]):
        last_changed (str):
        id (str):
        groups (List[str]):
        effects (List['ZoneEffect']):
        alias (str):
        group (Union[Unset, str]):
        account_id (Union[Unset, str]):
    """

    pattern: List[str]
    last_changed: str
    id: str
    groups: List[str]
    effects: List["ZoneEffect"]
    alias: str
    group: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pattern = self.pattern

        last_changed = self.last_changed
        id = self.id
        groups = self.groups

        effects = []
        for effects_item_data in self.effects:
            effects_item = effects_item_data.to_dict()

            effects.append(effects_item)

        alias = self.alias
        group = self.group
        account_id = self.account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pattern": pattern,
                "lastChanged": last_changed,
                "id": id,
                "groups": groups,
                "effects": effects,
                "alias": alias,
            }
        )
        if group is not UNSET:
            field_dict["group"] = group
        if account_id is not UNSET:
            field_dict["accountId"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.zone_effect import ZoneEffect

        d = src_dict.copy()
        pattern = cast(List[str], d.pop("pattern"))

        last_changed = d.pop("lastChanged")

        id = d.pop("id")

        groups = cast(List[str], d.pop("groups"))

        effects = []
        _effects = d.pop("effects")
        for effects_item_data in _effects:
            effects_item = ZoneEffect.from_dict(effects_item_data)

            effects.append(effects_item)

        alias = d.pop("alias")

        group = d.pop("group", UNSET)

        account_id = d.pop("accountId", UNSET)

        sequence = cls(
            pattern=pattern,
            last_changed=last_changed,
            id=id,
            groups=groups,
            effects=effects,
            alias=alias,
            group=group,
            account_id=account_id,
        )

        sequence.additional_properties = d
        return sequence

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
