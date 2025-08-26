from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Welcome(_message.Message):
    __slots__ = ("session_id", "authid", "authrole", "authmethod", "authprovider", "roles")
    class Roles(_message.Message):
        __slots__ = ("dealer", "broker")
        class Dealer(_message.Message):
            __slots__ = ("caller_identification", "call_timeout", "call_canceling", "progressive_call_results", "pattern_based_registration", "shared_registration")
            CALLER_IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
            CALL_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
            CALL_CANCELING_FIELD_NUMBER: _ClassVar[int]
            PROGRESSIVE_CALL_RESULTS_FIELD_NUMBER: _ClassVar[int]
            PATTERN_BASED_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
            SHARED_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
            caller_identification: bool
            call_timeout: bool
            call_canceling: bool
            progressive_call_results: bool
            pattern_based_registration: bool
            shared_registration: bool
            def __init__(self, caller_identification: bool = ..., call_timeout: bool = ..., call_canceling: bool = ..., progressive_call_results: bool = ..., pattern_based_registration: bool = ..., shared_registration: bool = ...) -> None: ...
        class Broker(_message.Message):
            __slots__ = ("publisher_identification", "publisher_exclusion", "acknowledge_event_received", "pattern_based_subscription")
            PUBLISHER_IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
            PUBLISHER_EXCLUSION_FIELD_NUMBER: _ClassVar[int]
            ACKNOWLEDGE_EVENT_RECEIVED_FIELD_NUMBER: _ClassVar[int]
            PATTERN_BASED_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
            publisher_identification: bool
            publisher_exclusion: bool
            acknowledge_event_received: bool
            pattern_based_subscription: bool
            def __init__(self, publisher_identification: bool = ..., publisher_exclusion: bool = ..., acknowledge_event_received: bool = ..., pattern_based_subscription: bool = ...) -> None: ...
        DEALER_FIELD_NUMBER: _ClassVar[int]
        BROKER_FIELD_NUMBER: _ClassVar[int]
        dealer: Welcome.Roles.Dealer
        broker: Welcome.Roles.Broker
        def __init__(self, dealer: _Optional[_Union[Welcome.Roles.Dealer, _Mapping]] = ..., broker: _Optional[_Union[Welcome.Roles.Broker, _Mapping]] = ...) -> None: ...
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHID_FIELD_NUMBER: _ClassVar[int]
    AUTHROLE_FIELD_NUMBER: _ClassVar[int]
    AUTHMETHOD_FIELD_NUMBER: _ClassVar[int]
    AUTHPROVIDER_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    authid: str
    authrole: str
    authmethod: str
    authprovider: str
    roles: Welcome.Roles
    def __init__(self, session_id: _Optional[int] = ..., authid: _Optional[str] = ..., authrole: _Optional[str] = ..., authmethod: _Optional[str] = ..., authprovider: _Optional[str] = ..., roles: _Optional[_Union[Welcome.Roles, _Mapping]] = ...) -> None: ...
