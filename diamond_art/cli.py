"""Console script for diamond_art."""
import sys

import click

from diamond_art.diamond_art import SymbolError

from . import DiamondArt


@click.command()
@click.argument("input")
@click.argument("output")
def main(input, output):
    """Console script for diamond_art."""
    try:
        painting = DiamondArt(input)
        painting.save(output)
    except SymbolError as err:
        click.echo(err, err=True)
        exit(1)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
