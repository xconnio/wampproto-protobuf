from protobuf import options_pb2 as _options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Register(_message.Message):
    __slots__ = ("request_id", "procedure", "disclose_caller", "invoke", "match")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROCEDURE_FIELD_NUMBER: _ClassVar[int]
    DISCLOSE_CALLER_FIELD_NUMBER: _ClassVar[int]
    INVOKE_FIELD_NUMBER: _ClassVar[int]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    procedure: str
    disclose_caller: bool
    invoke: _options_pb2.Invoke
    match: _options_pb2.Match
    def __init__(self, request_id: _Optional[int] = ..., procedure: _Optional[str] = ..., disclose_caller: bool = ..., invoke: _Optional[_Union[_options_pb2.Invoke, str]] = ..., match: _Optional[_Union[_options_pb2.Match, str]] = ...) -> None: ...
