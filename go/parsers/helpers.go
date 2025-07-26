package parsers

import (
	"fmt"

	"github.com/fxamacker/cbor/v2"
)

type ArgsKwArgs interface {
	Args() []any
	KwArgs() map[string]any
}

type argsKwArgs struct {
	args   []any
	kwArgs map[string]any
}

func (a *argsKwArgs) Args() []any {
	return a.args
}

func (a *argsKwArgs) KwArgs() map[string]any {
	return a.kwArgs
}

func ToCBORPayload(data ArgsKwArgs) ([]byte, uint64, error) {
	var payload []any
	payload = append(payload, data.Args())
	payload = append(payload, data.KwArgs())
	payloadData, err := cbor.Marshal(payload)
	if err != nil {
		return nil, 0, err
	}

	return payloadData, 1, nil
}

func FromCBORPayload(data []byte) (ArgsKwArgs, error) {
	var payload []any
	if err := cbor.Unmarshal(data, &payload); err != nil {
		return nil, fmt.Errorf("failed to unmarshal cbor payload: %w", err)
	}

	result := &argsKwArgs{}

	args, ok := payload[0].([]any)
	if ok {
		result.args = args
	}

	kwArgs, ok := payload[1].(map[string]any)
	if ok {
		result.kwArgs = kwArgs
	}

	return result, nil
}
