from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Call(_message.Message):
    __slots__ = ("request_id", "procedure", "payload_serializer_id")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROCEDURE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SERIALIZER_ID_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    procedure: str
    payload_serializer_id: int
    def __init__(self, request_id: _Optional[int] = ..., procedure: _Optional[str] = ..., payload_serializer_id: _Optional[int] = ...) -> None: ...
