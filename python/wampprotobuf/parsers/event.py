from typing import Any

from wampproto.messages import Message
from wampproto.messages.event import IEventFields, Event

from wampprotobuf.gen import event_pb2
from wampprotobuf.parsers import helpers


class EventFields(IEventFields):
    def __init__(self, msg: event_pb2.Event):
        super().__init__()
        self._msg = msg
        self._args = None
        self._kwargs = None
        self._unpacked = False

    @property
    def subscription_id(self) -> int:
        return self._msg.subscription_id

    @property
    def publication_id(self) -> int:
        return self._msg.publication_id

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
    result = event_pb2.Event()
    result.ParseFromString(payload)

    return Event(EventFields(result))


def to_protobuf(event: Event) -> bytes:
    result = event_pb2.Event()
    result.subscription_id = event.subscription_id
    result.publication_id = event.publication_id

    if event.payload_is_binary():
        result.payload = event.payload
        result.payload_serializer = event.payload_serializer
    else:
        try:
            payload = helpers.to_cbor_payload(event.args, event.kwargs)
        except Exception as e:
            raise Exception(f"error in serialization to cbor: {e}")

        serializer = 1

        result.payload = payload
        result.payload_serializer = serializer

    return result.SerializeToString()
