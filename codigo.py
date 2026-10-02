#titulo - sistema de vendas
#  
# seção cadastrar vendas
    #campo data
    #campo vendedor
    #campo produto
    #campo quantidade
    #campo valor
    # botao cadastrar venda
        #quando u clicar no botão - adicionar a venda na tabela de vendas
#seção vendas cadastradas 
    #tabela com as vendas cadastradas

#seção dashboard
    #carde/metrica - faturamento toral
    #grafico de barras/coluna - vendas por vendedor
    #grafico de pizza - venda por produto

import streamlit as st
import pandas as pd
import plotly.express as px

#Carregar a Base de dados
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# sistema de vendas")

# Seção de cadastro de vendas
st.sidebar.write("## cadastrar Vendas")
data = st.sidebar.date_input("Data")
vendedor =  st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carlos"])
produto = st.sidebar.selectbox("produtos", ["Notbook", "Celular", "Fone", "Tablet"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor", step=0.01)
botao_cadastrar = st.sidebar.button("Cadastrar Vendas")

#Logica para cadastrar a venda
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas)
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.sidebar.success("Venda cadastrada com sucesso!", icon="✅")

# Seção de visualizar as vendas
st.write("### Vedas Cadastradas")
st.dataframe(tabela_vendas)

# Seção de Dashboard
st.write("## Dashboard")

#card/metrica - faturamento toral
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", faturamento)
 #grafico de barras/coluna - vendas por vendedor
grafico1 = px.bar(tabela_vendas, x= "vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)
#grafico de pizza - venda por produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5)
st.plotly_chart(grafico2)
