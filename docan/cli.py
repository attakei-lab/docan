"""CLI procedure."""
import click

from . import __version__


@click.group()
def cli():  # noqa: D103
    pass


@cli.command()
def version():
    """Display package version."""
    click.echo(f"{__package__} v{__version__}")


def main():
    """Entrypoint for CLI."""
    cli()
