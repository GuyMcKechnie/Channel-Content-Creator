import asyncio
import subprocess
from browser_use import Agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr
from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv('GEMINI_API_KEY')))

browser = Browser(
    config = BrowserConfig(
        chrome_instance_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        headless=True
    )
)

prompt = """You are an AI assistant tasked with sending motivational biblical messages to a WhatsApp group called 'Content Queue' using WhatsApp Web. Execute the following steps: 1. Open WhatsApp Web: Using the web browser, open https://web.whatsapp.com/. 2. Locate the search bar in WhatsApp Web. Type 'Content Queue' into the search bar. Select and enter the chat named 'Content Queue' from the search results, under the CHATS section, by clicking on it. Ensure you are in the chat by checking if there are messages in the right pane. If this is not true, then do not move to step 2, keep trying to enter the chat. 3. Compose the Message: Create a short MORNING motivation biblical caption. It may include a verse but is not mandatory. Ensure that the message is not similar to the previous morning's messages. Make sure that the content is unique, non-generic, creative, and non-AI. Include relevant emojis only sparsely throughout the message. Ensure there are NO hashtags. 4. Send the Message: Locate the message input box at the bottom of the chat. Type or paste the formatted message into the input box. Do not input it into the search input box you must be in the chat. Press the 'Send' button or use the keyboard shortcut (e.g., Enter) to send the message. 5. Confirmation: Check the chat to confirm the message has been sent successfully. Log the message that was sent, the time it was sent, and the Biblical verse that was selected. 6. Error Handling: If you encounter any issues (e.g., cannot find the chat, WhatsApp Web not loading), stop the process, log the error, and notify the user 'Could not send morning message to content queue. See error logs'."""

agent = Agent(
    task=prompt,
    llm=llm,
    browser=browser,
)

async def main():
    await agent.run()

if __name__ == '__main__':
    asyncio.run(main())