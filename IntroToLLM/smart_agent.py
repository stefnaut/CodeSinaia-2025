import ollama

class SmartAgent:

    def __init__(self, model_name):
        self.model_name = model_name

        self.chat_log = []

        with open("context_prompt.txt", "r") as file:
            self.context_prompt = file.read()

        self.chat_log.append({'role': 'user', 'content': self.context_prompt})

    def chat(self, message):
        self.chat_log.append({'role': 'user', 'content': message})

        response = ollama.chat(
            model=self.model_name,
            messages=self.chat_log,
            stream=False
        )

        answer_text = response['message']['content']
        self.chat_log.append({'role': 'assistant', 'content': answer_text})

        return answer_text
