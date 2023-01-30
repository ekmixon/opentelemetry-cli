import sys
import time
from datetime import datetime


PY36 = sys.version_info[:2] == (3, 6)


def time_ns():
    if not PY36:
        return time.time_ns()
    now = datetime.now()
    return int(now.timestamp() * 1e9)
