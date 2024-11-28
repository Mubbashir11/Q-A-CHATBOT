
Chatbot with OpenAI
This repository contains a simple web application for a Q&A chatbot built using Streamlit and OpenAI's API. The app allows users to input their OpenAI API key, select a language model, and customize parameters like temperature and token limits to generate responses to user queries.

Features
Integration with OpenAI: Supports multiple OpenAI models like text-davinci-003, GPT-4, and GPT-4 Turbo.
Interactive Interface: A user-friendly interface for asking questions and customizing settings.

Adjustable Parameters:
Temperature: Controls randomness in the model's output.
Max Tokens: Sets the limit for the response length.

Technologies Used
Python
Streamlit: For building the web interface.
OpenAI API: To generate conversational responses.
LangChain: For managing prompts and output parsers.
dotenv: For securely loading environment variables.

Prerequisites
Python: Make sure Python 3.9 or above is installed on your system.
OpenAI API Key: Sign up on OpenAI to get your API key.
Installation


Clone this repository:

git clone https://github.com/your-username/chatbot-with-openai.git
cd chatbot-with-openai

Create and activate a virtual environment:
python -m venv  env
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required Python packages:

pip install -r requirements.txt
Create a .env file in the project root directory and add your environment variables:

LANGCHAIN_API_KEY=your-langchain-api-key
Run the Streamlit app:
streamlit run chatbot.py
Open the application in your browser (default: http://localhost:8501).

Enter your OpenAI API key, select a model, and configure settings using the sidebar.

Type your question in the input field and get a response from the chatbot.

File Structure
python
Copy code
chatbot-with-openai/
│
├── app.py                # Main application code
├── requirements.txt      # Dependencies
├── .env.example          # Template for environment variables
└── README.md             # Project documentation
Environment Variables
The app uses environment variables for secure configuration. Add the following variables to your .env file:

env
Copy code
LANGCHAIN_API_KEY=your-api-key
LANCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=Q&A Chatbot with OPENAI
Customization
Modify the system message in app.py to change the assistant's behavior.
Adjust temperature and max tokens sliders in the Streamlit sidebar for fine-tuning.
Screenshots
Settings Panel


