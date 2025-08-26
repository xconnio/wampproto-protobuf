from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Publish(_message.Message):
    __slots__ = ("request_id", "topic", "payload_serializer_id", "exclude_me", "acknowledge")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SERIALIZER_ID_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_ME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGE_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    topic: str
    payload_serializer_id: int
    exclude_me: bool
    acknowledge: bool
    def __init__(self, request_id: _Optional[int] = ..., topic: _Optional[str] = ..., payload_serializer_id: _Optional[int] = ..., exclude_me: bool = ..., acknowledge: bool = ...) -> None: ...
