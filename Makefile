clean:
	rm -rf python/wampprotobuf/gen

gen-py:
	rm -rf python/wampprotobuf/gen
	mkdir python/wampprotobuf/gen -p
	protoc protobuf/*.proto --python_out=python/wampprotobuf/gen
	mv python/wampprotobuf/gen/protobuf/* python/wampprotobuf/gen/
	rm -r python/wampprotobuf/gen/protobuf
	touch python/wampprotobuf/gen/__init__.py
