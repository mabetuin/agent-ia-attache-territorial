import streamlit as st
from agent_attache import get_response_from_agent

st.set_page_config(page_title="Agent IA - Attaché Territorial")

st.title("👩‍💼 Agent IA - Attaché Territorial")
st.write("Pose une question sur les procédures de la fonction publique territoriale.")

user_input = st.text_area("📨 Ta question :", height=150)

if st.button("Envoyer") and user_input.strip():
    with st.spinner("Réponse en cours..."):
        response = get_response_from_agent(user_input)
        st.markdown("### 🧠 Réponse :")
        st.write(response)

