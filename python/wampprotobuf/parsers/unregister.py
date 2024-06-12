from wampproto.messages import Message
from wampproto.messages.unregister import IUnRegisterFields, UnRegister

from wampprotobuf.gen import unregister_pb2


class UnRegisterFields(IUnRegisterFields):
    def __init__(self, msg: unregister_pb2.UnRegister):
        super().__init__()
        self._msg = msg

    @property
    def request_id(self) -> int:
        return self._msg.request_id

    @property
    def registration_id(self) -> int:
        return self._msg.registration_id


def from_protobuf(payload: bytes) -> Message:
    result = unregister_pb2.UnRegister()
    result.ParseFromString(payload)

    return UnRegister(UnRegisterFields(result))


def to_protobuf(unregister: UnRegister) -> bytes:
    result = unregister_pb2.UnRegister()
    result.request_id = unregister.request_id
    result.registration_id = unregister.registration_id

    return result.SerializeToString()
