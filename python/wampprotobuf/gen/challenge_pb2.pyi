from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Challenge(_message.Message):
    __slots__ = ["auth_method", "challenge"]
    AUTH_METHOD_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    auth_method: str
    challenge: str
    def __init__(self, auth_method: _Optional[str] = ..., challenge: _Optional[str] = ...) -> None: ...
