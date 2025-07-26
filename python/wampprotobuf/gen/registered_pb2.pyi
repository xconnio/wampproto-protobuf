from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Registered(_message.Message):
    __slots__ = ["registration_id", "request_id"]
    REGISTRATION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    registration_id: int
    request_id: int
    def __init__(self, request_id: _Optional[int] = ..., registration_id: _Optional[int] = ...) -> None: ...
