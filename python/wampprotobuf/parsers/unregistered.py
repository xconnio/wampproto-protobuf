from wampproto.messages import Message
from wampproto.messages.unregistered import IUnRegisteredFields, UnRegistered

from wampprotobuf.gen import unregistered_pb2


class UnRegisteredFields(IUnRegisteredFields):
    def __init__(self, msg: unregistered_pb2.UnRegistered):
        super().__init__()
        self._msg = msg

    @property
    def request_id(self) -> int:
        return self._msg.request_id


def from_protobuf(payload: bytes) -> Message:
    result = unregistered_pb2.UnRegistered()
    result.ParseFromString(payload)

    return UnRegistered(UnRegisteredFields(result))


def to_protobuf(unregister: UnRegistered) -> bytes:
    result = unregistered_pb2.UnRegistered()
    result.request_id = unregister.request_id

    return result.SerializeToString()
