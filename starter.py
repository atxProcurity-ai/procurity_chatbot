from llama_index.core import VectorStoreIndex, SimpleDirectoryReader 

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("What did the president say about Ketanji Brown Jackson")
print(response)

