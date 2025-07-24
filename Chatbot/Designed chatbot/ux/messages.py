import tkinter as tk
from chatbot.probability import get_response
from ux.alerts import empty_message_alert, clear_success_alert
def send_message(entry, chat_log):
    
    if not entry.get():
        empty_message_alert()
        return

    user_message = None
    
    #TODO: get entry's text in the user_message variable using the get method4
    user_message = entry.get()
    
    #TODO: if user_message is blank, empty_message_alert
    if user_message.strip() == "":
        empty_message_alert()
        return

    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"You: {user_message.strip()}\n")
    
    bot_response = None
    #TODO: get response for the user message as the bot_response using the get_response function from chatbot.probability
    bot_response = get_response(user_message.strip())
    
    chat_log.insert(tk.END, f"Bot: {bot_response}\n\n")
    
    chat_log.see("end")
    chat_log.config(state=tk.DISABLED)
    entry.delete(0, tk.END)
    
def clear_chat(chat_log):
    chat_log.config(state=tk.NORMAL)
    chat_log.delete('1.0', tk.END)
    chat_log.config(state=tk.DISABLED)
    
    #TODO: alert for succesful clear
    clear_success_alert()
