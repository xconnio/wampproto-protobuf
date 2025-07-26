package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type Unregistered struct {
	gen *gen.UnRegistered
}

func NewUnregisteredFields(gen *gen.UnRegistered) messages.UnregisteredFields {
	return &Unregistered{gen: gen}
}

func (u *Unregistered) RequestID() uint64 {
	return u.gen.GetRequestId()
}

func UnregisteredToProtobuf(unregistered *messages.Unregistered) ([]byte, error) {
	msg := &gen.UnRegistered{
		RequestId: unregistered.RequestID(),
	}

	data, err := proto.Marshal(msg)
	if err != nil {
		return nil, err
	}

	byteValue := byte(messages.MessageTypeUnregistered & 0xFF)
	return append([]byte{byteValue}, data...), nil
}

func ProtobufToUnregistered(data []byte) (*messages.Unregistered, error) {
	msg := &gen.UnRegistered{}
	err := proto.Unmarshal(data, msg)
	if err != nil {
		return nil, err
	}

	return messages.NewUnregisteredWithFields(NewUnregisteredFields(msg)), nil
}
