#!/usr/bin/env bash
set -eu -o pipefail

for file in ".connect"/*/*".json"; do
  if [ -f "$file" ]; then
    BASE_FILE=$(echo "$file" | cut -d '.' -f -2)
    YAML_FILE="$BASE_FILE.yml"
    cat "$file" | yq -P > "$YAML_FILE"
  fi
done
