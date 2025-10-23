from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime
from rasa_sdk.events import UserUtteranceReverted
import requests

class ActionCurrentTime(Action):

    def name(self) -> Text:
        return "action_current_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        
        dispatcher.utter_message(text=f"Práve je {current_time}")

        return []

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # Get user message from Rasa tracker
        user_message = tracker.latest_message.get('text')
        print(user_message)

        # Send request to OpenAI API
        url = 'https://api.openai.com/v1/chat/completions'
        headers = {
            'Authorization': "xxxxxxx",
            'Content-Type': "application/json"
        }
        data = {
            'model': "gpt-3.5-turbo",
            'messages': [{"role": "system", "content": "You are an AI assistant for the user. You help to solve user query"},
                         {"role": "user", "content": "You: " + user_message}],
            'max_tokens': 100
        }
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            chatgpt_response = response.json()
            if 'choices' in chatgpt_response and len(chatgpt_response['choices']) > 0:
                message = chatgpt_response['choices'][0]['message']['content']
                dispatcher.utter_message(message)
            else:
                # Handle the case where 'choices' key is not present or empty
                dispatcher.utter_message("chyba cislo 1")
        else:
            print("Response Status Code:", response.status_code)
             # Handle error and return an event indicating the failure
            dispatcher.utter_message("chyba cislo 2")
            return [UserUtteranceReverted()]
