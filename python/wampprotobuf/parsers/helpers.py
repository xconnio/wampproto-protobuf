from typing import Any

import cbor2


def to_cbor_payload(args: list[Any], kwargs: dict[str, Any]) -> bytes:
    payload = [args, kwargs]
    return cbor2.dumps(payload)


def from_cbor_payload(data: bytes) -> (list[Any], dict[str, Any]):
    payload = cbor2.loads(data)
    return payload[0], payload[1]
