import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate 
import os 
from dotenv import load_dotenv

load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANCHAIN_TRACING_V2'] = "true"
os.environ["LANGCHAIN_PROJECT"]= "Q&A Chatbot with OPENAI"

system_message = "You are an helpful assistant. Please respond to the user query."
prompt = ChatPromptTemplate.from_messages([("system", system_message), ("user", "Question:{question}")])

def generate_response(question,api_key, llm,temperature,max_tokens):
    openai.api_key = api_key
    llm = ChatOpenAI(model = engine)
    output_parser = StrOutputParser()
    chain = prompt|llm|outputparser
    answer = chain.invoke({'question': question})
    return answer

st.title(" Chatbot with OpenAI")
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Please Enter your OpenAI api key", type = "password")
engine= st.sidebar.selectbox("Select the model", ["text-davinci-003", "GPT-4o", "GPT-4 Turbo"])
temperature = st.sidebar.slider ("Temperature", min_value = 0.0, max_value = 1.0, value =0.6)
max_tokens = st.sidebar.slider ("Max Tokens", min_value = 50, max_value = 100, value =75)
st.write ("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input, api_key, llm, temperature, max_tokens)
    st.write(response)
else:
    st.write("Please write your Question")