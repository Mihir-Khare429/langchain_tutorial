from fastapi import FastAPI
from langchain.prompt import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_commubnity.llms import ollama
from dotenv import load_dotenv

load_dotenv()

os.environ["OPEN_API_KEY"]=os.getenv("OPEN_API_KEY")

app = FastAPI(
    title="Langchain with FastAPI",
    description="An example of Langchain integrated with FastAPI",
    version="1.0.0"
)

add_routes(
    app,
    ChatOpenAI(model_name="gpt-3.5-turbo"),
    path="/openai-chat"
)

model =ChatOpenAI()
llm_ollama=ollama.Ollama(model="mistral")

prompt1=ChatPromptTemplate.from_template("Write a short poem about {topic} arouind 100 words.")
prompt2=ChatPromptTemplate.from_template("Write a short essay about {topic} arouind 100 words.")

add_routes(
    app,
    prompt1|model,
    path="/openai-poem"
)

add_routes(
    app,
    prompt2|llm_ollama,
    path="/openai-essay"
)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)