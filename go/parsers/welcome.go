package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type welcome struct {
	gen *gen.Welcome
}

func NewWelcomeFields(call *gen.Welcome) messages.WelcomeFields {
	return &welcome{
		gen: call,
	}
}

func (w *welcome) SessionID() int64 {
	return w.gen.GetSessionId()
}

func (w *welcome) Details() map[string]any {
	return map[string]any{
		"authid":   "anonymous",
		"authrole": "anonymous",
	}
}

func WelcomeToProtobuf(welcome *messages.Welcome) ([]byte, error) {
	msg := &gen.Welcome{
		SessionId: welcome.SessionID(),
		AuthRole:  "anonymous",
	}

	data, err := proto.Marshal(msg)
	if err != nil {
		return nil, err
	}

	byteValue := byte(messages.MessageTypeWelcome & 0xFF)
	return append([]byte{byteValue}, data...), nil
}

func ProtobufToWelcome(data []byte) (*messages.Welcome, error) {
	msg := &gen.Welcome{}
	err := proto.Unmarshal(data, msg)
	if err != nil {
		return nil, err
	}

	return messages.NewWelcomeWithFields(NewWelcomeFields(msg)), nil
}
