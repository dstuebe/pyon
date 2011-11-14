#!/usr/bin/env python

"""
Entry point for importing common Ion packages. Most files should only need to import from here.
"""

__author__ = 'Adam R. Smith'
__license__ = 'Apache 2.0'

__all__ = []

def assert_environment():
    """This asserts the mandatory (minimal) execution environment for pyon"""
    import os.path
    if not os.path.exists("res"):
        raise StandardError("pyon environment assertion failed: res/ directory not found")
    if not os.path.exists("res/config"):
        raise StandardError("pyon environment assertion failed: res/config directory not found")
    if not os.path.exists("res/config/pyon.yml"):
        raise StandardError("pyon environment assertion failed: pyon.yml config missing")

assert_environment()

# Tell the magic import log setup to pass through this file
from pyon.util.log import import_paths
import_paths.append(__name__)

from pyon.util.log import log
__all__ += ['log']

from pyon.core.bootstrap import CFG, obj_registry, IonObject, sys_name
__all__ += ['CFG', 'obj_registry', 'IonObject', 'sys_name']

from pyon.util.async import spawn, switch
__all__ += ['spawn', 'switch']

from pyon.core.process import PyonProcessError, GreenProcess, GreenProcessSupervisor, PythonProcess
__all__ += ['PyonProcessError', 'GreenProcess', 'GreenProcessSupervisor', 'PythonProcess']

from pyon.net import messaging, channel, endpoint
__all__ += ['messaging', 'channel', 'endpoint']

from pyon.ion.process import IonProcessSupervisor
__all__ += ['IonProcessSupervisor']

from pyon.container.cc import Container
__all__ += ['Container']
