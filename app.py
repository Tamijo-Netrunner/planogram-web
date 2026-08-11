import streamlit as st
import planogram
import requests

def get_format_data():
  url = "https://api-preview.netrunnerdb.com/api/v3/public/card_pools/startup_02"
  response = requests.get(url)
  if response.status_code == 200
    data = response.json()
    return id
  else
    return "Nope!"

st.title("Planogram Web")

"The runner has jacked in"

get_format_data()
