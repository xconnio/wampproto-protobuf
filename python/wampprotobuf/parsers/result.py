from typing import Any

from wampproto.messages import Message
from wampproto.messages.result import IResultFields, Result

from wampprotobuf.gen import result_pb2
from wampprotobuf.parsers import helpers


class ResultFields(IResultFields):
    def __init__(self, msg: result_pb2.Result):
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
    result = result_pb2.Result()
    result.ParseFromString(payload)

    return Result(ResultFields(result))


def to_protobuf(result: Result) -> bytes:
    result_pb = result_pb2.Result()
    result_pb.request_id = result.request_id

    if result.payload_is_binary():
        result_pb.payload = result.payload
        result_pb.payload_serializer = result.payload_serializer
    else:
        try:
            payload = helpers.to_cbor_payload(result.args, result.kwargs)
        except Exception as e:
            raise Exception(f"error in serialization to cbor: {e}")

        serializer = 1

        result_pb.payload = payload
        result_pb.payload_serializer = serializer

    return result_pb.SerializeToString()
