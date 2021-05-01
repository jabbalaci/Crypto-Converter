import shlex
import sys
from subprocess import PIPE, STDOUT, Popen


def get_platform() -> str:
    text = sys.platform
    if text.startswith("linux"):
        return "linux"
    if text.startswith("win"):
        return "windows"
    # else
    # raise RuntimeError("unknown platform")
    return "else"


def get_simple_cmd_output(cmd: str, stderr=STDOUT) -> str:
    args = shlex.split(cmd)
    return Popen(args, stdout=PIPE, stderr=stderr).communicate()[0].decode("utf8")
