from typing import Any

from wampproto.messages import Message
from wampproto.messages.subscribe import ISubscribeFields, Subscribe

from wampprotobuf.gen import subscribe_pb2


class SubscribeFields(ISubscribeFields):
    def __init__(self, msg: subscribe_pb2.Subscribe):
        self._msg = msg

    @property
    def request_id(self) -> int:
        return self._msg.request_id

    @property
    def topic(self) -> str:
        return self._msg.topic

    @property
    def options(self) -> dict[str, Any]:
        return {}


def from_protobuf(payload: bytes) -> Message:
    result = subscribe_pb2.Subscribe()
    result.ParseFromString(payload)

    return Subscribe(SubscribeFields(result))


def to_protobuf(subscribe: Subscribe) -> bytes:
    result = subscribe_pb2.Subscribe()
    result.request_id = subscribe.request_id
    result.topic = subscribe.topic

    return result.SerializeToString()
