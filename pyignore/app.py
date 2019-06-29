import click

from pyignore.config import APP_NAME, APP_VERSION
from pyignore.template_store import TemplateStore


@click.command()
@click.version_option(version=APP_VERSION, prog_name=APP_NAME)
@click.argument('args', nargs=-1)
def main(args: tuple):
    store = TemplateStore()
    keys = store.get_keys(args[0])
    if len(keys) == 1:
        f = store.templates.get(keys[0])
        f.write()


if __name__ == '__main__':
    main()
