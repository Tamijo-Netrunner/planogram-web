import streamlit as st
import planogram
import json
import requests

def search_card(searchInput):
  url = "https://api-preview.netrunnerdb.com/api/v3/public/cards?filter[search]=" + searchInput
  response = requests.get(url)
  return url

st.title("Planogram Web")

"The runner has jacked in"

queryInputFromBox = st.text_input(label=" ", value="", help="Search for netrunner cards.")

if st.button("Search"):
    queryInput = queryInputFromBox
    search_card(queryInput)
