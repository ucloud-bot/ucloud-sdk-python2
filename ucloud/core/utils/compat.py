# -*- coding: utf-8 -*-

import sys

PY3 = sys.version_info[0] == 3
if PY3:
    str = str
    string_types = (str,)
    from collections.abc import Callable
else:
    import types

    str = unicode
    string_types = types.StringTypes
    from collections import Callable
