from openai import OpenAI
import streamlit as st
import json 
import requests

# setting an API key
f=open("Keys/API_key.txt")
key=f.read()
client=OpenAI(api_key=key)

# Setting the title and header
st.snow()
st.title("GEN AI CODE REVIEWER 🖥️")
st.subheader("BUGS FIXING 🐞")
# Taking user input
prompt = st.text_area(label='Enter Your Python Code', value="", height=None, placeholder="Enter your code here", disabled=False, label_visibility="visible")


# if the button is clicked, generate the response

if st.button('Generate') == True:
    st.balloons()    
    response =client.chat.completions.create(
              model='gpt-3.5-turbo-0125',
              messages=[
              {'role': 'system','content':"""You are a wonderful AI assistant.
                                             Given a python code you need to find errors in the code and give correct syntax of the code and also count of the errors in the code. """},
                                    
              {"role" : "user","content":prompt}
              ]
    )

# print the response on the web app
    st.write(response.choices[0].message.content)