from langchain_groq import ChatGroq

def create_chat_groq():
    """
        Funtion to intialise chat groq

        returns:
             chatgroq
    """
    return  ChatGroq(
            model="mixtral-8x7b-32768",
            temperature=0.9,
            max_tokens=None,
            timeout=None,
            max_retries=2
           )