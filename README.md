# Título: Web Site de um sistema de gestão escolar desenvolvido com o Streamlit

## Descrição:

Este código é um aplicativo web desenvolvido com o Streamlit, uma ferramenta para criação de aplicativos de dados interativos em Python. O simples sistema de gestão escolar é uma aplicação desenvolvida para facilitar a administração de uma escola, permitindo o registro de frequência dos alunos em práticas experimentais e a realização de inscrições em atividades integradoras.

## Funcionalidades:

### Frequência - Práticas Experimentais:
- Permite aos professores registrar a frequência dos alunos em práticas experimentais.
- Os professores podem selecionar a turma, a data e os alunos ausentes.
- Os registros de frequência são salvos automaticamente em uma planilha do Google Sheets.

### Inscrições - Práticas Integradoras:
- Permite aos alunos se inscreverem em atividades integradoras oferecidas pela escola.
- Os alunos podem escolher a turma, o nome e as atividades que desejam participar.
- Restrições são aplicadas para garantir que as turmas não ultrapassem um número máximo de participantes.
- Os detalhes das inscrições são armazenados em uma planilha do Google Sheets.

## Bibliotecas Utilizadas:
- **Streamlit**: Utilizada para a criação da interface web interativa.
- **Pandas**: Utilizada para manipulação de dados, incluindo a conversão de dados entre DataFrames e planilhas do Google Sheets.
- **gspread**: O código utiliza a biblioteca `gspread` para autenticar-se e acessar uma planilha no Google Drive, onde estão armazenados os dados de frequência e das inscrições.
- **io e base64**: Utilizadas para processamento de arquivos e codificação de dados.

## Como usar: 
1. Acesse o menu lateral para selecionar entre as opções de Frequência ou Inscrições.
2. Na página de Frequência, selecione a turma, a data e os alunos ausentes. Clique em "Salvar!" para registrar a frequência.
3. Na página de Inscrições, selecione a turma, seu nome e as atividades desejadas. Clique em "Inscrever-se!" para confirmar sua inscrição.
4. Segue o link: https://inscricoes-praticas-integradoras-ect.streamlit.app/
