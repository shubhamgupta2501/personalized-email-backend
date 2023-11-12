from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()  # Load environment variables from .env

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Correct origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




# Initialize the ChatOpenAI model with the API key
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define a Pydantic model for the request body
class EmailPrompt(BaseModel):
    prompt: str

@app.post("/generate-email")
async def generate_email(email_prompt: EmailPrompt):
    try:
        # Create a list of messages for the conversation
        messages = [
            SystemMessage(
                content="You are an AI trained to assist with tasks to write emails according to the prompt"
            ),
            HumanMessage(
                content=email_prompt.prompt  # The user's prompt
            )
        ]

        # Construct the chat prompt template with the messages
        chat_prompt = ChatPromptTemplate(messages=messages)

        # Format the chat messages for the prompt
        formatted_prompt = chat_prompt.format_messages()

        # Pass the formatted prompt to the language model
        response = llm(formatted_prompt)

        # Extract the generated email content from the response
        
        generated_email = response.content

        # Check if the response is empty
        if not generated_email:
            return {"error": "No content was generated. Please try again with a different prompt or parameters."}

        return {"generated_email": generated_email}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))