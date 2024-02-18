# This is the simplest method. This splits based on characters (by default "\n\n") and measure chunk length by number of characters.
# This is a long document we can split up.
with open('../../../state_of_the_union.txt') as f:
    state_of_the_union = f.read()

from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(        
    separator = "\n\n",
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
)

texts = text_splitter.create_documents([state_of_the_union])
print(texts[0])