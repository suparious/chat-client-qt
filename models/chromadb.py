from config.settings import CHROMADB_CONNECTION_STRING
import chromadb

# Initialize ChromaDB connection
chroma_db = chromadb.ChromaDB(CHROMADB_CONNECTION_STRING)

def store_conversation(conversation_id, message):
    """
    Store a message in ChromaDB with a unique conversation ID.
    Args:
        conversation_id (str): The unique identifier for the conversation.
        message (str): The message to store.
    """
    chroma_db.store(conversation_id, message)

def retrieve_conversation(conversation_id):
    """
    Retrieve the conversation history from ChromaDB using the conversation ID.
    Args:
        conversation_id (str): The unique identifier for the conversation.
    Returns:
        list: The conversation history.
    """
    return chroma_db.retrieve(conversation_id)

# Example usage
# store_conversation('12345', 'Hello, how are you?')
# conversation_history = retrieve_conversation('12345')
