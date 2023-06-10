# if we define mod_name = 'math'
# and then run import mod_name
# we will get No module named 'mod_name' found
# in order to find the mod, we need something called importlib

import sys
import importlib

mod_name = 'math'

importlib.import_module(mod_name)

print('math' in sys.modules)
# should return True
# however, if we run math.sqrt(2) right now, it will give NameError: name 'math' is not defined
# because we only don't have it in our name space yet.

#if we run print('math' in globals), it will return False

# The following line would assign a handle to that math module
# it's like import math as math2
# math2 = sys.modules['math']
# another way to do it is:
math2 = importlib.import_module(mod_name)

# now when you check print('math' in globals), it will return True
print('math' in globals)

id(math2)
id(sys.modules['math'])
# they will return the same id

math2.sqrt(2)

# finder + loader == importer