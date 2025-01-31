#!/usr/bin/env python3
import dataclasses
import functools
import json
import subprocess
import sys

from pydantic_ai import Agent, UnexpectedModelBehavior, capture_run_messages
from pydantic_ai.models.openai import OpenAIModel
from rich.pretty import pprint

from . import model

pprint = functools.partial(pprint, indent_guides=False)

# gpt-3.5-turbo
# gpt-4o-mini
ai_model = OpenAIModel("gpt-4o-mini")

agent = Agent(ai_model, result_type=model.SynadiaConnectComponent)


def main():
    user_prompt = " ".join(sys.argv[1:]).strip()
    if user_prompt == "":
        cmd = sys.argv[0]
        if not cmd.startswith("./"):
            cmd = f"python3 {cmd}"
        print(
            f"usage: {cmd} <user prompt>\n\n  Example: {cmd} Configure an RSS feed sink component"
        )
        exit(1)

    with capture_run_messages() as messages:
        try:
            result = agent.run_sync(user_prompt)
        except UnexpectedModelBehavior:
            for message in messages:
                json.dump(
                    dataclasses.asdict(message), sys.stdout, indent=4, default=str
                )
            sys.exit(1)

    pprint(result.data.model_dump(exclude_none=True, exclude_unset=True))

    # Save generated model to file
    model_json = result.data.model_dump_json(
        indent=4, exclude_none=True, exclude_unset=True
    )
    kind = result.data.kind.value
    component_name = result.data.name.replace(" ", "_").casefold()
    filepath = f"../.connect/{kind}s/{component_name}.json"
    with open(filepath, "w") as fout:
        fout.write(model_json)

    subprocess.call(["make", "convert"])


if __name__ == "__main__":
    main()
