package parsers

import (
	"github.com/fxamacker/cbor/v2"
	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type Call struct {
	callGen *gen.Call
}

func NewCallFields(callGen *gen.Call) messages.CallFields {
	return &Call{callGen: callGen}
}

func (c *Call) RequestID() int64 {
	return c.callGen.GetRequestId()
}

func (c *Call) Options() map[string]any {
	return nil
}

func (c *Call) Procedure() string {
	return c.callGen.GetProcedure()
}

func (c *Call) Args() []any {
	return nil
}

func (c *Call) KwArgs() map[string]any {
	return nil
}

func CallToProtobuf(call *messages.Call) ([]byte, error) {
	var payload []any
	payload = append(payload, call.Args())
	payload = append(payload, call.KwArgs())
	payloadData, err := cbor.Marshal(payload)
	if err != nil {
		return nil, err
	}

	msg := &gen.Call{
		RequestId:         call.RequestID(),
		Procedure:         call.Procedure(),
		PayloadSerializer: 1,
		Payload:           payloadData,
	}

	data, err := proto.Marshal(msg)
	if err != nil {
		return nil, err
	}

	byteValue := byte(messages.MessageTypeCall & 0xFF)
	return append([]byte{byteValue}, data...), nil
}

func ProtobufToCall(data []byte) (*messages.Call, error) {
	msg := &gen.Call{}
	err := proto.Unmarshal(data, msg)
	if err != nil {
		return nil, err
	}

	return messages.NewCallWithFields(NewCallFields(msg)), nil
}
