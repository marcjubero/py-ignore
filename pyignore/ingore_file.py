import os


class IgnoreFile:
    def __init__(self, path: str = None, name: str = None):
        if not os.path.isfile(path):
            raise Exception('Invalid .gitignore file path')

        self._name = name or path.split('/')[-1]

        with open(path, 'r') as fd:
            self._lines = dict.fromkeys(fd.readlines())

    @property
    def name(self):
        return self._name

    @property
    def lines(self):
        return self._lines

    def write(self, path: str = None):
        path = path or '.gitignore'
        with open(path, 'w') as fd:
            _ = [fd.write(line) for line in self._lines.keys()]

    # TODO 2019-06-29 create class constuctor from other classes
    # @classmethod
    # def from_files(cls, files: List['IgnoreFile']):
    #    f = cls()
    #    return f
