from wampproto import serializers, messages


class ProtobufSerializer(serializers.Serializer):
    def serialize(self, message: messages.Message) -> bytes:
        pass

    def deserialize(self, data: bytes) -> messages.Message:
        pass
