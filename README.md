Generate a [Synadia Connect](https://github.com/synadia-io/connect) component with AI!

```
❯ ./main.py generate a nats source component
{
    'model_version': '1.0.0',
    'name': 'nats_source',
    'label': 'NATS Source',
    'kind': <ComponentKind.source: 'source'>,
    'status': <ComponentStatus.stable: 'stable'>,
    'description': 'A source component that pulls data from NATS messaging system.',
    'fields': [
        {
            'path': 'server_url',
            'name': 'Server URL',
            'label': 'NATS Server URL',
            'kind': <FieldKind.scalar: 'scalar'>,
            'type': <FieldType.string: 'string'>,
            'description': 'The URL of the NATS server to connect to.',
            'default': 'nats://localhost:4222'
        },
        {
            'path': 'subject',
            'name': 'Subject',
            'label': 'NATS Subject',
            'kind': <FieldKind.scalar: 'scalar'>,
            'type': <FieldType.string: 'string'>,
            'description': 'The NATS subject to subscribe to for incoming messages.',
            'default': 'my.subject'
        },
        {
            'path': 'queue_group',
            'name': 'Queue Group',
            'label': 'Queue Group',
            'kind': <FieldKind.scalar: 'scalar'>,
            'type': <FieldType.string: 'string'>,
            'description': 'The queue group to use for load balancing among multiple subscribers.',
            'optional': True
        },
        {
            'path': 'durable',
            'name': 'Durable Subscription',
            'label': 'Durable Subscription',
            'kind': <FieldKind.scalar: 'scalar'>,
            'type': <FieldType.bool: 'bool'>,
            'description': 'Whether to create a durable subscription to persist messages.',
            'default': False
        }
    ]
}
```

### Getting started

Set your OpenAI API key, create a virtual environment, install dependencies, and run it.

```shell
echo "OPENAI_API_KEY=__YOUR_OPENAPI_KEY__" > .env 
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install requirements.txt
python3 -m main generate a nats source component
```

To regenerate `model.py`, run `make generate`.

To convert generated schemas from JSON to YAML, run `make convert`.
