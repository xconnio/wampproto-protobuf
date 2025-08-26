package parsers

import (
	"log"
	"sync"

	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-go/serializers"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type Publish struct {
	gen *gen.Publish

	args   []any
	kwArgs map[string]any
	once   sync.Once
}

func NewPublishFields(gen *gen.Publish) messages.PublishFields {
	return &Publish{gen: gen}
}

func (p *Publish) RequestID() uint64 {
	return p.gen.GetRequestId()
}

func (p *Publish) Options() map[string]any {
	return map[string]any{}
}

func (p *Publish) Topic() string {
	return p.gen.GetTopic()
}

func (p *Publish) unpack() {
	args, kwargs, err := serializers.DecodeCBOR(p.Payload())
	if err != nil {
		log.Println("error parsing CBOR payload:", err)
	} else {
		p.args = args
		p.kwArgs = kwargs
	}
}

func (p *Publish) Args() []any {
	p.once.Do(p.unpack)
	return p.args
}

func (p *Publish) KwArgs() map[string]any {
	p.once.Do(p.unpack)
	return p.kwArgs
}

func (p *Publish) PayloadIsBinary() bool {
	return true
}

func (p *Publish) Payload() []byte {
	return p.gen.GetPayload()
}

func (p *Publish) PayloadSerializer() uint64 {
	return p.gen.GetPayloadSerializer()
}

func PublishToProtobuf(publish *messages.Publish) ([]byte, error) {
	var msg *gen.Publish
	if publish.PayloadIsBinary() {
		msg = &gen.Publish{
			RequestId:         publish.RequestID(),
			Topic:             publish.Topic(),
			PayloadSerializer: publish.PayloadSerializer(),
			Payload:           publish.Payload(),
		}
	} else {
		payload, err := serializers.EncodeCBOR(publish.Args(), publish.KwArgs())
		if err != nil {
			return nil, err
		}

		msg = &gen.Publish{
			RequestId:         publish.RequestID(),
			Topic:             publish.Topic(),
			PayloadSerializer: serializers.CBORSerializerID,
			Payload:           payload,
		}
	}

	data, err := proto.Marshal(msg)
	if err != nil {
		return nil, err
	}

	byteValue := byte(messages.MessageTypePublish & 0xFF)
	return append([]byte{byteValue}, data...), nil
}

func ProtobufToPublish(data []byte) (*messages.Publish, error) {
	msg := &gen.Publish{}
	err := proto.Unmarshal(data, msg)
	if err != nil {
		return nil, err
	}

	return messages.NewPublishWithFields(NewPublishFields(msg)), nil
}
