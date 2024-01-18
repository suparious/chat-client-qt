import openai
from config.settings import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_openai_response(model, prompt):
    """
    Function to get a response from an OpenAI model.
    Args:
        model (str): The model to use (e.g., 'text-davinci-003').
        prompt (str): The prompt to send to the model.
    Returns:
        str: The response from the model.
    """
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error getting response from OpenAI: {e}")
        return "Sorry, I couldn't process your request."

# Example usage
# response = get_openai_response('text-davinci-003', 'Translate the following English text to French: Hello, how are you?')
