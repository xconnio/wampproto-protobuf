from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Published(_message.Message):
    __slots__ = ["publication_id", "request_id"]
    PUBLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    publication_id: int
    request_id: int
    def __init__(self, request_id: _Optional[int] = ..., publication_id: _Optional[int] = ...) -> None: ...
