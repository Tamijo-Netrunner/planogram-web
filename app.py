import streamlit as st
import planogram
import json
import requests
import reflex as rx

query = "gamble"

def search_card():
  url = "https://api-preview.netrunnerdb.com/api/v3/public/cards?filter[search]=" + query
  response = requests.get(url)

  if response.status_code == 200:
    data =  response.json()
    return data
  else:
    return None

# st.title("Planogram Web")

# "The runner has jacked in"

# st.write(search_card())


ui.label('The runner has jacked in')

ui.run()
