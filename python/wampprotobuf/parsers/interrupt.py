from typing import Any

from wampproto.messages import Message
from wampproto.messages.interrupt import IInterruptFields, Interrupt

from wampprotobuf.gen import interrupt_pb2


class InterruptFields(IInterruptFields):
    def __init__(self, msg: interrupt_pb2.Interrupt):
        super().__init__()
        self._msg = msg

    @property
    def request_id(self) -> int:
        return self._msg.request_id

    @property
    def options(self) -> dict[str, Any]:
        return {}


def from_protobuf(payload: bytes) -> Message:
    result = interrupt_pb2.Interrupt()
    result.ParseFromString(payload)

    return Interrupt(InterruptFields(result))


def to_protobuf(interrupt: Interrupt) -> bytes:
    result = interrupt_pb2.Interrupt()
    result.request_id = interrupt.request_id

    return result.SerializeToString()
