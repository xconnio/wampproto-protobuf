package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type Unsubscribed struct {
	gen *gen.UnSubscribed
}

func NewUnsubscribedFields(gen *gen.UnSubscribed) messages.UnsubscribedFields {
	return &Unsubscribed{gen: gen}
}

func (u *Unsubscribed) RequestID() int64 {
	return u.gen.GetRequestId()
}

func UnsubscribedToProtobuf(unsubscribed *messages.Unsubscribed) ([]byte, error) {
	msg := &gen.UnSubscribed{
		RequestId: unsubscribed.RequestID(),
	}

	data, err := proto.Marshal(msg)
	if err != nil {
		return nil, err
	}

	byteValue := byte(messages.MessageTypeUnsubscribed & 0xFF)
	return append([]byte{byteValue}, data...), nil
}

func ProtobufToUnsubscribed(data []byte) (*messages.Unsubscribed, error) {
	msg := &gen.UnSubscribed{}
	err := proto.Unmarshal(data, msg)
	if err != nil {
		return nil, err
	}

	return messages.NewUnsubscribedWithFields(NewUnsubscribedFields(msg)), nil
}
