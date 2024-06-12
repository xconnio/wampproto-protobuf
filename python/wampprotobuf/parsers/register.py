from typing import Any

from wampproto.messages import Message
from wampproto.messages.register import IRegisterFields, Register

from wampprotobuf.gen import register_pb2


class RegisterFields(IRegisterFields):
    def __init__(self, msg: register_pb2.Register):
        super().__init__()
        self._msg = msg

    @property
    def request_id(self) -> int:
        return self._msg.request_id

    @property
    def uri(self) -> str:
        return self._msg.procedure

    @property
    def options(self) -> dict[str, Any]:
        return {}


def from_protobuf(payload: bytes) -> Message:
    result = register_pb2.Register()
    result.ParseFromString(payload)

    return Register(RegisterFields(result))


def to_protobuf(register: Register) -> bytes:
    result = register_pb2.Register()
    result.request_id = register.request_id
    result.procedure = register.uri

    return result.SerializeToString()
