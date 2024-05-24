from typing import Any

from wampproto.messages import Message
from wampproto.messages.hello import IHelloFields, Hello

from wampprotobuf.gen import hello_pb2


class HelloFields(IHelloFields):
    def __init__(self, msg: hello_pb2.Hello):
        super().__init__()
        self._msg = msg

    @property
    def realm(self) -> str:
        return self._msg.realm

    @property
    def roles(self) -> dict[str, Any]:
        return {}

    @property
    def authid(self) -> str:
        return self._msg.authid

    @property
    def authrole(self) -> str:
        return ""

    @property
    def authmethods(self) -> list[str]:
        return self._msg.authmethod

    @property
    def authextra(self) -> dict:
        return {}


def from_protobuf(payload: bytes) -> Message:
    result = hello_pb2.Hello()
    result.ParseFromString(payload)

    return Hello(HelloFields(result))


def to_protobuf(hello: Hello) -> bytes:
    result = hello_pb2.Hello()
    result.realm = hello.realm
    result.authid = hello.authid
    result.authprovider = "static"

    return result.SerializeToString()
