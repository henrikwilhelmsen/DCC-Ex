# {{ NAME }}

A CLI wrapper for {{ DCC }}, adding a command that will locate and run the {{ DCC }} executable. This package has been auto-generated as part of the [dccex project](https://git.hwanimation.tech/hwanimationtech/dccex) to add the versioned {{ DCC }} specific command.

It adds the following commands: {{ VERSIONED_CMDS }}.

All command-line arguments are passed through to the DCC executable.

## Usage

Install it permanently with `uv tool`:

```sh
uv tool install {{ VERSIONED_NAME }}
{{ EXAMPLE_CMD }}
```

Run it once with `uvx` without installing it:

```sh
uvx --from {{ VERSIONED_NAME }} {{ EXAMPLE_CMD }}
```

Or add the package as a dependency and run it from Python:

```sh
uv add {{ VERSIONED_NAME }}
```

```python
from {{ SRC_NAME }} import {{ CMD }}

{{ CMD }}()
```

The requested {{ DCC }} version must be installed locally.

For more information, see the [dccex project](https://git.hwanimation.tech/hwanimationtech/dccex).
