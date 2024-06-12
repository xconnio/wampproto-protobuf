from typing import Any

from wampproto.messages import Message
from wampproto.messages.yield_ import IYieldFields, Yield

from wampprotobuf.gen import yield_pb2
from wampprotobuf.parsers import helpers


class YieldFields(IYieldFields):
    def __init__(self, msg: yield_pb2.Yield):
        super().__init__()
        self._msg = msg
        self._args = None
        self._kwargs = None
        self._unpacked = False

    @property
    def request_id(self) -> int:
        return self._msg.request_id

    def unpack(self):
        try:
            self._unpacked = True
            args, kwargs = helpers.from_cbor_payload(self._msg.payload)
            self._args = args
            self._kwargs = kwargs
        except Exception as e:
            print(f"error parsing CBOR payload: {e}")

    @property
    def args(self) -> list[Any] | None:
        if not self._unpacked:
            self.unpack()

        return self._args

    @property
    def kwargs(self) -> dict[str, Any] | None:
        if not self._unpacked:
            self.unpack()

        return self._kwargs

    @property
    def options(self) -> dict[str, Any]:
        return {}

    def payload_is_binary(self) -> bool:
        return True

    @property
    def payload(self) -> bytes | None:
        return self._msg.payload

    @property
    def payload_serializer(self) -> int:
        return self._msg.payload_serializer


def from_protobuf(payload: bytes) -> Message:
    result = yield_pb2.Yield()
    result.ParseFromString(payload)

    return Yield(YieldFields(result))


def to_protobuf(yield_: Yield) -> bytes:
    result = yield_pb2.Yield()
    result.request_id = yield_.request_id

    if yield_.payload_is_binary():
        result.payload = yield_.payload
        result.payload_serializer = yield_.payload_serializer
    else:
        try:
            payload = helpers.to_cbor_payload(yield_.args, yield_.kwargs)
        except Exception as e:
            raise Exception(f"error in serialization to cbor: {e}")

        serializer = 1

        result.payload = payload
        result.payload_serializer = serializer

    return result.SerializeToString()
