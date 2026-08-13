import streamlit as st
import planogram
import json
import requests

query = ""

def search_card():
  api_url = "https://api-preview.netrunnerdb.com/api/v3/public/cards?filter[search]=" + query
  response = response.json()
  return response

st.title("Planogram Web")

"The runner has jacked in"

st.write(search_card())

