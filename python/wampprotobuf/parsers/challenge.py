from typing import Any

from wampproto.messages import Message
from wampproto.messages.challenge import IChallengeFields, Challenge

from wampprotobuf.gen import challenge_pb2


class ChallengeFields(IChallengeFields):
    def __init__(self, msg: challenge_pb2.Challenge):
        super().__init__()
        self._msg = msg

    @property
    def authmethod(self) -> str:
        return self._msg.auth_method

    @property
    def extra(self) -> dict[str, Any]:
        return {}


def from_protobuf(payload: bytes) -> Message:
    result = challenge_pb2.Challenge()
    result.ParseFromString(payload)

    return Challenge(ChallengeFields(result))


def to_protobuf(challenge: Challenge) -> bytes:
    result = challenge_pb2.Challenge()
    result.auth_method = challenge.authmethod

    return result.SerializeToString()
