# Simulado Questões 21 a 30 - Streamlit
# Execute com:
# streamlit run app.py

import streamlit as st

st.set_page_config(
    page_title="Simulado - Questões 21 a 30",
    layout="wide"
)

st.title("📚 Simulado - Questões 21 a 30")
st.write("Responda as questões e confira seu desempenho ao final.")

questoes = [

    {
        "pergunta": """Segundo a Resolução CEE/SC n.° 100, de 13 de dezembro de 2016, o público da Educação Especial é formado pelos estudantes com:""",
        "alternativas": {
            "A": "Deficiência sensorial, intelectual e física e Transtorno do Espectro Autista (TEA).",
            "B": "Deficiência intelectual e física, Transtorno do Espectro Autista (TEA), Transtorno de Déficit de Atenção/Hiperatividade (TDAH), Disortografia e Altas habilidades/Superdotação (AH/SD).",
            "C": "Deficiência, Transtorno do Espectro Autista (TEA), Transtorno de Déficit de Atenção/Hiperatividade (TDAH) e Altas Habilidades/Superdotação (AH/SD).",
            "D": "Deficiência sensorial, intelectual e física; Transtorno do Espectro Autista (TEA) e Dislexia e Discalculia.",
            "E": "Deficiência sensorial, intelectual e física; Transtorno do Espectro Autista (TEA) e Altas Habilidades/Superdotação (AH/SD)."
        },
        "correta": "C"
    },

    {
        "pergunta": """As Práticas Baseadas em Evidências (PBE) garantem que intervenções sejam fundamentadas em pesquisa rigorosa, promovendo resultados eficazes e otimizando recursos.

Associe a segunda coluna de acordo com a primeira, relacionando a correspondência entre as PBE e suas respectivas caracterizações.

Primeira coluna: Práticas Baseadas em Evidência

1. Intervenções Baseadas no Antecedente  
2. Intervenção Naturalística  
3. Instrução e Intervenção Mediadas por Pares

Segunda coluna: caracterização

( ) Trata-se de uma coleção de práticas, incluindo arranjo ambiental e técnicas de interação implementadas durante rotinas diárias e atividades na sala de aula ou no ambiente doméstico do aluno.

( ) Variedade de modificações feitas no ambiente/contexto em uma tentativa de alterar ou moldar o comportamento de um aluno.

( ) A interação social entre pares é a característica definidora da intervenção. Na maioria das vezes, mas nem sempre, o colega do aluno é uma criança neurotípica da mesma idade geral.

Assinale a alternativa que apresenta a correta associação entre as colunas:""",
        "alternativas": {
            "A": "2 − 3 − 1.",
            "B": "2 − 1 − 3.",
            "C": "3 − 2 − 1.",
            "D": "3 − 1 − 2.",
            "E": "1 − 2 − 3."
        },
        "correta": "B"
    },

    {
        "pergunta": """Os processos avaliativos são formados por dois distintos, porém encadeados, processos denominados de avaliação diagnóstica e avaliação de desenvolvimento.

Acerca das especificidades de cada processo avaliativo, considere as afirmativas a seguir e registre V, para verdadeiras, e F, para falsas:

( ) A avaliação diagnóstica encaminhada por suspeita de TEA possui objetivo de identificar déficits relacionados à comunicação, interação social e ocorrência de comportamentos restritos, bem como possíveis prejuízos relacionados à linguagem e ao funcionamento intelectual.

( ) A avaliação de desenvolvimento é iniciada com uma triagem com profissional capacitado para observar condições ambientais e cadastrar relatórios do educando.

( ) A avaliação de desenvolvimento busca caracterizar repertório comportamental atual do educando diagnosticado com TEA, seus comportamentos/habilidades emergentes e suas interações ambientais.

Assinale a alternativa que apresenta a sequência correta:""",
        "alternativas": {
            "A": "F − F − V.",
            "B": "V − F − V.",
            "C": "V − F − F.",
            "D": "F − V − F.",
            "E": "V − V − F."
        },
        "correta": "B"
    },

    {
        "pergunta": """__________________ concentram-se especificamente em um comportamento que necessita ser reduzido, modificado ou intensificado.

Assinale a alternativa que corretamente preenche a lacuna no excerto:""",
        "alternativas": {
            "A": "Modelos Abrangentes de Tratamento.",
            "B": "Aprendizagem sem erro.",
            "C": "CA (Comunicação Alternativa).",
            "D": "Práticas de Intervenção Focada.",
            "E": "PECS (Picture Exchange Communication System)."
        },
        "correta": "D"
    },

    {
        "pergunta": """______________________________ é uma intervenção comportamental que ensina o estudante a usar figuras/símbolos para se comunicar com outras pessoas.

Assinale a alternativa que corretamente preenche a lacuna no excerto:""",
        "alternativas": {
            "A": "Práticas de Intervenção Focada.",
            "B": "Aprendizagem sem erro.",
            "C": "CA (Comunicação Alternativa).",
            "D": "Modelos Abrangentes de Tratamento.",
            "E": "PECS (Picture Exchange Communication System)."
        },
        "correta": "E"
    },

    {
        "pergunta": """Acerca da Política Nacional de Educação Especial na Perspectiva da Educação Inclusiva (2008) e dos Recursos Pedagógicos e Tecnológicos para a Inclusão, analise as afirmações apresentadas a seguir:

I. A Política Nacional de Educação Especial na Perspectiva da Educação Inclusiva (2008) orienta a organização do Atendimento Educacional Especializado (AEE), preferencialmente, na rede regular de ensino, definindo-o como um serviço da educação especial que identifica, elabora e organiza recursos pedagógicos e de acessibilidade.

II. O Sistema Braille e o Soroban são recursos pedagógicos essenciais para o estudante com deficiência visual no AEE, sendo o Soroban específico para o cálculo matemático.

III. O atendimento educacional especializado é organizado para apoiar o desenvolvimento dos alunos, constituindo oferta e frequência obrigatória.

É correto o que se afirma em:""",
        "alternativas": {
            "A": "III, apenas.",
            "B": "I e II, apenas.",
            "C": "I, II e III.",
            "D": "II e III, apenas.",
            "E": "I, apenas."
        },
        "correta": "B"
    },

    {
        "pergunta": """O AEE representa um espaço de construção de estratégias pedagógicas acessíveis e de valorização da diversidade.

Sobre o Atendimento Educacional Especializado (AEE) de estudantes com Surdez, analise as afirmações apresentadas a seguir:

I. O professor do AEE de estudantes com surdez não tem como atribuição o ensino de Libras para o estudante com surdez, sendo esta função exclusiva do Intérprete/Tradutor de Libras (TIL), que atua na sala de aula comum.

II. A abordagem bilíngue na educação de surdos considera a Língua Brasileira de Sinais (Libras) como Primeira Língua (L1) para o desenvolvimento cognitivo e linguístico, e a Língua Portuguesa escrita como Segunda Língua (L2), essencial para a participação social e acesso ao currículo.

III. O público-alvo do AEE inclui o estudante com surdez ou deficiência auditiva, e o serviço deve prover recursos e estratégias para garantir sua acessibilidade curricular e comunicacional, inclusive o trabalho com a identidade e cultura surda.

É correto o que se afirma em:""",
        "alternativas": {
            "A": "I, apenas.",
            "B": "I e II, apenas.",
            "C": "I, II e III.",
            "D": "III, apenas.",
            "E": "II e III, apenas."
        },
        "correta": "E"
    },

    {
        "pergunta": """Associe a segunda coluna de acordo com a primeira, relacionando as diferentes áreas e conceitos da Educação Especial com suas respectivas especificidades e recursos relacionados.

Primeira coluna: áreas e conceitos

1. Deficiência Visual (Baixa Visão)  
2. Deficiência Intelectual  
3. Transtorno do Espectro Autista (TEA)  
4. Deficiência Múltipla

Segunda coluna: especificidades e recursos

( ) Condição que se caracteriza pela associação de duas ou mais deficiências que implicam em necessidades educacionais especiais mais complexas.

( ) O trabalho do professor do AEE foca na mediação pedagógica para a construção do conhecimento, desenvolvimento da autonomia e de habilidades adaptativas, considerando o ritmo individual e o grau de comprometimento.

( ) O trabalho do AEE, além do foco na comunicação e interação social, deve considerar a elaboração de estratégias para lidar com o perfil sensorial e a rigidez comportamental, podendo utilizar o Sistema PECS.

( ) O uso de recursos ópticos e não ópticos e a prática de Orientação e Mobilidade (OM) são recursos importantes para a acessibilidade e autonomia.

Assinale a alternativa que apresenta a correta associação entre as colunas:""",
        "alternativas": {
            "A": "1 − 2 − 3 − 4.",
            "B": "4 − 2 − 3 − 1.",
            "C": "2 − 1 − 4 − 3.",
            "D": "4 − 3 − 2 − 1.",
            "E": "3 − 4 − 1 − 2."
        },
        "correta": "B"
    },

    {
        "pergunta": """Com relação ao Planejamento, Avaliação e Adequações Curriculares, considere as afirmativas a seguir e registre V, para verdadeiras, e F, para falsas:

( ) O atendimento educacional especializado requer articulação entre professor do AEE, docentes da sala comum e família para identificação de necessidades específicas e definição de estratégias pedagógicas diferenciadas que promovam acessibilidade ao currículo.

( ) As adequações curriculares devem ser realizadas nos aspectos avaliativos e de materiais, sendo a metodologia de ensino padronizada para todos os estudantes da classe comum.

( ) A avaliação inicial deve identificar o nível de desenvolvimento real do estudante, quanto à estrutura da percepção, atenção, pensamento e linguagem, bem como as competências para a realização das atividades de vida prática escolar, subsidiando o planejamento do AEE.

Assinale a alternativa que apresenta a sequência correta:""",
        "alternativas": {
            "A": "V − F − V.",
            "B": "V − F − F.",
            "C": "F − V − F.",
            "D": "V − V − V.",
            "E": "F − F − V."
        },
        "correta": "A"
    },

    {
        "pergunta": """O Plano de Desenvolvimento Individual (PDI) é um instrumento central no AEE.

Sobre o PDI, assinale a alternativa correta:""",
        "alternativas": {
            "A": "O PDI deve ser elaborado de forma colaborativa − envolvendo professor do AEE, família, equipe escolar e, quando possível, o estudante − e deve estabelecer objetivos, metas e estratégias individualizadas com prazos e formas de acompanhamento.",
            "B": "O PDI tem caráter estritamente administrativo e serve apenas para justificar a presença do aluno no AEE; não precisa conter metas ou estratégias pedagógicas.",
            "C": "O PDI é um documento exclusivo do professor do AEE, que o elabora sozinho para manter sigilo pedagógico; a família não participa de sua elaboração.",
            "D": "O PDI substitui integralmente o planejamento da classe comum, de modo que o estudante atendido pelo AEE não participa do planejamento coletivo da turma.",
            "E": "O PDI é obrigatório apenas para estudantes com deficiência intelectual e não é recomendado para outros públicos do AEE (por exemplo, surdez ou deficiência visual)."
        },
        "correta": "A"
    }
]

respostas_usuario = {}

for i, questao in enumerate(questoes):
    st.subheader(f"Questão {i+21}")

    st.write(questao["pergunta"])

    resposta = st.radio(
        "Selecione uma alternativa:",
        options=list(questao["alternativas"].keys()),
        format_func=lambda x: f"{x}) {questao['alternativas'][x]}",
        key=f"q_{i}"
    )

    respostas_usuario[i] = resposta
    st.divider()

if st.button("Finalizar simulado"):
    acertos = 0
    erros = []

    for i, questao in enumerate(questoes):
        resposta_usuario = respostas_usuario[i]
        resposta_correta = questao["correta"]

        if resposta_usuario == resposta_correta:
            acertos += 1
        else:
            erros.append({
                "questao": i + 21,
                "marcada": resposta_usuario,
                "correta": resposta_correta
            })

    st.success(f"✅ Você acertou {acertos} de {len(questoes)} questões.")

    percentual = (acertos / len(questoes)) * 100
    st.info(f"📊 Aproveitamento: {percentual:.1f}%")

    if erros:
        st.error("❌ Questões erradas:")

        for erro in erros:
            st.write(
                f"Questão {erro['questao']} → "
                f"Você marcou: {erro['marcada']} | "
                f"Correta: {erro['correta']}"
            )
    else:
        st.balloons()
        st.success("🎉 Parabéns! Você acertou todas!")