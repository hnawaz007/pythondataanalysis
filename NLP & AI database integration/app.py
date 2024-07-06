import os
import streamlit as st 
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.utilities import SQLDatabase
import re
#

pwd = os.environ['PGPASS']
uid = os.environ['PGUID']
server = "localhost"
db = "adventureworks"
port = 5432

def init_database() -> SQLDatabase:
  db_uri = f"postgresql://{uid}:{pwd}@{server}:{port}/{db}"
  return SQLDatabase.from_uri(db_uri, schema="sales")


def llm_query(question):
    # first sql llm
    llm = ChatOllama(model="llama-sql")
    prompt = ChatPromptTemplate.from_template(" {topic}")
    # chain
    chain = prompt | llm | StrOutputParser()
    # chain invokation
    sql = chain.invoke({"topic": f"{question}"})
    sql = re.sub(r'(?:(?<=_) | (?=_))','',sql)
    # return sql query
    return sql


def get_response(user_query: str, db: SQLDatabase, chat_history: list):

    sql_query = llm_query(user_query)

    template = """
    You are an experienced data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
    Based on the table schema, question, sql query, and sql response, write a natural language response.

    Conversation History: {chat_history}
    User question: {question}
    SQL Response: {response}"""

    prompt = ChatPromptTemplate.from_template(template)

    # llm
    llm = ChatOllama(model="llama3",  temperature=0)

    chain = (
    RunnablePassthrough.assign(
        response=lambda vars: db.run(sql_query),
    )
    | prompt
    | llm
    | StrOutputParser()
    )

    return chain.invoke({
    "question": user_query,
    "chat_history": chat_history,
    })

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
      AIMessage(content="Hello! I'm a Data assistant. Ask me a question about your AdventureWorks :bike: Sales data."),
    ]

st.set_page_config(page_title="Chat with Postgres", page_icon=":thought_balloon:")

st.title("Chat with Postgres")


for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.markdown(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("User"):
            st.markdown(message.content)

# initialize the db
db = init_database()
st.session_state.db = db
st.success("Connected to database!")

user_query = st.chat_input("Type a question...")
if user_query is not None and user_query.strip() != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    
    with st.chat_message("User"):
        st.markdown(user_query)
        
    with st.chat_message("AI"):
        response = get_response(user_query, st.session_state.db, st.session_state.chat_history)
        st.markdown(response)
        
    st.session_state.chat_history.append(AIMessage(content=response))