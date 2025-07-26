from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Publish(_message.Message):
    __slots__ = ["payload", "payload_serializer", "request_id", "topic"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SERIALIZER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    payload_serializer: int
    request_id: int
    topic: str
    def __init__(self, request_id: _Optional[int] = ..., topic: _Optional[str] = ..., payload: _Optional[bytes] = ..., payload_serializer: _Optional[int] = ...) -> None: ...
