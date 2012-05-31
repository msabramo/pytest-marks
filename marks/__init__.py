__version__ = '0.2'

import sys

if sys.version_info > (3, ):
    from marks.marks import MarksDecorator
else:
    from marks import *
