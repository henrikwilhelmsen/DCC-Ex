# Copyright (C) 2026 Henrik Wilhelmsen.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at <https://mozilla.org/MPL/2.0/>.

"""Generate the DCC version specific packages from `./pkgs.json`."""

# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

import json
import logging
import shutil
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)
logging.basicConfig(
    level="DEBUG",
    format="%(levelname)s: %(message)s",
)

REPO_ROOT_DIR = (Path(__file__).parent.parent).resolve()
SCRIPTS_DATA_DIR = (Path(__file__).parent / "data").resolve()


@dataclass
class Package:
    """Dataclass representing a package to generate."""

    # The package name used for the top level package dir.
    name: str
    # The package version, NOT the DCC version. Used in the pyproject.toml.
    pkg_version: str
    # The DCC version, used to locate the DCC executable
    dcc_version: str
    # The DCC this package launches.
    dcc: str
    # The name of the commands this package exposes.
    cmds: list[str]

    @property
    def versioned_name(self) -> str:
        """Get the package name with the version appended, with - as a separator."""
        return f"{self.name}-{self.dcc_version}"

    @property
    def src_name(self) -> str:
        """Get the name of the Python package name, with . and - replaced with _."""
        return self.versioned_name.replace("-", "_").replace(".", "_")

    @property
    def versioned_cmds(self) -> list[str]:
        """Get a cmds list with dcc_version added to the end of each cmd.

        For use with CLI args, there are no separators e.g. for Blender 5.0 the property
        will return blender5.0
        """
        return [f"{cmd}{self.dcc_version}" for cmd in self.cmds]


@dataclass
class PackagePaths:
    """Dataclass representing all of the files in a generated package."""

    # The top-level package dir
    pkg_dir: Path
    # The src/<package> dir
    src_pkg_dir: Path
    # The package README file
    readme_file: Path
    # The package LICENSE file
    license_file: Path
    # The package pyproject.toml file
    pyproject_file: Path
    # The package __init__.py file
    init_file: Path


def get_pkgs() -> list[Package]:
    """Get all the packages from the pkgs.json file."""
    pkgs_json = Path(__file__).parent / "data" / "pkgs.json"
    json_data = json.loads(pkgs_json.read_text())
    return [
        Package(
            name=pkg_data["name"],
            pkg_version=pkg_data["pkg_version"],
            dcc_version=pkg_data["dcc_version"],
            dcc=pkg_data["dcc"],
            cmds=pkg_data["cmds"],
        )
        for pkg_data in json_data["packages"]
    ]


def get_package_paths(pkg: Package) -> PackagePaths:
    """Create a PackagePaths instance from the given package."""
    repo_root_dir = (Path(__file__).parent.parent).resolve()
    pkg_dir = repo_root_dir / "packages" / pkg.versioned_name
    src_pkg_dir = pkg_dir / "src" / pkg.src_name

    return PackagePaths(
        pkg_dir=pkg_dir,
        src_pkg_dir=src_pkg_dir,
        readme_file=pkg_dir / "README.md",
        license_file=pkg_dir / "LICENSE",
        pyproject_file=pkg_dir / "pyproject.toml",
        init_file=src_pkg_dir / "__init__.py",
    )


def replace_template_text_variables(pkg: Package, txt: str) -> str:
    """Replace {{ VAR_NAME }} variables in the given text with package attributes.

    E.g. {{ NAME }} will be replaces with `pkg.name`, {{ DCC }} is replaced
    by pkg.dcc etc.
    """
    txt = txt.replace("{{ NAME }}", pkg.name)
    txt = txt.replace("{{ VERSIONED_NAME }}", pkg.versioned_name)
    txt = txt.replace("{{ SRC_NAME }}", pkg.src_name)
    txt = txt.replace("{{ PKG_VERSION }}", pkg.pkg_version)
    txt = txt.replace("{{ DCC_VERSION }}", pkg.dcc_version)
    txt = txt.replace("{{ DCC }}", pkg.dcc)
    txt = txt.replace("{{ SRC_NAME }}", pkg.src_name)
    txt = txt.replace(
        "{{ VERSIONED_CMDS }}",
        ", ".join(f"`{cmd}`" for cmd in pkg.versioned_cmds),
    )
    return txt.replace("{{ DCC_VERSION }}", pkg.dcc_version)


def write_pkg_pyproject_toml_file(pkg: Package, pyproject_file: Path) -> None:
    """Write the pyproject.toml file for the package.

    Writes to the pyproject_file directly, assumes that the file has already
    been created.
    """
    # Load the template data and replace variables
    tmpl_data = (SCRIPTS_DATA_DIR / "pyproject.toml.tmpl").read_text()
    tmpl_data = replace_template_text_variables(
        pkg=pkg,
        txt=tmpl_data,
    )
    # Create the project scripts entry
    scripts_line = "[project.scripts]"
    all_data = [tmpl_data, scripts_line]

    # Fill in the project scripts entry points
    for cmd in pkg.cmds:
        cmd_line = f'"{cmd}{pkg.dcc_version}" = "{pkg.src_name}:{cmd}"'
        all_data.append(cmd_line)

    # Add newline to keep linters happy
    all_data.append("")

    # Write the data to file
    pyproject_file.write_text("\n".join(all_data))


def write_pkg_init_file(pkg: Package, init_file: Path) -> None:
    """Write the __init__.py file for the package.

    Writes to the init_file directly, assumes that the file has already
    been created.
    """
    # Load the template data and replace variables
    tmpl_data = (SCRIPTS_DATA_DIR / "__init__.py.tmpl").read_text()
    tmpl_data = replace_template_text_variables(pkg=pkg, txt=tmpl_data)
    all_init_data = [tmpl_data]

    # Create the function to run each command
    cmd_fn_tmpl = '''
def {{ CMD }}() -> None:
    """Run {{ CMD }}."""
    setup_logging()
    sys.exit(call_dcc_exe(dcc_exe="{{ CMD }}", version="{{ VERSION }}"))
'''
    for cmd in pkg.cmds:
        cmd_fn = cmd_fn_tmpl.replace("{{ CMD }}", cmd)
        cmd_fn = cmd_fn.replace("{{ VERSION }}", pkg.dcc_version)
        all_init_data.append(cmd_fn)

    init_file.write_text("\n".join(all_init_data))


def write_pkg_readme_file(pkg: Package, readme_file: Path) -> None:
    """Write the README.md file for the package.

    Writes to the readme_file directly, assumes that the file has already
    been created.
    """
    tmpl_data = (SCRIPTS_DATA_DIR / "README.md").read_text()
    tmpl_data = replace_template_text_variables(pkg=pkg, txt=tmpl_data)

    # Versioned commands are used in the command-line examples
    tmpl_data = tmpl_data.replace("{{ EXAMPLE_CMD }}", pkg.versioned_cmds[0])
    # The regular, non-versioned command is used in the Python examples
    tmpl_data = tmpl_data.replace("{{ CMD }}", pkg.cmds[0])

    readme_file.write_text(tmpl_data)


def create_pkg_files(pkg: Package) -> None:
    """Create all the files for the given package."""
    # Get package paths and remove existing package dir
    pkg_paths = get_package_paths(pkg=pkg)
    if pkg_paths.pkg_dir.exists():
        shutil.rmtree(pkg_paths.pkg_dir)

    # Create package files
    pkg_paths.pkg_dir.mkdir(parents=True)
    pkg_paths.src_pkg_dir.mkdir(parents=True)
    for f in (pkg_paths.readme_file, pkg_paths.pyproject_file, pkg_paths.init_file):
        f.touch()

    # Copy license to pkg dir
    src_license_file = REPO_ROOT_DIR / "LICENSE"
    shutil.copy2(src_license_file, pkg_paths.license_file)

    # Write the contents of the package files
    write_pkg_pyproject_toml_file(pkg=pkg, pyproject_file=pkg_paths.pyproject_file)
    write_pkg_init_file(pkg=pkg, init_file=pkg_paths.init_file)
    write_pkg_readme_file(pkg=pkg, readme_file=pkg_paths.readme_file)


def main() -> None:
    """Run the package generation."""
    packages = get_pkgs()
    for pkg in packages:
        create_pkg_files(pkg)
        logger.info("Created package: %s", pkg)


if __name__ == "__main__":
    main()
