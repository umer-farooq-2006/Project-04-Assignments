import streamlit as st
import requests

st.title("🌍 Country Information App")

country = st.text_input("Enter a country name")

if country:
    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()[0]
        st.write(f"**Country:** {data['name']['common']}")
        st.write(f"**Capital:** {data.get('capital', ['N/A'])[0]}")
        st.write(f"**Region:** {data['region']}")
        st.write(f"**Population:** {data['population']}")
        st.write(f"**Area:** {data['area']} km²")
        st.image(data['flags']['png'], width=200)
    else:
        st.error("Country not found.")
