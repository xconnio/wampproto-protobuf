from wampproto.messages import Message
from wampproto.messages.unsubscribed import IUnsubscribedFields, Unsubscribed

from wampprotobuf.gen import unsubscribed_pb2


class UnSubscribedFields(IUnsubscribedFields):
    def __init__(self, msg: unsubscribed_pb2.UnSubscribed):
        self._msg = msg

    @property
    def request_id(self) -> int:
        return self._msg.request_id


def from_protobuf(payload: bytes) -> Message:
    result = unsubscribed_pb2.UnSubscribed()
    result.ParseFromString(payload)

    return Unsubscribed(UnSubscribedFields(result))


def to_protobuf(unsubscribed: Unsubscribed) -> bytes:
    result = unsubscribed_pb2.UnSubscribed()
    result.request_id = unsubscribed.request_id

    return result.SerializeToString()
