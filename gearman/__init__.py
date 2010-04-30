"""
Gearman client.
"""

__author__ = "Matthew Tai <mtai@yelp.com>"
__version__ = "2.x.x"
__license__ = "MIT"

from gearman.client import GearmanClient
from gearman.worker import GearmanWorker

# GearmanConnection - wraps a socket and parses commands
# GearmanClientBase - Uses a connection and reads down a list of commands... does command_handler callbacks

# GearmanClientHandler - Wraps a GearmanClientBase and does Client specific ops
# GearmanWorkerHandler - Wraps a GearmanClientBase and does Worker specific ops