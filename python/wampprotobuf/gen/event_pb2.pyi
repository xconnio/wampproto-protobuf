from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Event(_message.Message):
    __slots__ = ["payload", "payload_serializer", "publication_id", "publisher", "publisher_auth_id", "publisher_auth_role", "subscription_id"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SERIALIZER_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_AUTH_ROLE_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    payload_serializer: int
    publication_id: int
    publisher: int
    publisher_auth_id: str
    publisher_auth_role: str
    subscription_id: int
    def __init__(self, subscription_id: _Optional[int] = ..., publication_id: _Optional[int] = ..., payload: _Optional[bytes] = ..., payload_serializer: _Optional[int] = ..., publisher: _Optional[int] = ..., publisher_auth_id: _Optional[str] = ..., publisher_auth_role: _Optional[str] = ...) -> None: ...
