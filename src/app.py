import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from streamlit_chat import message
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Pinecone as PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from config.connect import initialize
from template.chatdev_class import ChatDevClass
from data.arrays import models

initialize()
model = st.sidebar.selectbox('Selecione o modelo', models)
openai = ChatOpenAI(model_name=model, temperature=0)
template = ChatDevClass()

prompt_template = PromptTemplate.from_template(template=template.model)
    
st.title('ChatGPT personalizado')
question = ""

def onClick(question):
    message(question, is_user=True) 
    
    prompt = prompt_template.format(question=question)
    response = openai.invoke(prompt)
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  
        chunk_overlap=100,
        length_function=len
    )
    chunks = text_splitter.create_documents([response.content])
    
    embeddings = OpenAIEmbeddings(model='text-embedding-ada-002')
    index_name = 'llm' 
    vector_store = PineconeVectorStore.from_documents(chunks, embeddings, index_name=index_name)
    
    llm = ChatOpenAI(model=model, temperature=0.2)
    retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={'k': 3})
    chain = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=retriever)
    
    answer = chain.run(question)  
    
    message("Aqui está...") 
    st.write(answer)

        
question = st.text_input("", key="user_input")
if st.button('Pesquisar'):  
        onClick(question)
  