import os

from .base_conf import *

if (os.getenv("SERVER_CONF") or '').lower() == 'dev':
    from .dev_conf import *
elif (os.getenv("SERVER_CONF") or '').lower() == 'prod':
    from .prod_conf import *
else:
    try:
        from .local_conf import *
    except ImportError:
        pass
