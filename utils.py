import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bot-new-rubr-374f04a2b0ac.json"

import dialogflow_v2 as dialogflow
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "bot-new-rubr"

def detect_intent_from_text(msg, sender, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, sender)
    text_input = dialogflow.types.TextInput(text=msg, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result

def fetch_reply(msg, sender):
    response = detect_intent_from_text(msg, sender)
    return response.fulfillment_text
