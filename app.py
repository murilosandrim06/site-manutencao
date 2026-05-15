import streamlit as st
import pandas as pd
import numpy as np

# ======================================
# CONFIGURAÇÃO
# ======================================

st.set_page_config(

    page_title="Sorocaba Refrescos",

    page_icon="🏭",

    layout="wide"
)

# ======================================
# USUÁRIOS ADMIN
# ======================================

usuarios = {

    "murilo": "murilo123",

    "otavio": "otavio123",

    "joao": "joao123"
}

if "logado" not in st.session_state:

    st.session_state.logado = False

# ======================================
# LOGIN
# ======================================

if not st.session_state.logado:

    st.title("🔐 Login do Sistema")

    usuario = st.text_input(
        "Usuário"
    )

    senha = st.text_input(
        "Senha",
        type="password"
    )

    if st.button("Entrar"):

        if usuario in usuarios and usuarios[usuario] == senha:

            st.session_state.logado = True

            st.success(
                "Login realizado!"
            )

            st.rerun()

        else:

            st.error(
                "Usuário ou senha inválidos"
            )

    st.stop()

# ======================================
# TÍTULO
# ======================================

st.title(
    "🏭 Sistema de Manutenção Preventiva"
)

st.subheader(
    "Sorocaba Refrescos"
)

# ======================================
# BANCO TEMPORÁRIO
# ======================================

if "equipamentos" not in st.session_state:

    st.session_state.equipamentos = [

        {

            "Equipamento": "Máquina de envase",

            "Setor": "Produção",

            "Status": "Revisão em dia"
        },

        {

            "Equipamento": "Esteira transportadora",

            "Setor": "Logística",

            "Status": "Revisão pendente"
        }
    ]

# ======================================
# MENU
# ======================================

menu = st.sidebar.selectbox(

    "Menu",

    [

        "Dashboard",

        "Cadastrar",

        "Relatório",

        "KPIs",

        "Infraestrutura",

        "Estatística"
    ]
)

# ======================================
# DASHBOARD
# ======================================

if menu == "Dashboard":

    st.header(
        "📊 Dashboard Industrial"
    )

    df = pd.DataFrame(
        st.session_state.equipamentos
    )

    st.dataframe(
        df,
        use_container_width=True
    )

# ======================================
# CADASTRO
# ======================================

elif menu == "Cadastrar":

    st.header(
        "➕ Cadastro"
    )

    nome = st.text_input(
        "Nome do Equipamento"
    )

    setor = st.text_input(
        "Setor"
    )

    status = st.selectbox(

        "Status",

        [

            "Revisão em dia",

            "Revisão pendente"
        ]
    )

    if st.button(
        "Cadastrar Equipamento"
    ):

        st.session_state.equipamentos.append({

            "Equipamento": nome,

            "Setor": setor,

            "Status": status
        })

        st.success(
            "Equipamento cadastrado!"
        )

# ======================================
# RELATÓRIO
# ======================================

elif menu == "Relatório":

    st.header(
        "📄 Relatório"
    )

    total = len(
        st.session_state.equipamentos
    )

    pendentes = 0

    for item in st.session_state.equipamentos:

        if item["Status"] == "Revisão pendente":

            pendentes += 1

    revisados = total - pendentes

    st.metric(
        "Total",
        total
    )

    st.metric(
        "Revisados",
        revisados
    )

    st.metric(
        "Pendentes",
        pendentes
    )

# ======================================
# KPIs
# ======================================

elif menu == "KPIs":

    st.header(
        "📈 Indicadores"
    )

    eficiencia = 92

    disponibilidade = 97

    tempo_medio = 2.5

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Eficiência",
        f"{eficiencia}%"
    )

    col2.metric(
        "Disponibilidade",
        f"{disponibilidade}%"
    )

    col3.metric(
        "Tempo Médio",
        f"{tempo_medio}h"
    )

# ======================================
# INFRAESTRUTURA
# ======================================

elif menu == "Infraestrutura":

    st.header(
        "🖥️ Infraestrutura"
    )

    st.markdown("""

### 🔥 Firewall
Proteção da rede industrial.

### 🌐 VPN
Acesso remoto seguro.

### 💾 Backup
Backup automático diário.

### 🔒 Segurança
Controle de usuários e senhas.
""")

# ======================================
# ESTATÍSTICA
# ======================================

elif menu == "Estatística":

    st.header(
        "📉 Estatística"
    )

    falhas = [6, 5, 4, 3, 2]

    meses = [

        "Jan",

        "Fev",

        "Mar",

        "Abr",

        "Mai"
    ]

    media = np.mean(
        falhas
    )

    desvio = np.std(
        falhas
    )

    st.metric(
        "Média",
        f"{media:.2f}"
    )

    st.metric(
        "Desvio Padrão",
        f"{desvio:.2f}"
    )

    grafico = pd.DataFrame({

        "Falhas": falhas

    }, index=meses)

    st.line_chart(
        grafico
    )