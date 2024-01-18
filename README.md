# Chat Client in Qt6

## Directory Structure

```graphql
├── config/               # Configuration files
│   └── settings.py       # Centralized settings for the application
│
├── ui/                   # User interface files
│   ├── __init__.py
│   ├── main_window.py    # Main window of the chat client
│   └── styles.py         # Styling for the UI
│
├── models/               # Models and business logic
│   ├── __init__.py
│   ├── openai_model.py   # Module to interact with OpenAI models
│   └── chromadb.py       # Module for ChromaDB integration
│
├── main.py               # Main application entry point
└── requirements.txt      # Project dependencies
```
