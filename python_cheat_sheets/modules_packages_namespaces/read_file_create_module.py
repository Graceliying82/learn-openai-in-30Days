# Load a file from a path
import os.path
module_name = 'module1'
module_file = 'module1.py'
module_path = '.'

# Get the relative path
module_rel_file_path = os.path.join(module_path, module_file)
# Get the absolutely path
module_abs_file_path = os.path.abspath(module_rel_file_path)

# Read source code from file
with open(module_abs_file_path, 'r') as code_file:
    source_code = code_file.read()

######## a little bit explaination of this "with ... as ..." syntax
# with context_manager_expression as target_variable:
#   #code block
########
# 1. The context_manager_expression is an expression that evaluates to an object with a defined context manager protocol. 
#   This object represents the resource you want to manage. It could be a file, a database connection, a network socket, 
#   or any other resource that requires initialization and cleanup.
# 2. The target_variable is the variable that will be assigned the value of the object returned by the context manager. 
#   It allows you to conveniently access the managed resource within the code block.
# 3. The indented code block following the with statement is where you perform operations using the managed resource.
# 4. When the code block is entered, the context manager's __enter__() method is called, 
#   initializing the resource and returning the value that is assigned to the target_variable. This allows you to work with the resource.
# 5. Once the code block is exited (either normally or due to an exception), the context manager's __exit__() method is called. 
#   This method is responsible for cleaning up the resource and handling any necessary cleanup actions.
# 
# Conclusion: The with ... as ... syntax provides a cleaner and more concise way to handle resources compared to manual initialization 
#             and cleanup, ensuring that resources are properly managed and released.

import types
import sys

# Create a module object
mod = types.ModuleType(module_name)
mod.__file__ = module_abs_file_path

# Set a ref in sys.modules
sys.modules[module_name] = mod

# compile source code
code = compile(source_code, filename=module_abs_file_path, mode='exec')

# Execute compiled source code
exec(code, mod.__dict__)

# Done

mod.hello()

# This is what import a module doing. Define it -> add it to the name space -> compile -> exec