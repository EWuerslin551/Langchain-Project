from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
from docx import Document #from AI

DOCX_PATH = "/workspaces/Langchain-Project/Notes.docx"
model = ChatOllama(model= "FactExtracter")