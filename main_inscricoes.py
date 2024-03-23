import streamlit as st
import pandas as pd
import gspread
from io import BytesIO
import base64

# Autenticação e acesso ao Google Drive
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
client = gspread.service_account(filename='chaveJson-inscricao.json')

# Abra a planilha pelo nome
sheet = client.open('Planilhax').sheet1

# Converta a planilha em um DataFrame do pandas
data = sheet.get_all_values()
headers = data.pop(0)
dfx = pd.DataFrame(data, columns=headers)

# Confg das margens
st.set_page_config(layout="wide")

# Adiciona um estilo para ajustar a altura da página
st.markdown(
    """
    <style>
    .main {
        margin-top: -100px;
        margin-bottom: -100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
################################################
dadosIni = {'1ª Série - 1º A - AGROINDÚSTRIA': ['ANA LÍVIA ALVES DA SILVA', 'ANTÔNIO GUILHERME DA SILVA', 'APARECIDA JOHELYA TIMÓTEO GADELHA', 'ARTHUR NÓBREGA BATISTA', 'CHARLES HALLEY PORFÍRIO BEZERRA', 'DÉBORA KELLY BEZERRA PAIXÃO', 'EDUARDO VIEIRA GABRIEL FILHO', 'EMANOEL PEREIRA MASCARENHAS', 'EMANUELLE VITÓRIA GOMES DA SILVA', 'FRANCISCA CLARISSY DE OLIVEIRA', 'FRANCISCA FABRICIA MARTINS DOS SANTOS', 'FRANCISCO ESTEVÃO ANTERO DA SILVA', 'GUILHERME GOMES DUARTE', 'GUSTAVO RODRIGUES DE ANDRADE', 'GUSTAVO XAVIER PEREIRA', 'IARA ESTEPHANY GOMES MUNIZ', 'ISABELA VIRGÍNIO DANTAS', 'ITALA VITÓRIA MARTINS DE MEDEIROS', 'JADSON RODRIGUES DA NÓBREGA', 'JOÃO VICTOR GONÇALVES OLIVEIRA MELO', 'JOÃO VICTOR GRANJEIRO MOTA', 'JOÃO VICTOR LOPES DE LIMA', 'JOÃO VICTOR LOPES DE LIMA', 'JOSÉ LUIZ LUCENA LOPES', 'KEYTON RANEY BARBOSA DA SILVA', 'LARA JOANY NÓBREGA ALVES', 'MARIA CLARA DANTAS ESTRELA', 'MARIA EDUARDA GOMES SANTOS', 'MARIA EDUARDA PEREIRA DA SILVA', 'MARIA ISABELA DE SÁ', 'MONNARA BEZERRA DE ABREU', 'NICOLLY HELOISA SOBRINHO SILVA', 'PEDRO HENRIQUE CIPRIANO E SILVA', 'PIETRO MOREIRA DE SOUSA', 'RAQUELY DE LUCENA PEREIRA', 'VINICIUS RODRIGUES DE ANDRADE', 'VINÍCIO GABRIEL JESUS DA SILVA'],
 '1ª Série - 1º A - SER': ['ABIDA VIEIRA DA SILVA', 'ANA HELOISA GOMES DA SILVA', 'ARTHUR QUEIROGA SÁ ABRANTES DE SENA MOREIRA', 'AYANA JHENNIFER VANDERLEY DUTRA', 'BEATRIZ EDUARDA OLIVEIRA DE ARAÚJO', 'BIANCA MARIA FERREIRA DE OLIVEIRA', 'DARLAN ROBERT DE MOURA OLIVEIRA', 'DAVI DAVIDSON VITALINO LIMA', 'DAVID ALAN DE MOURA OLIVEIRA', 'DAVID PIERRE DOMINGOS LOPES', 'EVELYN RODRIGUES SATURNINO', 'FRANCISCO KLEYTON PEREIRA NOGUEIRA', 'GABRIEL FERREIRA SILVA', 'GEOVANA DA SILVA GOMES', 'GERALDO LOPES DA SILVA NETO', 'GUSTAVO KEWIN VIDERES GONÇALVES', 'ITALO FERNANDES MEDEIROS DA SILVA', 'JOÃO GABRIEL GOMES MOURA', 'JOÃO MANOEL ARAÚJO FORMIGA', 'JOÃO PEDRO DA SILVA SANTOS', 'JOÃO VITOR TEIXEIRA DE SOUSA', 'JOSÉ GILIARDO DA SILVA LIMA', 'JOSÉ SALONYEL EMILIANO DE SOUSA', 'JOZIEDSON MATIAS ROLIM', 'KIRLEY WEVERTON DE SOUSA RIBEIRO', 'LOHANNY MENDES GOMES', 'MARCELO DIÓGENES DE ALMEIDA SILVA', 'MARCOS ARTUR SOUSA DOS SANTOS', 'MARCOS VINICIUS SILBÉRIO BARBOSA', 'MARINA GIOVANNA DONATO ARAUJO', 'MILENA ABRANTES FERREIRA', 'MILENA LOHANY GUEDES DE MELO', 'MYRELY JANYNY FRANÇA COSTA', 'RIKELLY FRANÇA VIEIRA', 'RYCKELME KAIQUE SARMENTO LOPES', 'SANDRO MACCLANE ARAKYT LEAL DA SILVA', 'THALITA FERNANDES DA SILVA', 'THAYNA PEREIRA TAVARES', 'VALENTINA CAMPOS GOMES DA SILVA'],
 '1ª Série - 1º B - COMÉRCIO': ['ALINE ALVES DE GOIS', 'ANA CAROLINA FELIX DO NASCIMENTO', 'ANA JÚLIA PEREIRA DO NASCIMENTO', 'ANA RAQUELLY BARBOSA DE SOUSA', 'ANA VITÓRIA DA SILVA', 'ANDREA SOARES ALVES DA SILVA', 'ARYEL VICTOR TEOTÔNIO DA SILVA', 'EMILLY RAQUELLY FERNANDES MATIAS', 'FABIANO VIEIRA DA SILVA', 'FRANCISCO WILLIAM DE SOUSA FERREIRA', 'GAEL VICTOR MARTINS DE OLIVEIRA', 'HENRIQUE ALVES DE OLIVEIRA', 'JAMILLEY KIARA SOARES DE OLIVEIRA', 'KALLYNNY PESSOA MARTINS', 'KAROLAYNE HIGINO FERREIRA DA SILVA', 'KAUÃ BOMFIM XAVIER SANTOS', 'LARA APARECIDA PONTES DE LIMA', 'LUCAS JONATHASMOURA DA SILVA', 'LUCAS RODRIGUES DA SILVA SANTOS', 'LUCAS VINICIUS ALVES DA SILVA', 'LUIS FABIANO COURA DA SILVA', 'MARIA CLARA AFONSO DA SILVA', 'MARIA CLARA DE PAIVA ALVES', 'MARIA ELAILY COELHO PEREIRA', 'MARIANA DA COSTA SANTOS', 'MIRIAN CANDIDO DA SILVA', 'NIKOLLY RODRIGUES DA SILVA', 'RAÍ FELIPE SOARES DA SILVA', 'RHAAN PIRES DE ARAÚJO', 'SABRINA SILVA GADELHA', 'SARAH LETICIA PEREIRA DA COSTA', 'VITÓRIA DE ARAÚJO BONIFÁCIO', 'YASMIM ESTRELA EUFRÁSIO'],
 '1ª Série - 1º A - COMÉRCIO': ['01 ALISSON DORIO DA SILVA', '02 ALLAN RENATO BATISTA DA SILVA', '03 AMANDA FURTADO LACERDA', '04 ASAPH SEBASTIÃO R. DA SILVA', '05 AYSLAN FERREIRA BARBOSA GOMES', '06 BIANCA MARIANY HONORATO PEREIRA', '07 CRISLANNY LAILA ALVES DE SOUSA', '08 DAUANY CRISTINA DIOLINO PEREIRA', '09 DEISY HELLEN ALMEIDA BARROS', '10 ELLEN SAFIRA BRAGA DA SILVA', '11 EMILLI VITORIA J. DA NÓBREGA FF', '12 ERICK JUAN PEREIRA DE SOUSA FF', '13 FRANCISCO WALISSON D. JUNIOR', 'FRANCISCO ALLAN FREITAS DOS SANTOS', '14 GRAZIELLY MARCELINO DIAS FF', '15 HEITOR CAVALCANTE DIAS', '16 JAMILI QUERINO RODRIGUES', '17 FRANCISCO ALLAN FREITAS DOS SANTOS', '18 JOÃO IGOR AVELINO DE LIMA', '29 JOSÉ RUAN GONÇALVES LACERDA', '20 LUDMYLLA DE SOUSA VIEIRA', '22 MARIA EDUARDA FELIZ CUSTÓDIA', '23 MESSIAS JERÔNIMO DE SOUSA', '24 NATALIANE DA SILVA GOMES', '25 NICOLAS ARIEL FERREIRA BARBOSA FF', '26 NILSON DA CONCEIÇÃO M. DE C.', '27 PABLO GUILHERME S. FIGUEIREDO', '28 PEDRO HENRIQUE DA SILVA', '39 ROBSON PEREIRA PAZ', '30 ZACARIAS AFONSO RODRIGUES FERNANDES'],
 'TURMAS': ['1ª Série - 1º A - AGROINDÚSTRIA', '1ª Série - 1º A - COMÉRCIO', '1ª Série - 1º A - SER', '1ª Série - 1º B - COMÉRCIO'],
 'S1 H1': ['Futsal 1', 'Audiovisual', 'Artes', 'Clube do Livro', 'Investimentos'],
 'S1 H2': ['Vôlei 2', 'Socioemocional', 'Astronomia', 'Clube do Estudos', 'Jogos de Mesa'],
 'S2 H1': ['Futsal 2', 'Audiovisual', 'Artes', 'Clube do Livro', 'Culinária'],
 'S2 H2': ['Vôlei 2', 'Oratória', 'Robótica', 'Clube do Estudos', 'Jogos de Mesa']
}

################################################

st.sidebar.title("Menu")
genre = st.sidebar.radio("Selecione uma das páginas:", ["Inscrições - Práticas integradoras", "Outras"], key="Inscrições")

# Página de Inscrições - Práticas integradoras
if genre == "Inscrições - Práticas integradoras":
    st.title('Inscrições - Práticas integradoras:')

    SelecTurma = st.selectbox("Selecione a turma:", dadosIni["TURMAS"])
    SelecEstudante = st.selectbox("Selecione o seu nome:", dadosIni[SelecTurma])

    col1, col2 = st.columns(2)

    with col1:
        st.header("1ª e 3ª Semana do Mês (S1e3)")
        S1_H1 = st.radio("Atividades do 6ª e 7ª horário (H6e7)", dadosIni["S1 H1"])
        S1_H2 = st.radio("Atividades do 8ª e 9ª horário (H8e9)", dadosIni["S1 H2"])

    with col2:
        st.header("2ª e 4ª Semana do Mês (S2e4)")
        S2_H1 = st.radio("Atividades do 6ª e 7ª horário (H6e7)", dadosIni["S2 H1"])
        S2_H2 = st.radio("Atividades do 8ª e 9ª horário (H8e9)", dadosIni["S2 H2"])

    if st.button("Inscrever-se!"):
        inscrito = {
            "Nome": [SelecEstudante],
            "Turma": [SelecTurma],
            "S1e3 - H6e7": [S1_H1],
            "S1e3 - H8e9": [S1_H2],
            "S2e4 - H6e7": [S2_H1],
            "S2e4 - H8e9": [S2_H2]
        }

        df = pd.DataFrame(inscrito)
        # Concatenar o DataFrame existente com o novo DataFrame
        dfx = pd.concat([df, dfx], ignore_index=True)

        # Salvar o DataFrame atualizado na planilha do Google Sheets
        sheet.clear()
        sheet.update([dfx.columns.values.tolist()] + dfx.values.tolist())

        st.write("Inscrição realizada com sucesso!")
        st.dataframe(dfx)

else:
    st.title("Outra página")
    st.title('G Pordeus...')

