# Where am I?
# I forgot what system I'm running on. Can you help me find my hostname?

# Each computer has a name associated with it. Your goal is to return a string version (case-sensitive) of the host that your kata code runs on.

import socket

def get_pid():
    return socket.gethostname()
