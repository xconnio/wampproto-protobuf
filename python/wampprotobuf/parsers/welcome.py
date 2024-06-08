from typing import Any

from wampproto.messages import Message
from wampproto.messages.welcome import IWelcomeFields, Welcome

from wampprotobuf.gen import welcome_pb2


class WelcomeFields(IWelcomeFields):
    def __init__(self, msg: welcome_pb2.Welcome):
        super().__init__()
        self._msg = msg

    @property
    def session_id(self) -> int:
        return self._msg.session_id

    @property
    def roles(self) -> dict[str, Any]:
        return {}

    @property
    def authid(self) -> str:
        return self._msg.auth_id

    @property
    def authrole(self) -> str:
        return self._msg.auth_role

    @property
    def authmethod(self) -> str:
        return ""

    @property
    def authextra(self) -> dict[str, Any]:
        return {}


def from_protobuf(payload: bytes) -> Message:
    result = welcome_pb2.Welcome()
    result.ParseFromString(payload)

    return Welcome(WelcomeFields(result))


def to_protobuf(welcome: Welcome) -> bytes:
    result = welcome_pb2.Welcome()
    result.session_id = welcome.session_id
    result.auth_id = welcome.authid
    result.auth_role = welcome.authrole

    return result.SerializeToString()
