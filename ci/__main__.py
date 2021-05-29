import click
import os
import sys
from subprocess import check_call, run


@click.group()
def cli():
    pass


@cli.command(name='install')
def install():
    check_call(
        ["python3", "-m", "venv", ".venv"]
    )
    if "win" in sys.platform:
        cmd = ["ci\install-windows.ps1"]
    else:
        cmd = ["bash", "ci/install-linux.sh"]
    check_call(cmd)


if __name__ == '__main__':
    cli()
