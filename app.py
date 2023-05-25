import streamlit as st
import re


def validar_dado(padroes, dado):
    for tipo, padrao in padroes:
        if re.match(re.compile(padrao), dado):
            return tipo
    return 'Dado não'


st.title('Verificador de Dados')

padroes = [
    ('E-mail', r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]{2,}\.[a-zA-Z]{2,3}$'),
    ('Telefone', r'^\(\d{2}\)\s\d{5}-\d{4}$'),
    ('Placa', r'^[A-Z]{3}[0-9][A-Z][0-9]{2}$'),
    ('CEP', r'^\d{5}-\d{3}$'),
    ('Data', r'^\d{2}\/\d{2}\/\d{4}$'),
    ('Nome', r'^[A-Z][a-z]{2,}$'),
]

dado = st.text_input(
    label='Digite o dado a ser verificado:',
    placeholder='Pode ser: e-mail, telefone, placa, CEP, data ou nome'
)

st.write(validar_dado(padroes, dado), 'encontrado!')
