package parsers

import (
	"log"
	"sync"

	"google.golang.org/protobuf/proto"

	"github.com/xconnio/wampproto-go/messages"
	"github.com/xconnio/wampproto-protobuf/go/gen"
)

type Error struct {
	gen *gen.Error

	args   []any
	kwArgs map[string]any
	once   sync.Once
}

func NewErrorFields(gen *gen.Error) messages.ErrorFields {
	return &Error{gen: gen}
}

func (e *Error) MessageType() int64 {
	return e.gen.MessageType
}

func (e *Error) RequestID() int64 {
	return e.gen.RequestId
}

func (e *Error) Details() map[string]any {
	return map[string]any{}
}

func (e *Error) URI() string {
	return e.gen.Uri
}

func (e *Error) unpack() {
	unpacked, err := FromCBORPayload(e.Payload())
	if err != nil {
		log.Println("error parsing CBOR payload:", err)
	} else {
		e.args = unpacked.Args()
		e.kwArgs = unpacked.KwArgs()
	}
}

func (e *Error) Args() []any {
	e.once.Do(e.unpack)
	return e.args
}

func (e *Error) KwArgs() map[string]any {
	e.once.Do(e.unpack)
	return e.kwArgs
}

func (e *Error) PayloadIsBinary() bool {
	return true
}

func (e *Error) Payload() []byte {
	return e.gen.GetPayload()
}

func (e *Error) PayloadSerializer() int {
	return int(e.gen.GetPayloadSerializer())
}

func ErrorToProtobuf(error *messages.Error) ([]byte, error) {
	var msg *gen.Error
	if error.PayloadIsBinary() {
		msg = &gen.Error{
			MessageType:       error.MessageType(),
			RequestId:         error.RequestID(),
			Uri:               error.URI(),
			PayloadSerializer: int32(error.PayloadSerializer()),
			Payload:           error.Payload(),
		}
	} else {
		payload, serializer, err := ToCBORPayload(error)
		if err != nil {
			return nil, err
		}

		msg = &gen.Error{
			MessageType:       error.MessageType(),
			RequestId:         error.RequestID(),
			Uri:               error.URI(),
			PayloadSerializer: int32(serializer),
			Payload:           payload,
		}
	}

	data, err := proto.Marshal(msg)
	if err != nil {
		return nil, err
	}

	byteValue := byte(messages.MessageTypeError & 0xFF)
	return append([]byte{byteValue}, data...), nil
}

func ProtobufToError(data []byte) (*messages.Error, error) {
	msg := &gen.Error{}
	err := proto.Unmarshal(data, msg)
	if err != nil {
		return nil, err
	}

	return messages.NewErrorWithFields(NewErrorFields(msg)), nil
}
