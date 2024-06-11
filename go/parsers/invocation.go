package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type invocationFields struct {
	gen *gen.Invocation
	messages.BinaryPayload
}

func NewInvocationFields(gen *gen.Invocation) messages.InvocationFields {
	return &invocationFields{gen: gen}
}

func (r *invocationFields) RequestID() int64 {
	return r.gen.GetRequestId()
}

func (r *invocationFields) RegistrationID() int64 {
	return r.gen.GetRegistrationId()
}

func (r *invocationFields) Details() map[string]any {
	return map[string]any{}
}

func (r *invocationFields) Args() []any {
	return nil
}

func (r *invocationFields) KwArgs() map[string]any {
	return nil
}

func (r *invocationFields) PayloadIsBinary() bool {
	return true
}

func (r *invocationFields) Payload() []byte {
	return r.gen.GetPayload()
}

func (r *invocationFields) PayloadSerializer() int {
	return int(r.gen.GetPayloadSerializer())
}

func InvocationToProtobuf(invocation *messages.Invocation) ([]byte, error) {
	payload, serializer, err := ToCBORPayload(invocation)
	if err != nil {
		return nil, err
	}

	msg := &gen.Invocation{
		RequestId:         invocation.RequestID(),
		RegistrationId:    invocation.RegistrationID(),
		PayloadSerializer: int32(serializer),
		Payload:           payload,
	}

	data, err := proto.Marshal(msg)
	if err != nil {
		return nil, err
	}

	byteValue := byte(messages.MessageTypeInvocation & 0xFF)
	return append([]byte{byteValue}, data...), nil
}

func ProtobufToInvocation(data []byte) (*messages.Invocation, error) {
	msg := &gen.Invocation{}
	err := proto.Unmarshal(data, msg)
	if err != nil {
		return nil, err
	}

	return messages.NewInvocationWithFields(NewInvocationFields(msg)), nil
}
