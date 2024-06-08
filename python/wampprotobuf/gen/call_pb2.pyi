from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Call(_message.Message):
    __slots__ = ("request_id", "procedure", "payload", "payload_serializer", "disclose_me", "timeout", "receive_progress", "progress")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROCEDURE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SERIALIZER_FIELD_NUMBER: _ClassVar[int]
    DISCLOSE_ME_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    RECEIVE_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    procedure: str
    payload: bytes
    payload_serializer: int
    disclose_me: bool
    timeout: int
    receive_progress: bool
    progress: bool
    def __init__(self, request_id: _Optional[int] = ..., procedure: _Optional[str] = ..., payload: _Optional[bytes] = ..., payload_serializer: _Optional[int] = ..., disclose_me: bool = ..., timeout: _Optional[int] = ..., receive_progress: bool = ..., progress: bool = ...) -> None: ...
