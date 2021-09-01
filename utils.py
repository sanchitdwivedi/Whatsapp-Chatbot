import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bot-new-rubr-76aca2d81f57.json"

import dialogflow_v2 as dialogflow
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "bot-new-rubr"

from googlesearch import search

def detect_intent_from_text(msg, sender, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, sender)
    text_input = dialogflow.types.TextInput(text=msg, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result

def getGoogleResult(parameters):
    query = parameters.fields["query"]
    return search(query.string_value, tld="co.in", num=1, stop=1, pause=1)

def fetch_reply(msg, sender):
    response = detect_intent_from_text(msg, sender)
    if response.intent.display_name == 'Google search':
        return "".join(getGoogleResult(response.parameters))
        
    else:
        return response.fulfillment_text
    
