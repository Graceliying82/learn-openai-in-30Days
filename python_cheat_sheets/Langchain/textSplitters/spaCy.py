#spaCy is an open-source software library for advanced natural language processing, written in the programming languages Python and Cython.
# Another alternative to NLTK is to use spaCy tokenizer.


#!pip install spacy

# This is a long document we can split up.
with open("../../../state_of_the_union.txt") as f:
    state_of_the_union = f.read()

from langchain.text_splitter import SpacyTextSplitter

text_splitter = SpacyTextSplitter(chunk_size=1000)

texts = text_splitter.split_text(state_of_the_union)
print(texts[0])

