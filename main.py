from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from config import *
from langchain.docstore.document import Document
from pineconne import *
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model=HuggingFaceEmbeddings(model_name=embed_model)

def doc_loader(file_path):
    loader=PyMuPDFLoader(file_path)
    pages=loader.load()
    return pages

def text_splitter(content):
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap ,
        length_function=len,
        is_separator_regex=False,
    )
    doc_list = []
    for page in content:
        page_splits = text_splitter.split_text(page.page_content)
        doc_list.extend(page_splits)
    return doc_list

if __name__=="__main__":
    pages=doc_loader(file_path)
    split_text=text_splitter(pages)
    
    pineconee=index_creation(api_key, index_name, dimensions)
    put_data(index_name,split_text,embedding_model,pineconee)
    