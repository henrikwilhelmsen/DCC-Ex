# mobuex

A CLI wrapper for mobu, adding a command that will locate and run the mobu executable. This package has been auto-generated as part of the [dccex project](https://git.hwanimation.tech/hwanimationtech/dccex) to add the versioned mobu specific command.

It adds the following commands: `mobu2024`, `mobupy2024`.

All command-line arguments are passed through to the DCC executable.

## Usage

Install it permanently with `uv tool`:

```sh
uv tool install mobuex-2024
mobu2024
```

Run it once with `uvx` without installing it:

```sh
uvx --from mobuex-2024 mobu2024
```

Or add the package as a dependency and run it from Python:

```sh
uv add mobuex-2024
```

```python
from mobuex_2024 import mobu

mobu()
```

The requested mobu version must be installed locally.

For more information, see the [dccex project](https://git.hwanimation.tech/hwanimationtech/dccex).
