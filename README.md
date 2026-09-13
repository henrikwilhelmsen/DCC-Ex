# dccex

`dccex` locates installed Digital Content Creation (DCC) applications and runs
them with the arguments you provide.

Version-specific packages expose commands such as `blender5` and `maya2026`, making it easy to select a DCC version in shell scripts, CI, and project tooling.

See [the packages directory](./packages) for which versioned packages are available.

## Command-line usage

### uv tool

Install a version-specific package once with `uv tool`:

```sh
uv tool install blenderex-5
blender5
```

```sh
uv tool install mayaex-2026
mayapy2026 --version
```

### uvx

Use `uvx` to run the command once without installing. `--from` selects
the package while the final command is the generated DCC command:

```sh
uvx --from blenderex-5 blender5
```

```sh
uvx --from mayaex-2026 mayapy2026 --version
```

### uvx.sh

For a one-line install without requiring `uv`, [uvx.sh](https://uvx.sh/) can be used:

MacOS/Linux:

```sh
curl -LsSf uvx.sh/mayaex-2026/install.sh | sh
```

Windows:

```sh
powershell -ExecutionPolicy ByPass -c "irm https://uvx.sh/mayaex-2026/install.ps1 | iex"
```

## Library usage

Add the core package to a Python project, then call `call_dcc_exe` with the
executable name and required DCC version. It returns the launched process's
exit code, or `1` when the executable cannot be located.

Install with `uv`:

```sh
uv add dccex
```

Or with `pip`:

```sh
pip install dccex
```

### Example

```python
import sys

from dccex import call_dcc_exe

exit_code = call_dcc_exe(dcc_exe="blender", version="5", args=["--version"])
sys.exit(exit_code)
```

The supported executable names are `"blender"`, `"maya"`, `"mayapy"`,
`"mobu"`, and `"mobupy"`.

## Development

The version-specific packages are generated from `scripts/data/pkgs.json`:

```sh
uv run scripts/gen_pkgs.py
```

Do not edit files under `packages/` directly; update the templates or package
data and regenerate them instead.

## License

`dccex` is licensed under the [Mozilla Public License 2.0](LICENSE).
