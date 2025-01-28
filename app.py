#front end code lam edula dhan iruku

from dotenv import load_dotenv
import streamlit as st
import chain

load_dotenv()

def poem_generator_app():
    """"

    poem_generator app

    """
    with st.form ("peom_generator"):
         topic = st.text_input("Enter the topic of the poem")
         submitted= st.form_submit_button("Submit")

         if(submitted):
              response=chain.generate_poem(topic)
              st.info(response)
              

    

poem_generator_app()
