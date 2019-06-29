from pathlib import Path

from pyignore.config import SAMPLES_DIR
from pyignore.ingore_file import IgnoreFile


class TemplateStore:
    def __init__(self):
        self._templates = {
            f.name.split('.')[0]: IgnoreFile(str(f), f.name)
            for f in Path(SAMPLES_DIR).glob('**/*.gitignore')
            if not f.name.startswith('.')
        }

    @property
    def templates(self):
        return self._templates

    def get_keys(self, filter_key: str = None):
        def callback(k):
            # return k.lower().find(filter_key.lower()) != -1
            return filter_key.lower() in k.lower()

        keys = self._templates.keys()
        return keys if filter_key is None else list(filter(callback, keys))
