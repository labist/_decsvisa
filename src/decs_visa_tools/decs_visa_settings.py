"""
Utility module that holds some useful settings
"""

from pathlib import Path

#############################################
#    Configuration settings required     #
#############################################

# path to the system settings .env file
DOT_ENV_PATH = Path("~/.hlab/decs_env").expanduser()

##############################################

# required for features such as match/case
PYTHON_MIN_MAJOR = 3
PYTHON_MIN_MINOR = 10

# Connection details for the socket_server
# These values should be consistent with
# those in the .env file.
PORT = 33576
HOST = "localhost"

# queue message to indicate system should stop
# this can be sent from the client.
SHUTDOWN = "SHUTDOWN"

# socket server write delimiter
WRITE_DELIM = "\n"

# socket server read delimiter
READ_DELIM = "\n"