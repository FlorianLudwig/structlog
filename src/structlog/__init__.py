# SPDX-License-Identifier: MIT OR Apache-2.0
# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the MIT License.  See the LICENSE file in the root of this
# repository for complete details.

"""
Structured Logging for Python
"""

from structlog import (
    contextvars,
    dev,
    processors,
    stdlib,
    testing,
    threadlocal,
    types,
)
from structlog._base import BoundLoggerBase, get_context
from structlog._config import (
    configure,
    configure_once,
    get_config,
    get_logger,
    getLogger,
    is_configured,
    reset_defaults,
    wrap_logger,
)
from structlog._generic import BoundLogger
from structlog._log_levels import make_filtering_bound_logger
from structlog._loggers import (
    BytesLogger,
    BytesLoggerFactory,
    PrintLogger,
    PrintLoggerFactory,
    WriteLogger,
    WriteLoggerFactory,
)
from structlog.exceptions import DropEvent
from structlog.testing import ReturnLogger, ReturnLoggerFactory


try:
    from structlog import twisted
except ImportError:
    twisted = None  # type: ignore


__version__ = "22.1.0.dev0"

__title__ = "structlog"
# __doc__ is None when running with PYTHONOPTIMIZE=2 / -OO
__description__ = (__doc__ or "").strip()

__uri__ = "https://www.structlog.org/"

__author__ = "Hynek Schlawack"
__email__ = "hs@ox.cx"

__license__ = "MIT or Apache License, Version 2.0"
__copyright__ = "Copyright (c) 2013 " + __author__


__all__ = [
    "BoundLogger",
    "BoundLoggerBase",
    "BytesLogger",
    "BytesLoggerFactory",
    "configure_once",
    "configure",
    "contextvars",
    "dev",
    "DropEvent",
    "get_config",
    "get_context",
    "get_logger",
    "getLogger",
    "is_configured",
    "make_filtering_bound_logger",
    "PrintLogger",
    "PrintLoggerFactory",
    "processors",
    "reset_defaults",
    "ReturnLogger",
    "ReturnLoggerFactory",
    "stdlib",
    "testing",
    "threadlocal",
    "twisted",
    "types",
    "wrap_logger",
    "WriteLogger",
    "WriteLoggerFactory",
]
