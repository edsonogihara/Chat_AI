import streamlit as st
from chat import conversar

st.set_page_config(page_title="Chatbot de Filmes e Séries 🎬", page_icon="🎬")

st.title("🤖 Chatbot de Filmes e Séries")

# Inicializar histórico na sessão
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Você é um especialista em filmes e séries."}
    ]

# Mostrar histórico no chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])

# Input do usuário
if prompt := st.chat_input("Pergunte algo sobre filmes ou séries....."):
    # Adicionar mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Obter resposta do bot
    reply = conversar(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
