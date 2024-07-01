package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type Unregister struct {
	gen *gen.UnRegister
}

func NewUnregisterFields(gen *gen.UnRegister) messages.UnRegisterFields {
	return &Unregister{gen: gen}
}

func (u *Unregister) RequestID() int64 {
	return u.gen.GetRequestId()
}

func (u *Unregister) RegistrationID() int64 {
	return u.gen.GetRegistrationId()
}

func UnregisterToProtobuf(unregister *messages.UnRegister) ([]byte, error) {
	msg := &gen.UnRegister{
		RequestId:      unregister.RequestID(),
		RegistrationId: unregister.RegistrationID(),
	}

	data, err := proto.Marshal(msg)
	if err != nil {
		return nil, err
	}

	byteValue := byte(messages.MessageTypeUnRegister & 0xFF)
	return append([]byte{byteValue}, data...), nil
}

func ProtobufToUnregister(data []byte) (*messages.UnRegister, error) {
	msg := &gen.UnRegister{}
	err := proto.Unmarshal(data, msg)
	if err != nil {
		return nil, err
	}

	return messages.NewUnRegisterWithFields(NewUnregisterFields(msg)), nil
}
