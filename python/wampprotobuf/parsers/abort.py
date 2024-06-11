from typing import Any

from wampproto.messages import Message
from wampproto.messages.abort import IAbortFields, Abort

from wampprotobuf.gen import abort_pb2


class AbortFields(IAbortFields):
    def __init__(self, msg: abort_pb2.Abort):
        super().__init__()
        self._msg = msg
        self._args = None
        self._kwargs = None

    @property
    def details(self) -> dict[str, Any]:
        return {}

    @property
    def reason(self) -> str:
        return self._msg.reason


def from_protobuf(payload: bytes) -> Message:
    result = abort_pb2.Abort()
    result.ParseFromString(payload)

    return Abort(AbortFields(result))


def to_protobuf(abort: Abort) -> bytes:
    result = abort_pb2.Abort()
    result.reason = abort.reason

    return result.SerializeToString()
