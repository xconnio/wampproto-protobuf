package parsers

import (
	"github.com/fxamacker/cbor/v2"
)

type ArgsKwArgs interface {
	Args() []any
	KwArgs() map[string]any
}

func ToCBORPayload(data ArgsKwArgs) ([]byte, int, error) {
	var payload []any
	payload = append(payload, data.Args())
	payload = append(payload, data.KwArgs())
	payloadData, err := cbor.Marshal(payload)
	if err != nil {
		return nil, 0, err
	}

	return payloadData, 1, nil
}
