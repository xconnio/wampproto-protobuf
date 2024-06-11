from typing import Any

from wampproto.messages import Message
from wampproto.messages.authenticate import IAuthenticateFields, Authenticate

from wampprotobuf.gen import authenticate_pb2


class AuthenticateFields(IAuthenticateFields):
    def __init__(self, msg: authenticate_pb2.Authenticate):
        super().__init__()
        self._msg = msg

    @property
    def signature(self) -> str:
        return self._msg.signature

    @property
    def extra(self) -> dict[str, Any]:
        return {}


def from_protobuf(payload: bytes) -> Message:
    result = authenticate_pb2.Authenticate()
    result.ParseFromString(payload)

    return Authenticate(AuthenticateFields(result))


def to_protobuf(authenticate: Authenticate) -> bytes:
    result = authenticate_pb2.Authenticate()
    result.signature = authenticate.signature

    return result.SerializeToString()
