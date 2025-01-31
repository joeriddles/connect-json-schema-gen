### Getting started

Set your OpenAI API key, create a virtual environment, install dependencies, and run it.

```shell
echo "OPENAI_API_KEY=__YOUR_OPENAPI_KEY__" > .env 
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install requirements.txt
python3 -m main
```

To regenerate `model.py` run `make generate`.
