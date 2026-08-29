# dccex

`dccex` locates installed Digital Content Creation (DCC) applications and runs
them with the arguments you provide.

Version-specific companion packages expose
commands such as `blender5` and `maya2026`, making it practical to select a DCC
version in shell scripts, CI, and project tooling.

See [the packages directory](./packages) for which versioned packages are available.

## Command-line usage

### uv tool

Install a version-specific package once to add its command to the `uv` tools
bin directory (make sure it is on your `PATH` with `uv tool update-shell`):

```sh
uv tool install blenderex-5
blender5
```

For example, install Maya 2026 and invoke its bundled Python interpreter:

```sh
uv tool install mayaex-2026
mayapy2026 --version
```

### uvx

Use `uvx` when you do not want to keep the command installed. `--from` selects
the package while the final command is the generated DCC command:

```sh
uvx --from blenderex-5 blender5
uvx --from mayaex-2026 mayapy2026 --version
```

### pixi

Run a version-specific command without adding it to a `pixi.toml` by supplying
the package as an execution specification:

```sh
pixi exec --spec blenderex-5 blender5
pixi exec --spec mayaex-2026 mayapy2026 --version
```

## Library usage

Add the core package to a Python project, then call `call_dcc_exe` with the
executable name and required DCC version. It returns the launched process's
exit code, or `1` when the executable cannot be located.

```sh
uv add dccex
```

```python
import sys

from dccex import call_dcc_exe

exit_code = call_dcc_exe(dcc_exe="blender", version="5")
sys.exit(exit_code)
```

The supported executable names are `"blender"`, `"maya"`, `"mayapy"`,
`"mobu"`, and `"mobupy"`. Arguments are read from `sys.argv[1:]`, so a
library wrapper can set up its own command-line interface before calling
`call_dcc_exe`.

## Development

The version-specific packages are generated from `scripts/data/pkgs.json`:

```sh
uv run scripts/gen_pkgs.py
```

Do not edit files under `packages/` directly; update the templates or package
data and regenerate them instead.

## License

`dccex` is licensed under the [Mozilla Public License 2.0](LICENSE).
