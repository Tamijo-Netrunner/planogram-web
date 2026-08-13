import streamlit as st
import planogram
import json
import requests

query = "gamble"

def search_card():
  api_url = "https://api-preview.netrunnerdb.com/api/v3/public/cards?filter[search]=" + query
  response = requests.get(url)

  if response.status_code == 200:
    data =  response.json()
    return data
  else:
    return None

st.title("Planogram Web")

"The runner has jacked in"

st.write(search_card())
