package parsers

import (
	"log"
	"sync"

	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type Yield struct {
	gen *gen.Yield

	args   []any
	kwArgs map[string]any
	once   sync.Once
}

func NewYieldFields(gen *gen.Yield) messages.YieldFields {
	return &Yield{gen: gen}
}

func (y *Yield) RequestID() int64 {
	return y.gen.GetRequestId()
}

func (y *Yield) Options() map[string]any {
	return map[string]any{}
}

func (y *Yield) unpack() {
	unpacked, err := FromCBORPayload(y.Payload())
	if err != nil {
		log.Println("error parsing CBOR payload:", err)
	} else {
		y.args = unpacked.Args()
		y.kwArgs = unpacked.KwArgs()
	}
}

func (y *Yield) Args() []any {
	y.once.Do(y.unpack)
	return y.args
}

func (y *Yield) KwArgs() map[string]any {
	y.once.Do(y.unpack)
	return y.kwArgs
}

func (y *Yield) PayloadIsBinary() bool {
	return true
}

func (y *Yield) Payload() []byte {
	return y.gen.GetPayload()
}

func (y *Yield) PayloadSerializer() int {
	return int(y.gen.GetPayloadSerializer())
}

func YieldToProtobuf(yield *messages.Yield) ([]byte, error) {
	var msg *gen.Yield
	if yield.PayloadIsBinary() {
		msg = &gen.Yield{
			RequestId:         yield.RequestID(),
			PayloadSerializer: int32(yield.PayloadSerializer()),
			Payload:           yield.Payload(),
		}
	} else {
		payload, serializer, err := ToCBORPayload(yield)
		if err != nil {
			return nil, err
		}

		msg = &gen.Yield{
			RequestId:         yield.RequestID(),
			PayloadSerializer: int32(serializer),
			Payload:           payload,
		}
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
