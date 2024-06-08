from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Error(_message.Message):
    __slots__ = ("message_type", "request_id", "uri", "payload", "payload_serializer")
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SERIALIZER_FIELD_NUMBER: _ClassVar[int]
    message_type: int
    request_id: int
    uri: str
    payload: bytes
    payload_serializer: int
    def __init__(self, message_type: _Optional[int] = ..., request_id: _Optional[int] = ..., uri: _Optional[str] = ..., payload: _Optional[bytes] = ..., payload_serializer: _Optional[int] = ...) -> None: ...
