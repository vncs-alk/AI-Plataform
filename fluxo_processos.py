import streamlit as st
import pandas as pd

@st.dialog("Detalhes da Esteira Micro", width="large")
def modal_esteira_micro(cliente, status, comercial, deadline):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader(f"Cliente: {cliente}")
        st.write(f"**Comercial:** {comercial} | **Prazo (SLA):** {deadline}")
    with col2:
        st.info(f"**Status Geral:** {status}")

    st.divider()
    
    st.markdown("### 📊 Progresso dos Times")
    if status == "Concluído" or status == "Revisão Final":
        st.progress(1.0)
    elif status == "Em Preenchimento":
        st.progress(0.25)
    else:
        st.progress(0.60)

    st.write("")
    
    cols = st.columns(3)
    
    with cols[0]:
        with st.container(border=True):
            st.markdown("### 🟢 Risco")
            st.caption("Status: Concluído")
            st.write("**Responsável:** Analista Sênior")
            
    with cols[1]:
        with st.container(border=True):
            st.markdown("### 🟡 Jurídico")
            st.caption("Status: Em Análise")
            st.write("**Responsável:** Consultoria Interna")
            
    with cols[2]:
        with st.container(border=True):
            st.markdown("### 🔴 Compliance")
            st.caption("Status: Aguardando Resposta")
            st.write("**Responsável:** —")

    st.divider()
    
    st.markdown("### 📜 Últimos Eventos")
    st.write("**Ontem 14:30** — Status do time Risco alterado para: Concluído")
    st.write("**Ontem 10:00** — Documento enviado para a esteira micro.")

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Acompanhamento Macro")

# --- BARRA DE NAVEGAÇÃO SUPERIOR ---
col_voltar, espaco_vazio = st.columns([1, 6])
with col_voltar:
    if st.button("⬅️ Voltar à Automação", use_container_width=True):
        st.switch_page('streamlit_app.py')

# --- CONTEÚDO PRINCIPAL ---
st.title("Painel Central de Demandas")
st.divider()

col_espera, col_concluidos, col_historico, col_total = st.columns(4)
with col_espera:
    st.metric("Pedidos a serem negociados", "12")
with col_concluidos:
    st.metric("Pedidos em andamento", "45")
with col_historico:
    st.metric("Pedidos em atraso", "3")
with col_total:
    st.metric("Total de pedidos", "60")

st.divider()

st.subheader("Fila de Demandas (DDQs)")

dados_mock = [
    {"Cliente": "Quantuns Alpha", "Comercial": "João Silva", "Categoria": "Institucional", "Status": "Em Preenchimento", "Deadline": "15/07/2026"},
    {"Cliente": "Fundo Beta", "Comercial": "Maria Souza", "Categoria": "Corporate", "Status": "Aguardando Times", "Deadline": "18/07/2026"},
    {"Cliente": "Gama Partners", "Comercial": "Carlos Eduardo", "Categoria": "Wealth", "Status": "Revisão Final", "Deadline": "12/07/2026"}
]
df_pedidos = pd.DataFrame(dados_mock)

evento_tabela = st.dataframe(
    df_pedidos, 
    use_container_width=True, 
    hide_index=True,
    selection_mode="single-row",
    on_select="rerun"
)

if evento_tabela.selection.rows:
    linha_selecionada = evento_tabela.selection.rows[0]
    cliente_selecionado = df_pedidos.iloc[linha_selecionada]["Cliente"]
    status_selecionado = df_pedidos.iloc[linha_selecionada]["Status"]
    comercial_selecionado = df_pedidos.iloc[linha_selecionada]["Comercial"]
    deadline_selecionado = df_pedidos.iloc[linha_selecionada]["Deadline"]
    
    modal_esteira_micro(cliente_selecionado, status_selecionado, comercial_selecionado, deadline_selecionado)

st.divider()

st.subheader("Consulta de Base Histórica")
st.info("A IA de consulta ao banco de dados está desativada para este MVP.")
st.chat_input("Pesquise na base histórica de DDQs...", disabled=True)