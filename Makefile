generate:
	curl -fsSL https://raw.githubusercontent.com/synadia-io/connect/main/schemas/component.json -o component.json
	pipx run datamodel-code-generator --input component.json --input-file-type jsonschema --output model.py

convert:
	./convert.sh
