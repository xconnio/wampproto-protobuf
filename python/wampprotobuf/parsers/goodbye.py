from typing import Any

from wampproto.messages import Message
from wampproto.messages.goodbye import IGoodbyeFields, Goodbye

from wampprotobuf.gen import goodbye_pb2


class GoodbyeFields(IGoodbyeFields):
    def __init__(self, msg: goodbye_pb2.Goodbye):
        super().__init__()
        self._msg = msg

    @property
    def details(self) -> dict[str, Any]:
        return {}

    @property
    def reason(self) -> str:
        return self._msg.reason


def from_protobuf(payload: bytes) -> Message:
    result = goodbye_pb2.Goodbye()
    result.ParseFromString(payload)

    return Goodbye(GoodbyeFields(result))


def to_protobuf(goodbye: Goodbye) -> bytes:
    result = goodbye_pb2.Goodbye()
    result.reason = goodbye.reason

    return result.SerializeToString()
