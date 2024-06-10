package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type Subscribe struct {
	gen *gen.Subscribe
}

func NewSubscribeFields(gen *gen.Subscribe) messages.SubscribeFields {
	return &Subscribe{gen: gen}
}

func (s *Subscribe) RequestID() int64 {
	return s.gen.GetRequestId()
}

func (s *Subscribe) Options() map[string]any {
	return map[string]any{}
}

func (s *Subscribe) Topic() string {
	return s.gen.GetTopic()
}

func SubscribeToProtobuf(subscribe *messages.Subscribe) ([]byte, error) {
	msg := &gen.Subscribe{
		RequestId: subscribe.RequestID(),
		Topic:     subscribe.Topic(),
	}

	data, err := proto.Marshal(msg)
	if err != nil {
		return nil, err
	}

	byteValue := byte(messages.MessageTypeSubscribe & 0xFF)
	return append([]byte{byteValue}, data...), nil
}

func ProtobufToSubscribe(data []byte) (*messages.Subscribe, error) {
	msg := &gen.Subscribe{}
	err := proto.Unmarshal(data[1:], msg)
	if err != nil {
		return nil, err
	}

	return messages.NewSubscribeWithFields(NewSubscribeFields(msg)), nil
}
