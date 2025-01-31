import dataclasses
import json
import sys

from pydantic_ai import Agent, UnexpectedModelBehavior, capture_run_messages
from pydantic_ai.models.openai import OpenAIModel

import model

# gpt-3.5-turbo
# gpt-4o-mini
ai_model = OpenAIModel("gpt-4o-mini")

agent = Agent(ai_model, result_type=model.SynadiaConnectComponent)

if __name__ == "__main__":
    # print(result.usage())
    with capture_run_messages() as messages:
        try:
            result = agent.run_sync("Configure an RSS feed sink component")
        except UnexpectedModelBehavior:
            for message in messages:
                json.dump(
                    dataclasses.asdict(message), sys.stdout, indent=4, default=str
                )
            sys.exit(1)

    print(repr(result.data))

    # Save generated model to file
    model_json = result.data.model_dump_json(
        indent=4, exclude_none=True, exclude_unset=True
    )
    kind = result.data.kind.value
    component_name = result.data.name.replace(" ", "_").casefold()
    filepath = f".connect/{kind}s/{component_name}.json"
    with open(filepath, "w") as fout:
        fout.write(model_json)
