"""Console script for gem_painting."""
import sys
import click

from gem_painting.gem_painting import SymbolError
from . import GemPainting


@click.command()
@click.argument("input")
@click.argument("output")
def main(input, output):
    """Console script for gem_painting."""
    try:
        painting = GemPainting(input)
        painting.save(output)
    except SymbolError as err:
        click.echo(err, err=True)
        exit(1)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
