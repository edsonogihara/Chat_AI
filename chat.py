from openai import OpenAI
import streamlit as st
import os

# Carregar chave da API
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

SYSTEM_PROMPT = """
Você é um especialista em filmes e séries.
Responda sempre de forma detalhada, simpática e bem-humorada.
Se o assunto não for sobre filmes ou séries, diga que foi programado para responder apenas sobre filmes e séries, tente encaixar um filme ou série na desculpa ao assunto apresentado.
"""

def conversar(messages):
    """
    Recebe o histórico de mensagens e retorna a resposta do bot.
    Garante que o SYSTEM_PROMPT sempre seja incluído.
    """
    # Garante que o prompt do sistema esteja no início
    msgs = [{"role": "system", "content": SYSTEM_PROMPT}] + messages

    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=msgs
    )
    reply = response.choices[0].message.content
    return reply

