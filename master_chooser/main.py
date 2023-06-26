import random
import yaml
import master_chooser.constants as c
from pathlib import Path


def main():
    remaining_devs = load_devs(c.REMAINING_DEVS_FILENAME)
    if not remaining_devs:
        remaining_devs = load_devs(c.DEVS_FILENAME)

    dev, remaining_devs = choose_master(remaining_devs)
    save_remaining_devs(remaining_devs)
    save_current_dev(dev)
    print(dev)


def load_devs(filename: Path) -> list[str] | None:
    try:
        with open(filename, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        with open(filename, 'x'):
            return None


def choose_master(remaining_devs: list[str]):
    dev = random.choice(remaining_devs)
    remaining_devs.remove(dev)
    return dev, remaining_devs


def save_remaining_devs(remaining_devs: list[str]):
    with open(c.REMAINING_DEVS_FILENAME, 'w') as f:
        yaml.dump(remaining_devs, f)


def save_current_dev(dev: str):
    with open(c.CURRENT_DEV_FILENAME, 'w') as f:
        f.write(dev)


if __name__ == '__main__':
    main()
