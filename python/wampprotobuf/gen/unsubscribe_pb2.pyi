from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnSubscribe(_message.Message):
    __slots__ = ("request_id", "subscription_id")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    subscription_id: int
    def __init__(self, request_id: _Optional[int] = ..., subscription_id: _Optional[int] = ...) -> None: ...
