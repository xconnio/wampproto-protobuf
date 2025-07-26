package parsers

import (
	"log"
	"sync"

	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type Abort struct {
	gen *gen.Abort

	args   []any
	kwArgs map[string]any
	once   sync.Once
}

func NewAbortFields(gen *gen.Abort) messages.AbortFields {
	return &Abort{gen: gen}
}

func (a *Abort) Details() map[string]any {
	return map[string]any{}
}

func (a *Abort) Reason() string {
	return a.gen.Reason
}

func (a *Abort) unpack() {
	unpacked, err := FromCBORPayload(a.gen.GetPayload())
	if err != nil {
		log.Println("error parsing CBOR payload:", err)
	} else {
		a.args = unpacked.Args()
		a.kwArgs = unpacked.KwArgs()
	}
}

func (a *Abort) Args() []any {
	a.once.Do(a.unpack)
	return a.args
}

func (a *Abort) KwArgs() map[string]any {
	a.once.Do(a.unpack)
	return a.kwArgs
}

func AbortToProtobuf(abort *messages.Abort) ([]byte, error) {
	payload, serializer, err := ToCBORPayload(abort)
	if err != nil {
		return nil, err
	}

	msg := &gen.Abort{
		Reason:            abort.Reason(),
		PayloadSerializer: serializer,
		Payload:           payload,
	}

	data, err := proto.Marshal(msg)
	if err != nil {
		return nil, err
	}

	byteValue := byte(messages.MessageTypeAbort & 0xFF)
	return append([]byte{byteValue}, data...), nil
}

func ProtobufToAbort(data []byte) (*messages.Abort, error) {
	msg := &gen.Abort{}
	err := proto.Unmarshal(data, msg)
	if err != nil {
		return nil, err
	}

	return messages.NewAbortWithFields(NewAbortFields(msg)), nil
}
