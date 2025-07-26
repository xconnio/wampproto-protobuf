from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Result(_message.Message):
    __slots__ = ["payload", "payload_serializer", "progress", "request_id"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SERIALIZER_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    payload_serializer: int
    progress: bool
    request_id: int
    def __init__(self, request_id: _Optional[int] = ..., payload: _Optional[bytes] = ..., payload_serializer: _Optional[int] = ..., progress: bool = ...) -> None: ...
