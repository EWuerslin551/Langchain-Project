#importing libraries
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
from docx import Document #from AI

#setting the outside model to use
model = ChatOllama(model= "Summeriser")

#taking the text out of the Word Document
def read_docx(path):
    doc = Document(path)            #|              
    full_text = []                  #|
    for para in doc.paragraphs:     #|AI Made   
        full_text.append(para.text) #|
    return '\n'.join(full_text)     #|

#making the propt to be used later (slightly redundant)
prompt = ChatPromptTemplate.from_template(
    """ 
    You Are an Ai assistant that extracts factual information from documents. Your goal is to help  students by summerising their not document into key ideas and specific facts. if you do not deem there enough information for a good answer do not provide an answer, other wise aim for arround 3 ideas and 5 specific facts.

    Answer mainly based off the context provided, but if the notes seem to match a major cource you can include ideas from that section of the cource. Answer wiht only the details and facts, nothing else


    Context:
    {context}

    Answer:
    """)

#setting paser and definigg the chain
outputParser = StrOutputParser()
chain = prompt | model | outputParser

#goes through the chain
def aiResponce(docxText):
    print("\nGenerating AI Responce...\n")
    return chain.invoke({"context": docxText})


#user interface:
while True:
    userInput = input("\n\n\nPath to Word Document (format: Example.docx) use 'exit' to quit: ")

    #Checking if the user wants to exit
    if userInput.lower() == 'exit':
        break

    #making sure the word Document Exists
    try:
        userInput = f"/workspaces/Langchain-Project/{userInput}"
        docxOutput = read_docx(userInput)
    except:
        print("File not found. Please try again.")
        continue 

    #using the funtion to give the user a result
    aiOutput = aiResponce(docxOutput)
    print("\nAI Responce:\n" + aiOutput)
        
    
