# mayaex

A CLI wrapper for maya, adding a command that will locate and run the maya executable. This package has been auto-generated as part of the [dccex project](https://git.hwanimation.tech/hwanimationtech/dccex) to add the versioned maya specific command.

It adds the following commands: `maya2025`, `mayapy2025`.

All command-line arguments are passed through to the DCC executable.

## Usage

Install it permanently with `uv tool`:

```sh
uv tool install mayaex-2025
maya2025
```

Run it once with `uvx` without installing it:

```sh
uvx --from mayaex-2025 maya2025
```

Or add the package as a dependency and run it from Python:

```sh
uv add mayaex-2025
```

```python
from mayaex_2025 import maya2025

maya2025()
```

The requested maya version must be installed locally.

For more information, see the [dccex project](https://git.hwanimation.tech/hwanimationtech/dccex).
