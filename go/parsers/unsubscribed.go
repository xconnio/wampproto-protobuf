package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type Unsubscribed struct {
	gen *gen.UnSubscribed
}

func NewUnsubscribedFields(gen *gen.UnSubscribed) messages.UnSubscribedFields {
	return &Unsubscribed{gen: gen}
}

func (u *Unsubscribed) RequestID() int64 {
	return u.gen.GetRequestId()
}

func UnsubscribedToProtobuf(unsubscribed *messages.UnSubscribed) ([]byte, error) {
	msg := &gen.UnSubscribed{
		RequestId: unsubscribed.RequestID(),
	}

	data, err := proto.Marshal(msg)
	if err != nil {
		return nil, err
	}

	byteValue := byte(messages.MessageTypeUnSubscribed & 0xFF)
	return append([]byte{byteValue}, data...), nil
}

func ProtobufToUnsubscribed(data []byte) (*messages.UnSubscribed, error) {
	msg := &gen.UnSubscribed{}
	err := proto.Unmarshal(data, msg)
	if err != nil {
		return nil, err
	}

	return messages.NewUnSubscribedWithFields(NewUnsubscribedFields(msg)), nil
}
