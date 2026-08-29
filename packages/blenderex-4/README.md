# blenderex

A CLI wrapper for blender, adding a command that will locate and run the blender executable. This package has been auto-generated as part of the [dccex project](https://git.hwanimation.tech/hwanimationtech/dccex) to add the versioned blender specific command.

It adds the following commands: `blender4`.

All command-line arguments are passed through to the DCC executable.

## Usage

Install it permanently with `uv tool`:

```sh
uv tool install blenderex-4
blender4
```

Run it once with `uvx` without installing it:

```sh
uvx --from blenderex-4 blender4
```

Or add the package as a dependency and run it from Python:

```sh
uv add blenderex-4
```

```python
from blenderex_4 import blender4

blender4()
```

The requested blender version must be installed locally.

For more information, see the [dccex project](https://git.hwanimation.tech/hwanimationtech/dccex).
