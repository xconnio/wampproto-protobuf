package parsers

import (
	"log"
	"sync"

	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type Invocation struct {
	gen *gen.Invocation

	args   []any
	kwArgs map[string]any
	once   sync.Once
}

func NewInvocationFields(gen *gen.Invocation) messages.InvocationFields {
	return &Invocation{gen: gen}
}

func (i *Invocation) RequestID() uint64 {
	return i.gen.GetRequestId()
}

func (i *Invocation) RegistrationID() uint64 {
	return i.gen.GetRegistrationId()
}

func (i *Invocation) Details() map[string]any {
	return map[string]any{}
}

func (i *Invocation) unpack() {
	unpacked, err := FromCBORPayload(i.Payload())
	if err != nil {
		log.Println("error parsing CBOR payload:", err)
	} else {
		i.args = unpacked.Args()
		i.kwArgs = unpacked.KwArgs()
	}
}

func (i *Invocation) Args() []any {
	i.once.Do(i.unpack)
	return i.args
}

func (i *Invocation) KwArgs() map[string]any {
	i.once.Do(i.unpack)
	return i.kwArgs
}

func (i *Invocation) PayloadIsBinary() bool {
	return true
}

func (i *Invocation) Payload() []byte {
	return i.gen.GetPayload()
}

func (i *Invocation) PayloadSerializer() uint64 {
	return i.gen.GetPayloadSerializer()
}

func InvocationToProtobuf(invocation *messages.Invocation) ([]byte, error) {
	var msg *gen.Invocation
	if invocation.PayloadIsBinary() {
		msg = &gen.Invocation{
			RequestId:         invocation.RequestID(),
			RegistrationId:    invocation.RegistrationID(),
			PayloadSerializer: invocation.PayloadSerializer(),
			Payload:           invocation.Payload(),
		}
	} else {
		payload, serializer, err := ToCBORPayload(invocation)
		if err != nil {
			return nil, err
		}

		msg = &gen.Invocation{
			RequestId:         invocation.RequestID(),
			RegistrationId:    invocation.RegistrationID(),
			PayloadSerializer: serializer,
			Payload:           payload,
		}
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
