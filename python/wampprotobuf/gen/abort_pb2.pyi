from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Abort(_message.Message):
    __slots__ = ["payload", "payload_serializer", "reason"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SERIALIZER_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    payload_serializer: int
    reason: str
    def __init__(self, reason: _Optional[str] = ..., payload: _Optional[bytes] = ..., payload_serializer: _Optional[int] = ...) -> None: ...
