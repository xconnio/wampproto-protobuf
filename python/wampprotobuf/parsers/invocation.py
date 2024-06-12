from typing import Any

from wampproto.messages import Message
from wampproto.messages.invocation import IInvocationFields, Invocation

from wampprotobuf.gen import invocation_pb2
from wampprotobuf.parsers import helpers


class InvocationFields(IInvocationFields):
    def __init__(self, msg: invocation_pb2.Invocation):
        super().__init__()
        self._msg = msg
        self._args = None
        self._kwargs = None
        self._unpacked = False

    @property
    def request_id(self) -> int:
        return self._msg.request_id

    @property
    def registration_id(self) -> int:
        return self._msg.registration_id

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
    def details(self) -> dict[str, Any]:
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
    result = invocation_pb2.Invocation()
    result.ParseFromString(payload)

    return Invocation(InvocationFields(result))


def to_protobuf(invocation: Invocation) -> bytes:
    result = invocation_pb2.Invocation()
    result.request_id = invocation.request_id
    result.registration_id = invocation.registration_id

    if invocation.payload_is_binary():
        result.payload = invocation.payload
        result.payload_serializer = invocation.payload_serializer
    else:
        try:
            payload = helpers.to_cbor_payload(invocation.args, invocation.kwargs)
        except Exception as e:
            raise Exception(f"error in serialization to cbor: {e}")

        serializer = 1

        result.payload = payload
        result.payload_serializer = serializer

    return result.SerializeToString()
