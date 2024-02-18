# CodeTextSplitter allows you to split your code with multiple language support. Import enum Language and specify the language.

from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    Language,
)

# Full list of support languages
[e.value for e in Language]
'''
    ['cpp',
     'go',
     'java',
     'js',
     'php',
     'proto',
     'python',
     'rst',
     'ruby',
     'rust',
     'scala',
     'swift',
     'markdown',
     'latex',
     'html',
     'sol',]
'''

 # You can also see the separators used for a given language
RecursiveCharacterTextSplitter.get_separators_for_language(Language.PYTHON)
'''
['\nclass ', '\ndef ', '\n\tdef ', '\n\n', '\n', ' ', '']
'''

#Here's an example using the PythonTextSplitter
PYTHON_CODE = """
def hello_world():
    print("Hello, World!")

# Call the function
hello_world()
"""
python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=50, chunk_overlap=0
)
python_docs = python_splitter.create_documents([PYTHON_CODE])
python_docs

#output is:
#    [Document(page_content='def hello_world():\n    print("Hello, World!")', metadata={}),
#     Document(page_content='# Call the function\nhello_world()', metadata={})]