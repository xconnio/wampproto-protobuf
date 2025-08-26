package parsers

type ArgsKwArgs interface {
	Args() []any
	KwArgs() map[string]any
}
