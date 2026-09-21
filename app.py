import streamlit as st
import pandas as pd
import os

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="Aurea Joias",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

ARQUIVO = "joias.csv"

# =========================================================
# IMAGENS
# =========================================================

IMAGEM_HERO = (
    "https://images.unsplash.com/"
    "photo-1515562141207-7a88fb7ce338"
    "?auto=format&fit=crop&w=1800&q=90"
)

IMAGEM_JOIAS = (
    "https://images.unsplash.com/"
    "photo-1605100804763-247f67b3557e"
    "?auto=format&fit=crop&w=1200&q=85"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Poppins:wght@400;500;600;700&display=swap'
);

html,
body,
[class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
        linear-gradient(
            135deg,
            #F8F4EE 0%,
            #EFE4D5 50%,
            #E6D2B8 100%
        );
}

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* =========================================================
SIDEBAR
========================================================= */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #211B18,
            #392C25
        );

    border-right:
        2px solid #C8A96B;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* =========================================================
LOGO
========================================================= */

.logo-title {
    font-family: 'Playfair Display', serif;
    font-size: 30px;
    font-weight: 700;
    color: #D8B56A !important;
    margin-bottom: 5px;
}

.logo-subtitle {
    font-size: 11px;
    font-weight: 700;
    color: #E8D5B5 !important;
    letter-spacing: 1px;
}

/* =========================================================
TÍTULOS
========================================================= */

.page-title {
    font-family: 'Playfair Display', serif;
    font-size: 40px;
    font-weight: 700;
    color: #342A25 !important;
    margin-bottom: 5px;
}

.page-subtitle {
    font-size: 17px;
    color: #6B5A4D !important;
    margin-bottom: 30px;
}

/* =========================================================
HERO
========================================================= */

.hero-container {
    position: relative;
    height: 430px;
    width: 100%;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 35px;

    background-size: cover;
    background-position: center;

    box-shadow:
        0 15px 35px rgba(0,0,0,0.22);
}

.hero-overlay {
    position: absolute;
    inset: 0;

    background:
        linear-gradient(
            90deg,
            rgba(34,27,23,0.96) 0%,
            rgba(34,27,23,0.78) 45%,
            rgba(34,27,23,0.12) 100%
        );
}

.hero-content {
    position: absolute;
    top: 50%;
    left: 7%;

    transform: translateY(-50%);

    max-width: 600px;
}

.hero-number {
    font-size: 70px;
    font-weight: 800;
    color: #D8B56A !important;
    line-height: 1;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 48px;
    font-weight: 700;
    color: #FFFFFF !important;

    margin-top: 12px;
    line-height: 1.1;
}

.hero-text {
    font-size: 17px;
    color: #F3E9DA !important;

    margin-top: 20px;
    line-height: 1.7;
}

.hero-badge {
    display: inline-block;

    margin-top: 24px;

    padding: 10px 22px;

    border-radius: 30px;

    background: #B38A45;

    color: #FFFFFF !important;

    font-size: 14px;
    font-weight: 700;
}

/* =========================================================
CARDS
========================================================= */

.info-card {
    background: #FFFFFF;

    border-radius: 22px;

    padding: 28px;

    min-height: 170px;

    border:
        1px solid rgba(179,138,69,0.35);

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);
}

.card-icon {
    font-size: 32px;
}

.card-number {
    font-size: 34px;
    font-weight: 800;

    color: #342A25 !important;

    margin-top: 10px;
}

.card-label {
    font-size: 14px;
    font-weight: 700;

    color: #766452 !important;

    margin-top: 5px;
}

/* =========================================================
CARD ESCURO
========================================================= */

.dark-card {
    background:
        linear-gradient(
            135deg,
            #241D19,
            #49372B
        );

    border-radius: 24px;

    padding: 30px;

    box-shadow:
        0 12px 30px rgba(0,0,0,0.16);
}

.dark-card h2 {
    color: #FFFFFF !important;
    margin-top: 0;
}

.dark-card p {
    color: #E9DDCE !important;
    line-height: 1.7;
}

/* =========================================================
FORMULÁRIO
========================================================= */

[data-testid="stForm"] {
    background:
        rgba(255,255,255,0.88);

    padding: 30px;

    border-radius: 25px;

    border:
        1px solid #D6BD91;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.08);
}

/* =========================================================
LABELS
========================================================= */

[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span,
.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stTextArea label {
    color: #342A25 !important;

    opacity: 1 !important;

    font-size: 15px !important;

    font-weight: 700 !important;
}

/* =========================================================
INPUTS
========================================================= */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #FFFFFF !important;

    color: #302721 !important;

    -webkit-text-fill-color:
        #302721 !important;

    border:
        2px solid #BDA477 !important;

    border-radius: 12px !important;

    font-size: 16px !important;

    font-weight: 500 !important;
}

.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {
    border:
        2px solid #A77B35 !important;

    box-shadow:
        0 0 0 3px rgba(167,123,53,0.15) !important;
}

input::placeholder,
textarea::placeholder {
    color: #766B61 !important;
    opacity: 1 !important;
}

/* =========================================================
SELECTBOX
========================================================= */

[data-baseweb="select"] > div {
    background-color: #3A302A !important;

    border:
        2px solid #BDA477 !important;

    border-radius: 12px !important;
}

[data-baseweb="select"] > div * {
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;

    opacity: 1 !important;
}

[data-baseweb="select"] input {
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[data-baseweb="select"] [class*="singleValue"] {
    color: #FFFFFF !important;
}

[data-baseweb="select"] svg {
    fill: #FFFFFF !important;
    color: #FFFFFF !important;
}

[data-baseweb="select"] > div:hover {
    border-color: #D8B56A !important;
}

[data-baseweb="popover"] {
    background-color: #3A302A !important;
}

[data-baseweb="menu"] {
    background-color: #3A302A !important;
}

[role="option"] {
    background-color: #3A302A !important;

    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[role="option"]:hover {
    background-color: #76582F !important;

    color: #FFFFFF !important;
}

/* =========================================================
BOTÕES
========================================================= */

.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    background:
        linear-gradient(
            135deg,
            #9A7032,
            #C49A54
        ) !important;

    color: #FFFFFF !important;

    border: none !important;

    border-radius: 14px !important;

    min-height: 54px;

    font-family:
        'Poppins', sans-serif !important;

    font-size: 15px !important;

    font-weight: 700 !important;

    box-shadow:
        0 8px 18px rgba(154,112,50,0.25);
}

.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    background:
        linear-gradient(
            135deg,
            #795524,
            #A77B35
        ) !important;

    color: #FFFFFF !important;

    transform:
        translateY(-1px);
}

/* =========================================================
TABELA
========================================================= */

[data-testid="stDataFrame"] {
    background: #FFFFFF;

    border-radius: 18px;

    overflow: hidden;

    border:
        1px solid #D6BD91;
}

/* =========================================================
RODAPÉ
========================================================= */

.footer {
    margin-top: 50px;

    text-align: center;

    color: #766452 !important;

    font-size: 14px;

    font-weight: 600;
}

/* =========================================================
RESPONSIVO
========================================================= */

@media (max-width: 768px) {

    .hero-container {
        height: 500px;
    }

    .hero-content {
        left: 8%;
        right: 8%;
    }

    .hero-title {
        font-size: 34px;
    }

    .hero-number {
        font-size: 55px;
    }

    .page-title {
        font-size: 30px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNÇÕES
# =========================================================

def carregar_dados():

    colunas = [
        "Tipo",
        "Produto",
        "Material",
        "Coleção",
        "Cor",
        "Tamanho",
        "Valor",
        "Observações"
    ]

    if os.path.exists(ARQUIVO):

        try:

            dados = pd.read_csv(ARQUIVO)

            return dados

        except Exception:

            return pd.DataFrame(columns=colunas)

    return pd.DataFrame(columns=colunas)


def salvar_dados(dados):

    dados.to_csv(
        ARQUIVO,
        index=False
    )


# =========================================================
# CARREGAR DADOS
# =========================================================

df = carregar_dados()

colunas_necessarias = [
    "Tipo",
    "Produto",
    "Material",
    "Coleção",
    "Cor",
    "Tamanho",
    "Valor",
    "Observações"
]

for coluna in colunas_necessarias:

    if coluna not in df.columns:

        df[coluna] = ""

df["Valor"] = pd.to_numeric(
    df["Valor"],
    errors="coerce"
).fillna(0)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
"""
<div class="logo-title">
💎 Aurea Joias
</div>

<div class="logo-subtitle">
GESTÃO INTELIGENTE DE JOIAS
</div>
""",
unsafe_allow_html=True
)

st.sidebar.markdown("<br>", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "NAVEGAÇÃO",
    [
        "🏠 Dashboard",
        "➕ Cadastrar Joia",
        "💎 Joias Cadastradas"
    ]
)

st.sidebar.markdown("---")

st.sidebar.caption(
    "Aurea Joias • 2026"
)


# =========================================================
# DASHBOARD
# =========================================================

if menu == "🏠 Dashboard":

    st.markdown(
    f"""
    <div class="hero-container"
    style="background-image: url('{IMAGEM_HERO}');">

    <div class="hero-overlay"></div>

    <div class="hero-content">

    <div class="hero-number">
    01.
    </div>

    <div class="hero-title">
    Elegância.<br>
    Brilho. Exclusividade.
    </div>

    <div class="hero-text">
    Tenha todas as suas joias organizadas em um único lugar.<br>
    Cadastre, consulte e acompanhe sua coleção
    de forma simples, rápida e profissional.
    </div>

    <div class="hero-badge">
    💎 GESTÃO INTELIGENTE
    </div>

    </div>

    </div>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
    """
    <div class="page-title">
    ✨ Visão geral da sua coleção
    </div>

    <div class="page-subtitle">
    Acompanhe suas joias e mantenha tudo organizado.
    </div>
    """,
    unsafe_allow_html=True
    )

    total_joias = len(df)

    valor_total = df["Valor"].sum()

    tipos = df["Tipo"].nunique()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
        f"""
        <div class="info-card">

        <div class="card-icon">
        💎
        </div>

        <div class="card-number">
        {total_joias}
        </div>

        <div class="card-label">
        JOIAS CADASTRADAS
        </div>

        </div>
        """,
        unsafe_allow_html=True
        )

    with col2:

        st.markdown(
        f"""
        <div class="info-card">

        <div class="card-icon">
        💰
        </div>

        <div class="card-number">
        R$ {valor_total:,.2f}
        </div>

        <div class="card-label">
        VALOR TOTAL DA COLEÇÃO
        </div>

        </div>
        """,
        unsafe_allow_html=True
        )

    with col3:

        st.markdown(
        f"""
        <div class="info-card">

        <div class="card-icon">
        ✨
        </div>

        <div class="card-number">
        {tipos}
        </div>

        <div class="card-label">
        TIPOS DE JOIAS
        </div>

        </div>
        """,
        unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    coluna1, coluna2 = st.columns([1.1, 1])

    with coluna1:

        st.markdown(
        """
        <div class="dark-card">

        <h2>
        ✨ Elegância em um só lugar
        </h2>

        <p>
        A Aurea Joias permite manter todas as
        suas peças organizadas em um único lugar.
        </p>

        <p>
        Cadastre, consulte, pesquise e acompanhe
        as informações da sua coleção de maneira
        moderna e profissional.
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )

    with coluna2:

        st.image(
            IMAGEM_JOIAS,
            use_container_width=True
        )


# =========================================================
# CADASTRAR JOIA
# =========================================================

elif menu == "➕ Cadastrar Joia":

    st.markdown(
    """
    <div class="page-title">
    ➕ Nova joia
    </div>

    <div class="page-subtitle">
    Adicione uma nova peça à sua coleção.
    </div>
    """,
    unsafe_allow_html=True
    )

    with st.form(
        "cadastro_joia",
        clear_on_submit=True
    ):

        col1, col2 = st.columns(2)

        with col1:

            tipo = st.selectbox(
                "💎 Tipo de Joia",
                [
                    "Anel",
                    "Brinco",
                    "Colar",
                    "Pulseira",
                    "Pingente",
                    "Tornozeleira",
                    "Relógio",
                    "Outros"
                ]
            )

            produto = st.text_input(
                "🏷️ Nome da Joia"
            )

            material = st.selectbox(
                "✨ Material",
                [
                    "Ouro 18K",
                    "Ouro 10K",
                    "Prata 925",
                    "Aço",
                    "Banhado a Ouro",
                    "Banhado a Prata",
                    "Outro"
                ]
            )

            colecao = st.text_input(
                "🌟 Coleção"
            )

        with col2:

            cor = st.selectbox(
                "🎨 Cor",
                [
                    "Dourado",
                    "Prateado",
                    "Rosé",
                    "Branco",
                    "Amarelo",
                    "Outro"
                ]
            )

            tamanho = st.text_input(
                "📏 Tamanho"
            )

            valor = st.number_input(
                "💰 Valor da Joia",
                min_value=0.0,
                value=0.0,
                step=100.0
            )

            observacoes = st.text_area(
                "📝 Observações"
            )

        cadastrar = st.form_submit_button(
            "💾 CADASTRAR JOIA"
        )

    if cadastrar:

        if (
            produto.strip()
            and colecao.strip()
        ):

            nova_joia = pd.DataFrame(
                [{
                    "Tipo": tipo,
                    "Produto": produto.strip(),
                    "Material": material,
                    "Coleção": colecao.strip(),
                    "Cor": cor,
                    "Tamanho": tamanho.strip(),
                    "Valor": float(valor),
                    "Observações": observacoes.strip()
                }]
            )

            df = pd.concat(
                [
                    df,
                    nova_joia
                ],
                ignore_index=True
            )

            salvar_dados(df)

            st.success(
                "💎 Joia cadastrada com sucesso!"
            )

            st.rerun()

        else:

            st.warning(
                "⚠️ Preencha o nome da joia e a coleção."
            )


# =========================================================
# JOIAS CADASTRADAS
# =========================================================

elif menu == "💎 Joias Cadastradas":

    st.markdown(
    """
    <div class="page-title">
    💎 Minha coleção
    </div>

    <div class="page-subtitle">
    Consulte e pesquise todas as joias cadastradas.
    </div>
    """,
    unsafe_allow_html=True
    )

    if df.empty:

        st.markdown(
        """
        <div class="dark-card">

        <h2>
        💎 Nenhuma joia cadastrada
        </h2>

        <p>
        Sua coleção ainda está vazia.
        Cadastre sua primeira joia para começar.
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )

    else:

        busca = st.text_input(
            "🔎 Pesquisar joia",
            placeholder="Digite tipo, produto, material ou coleção..."
        )

        if busca:

            mascara = (
                df.astype(str)
                .apply(
                    lambda coluna:
                    coluna.str.contains(
                        busca,
                        case=False,
                        na=False
                    )
                )
                .any(axis=1)
            )

            df_filtrado = df[mascara]

        else:

            df_filtrado = df

        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        opcoes_joias = df.index.tolist()

        joia_excluir = st.selectbox(
            "🗑️ Selecione uma joia para excluir",
            options=opcoes_joias,
            format_func=lambda indice:
                f"{df.loc[indice, 'Tipo']} - "
                f"{df.loc[indice, 'Produto']} "
                f"({df.loc[indice, 'Material']})"
        )

        if st.button(
            "🗑️ EXCLUIR JOIA"
        ):

            df = df.drop(
                joia_excluir
            )

            df = df.reset_index(
                drop=True
            )

            salvar_dados(df)

            st.success(
                "💎 Joia excluída com sucesso!"
            )

            st.rerun()


# =========================================================
# RODAPÉ
# =========================================================

st.markdown(
"""
<div class="footer">

💎 Aurea Joias<br>
Gestão inteligente de joias

</div>
""",
unsafe_allow_html=True
)