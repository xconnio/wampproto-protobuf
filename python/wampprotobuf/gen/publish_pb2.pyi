from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Publish(_message.Message):
    __slots__ = ("request_id", "topic", "payload", "payload_serializer")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SERIALIZER_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    topic: str
    payload: bytes
    payload_serializer: int
    def __init__(self, request_id: _Optional[int] = ..., topic: _Optional[str] = ..., payload: _Optional[bytes] = ..., payload_serializer: _Optional[int] = ...) -> None: ...
