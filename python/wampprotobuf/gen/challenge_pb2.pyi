from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Challenge(_message.Message):
    __slots__ = ("authmethod", "challenge", "salt", "iterations", "keylen")
    AUTHMETHOD_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    SALT_FIELD_NUMBER: _ClassVar[int]
    ITERATIONS_FIELD_NUMBER: _ClassVar[int]
    KEYLEN_FIELD_NUMBER: _ClassVar[int]
    authmethod: str
    challenge: str
    salt: str
    iterations: int
    keylen: int
    def __init__(self, authmethod: _Optional[str] = ..., challenge: _Optional[str] = ..., salt: _Optional[str] = ..., iterations: _Optional[int] = ..., keylen: _Optional[int] = ...) -> None: ...
