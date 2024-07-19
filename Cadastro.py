import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome, dt_nasc, tipo):
    if nome and dt_nasc <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome},{cpf},{sexo},{dt_nasc},{tipo},{rua},{num},{comp},{cidade},{estado},{cep}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False

st.set_page_config(
    page_title="Cadastro de clientes",
    page_icon="📄"
)

st.title("Cadastro de clientes")
st.divider()

st.header("Dados pesoais")
nome = st.text_input("Nome:",
                     key="nome_cliente")


cpf = st.text_input("CPF:")
st.text(cpf)

sexo = st.radio("Gênero", ["Masculino", "Feminino", "Outro"])

dt_nasc = st.date_input("Data nascimento:", format="DD/MM/YYYY")

tipo = st.selectbox("Tipo de cliente",
                    ["Pessoa Jurídica", "Pessoa Física"])

st.divider()
st.header("Endereço")

rua = st.text_input("Rua:")

num = st.text_input("Nº:")
comp = st.text_input("Complemento:")
cidade = st.text_input("Cidade:")
estado = st.selectbox("Estado:", 
                      ["Acre",
                    "Alagoas",
                    "Amapá",
                    "Amazonas",
                    "Bahia",
                    "Ceará",
                    "Distrito Federal",
                    "Espirito Santo",
                    "Goiás ",
                    "Maranhão",
                    "Mato Grosso do Sul",
                    "Mato Grosso",
                    "Minas Gerais",
                    "Pará",
                    "Paraíba",
                    "Paraná",
                    "Pernambuco",
                    "Piauí",
                    "Rio de Janeiro",
                    "Rio Grande do Norte",
                    "Rio Grande do Sul",
                    "Rondônia",
                    "Roraima",
                    "Santa Catarina",
                    "São Paulo",
                    "Sergipe",
                    "Tocantins",])

cep = st.text_input("CEP:")
st.text(cep)

st.markdown("""
### Cadastro de dados pessoais.

Nos termo descritos acima, se você marcar como aceito,
poderá realizar o seu cadastro.

            """)
st.checkbox("Eu aceito os termos",)

btn_cadastrar = st.button("Cadastrar",
                          on_click=gravar_dados,
                          args=[nome, dt_nasc, tipo])

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!",
                   icon="✅")
        st.balloons()
    else:
        st.error("Houve algum problema no cadastro!",
                 icon="🚫")
