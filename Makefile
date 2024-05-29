clean:
	rm -rf python/wampprotobuf/gen
	rm -rf go/gen

gen-py:
	rm -rf python/wampprotobuf/gen
	mkdir -p python/wampprotobuf/gen
	protoc protobuf/*.proto --python_out=python/wampprotobuf/gen --pyi_out=python/wampprotobuf/gen
	mv python/wampprotobuf/gen/protobuf/* python/wampprotobuf/gen/
	rm -r python/wampprotobuf/gen/protobuf
	touch python/wampprotobuf/gen/__init__.py

gen-go:
	rm -rf go/gen
	mkdir -p go/gen
	for file in protobuf/*.proto; do protoc --go_out=go --go_opt=M$$file=/gen $$file; done

gen: gen-py gen-go
