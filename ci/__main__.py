import click
import os
import sys
from subprocess import check_call

cwdir = os.path.dirname(__file__)


@click.group()
def cli():
    pass


@cli.command(name='install')
def install():
    check_call(
        ["python3", "-m", "venv", ".venv"]
    )
    if "win" in sys.platform:
        filename = os.path.join(cwdir, "install-windows.ps1")
        cmd = ["powershell.exe", filename]
    else:
        filename = os.path.join(cwdir, "install-linux.sh")
        cmd = ["bash", filename]
    check_call(cmd)


@cli.command(name='test')
def test():
    check_call(
        ['python', '-m', 'unittest', 'discover']
    )


if __name__ == '__main__':
    cli()
