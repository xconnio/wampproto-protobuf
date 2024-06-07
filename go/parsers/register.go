package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type Register struct {
	gen *gen.Register
}

func NewRegisterFields(gen *gen.Register) messages.RegisterFields {
	return &Register{gen: gen}
}

func (r *Register) RequestID() int64 {
	return r.gen.GetRequestId()
}

func (r *Register) Options() map[string]any {
	return map[string]any{}
}

func (r *Register) Procedure() string {
	return r.gen.GetProcedure()
}

func RegisterToProtobuf(register *messages.Register) ([]byte, error) {
	msg := &gen.Register{
		RequestId: register.RequestID(),
		Procedure: register.Procedure(),
	}

	data, err := proto.Marshal(msg)
	if err != nil {
		return nil, err
	}

	byteValue := byte(messages.MessageTypeRegister & 0xFF)
	return append([]byte{byteValue}, data...), nil
}

func ProtobufToRegister(data []byte) (*messages.Register, error) {
	msg := &gen.Register{}
	err := proto.Unmarshal(data, msg)
	if err != nil {
		return nil, err
	}

	return messages.NewRegisterWithFields(NewRegisterFields(msg)), nil
}
