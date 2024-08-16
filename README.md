# Sage AI Chatbot

Sage AI Chatbot is an advanced conversational bot powered by AI. You can upload PDF files to ask questions, and Sage will provide accurate and reliable answers quickly.

Sage is built using **LangChain**, **Python**, and **Streamlit**.


# Architecture and Workflow

A. Home Page

**Home.py**
The home page introduces the chatbot. 
A sidebar has been added to facilitate navigation through the chatbot’s functionalities.

B. Modules

**layout.py**: 
Manages the layout of the chatbot page.

**sidebar.py**: Contains components for model selection, temperature adjustment, and chat reset functionality.

**utils.py**: Handles the loading and examination of APIs, processes uploaded files, and sets up the chatbot.

**chatbot.py**: Utilizes LangChain to configure chatbot prompt templates and chains.

**embedder.py**: Responsible for splitting files, using OpenAI embeddings, and storing data in a vector store.

**history.py**: Manages the saving of conversation history and generation of chat content.

C. Pages

**Sage Chat.py**: Demonstrates the conversation content and functionalities of the chatbot.

