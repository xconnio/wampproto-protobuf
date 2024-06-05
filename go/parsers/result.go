package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type resultFields struct {
	gen *gen.Result
}

func NewResultFields(gen *gen.Result) messages.ResultFields {
	return &resultFields{gen: gen}
}

func (r *resultFields) RequestID() int64 {
	return r.gen.GetRequestId()
}

func (r *resultFields) Details() map[string]any {
	return nil
}

func (r *resultFields) Args() []any {
	return nil
}

func (r *resultFields) KwArgs() map[string]any {
	return nil
}

func (r *resultFields) PayloadIsBinary() bool {
	return true
}

func (r *resultFields) Payload() []byte {
	return r.gen.GetPayload()
}

func (r *resultFields) PayloadSerializer() int {
	return int(r.gen.GetPayloadSerializer())
}

func ResultToProtobuf(result *messages.Result) ([]byte, error) {
	payload, serializer, err := ToCBORPayload(result)
	if err != nil {
		return nil, err
	}

	msg := &gen.Yield{
		RequestId:         result.RequestID(),
		PayloadSerializer: int32(serializer),
		Payload:           payload,
	}

	data, err := proto.Marshal(msg)
	if err != nil {
		return nil, err
	}

	byteValue := byte(messages.MessageTypeResult & 0xFF)
	return append([]byte{byteValue}, data...), nil
}

func ProtobufToResult(data []byte) (*messages.Result, error) {
	msg := &gen.Result{}
	err := proto.Unmarshal(data, msg)
	if err != nil {
		return nil, err
	}

	return messages.NewResultWithFields(NewResultFields(msg)), nil
}
