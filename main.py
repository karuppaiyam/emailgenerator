# import streamlit as st
from langchain.prompts import PromptTemplate

from langchain_community.llms import CTransformers

def getLLMResponse(form_input, email_sender, email_recipient, email_style):

    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type = 'llama',
                        config={'max_new_tokens':256,
                                'temperature': 0.01})
    
    template = """
    Write a email with {style} style and includes topic :{email_topic}.\n\nSender: {sender}\nRecipient: {recipient}\n\nEmail Text:    
    """
    prompt = PromptTemplate(
        input_variables=["style","email_topic","sender","recipient"],
        template=template,  
        )

    response = llm.invoke(prompt.format(email_topic=form_input,sender=email_sender,recipient=email_recipient,style=email_style))
    print(response)

    return response

# st.set_page_config(page_title="Generate Emails",
#                    page_icon='📧',
#                    layout='centered',
#                    initial_sidebar_state='collapsed'
#                    )

# st.header("Genderate Email")

form_input = """
There is a problem with predictions
"""
email_sender = "karuppaiya"
email_recipient = "surya"
email_style = "Formal" #('Formal', 'Appreciating', 'Not Satisfied', 'Neutral')

output = getLLMResponse(form_input, email_sender, email_recipient, email_style)

print(output)




