import streamlit as st
from chat import gerar_resposta

st.set_page_config(page_title="Assistente de Suporte", layout="centered")
st.title("🤖 Assistente Virtual OST")

categoria = st.selectbox("Escolha a categoria do seu problema:", [
    "1 - Problemas de Hardware/Periféricos",
    "2 - Problemas com Windows",
    "3 - Problemas com Aplicativos Office365",
    "4 - Problemas com minha conta",
    "5 - Ajuda e Outros"
])

pergunta = st.text_input("Descreva seu problema:")

if st.button("Enviar"):
    if pergunta.strip():
        with st.spinner("Pensando..."):
            resposta = gerar_resposta(pergunta, categoria)
            st.success(resposta)
    else:
        st.warning("Digite uma pergunta antes de enviar.")
