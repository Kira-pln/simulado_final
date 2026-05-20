import streamlit as st

st.set_page_config(page_title="Simulado Concurso AEE", layout="wide")

# =========================
# QUESTÕES 21–30
# =========================

questoes = [

{
"pergunta": """Questão 21


Segundo a Resolução CEE/SC n.° 100/2016, o público da Educação Especial é formado pelos estudantes com:""",
"opcoes": [
"Deficiência sensorial, intelectual e física e TEA.",
"Deficiência intelectual e física, TEA, TDAH, Disortografia e AH/SD.",
"Deficiência, TEA, TDAH e Altas Habilidades/Superdotação.",
"Deficiência sensorial, intelectual e física; TEA; Dislexia e Discalculia.",
"Deficiência sensorial, intelectual e física; TEA e AH/SD."
],
"resposta": 2
},

{
"pergunta": """Questão 22


Associe PBE e suas caracterizações:""",
"opcoes": [
"2 − 3 − 1",
"2 − 1 − 3",
"3 − 2 − 1",
"3 − 1 − 2",
"1 − 2 − 3"
],
"resposta": 1
},

{
"pergunta": """Questão 23


Avaliação diagnóstica e de desenvolvimento:""",
"opcoes": [
"F − F − V",
"V − F − V",
"V − F − F",
"F − V − F",
"V − V − F"
],
"resposta": 1
},

{
"pergunta": """Questão 24


Concentram-se em um comportamento específico a ser modificado:""",
"opcoes": [
"Modelos Abrangentes",
"Aprendizagem sem erro",
"CA",
"Práticas de Intervenção Focada",
"PECS"
],
"resposta": 3
},

{
"pergunta": """Questão 25


Intervenção que ensina uso de figuras para comunicação:""",
"opcoes": [
"Intervenção Focada",
"Aprendizagem sem erro",
"Comunicação Alternativa",
"Modelos Abrangentes",
"PECS"
],
"resposta": 4
},

{
"pergunta": """Questão 26


Política Nacional de Educação Especial (2008):""",
"opcoes": [
"III apenas",
"I e II apenas",
"I, II e III",
"II e III apenas",
"I apenas"
],
"resposta": 1
},

{
"pergunta": """Questão 27


AEE e estudantes com surdez:""",
"opcoes": [
"I apenas",
"I e II apenas",
"I, II e III",
"III apenas",
"II e III apenas"
],
"resposta": 4
},

{
"pergunta": """Questão 28


Associação áreas Educação Especial:""",
"opcoes": [
"1 − 2 − 3 − 4",
"4 − 2 − 3 − 1",
"2 − 1 − 4 − 3",
"4 − 3 − 2 − 1",
"3 − 4 − 1 − 2"
],
"resposta": 1
},

{
"pergunta": """Questão 29


Planejamento e avaliação no AEE:""",
"opcoes": [
"V − F − V",
"V − F − F",
"F − V − F",
"V − V − V",
"F − F − V"
],
"resposta": 0
},

{
"pergunta": """Questão 30


Plano de Desenvolvimento Individual (PDI):""",
"opcoes": [
"Elaboração colaborativa com metas e estratégias.",
"Somente administrativo.",
"Exclusivo do professor do AEE.",
"Substitui planejamento da turma.",
"Apenas para deficiência intelectual."
],
"resposta": 0
},

]

# =========================
# SISTEMA
# =========================

if "respostas" not in st.session_state:
    st.session_state.respostas = [None] * len(questoes)

st.title("Simulado Concurso AEE - Questões 21 a 30")

for i, q in enumerate(questoes):
    st.markdown(q["pergunta"])

    resp = st.radio(
        "Selecione a alternativa:",
        [f"{chr(65+j)}) {op}" for j, op in enumerate(q["opcoes"])],
        key=f"q{i}"
    )

    st.session_state.respostas[i] = ord(resp[0]) - 65

# =========================
# RESULTADO
# =========================

if st.button("Finalizar Prova"):

    acertos = 0
    erros = []

    for i, q in enumerate(questoes):
        if st.session_state.respostas[i] == q["resposta"]:
            acertos += 1
        else:
            correta = chr(65 + q["resposta"])
            erros.append(f"Q{i+21} - correta: {correta}")

    st.subheader("Resultado Final")

    st.write(f"✅ Acertos: {acertos}/10")
    st.write(f"📊 Aproveitamento: {(acertos/10)*100:.1f}%")

    if erros:
        st.write("❌ Questões erradas:")
        for e in erros:
            st.write(e)
