#Language models have a token limit. You should not exceed the token limit. When you split your text into chunks it is therefore a good idea to count the number of tokens. There are many tokenizers. When you count tokens in your text you should use the same tokenizer as used in the language model.
#tiktoken is a fast BPE tokenizer created by OpenAI.

#!pip install tiktoken

# This is a long document we can split up.
with open("../../../state_of_the_union.txt") as f:
    state_of_the_union = f.read()
from langchain.text_splitter import CharacterTextSplitter

#one way
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=100, chunk_overlap=0
)
texts = text_splitter.split_text(state_of_the_union)


# another way
from langchain.text_splitter import TokenTextSplitter

text_splitter = TokenTextSplitter(chunk_size=10, chunk_overlap=0)

texts = text_splitter.split_text(state_of_the_union)
print(texts[0])
