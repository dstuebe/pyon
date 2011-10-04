#!/usr/bin/env python

__author__ = 'Adam R. Smith'
__license__ = 'Apache 2.0'

from pyon.util.config import Config
from pyon.core.object import IonObjectRegistry

#import logging.config
#import os

# Note: do we really want to do the res folder like this again?
#logging_conf_paths = ['res/config/logging.yml', 'res/config/logging.local.yml']
#LOGGING_CFG = Config(logging_conf_paths).data

# Ensure the logging directories exist
#for handler in LOGGING_CFG.get('handlers', {}).itervalues():
#    if 'filename' in handler:
#        log_dir = os.path.dirname(handler['filename'])
#        if not os.path.exists(log_dir):
#            os.makedirs(log_dir)

#logging.config.dictConfig(LOGGING_CFG)

conf_paths = ['res/config/pyon.yml', 'res/config/pyon.local.yml']
CFG = Config(conf_paths).data

service_conf_path = 'res/deploy/r2deploy.rel'
SERVICE_CFG = eval(open(service_conf_path).read())

obj_registry = IonObjectRegistry()
obj_registry.register_yaml_dir('obj', ['ion.yml'], ['services'])

# Make a default factory for IonObjects
IonObject = obj_registry.new

svc_registry = IonObjectRegistry()
svc_registry.register_yaml_dir('obj/services')
