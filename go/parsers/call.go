package parsers

import (
	"log"
	"sync"

	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type Call struct {
	gen *gen.Call

	args   []any
	kwArgs map[string]any
	once   sync.Once
}

func NewCallFields(callGen *gen.Call) messages.CallFields {
	return &Call{gen: callGen}
}

func (c *Call) RequestID() int64 {
	return c.gen.GetRequestId()
}

func (c *Call) Options() map[string]any {
	return map[string]any{}
}

func (c *Call) Procedure() string {
	return c.gen.GetProcedure()
}

func (c *Call) unpack() {
	unpacked, err := FromCBORPayload(c.Payload())
	if err != nil {
		log.Println("error parsing CBOR payload:", err)
	} else {
		c.args = unpacked.Args()
		c.kwArgs = unpacked.KwArgs()
	}
}

func (c *Call) Args() []any {
	c.once.Do(c.unpack)
	return c.args
}

func (c *Call) KwArgs() map[string]any {
	c.once.Do(c.unpack)
	return c.kwArgs
}

func (c *Call) PayloadIsBinary() bool {
	return true
}

func (c *Call) Payload() []byte {
	return c.gen.GetPayload()
}

func (c *Call) PayloadSerializer() int {
	return int(c.gen.GetPayloadSerializer())
}

func CallToProtobuf(call *messages.Call) ([]byte, error) {
	var msg *gen.Call
	if call.PayloadIsBinary() {
		msg = &gen.Call{
			RequestId:         call.RequestID(),
			Procedure:         call.Procedure(),
			PayloadSerializer: int32(call.PayloadSerializer()),
			Payload:           call.Payload(),
		}
	} else {
		payload, serializer, err := ToCBORPayload(call)
		if err != nil {
			return nil, err
		}

		msg = &gen.Call{
			RequestId:         call.RequestID(),
			Procedure:         call.Procedure(),
			PayloadSerializer: int32(serializer),
			Payload:           payload,
		}
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
