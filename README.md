# Document Splitter and Pinecone Storage

This repository contains a Python-based project that processes documents by splitting them into smaller chunks and storing them in a **Pinecone vector database**. This functionality is useful for applications like document search, retrieval-augmented generation (RAG), and semantic analysis.

## Features
1. **Document Splitting**:
   - Automatically splits large documents into manageable chunks.
   - Configurable chunk size and overlap for optimal retrieval.

2. **Vector Storage in Pinecone**:
   - Converts document chunks into embeddings.
   - Stores embeddings in **Pinecone** for fast and efficient vector search.

3. **Customizable Embedding Models**:
   - Supports integration with various embedding models (e.g., **OpenAI, Huggingface**).
   - Easily switch between models for specific use cases.

## Tools and Libraries Used
- **Pinecone**: For vector database storage and retrieval.
- **LangChain**: For document splitting and embedding generation.
- **Huggingface Transformers**: For creating embeddings from text chunks.
- **Python**: For scripting and orchestration.

## Workflow
1. **Document Input**:
   - Upload a document in formats such as `.txt`, `.pdf`, or `.docx`.

2. **Document Splitting**:
   - The document is split into smaller chunks based on predefined configurations (e.g., chunk size and overlap).

3. **Embedding Generation**:
   - Each chunk is converted into a vector using an embedding model.

4. **Storage in Pinecone**:
   - The generated vectors are stored in a Pinecone index for later retrieval.
