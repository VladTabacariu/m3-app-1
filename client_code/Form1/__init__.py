from ._anvil_designer import Form1Template
from anvil import *
from anvil.js.window import Appwrite
import anvil.js

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    
    client = Appwrite.Client()
    (client
      .setEndpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
      .setProject('643ed56ccf9c61cb99dd') # Your project ID
    )
    database = Appwrite.Databases(client)
    list = database.listDocuments("643fdd591a34cacf4635","643fdd6dd18939a543c0", [])
    print(list.documents[0])
    def called(response):
      print(response)
    client.subscribe('documents', called);

    
    self.repeating_panel_1.items = list.documents
    
    