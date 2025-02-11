"""Console script for diamond_art."""
import sys

import click

from diamond_art.diamond_art import SymbolError

from . import DiamondArt


@click.command()
@click.argument("input")
@click.argument("output")
@click.option(
    "-d",
    "--dpi",
    help=(
        "Approximate resolution of the output image (in pixels per inch). The exact "
        "resolution will differ slightly to preserve pixel boundaries."
    ),
    default=300,
)
@click.option(
    "-g",
    "--g_size",
    help=(
        "gem size (in mm). The exact "
        "gemsize wil vary if printed."
    ),
    default=2.5,
)
def main(input, output, g_size, dpi):
    """Console script for diamond_art."""
    try:
        painting = DiamondArt(input, gem_size=g_size, target_dpi=dpi)
        painting.save(output)
    except SymbolError as err:
        click.echo(err, err=True)
        exit(1)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
