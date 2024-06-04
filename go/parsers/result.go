package parsers

import (
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type resultFields struct {
	resultGen *gen.Result
}

func NewResultFields(gen *gen.Result) messages.ResultFields {
	return &resultFields{resultGen: gen}
}

func (r *resultFields) RequestID() int64 {
	return r.resultGen.GetRequestId()
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

func ResultToProtobuf(result *messages.Result) ([]byte, error) {
	msg := &gen.Call{
		RequestId:         result.RequestID(),
		PayloadSerializer: 1,
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
