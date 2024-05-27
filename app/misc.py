import json
import os


def get_settings() -> dict:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets/settings.json')) as f:
        settings = json.load(f)
    return settings


def save_settings(setting: str, value: str | int) -> None:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets/settings.json'), 'r') as f:
        settings = json.load(f)
        settings[setting] = value
        with open(os.path.dirname(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets/settings.json')),
                  'w') as f_2:
            json.dump(settings, f_2)


def get_emoji():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets/emoji.json'), 'r') as f:
        emoji = json.load(f)
    return emoji
