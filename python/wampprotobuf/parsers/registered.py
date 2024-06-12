from wampproto.messages import Message
from wampproto.messages.registered import IRegisteredFields, Registered

from wampprotobuf.gen import registered_pb2


class RegisteredFields(IRegisteredFields):
    def __init__(self, msg: registered_pb2.Registered):
        super().__init__()
        self._msg = msg

    @property
    def request_id(self) -> int:
        return self._msg.request_id

    @property
    def registration_id(self) -> int:
        return self._msg.registration_id


def from_protobuf(payload: bytes) -> Message:
    result = registered_pb2.Registered()
    result.ParseFromString(payload)

    return Registered(RegisteredFields(result))


def to_protobuf(registered: Registered) -> bytes:
    result = registered_pb2.Registered()
    result.request_id = registered.request_id
    result.registration_id = registered.registration_id

    return result.SerializeToString()
