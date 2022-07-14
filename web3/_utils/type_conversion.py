from typing import (
    Any,
    Union,
)

from eth_typing import (
    HexStr,
)
from eth_utils import (
    to_bytes,
    to_hex,
)


def to_hex_if_bytes(val: Union[HexStr, str, bytes, bytearray]) -> HexStr:
    """
    Note: This method does not validate against all cases and is only
    meant to work with bytes and hex strings.
    """
    return to_hex(val) if isinstance(val, (bytes, bytearray)) else to_hex(hexstr=val)


def to_bytes_if_hex(val: Union[HexStr, str, bytes, bytearray]) -> bytes:
    """
    Note: This method does not validate against all cases and is only
    meant to work with bytes and hex strings.
    """
    return to_bytes(hexstr=val) if isinstance(val, str) else val


def recursive_to_tuple_if_list(val: Any) -> Any:
    """
    Recursively replace lists with tuples.
    """
    if isinstance(val, (list, tuple)):
        return tuple(recursive_to_tuple_if_list(x) for x in val)
    elif isinstance(val, dict):
        return dict((k, recursive_to_tuple_if_list(v)) for k, v in val.items())
    else:
        return val
