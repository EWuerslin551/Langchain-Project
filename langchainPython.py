from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
from docx import Document #from AI

DOCX_PATH = "/workspaces/Langchain-Project/Notes.docx"
model = ChatOllama(model= "FactExtracter")
def read_docx(path):
    doc = Document(path)            #|              
    full_text = []                  #|
    for para in doc.paragraphs:     #|AI Made   
        full_text.append(para.text) #|
    return '\n'.join(full_text)     #|

prompt = ChatPromptTemplate.from_template(
    """ 
    You Are an Ai assistant that extracts factual information from documents. Your goal is to help  students by summerising their not document into key ideas and specific facts. if you do not deem there enough information for a good answer do not provide an answer, other wise aim for arround 3 ideas and 5 specific facts.

    Answer mainly based off the context provided, but if the notes seem to match a major cource you cna include ideas from that section of the cource. Answer wiht only the details and facts, nothing else

    Question:
    {input}

    Context:
    {context}

    Answer:
    """)
outputParser = StrOutputParser()



#user interface:
while True:
    input = input("Path to Word Document (format: Example.docx) use 'exit' to quit: ")
    try: 
       docxOutput = read_docx("/workspaces/Langchain-Project/" + input)
    except:
       print("File not found, please try again")
       continue
    
