from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Invocation(_message.Message):
    __slots__ = ("request_id", "registration_id", "payload_serializer_id", "caller", "caller_authid", "caller_authrole", "procedure")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SERIALIZER_ID_FIELD_NUMBER: _ClassVar[int]
    CALLER_FIELD_NUMBER: _ClassVar[int]
    CALLER_AUTHID_FIELD_NUMBER: _ClassVar[int]
    CALLER_AUTHROLE_FIELD_NUMBER: _ClassVar[int]
    PROCEDURE_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    registration_id: int
    payload_serializer_id: int
    caller: int
    caller_authid: str
    caller_authrole: str
    procedure: str
    def __init__(self, request_id: _Optional[int] = ..., registration_id: _Optional[int] = ..., payload_serializer_id: _Optional[int] = ..., caller: _Optional[int] = ..., caller_authid: _Optional[str] = ..., caller_authrole: _Optional[str] = ..., procedure: _Optional[str] = ...) -> None: ...
