package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type Registered struct {
	gen *gen.Registered
}

func NewRegisteredFields(gen *gen.Registered) messages.RegisteredFields {
	return &Registered{gen: gen}
}

func (r *Registered) RequestID() int64 {
	return r.gen.GetRequestId()
}

func (r *Registered) RegistrationID() int64 {
	return r.gen.RegistrationId
}

func RegisteredToProtobuf(registered *messages.Registered) ([]byte, error) {
	msg := &gen.Registered{
		RequestId:      registered.RequestID(),
		RegistrationId: registered.RegistrationID(),
	}

	data, err := proto.Marshal(msg)
	if err != nil {
		return nil, err
	}

	byteValue := byte(messages.MessageTypeRegistered & 0xFF)
	return append([]byte{byteValue}, data...), nil
}

func ProtobufToRegistered(data []byte) (*messages.Registered, error) {
	msg := &gen.Registered{}
	err := proto.Unmarshal(data, msg)
	if err != nil {
		return nil, err
	}

	return messages.NewRegisteredWithFields(NewRegisteredFields(msg)), nil
}
