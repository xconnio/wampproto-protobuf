from wampproto.messages import Message
from wampproto.messages.unregistered import IUnregisteredFields, Unregistered

from wampprotobuf.gen import unregistered_pb2


class UnRegisteredFields(IUnregisteredFields):
    def __init__(self, msg: unregistered_pb2.UnRegistered):
        super().__init__()
        self._msg = msg

    @property
    def request_id(self) -> int:
        return self._msg.request_id


def from_protobuf(payload: bytes) -> Message:
    result = unregistered_pb2.UnRegistered()
    result.ParseFromString(payload)

    return Unregistered(UnRegisteredFields(result))


def to_protobuf(unregister: Unregistered) -> bytes:
    result = unregistered_pb2.UnRegistered()
    result.request_id = unregister.request_id

    return result.SerializeToString()
