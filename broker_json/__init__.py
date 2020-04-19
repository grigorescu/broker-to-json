import os
import sys

# Import broker. Just do it?
try:
    import broker
except ImportError:
    # Next, we'll try to use the broker from zeekctl, but we need to find it.
    # We'll find it via zeek-config --python_dir

    broker_error_message = "Could not import the Python Broker bindings. See: " \
                           "https://docs.zeek.org/projects/broker/en/stable/python.html#installation-in-a-virtual" \
                           "-environment "

    import distutils.spawn

    which_zeekconfig = distutils.spawn.find_executable('zeek-config')
    if not which_zeekconfig:
        raise ImportError(broker_error_message)

    python_dir = os.popen('zeek-config --python_dir').read().strip()
    sys.path.append(python_dir)
    sys.path.append(os.path.join(python_dir, "broker"))

    try:
        import broker
    except ImportError:
            # We've done all we can
            raise ImportError(broker_error_message)

# Bring everything into our namespace
from .utils import *
