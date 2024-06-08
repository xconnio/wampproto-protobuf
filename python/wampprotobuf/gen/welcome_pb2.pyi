from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Welcome(_message.Message):
    __slots__ = ("session_id", "auth_id", "auth_role")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_ROLE_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    auth_id: str
    auth_role: str
    def __init__(self, session_id: _Optional[int] = ..., auth_id: _Optional[str] = ..., auth_role: _Optional[str] = ...) -> None: ...
