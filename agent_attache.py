import openai
import streamlit as st

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def get_response_from_agent(question):
    system_prompt = """
    Tu es un assistant IA jouant le rôle d’un attaché territorial dans la fonction publique territoriale française.
    Tu aides à répondre aux questions liées aux finances, marchés publics, ressources humaines, urbanisme, juridique, etc.
    Réponds de façon claire, précise et adaptée au contexte administratif.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content
