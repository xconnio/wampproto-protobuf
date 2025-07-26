from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Call(_message.Message):
    __slots__ = ["disclose_me", "payload", "payload_serializer", "procedure", "progress", "receive_progress", "request_id", "timeout"]
    DISCLOSE_ME_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SERIALIZER_FIELD_NUMBER: _ClassVar[int]
    PROCEDURE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    RECEIVE_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    disclose_me: bool
    payload: bytes
    payload_serializer: int
    procedure: str
    progress: bool
    receive_progress: bool
    request_id: int
    timeout: int
    def __init__(self, request_id: _Optional[int] = ..., procedure: _Optional[str] = ..., payload: _Optional[bytes] = ..., payload_serializer: _Optional[int] = ..., disclose_me: bool = ..., timeout: _Optional[int] = ..., receive_progress: bool = ..., progress: bool = ...) -> None: ...
