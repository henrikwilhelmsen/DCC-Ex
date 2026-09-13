# List available recipes
default:
    @just --list

# Sync all packages
sync:
    uv sync --dev --all-packages

# Lint with ruff and ty
lint:
    uv run ruff check
    uv run ruff format --diff
    uv run ty check

# Generate all of the version specific packages
gen:
    uv run scripts/gen_pkgs.py
