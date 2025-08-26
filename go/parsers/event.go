package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-go/serializers"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type Event struct {
	gen *gen.Event
	messages.BinaryPayload
}

func NewEventFields(gen *gen.Event) messages.EventFields {
	return &Event{gen: gen}
}

func (e *Event) SubscriptionID() uint64 {
	return e.gen.SubscriptionId
}

func (e *Event) PublicationID() uint64 {
	return e.gen.PublicationId
}

func (e *Event) Details() map[string]any {
	return map[string]any{}
}

func (e *Event) Args() []any {
	return nil
}

func (e *Event) KwArgs() map[string]any {
	return nil
}

func (e *Event) PayloadIsBinary() bool {
	return true
}

func (e *Event) Payload() []byte {
	return e.gen.GetPayload()
}

func (e *Event) PayloadSerializer() uint64 {
	return e.gen.GetPayloadSerializer()
}

func EventToProtobuf(event *messages.Event) ([]byte, error) {
	payload, err := serializers.EncodeCBOR(event.Args(), event.KwArgs())
	if err != nil {
		return nil, err
	}

	msg := &gen.Event{
		SubscriptionId:    event.SubscriptionID(),
		PublicationId:     event.PublicationID(),
		PayloadSerializer: serializers.CBORSerializerID,
		Payload:           payload,
	}

	data, err := proto.Marshal(msg)
	if err != nil {
		return nil, err
	}

	byteValue := byte(messages.MessageTypeEvent & 0xFF)
	return append([]byte{byteValue}, data...), nil
}

func ProtobufToEvent(data []byte) (*messages.Event, error) {
	msg := &gen.Event{}
	err := proto.Unmarshal(data, msg)
	if err != nil {
		return nil, err
	}

	return messages.NewEventWithFields(NewEventFields(msg)), nil
}
