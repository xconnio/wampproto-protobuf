from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnRegistered(_message.Message):
    __slots__ = ("request_id", "registration_id")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_ID_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    registration_id: int
    def __init__(self, request_id: _Optional[int] = ..., registration_id: _Optional[int] = ...) -> None: ...
