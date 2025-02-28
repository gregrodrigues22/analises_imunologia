import streamlit as st

# Carregar usuários do secrets.toml
users = {
    st.secrets["user1"]: st.secrets["password1"],
    st.secrets["user2"]: st.secrets["password2"],
    st.secrets["user3"]: st.secrets["password3"]
}

st.title("🔑 Login no Sistema")

email = st.text_input("E-mail")
password = st.text_input("Senha", type="password")

if st.button("Entrar"):
    if email in users and users[email] == password:
        st.success(f"✅ Bem-vindo, {email}!")
        st.session_state["authenticated"] = True
    else:
        st.error("❌ Usuário ou senha incorretos.")
