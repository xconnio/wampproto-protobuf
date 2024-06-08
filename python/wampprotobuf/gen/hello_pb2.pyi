from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Hello(_message.Message):
    __slots__ = ("realm", "auth_id", "auth_provider", "auth_method")
    REALM_FIELD_NUMBER: _ClassVar[int]
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    AUTH_METHOD_FIELD_NUMBER: _ClassVar[int]
    realm: str
    auth_id: str
    auth_provider: str
    auth_method: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, realm: _Optional[str] = ..., auth_id: _Optional[str] = ..., auth_provider: _Optional[str] = ..., auth_method: _Optional[_Iterable[str]] = ...) -> None: ...
