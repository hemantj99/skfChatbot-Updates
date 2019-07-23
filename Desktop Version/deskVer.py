from tkinter import *

import json
import uuid
import os

from google.protobuf.json_format import MessageToJson
from google.protobuf.struct_pb2 import Struct, Value

import dialogflow
context=dialogflow.types.context_pb2.Context(name='projects/skf-gqvclo/agent/sessions/637996ed-90a8-4900-83b0-b5f1f9a9xxxx/contexts/prueba_dialog_context')
credentials_file = os.path.expanduser('skfkey.json')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_file
project_id = format(json.load(open(credentials_file))['project_id'])

session_client = dialogflow.SessionsClient()

session = session_client.session_path(project_id, str(uuid.uuid4()))

window = Tk()
window.title('SKF-CHATBOT')
messages = Text(window)
messages.pack()

input_user = StringVar()
input_field = Entry(window, text=input_user)
input_field.pack(side=BOTTOM, fill=X)

def Enter_pressed(event):
   input_get = input_field.get()
   messages.configure(state='normal')
   messages.insert(INSERT, '%s\n' % input_get)
   input_user.set('')


   text_input = dialogflow.types.TextInput(text=input_get, language_code="en")
   query_input = dialogflow.types.QueryInput(text=text_input)

   query_parameter = dialogflow.types.QueryParameters(contexts=[context])


   response = session_client.detect_intent(session=session, query_input=query_input,query_params=query_parameter)

   print(response.query_result.fulfillment_text)
   messages.insert(INSERT,'%s\n\n' %response.query_result.fulfillment_text)

   parameters=response.query_result.parameters

   parameters_json = json.loads(MessageToJson(parameters))
   messages.configure(state='disabled')
   return "break"

frame = Frame(window) 
input_field.bind("<Return>", Enter_pressed)
frame.pack()

window.mainloop()
