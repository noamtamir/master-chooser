# Master chooser
A simple way to randomly choose 1 person from a group in a fair way, so that no one gets chosen more than once before the cycle finishes.

## Dependencies
- pyenv (`brew install pyenv`)
- python 3.11 (`pyenv install 3.11`)
- poetry (https://python-poetry.org/docs/#installation)
- make (`brew install make`)

## Setup
- `make venv`
- `source .venv/bin/activate` - Activate virtual environment
- `make install`
    - `poetry install --no-root` - install dependecies
- Create `master_chooser/storage/DEVS.yml` file with a list of devs to choose from. Example file: `master_chooser/storage/DEVS.example.yml`
- File names may be configured in `constants.py`

## Run
- `make run`
    - `poetry run main.py`