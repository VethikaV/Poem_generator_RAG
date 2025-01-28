from model import create_chat_groq
import prompt


def generate_poem(topic):
     """
        Funtion to create poem

        Args:
        topic of the poem

        returns:
             response string
    """
     prompt_template=prompt.poem_generator_prompt_from_hub()# edu dhan prompt ah call panura line
     llm=create_chat_groq()

     chain=prompt_template | llm

     
     response = chain.invoke({
          "topic" : topic
     })
     return response.content
