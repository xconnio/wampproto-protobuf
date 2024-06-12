from wampproto.messages import Message
from wampproto.messages.subscribed import ISubscribedFields, Subscribed

from wampprotobuf.gen import subscribed_pb2


class SubscribedFields(ISubscribedFields):
    def __init__(self, msg: subscribed_pb2.Subscribed):
        self._msg = msg

    @property
    def request_id(self) -> int:
        return self._msg.request_id

    @property
    def subscription_id(self) -> int:
        return self._msg.subscription_id


def from_protobuf(payload: bytes) -> Message:
    result = subscribed_pb2.Subscribed()
    result.ParseFromString(payload)

    return Subscribed(SubscribedFields(result))


def to_protobuf(subscribed: Subscribed) -> bytes:
    result = subscribed_pb2.Subscribed()
    result.request_id = subscribed.request_id
    result.subscription_id = subscribed.subscription_id

    return result.SerializeToString()
