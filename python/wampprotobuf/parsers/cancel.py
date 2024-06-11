from typing import Any

from wampproto.messages import Message
from wampproto.messages.cancel import ICancelFields, Cancel

from wampprotobuf.gen import cancel_pb2


class CancelFields(ICancelFields):
    def __init__(self, msg: cancel_pb2.Cancel):
        super().__init__()
        self._msg = msg

    @property
    def request_id(self) -> int:
        return self._msg.request_id

    @property
    def options(self) -> dict[str, Any]:
        return {}


def from_protobuf(payload: bytes) -> Message:
    result = cancel_pb2.Cancel()
    result.ParseFromString(payload)

    return Cancel(CancelFields(result))


def to_protobuf(cancel: Cancel) -> bytes:
    result = cancel_pb2.Cancel()
    result.request_id = cancel.request_id

    return result.SerializeToString()
