import streamlit as st

st.set_page_config(
    page_title="Due Diligence - Itaú Asset",
    layout="centered"
)

st.markdown("""
    <h1 style='text-align: center; color: #1E3A8A; margin-bottom: 10px;'>
        Due Diligence Itaú Asset
    </h1>
    <h3 style='text-align: center; color: #475569; margin-bottom: 40px;'>
        Selecione o módulo desejado
    </h3>
""", unsafe_allow_html=True)

st.divider()

modulos = [
    {
        "id": "automacao",
        "titulo": "🤖 **Automação Due Diligence**",
        "descricao": "Preenchimento automático de documentos, extração de informações e geração de relatórios.",
        "botao": "Acessar Automação",
        "rota": "pages/automacao.py",
        "ativo": True
    },
    {
        "id": "status_tracker",
        "titulo": "📊 **Acompanhamento de Status**",
        "descricao": "Acompanhe o fluxo de Due Diligence, status dos times e histórico de movimentações.",
        "botao": "Acessar Status Tracker",
        "rota": "pages/fluxo_processos.py",
        "ativo": True
    }
]

modulos_ativos = [m for m in modulos if m["ativo"]]
num_modulos = len(modulos_ativos)

if num_modulos > 0:
    colunas = st.columns(num_modulos, gap="large")
    
    for idx, modulo in enumerate(modulos_ativos):
        with colunas[idx]:
            with st.container(border=True):
                st.markdown(f"### {modulo['titulo']}")
                st.write("")
                st.write(modulo['descricao'])
                st.write("")
                if st.button(modulo['botao'], type="primary", use_container_width=True, key=f"btn_{modulo['id']}"):
                    st.switch_page(modulo['rota'])

st.divider()

st.markdown("""
    <div style='text-align: center; color: #64748B; font-size: 0.9em; margin-top: 50px;'>
        Sistema de Due Diligence • Itaú Asset Management
    </div>
""", unsafe_allow_html=True)