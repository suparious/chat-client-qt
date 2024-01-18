from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget, QComboBox
from PySide6.QtCore import Slot
from models.openai_model import get_openai_response
from models.chromadb import store_conversation, retrieve_conversation

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.conversation_id = 'unique_conversation_id'  # Example conversation ID

        # Main layout
        layout = QVBoxLayout()

        # Chat display area
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.load_conversation_history()
        layout.addWidget(self.chat_display)

        # Message input field
        self.message_input = QLineEdit()
        layout.addWidget(self.message_input)

        # Send button
        send_button = QPushButton('Send')
        send_button.clicked.connect(self.on_send_clicked)
        layout.addWidget(send_button)

        # Model selection dropdown
        self.model_selector = QComboBox()
        self.model_selector.addItems(['text-davinci-003', 'text-curie-001', 'text-babbage-001'])  # Actual OpenAI models
        layout.addWidget(self.model_selector)

        # Set the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def load_conversation_history(self):
        # Load and display previous conversation history from ChromaDB
        history = retrieve_conversation(self.conversation_id)
        for message in history:
            self.chat_display.append(message)

    @Slot()
    def on_send_clicked(self):
        # Handle send button click event
        user_message = self.message_input.text()
        self.chat_display.append(f'You: {user_message}')
        store_conversation(self.conversation_id, f'You: {user_message}')

        # Get response from selected OpenAI model
        selected_model = self.model_selector.currentText()
        ai_response = get_openai_response(selected_model, user_message)
        self.chat_display.append(f'AI: {ai_response}')
        store_conversation(self.conversation_id, f'AI: {ai_response}')

        self.message_input.clear()

# To run the application
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
