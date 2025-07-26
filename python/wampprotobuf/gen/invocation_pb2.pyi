from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Invocation(_message.Message):
    __slots__ = ["caller", "caller_auth_id", "caller_auth_role", "payload", "payload_serializer", "progress", "receive_progress", "registration_id", "request_id"]
    CALLER_AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    CALLER_AUTH_ROLE_FIELD_NUMBER: _ClassVar[int]
    CALLER_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SERIALIZER_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    RECEIVE_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    caller: int
    caller_auth_id: str
    caller_auth_role: str
    payload: bytes
    payload_serializer: int
    progress: bool
    receive_progress: bool
    registration_id: int
    request_id: int
    def __init__(self, request_id: _Optional[int] = ..., registration_id: _Optional[int] = ..., payload: _Optional[bytes] = ..., payload_serializer: _Optional[int] = ..., caller: _Optional[int] = ..., caller_auth_id: _Optional[str] = ..., caller_auth_role: _Optional[str] = ..., receive_progress: bool = ..., progress: bool = ...) -> None: ...
