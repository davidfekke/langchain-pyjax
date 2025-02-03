
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load PDF file
loader = PyPDFLoader("AIM_Bsc_w_Chg_1_2_and_3_dtd_9-5-24.pdf")
pages = loader.load_and_split()

# Create text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
)

# Split documents
docs = text_splitter.split_documents(pages)
print(len(docs))
print(docs[0].page_content)