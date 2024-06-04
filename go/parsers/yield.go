package parsers

import (
	"github.com/fxamacker/cbor/v2"
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type yieldFields struct {
	resultGen *gen.Yield
}

func NewYieldFields(gen *gen.Yield) messages.YieldFields {
	return &yieldFields{resultGen: gen}
}

func (r *yieldFields) RequestID() int64 {
	return r.resultGen.GetRequestId()
}

func (r *yieldFields) Options() map[string]any {
	return nil
}

func (r *yieldFields) Args() []any {
	return nil
}

func (r *yieldFields) KwArgs() map[string]any {
	return nil
}

func YieldToProtobuf(yield *messages.Yield) ([]byte, error) {
	var payload []any
	payload = append(payload, yield.Args())
	payload = append(payload, yield.KwArgs())
	payloadData, err := cbor.Marshal(payload)
	if err != nil {
		return nil, err
	}

	msg := &gen.Yield{
		RequestId:         yield.RequestID(),
		PayloadSerializer: 1,
		Payload:           payloadData,
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
