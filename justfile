# List available recipes
default:
    @just --list

sync:
    uv sync --dev --all-packages

lint:
    uv run ruff check
    uv run ruff format --diff
    uv run ty check
