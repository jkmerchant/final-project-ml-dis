from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.app_review.text:
      review  = self.app_review.text
      ## self.image_1.visible = False
      review_classifier = anvil.server.call('classify_review', review)
      self.result.visible = True
      self.image_1.source = anvil.server.call('print_key_words', review)
      self.image_1.visible = True
      ## TODO: make the result more animated
      self.result.text = review_classifier + " review"
    else:
      anvil.Notification("Please enter a movie review", timeout=2).show()
    pass

