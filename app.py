import streamlit as st
import planogram
import json
import requests

def search_card(searchInput):
  searchInput = searchInput.strip()
  #make sure the input is right before continuing
  if searchInput=="":
      st.warning("The search query is empty.", icon="⚠️")
      return
  url = "https://api-preview.netrunnerdb.com/api/v3/public/cards?filter[search]=" + searchInput
  response = requests.get(url)
  response


st.title("Planogram Web")

"The runner has jacked in"

queryInputFromBox = st.text_input(label="Label", placeholder="Placeholder", help="Search for netrunner cards.")

if st.button("Search"):
    queryInput = queryInputFromBox
    search_card(queryInput)


url = "https://api-preview.netrunnerdb.com/api/v3/public/cards?filter[search]=gamble"
response = requests.get(url)
response
response.json()
