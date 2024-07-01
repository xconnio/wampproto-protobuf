package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type Unregistered struct {
	gen *gen.UnRegistered
}

func NewUnregisteredFields(gen *gen.UnRegistered) messages.UnRegisteredFields {
	return &Unregistered{gen: gen}
}

func (u *Unregistered) RequestID() int64 {
	return u.gen.GetRequestId()
}

func UnregisteredToProtobuf(unregistered *messages.UnRegistered) ([]byte, error) {
	msg := &gen.UnRegistered{
		RequestId: unregistered.RequestID(),
	}

	data, err := proto.Marshal(msg)
	if err != nil {
		return nil, err
	}

	byteValue := byte(messages.MessageTypeUnRegistered & 0xFF)
	return append([]byte{byteValue}, data...), nil
}

func ProtobufToUnregistered(data []byte) (*messages.UnRegistered, error) {
	msg := &gen.UnRegistered{}
	err := proto.Unmarshal(data, msg)
	if err != nil {
		return nil, err
	}

	return messages.NewUnRegisteredWithFields(NewUnregisteredFields(msg)), nil
}
