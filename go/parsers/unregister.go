package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type Unregister struct {
	gen *gen.UnRegister
}

func NewUnregisterFields(gen *gen.UnRegister) messages.UnregisterFields {
	return &Unregister{gen: gen}
}

func (u *Unregister) RequestID() uint64 {
	return u.gen.GetRequestId()
}

func (u *Unregister) RegistrationID() uint64 {
	return u.gen.GetRegistrationId()
}

func UnregisterToProtobuf(unregister *messages.Unregister) ([]byte, error) {
	msg := &gen.UnRegister{
		RequestId:      unregister.RequestID(),
		RegistrationId: unregister.RegistrationID(),
	}

	data, err := proto.Marshal(msg)
	if err != nil {
		return nil, err
	}

	byteValue := byte(messages.MessageTypeUnregister & 0xFF)
	return append([]byte{byteValue}, data...), nil
}

func ProtobufToUnregister(data []byte) (*messages.Unregister, error) {
	msg := &gen.UnRegister{}
	err := proto.Unmarshal(data, msg)
	if err != nil {
		return nil, err
	}

	return messages.NewUnregisterWithFields(NewUnregisterFields(msg)), nil
}
