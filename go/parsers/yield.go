package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type yieldFields struct {
	gen *gen.Yield
}

func NewYieldFields(gen *gen.Yield) messages.YieldFields {
	return &yieldFields{gen: gen}
}

func (r *yieldFields) RequestID() int64 {
	return r.gen.GetRequestId()
}

func (r *yieldFields) Options() map[string]any {
	return map[string]any{}
}

func (r *yieldFields) Args() []any {
	return nil
}

func (r *yieldFields) KwArgs() map[string]any {
	return nil
}

func (r *yieldFields) PayloadIsBinary() bool {
	return true
}

func (r *yieldFields) Payload() []byte {
	return r.gen.GetPayload()
}

func (r *yieldFields) PayloadSerializer() int {
	return int(r.gen.GetPayloadSerializer())
}

func YieldToProtobuf(yield *messages.Yield) ([]byte, error) {
	payload, serializer, err := ToCBORPayload(yield)
	if err != nil {
		return nil, err
	}

	msg := &gen.Yield{
		RequestId:         yield.RequestID(),
		PayloadSerializer: int32(serializer),
		Payload:           payload,
	}

	data, err := proto.Marshal(msg)
	if err != nil {
		return nil, err
	}

	byteValue := byte(messages.MessageTypeYield & 0xFF)
	return append([]byte{byteValue}, data...), nil
}

func ProtobufToYield(data []byte) (*messages.Yield, error) {
	msg := &gen.Yield{}
	err := proto.Unmarshal(data, msg)
	if err != nil {
		return nil, err
	}

	return messages.NewYieldWithFields(NewYieldFields(msg)), nil
}
