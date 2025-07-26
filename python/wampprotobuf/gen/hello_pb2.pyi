from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Hello(_message.Message):
    __slots__ = ["auth_id", "auth_method", "auth_provider", "realm"]
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_METHOD_FIELD_NUMBER: _ClassVar[int]
    AUTH_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    REALM_FIELD_NUMBER: _ClassVar[int]
    auth_id: str
    auth_method: _containers.RepeatedScalarFieldContainer[str]
    auth_provider: str
    realm: str
    def __init__(self, realm: _Optional[str] = ..., auth_id: _Optional[str] = ..., auth_provider: _Optional[str] = ..., auth_method: _Optional[_Iterable[str]] = ...) -> None: ...
