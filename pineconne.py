from pinecone import Pinecone,ServerlessSpec

def index_creation(apikey,indexname,dimensions):
    pin=Pinecone(api_key=apikey)

    if indexname not in pin.list_indexes().names():
        pin.create_index(
            name=indexname,
            dimension=dimensions,
            metric='cosine',
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )
        print("Index creation successfully")

    return pin

def put_data(indexname,split_text,embedding_model,pineconee):
    index=pineconee.Index(indexname)
    
    embeddings=list()
    for split in split_text:
        embeddings.append(embedding_model.embed_query(split))

    vectors=list()
    for i,(split,embedding) in enumerate(zip(split_text,embeddings)):
        vector = {
        "id": str(i),
        "values": embedding,
        "metadata": {"text": split}
        }
        print(split)
        vectors.append(vector)

    index.upsert(vectors)