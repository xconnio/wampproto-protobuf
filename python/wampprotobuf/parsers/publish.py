from typing import Any

from wampproto.messages import Message
from wampproto.messages.publish import IPublishFields, Publish

from wampprotobuf.gen import publish_pb2
from wampprotobuf.parsers import helpers


class PublishFields(IPublishFields):
    def __init__(self, msg: publish_pb2.Publish):
        super().__init__()
        self._msg = msg
        self._args = None
        self._kwargs = None
        self._unpacked = False

    @property
    def request_id(self) -> int:
        return self._msg.request_id

    @property
    def uri(self) -> str:
        return self._msg.topic

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
    result = publish_pb2.Publish()
    result.ParseFromString(payload)

    return Publish(PublishFields(result))


def to_protobuf(publish: Publish) -> bytes:
    result = publish_pb2.Publish()
    result.request_id = publish.request_id
    result.topic = publish.uri

    if publish.payload_is_binary():
        result.payload = publish.payload
        result.payload_serializer = publish.payload_serializer
    else:
        try:
            payload = helpers.to_cbor_payload(publish.args, publish.kwargs)
        except Exception as e:
            raise Exception(f"error in serialization to cbor: {e}")

        serializer = 1

        result.payload = payload
        result.payload_serializer = serializer

    return result.SerializeToString()
