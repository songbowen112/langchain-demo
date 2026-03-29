import dotenv
from langchain_ollama import ChatOllama
from langchain_core.tools import create_retriever_tool
from langchain_classic.agents import create_tool_calling_agent

dotenv.load_dotenv()

llm = ChatOllama(base_url="http://localhost:11434", model="qwen3.5:2b", reasoning=False)

if __name__ == "__main__":
    response = llm.invoke("什么是LangChain?")
    print(response)
