# Web Site - desenvolvido com o Streamlit

Este código é um aplicativo web desenvolvido com o Streamlit, uma ferramenta para criação de aplicativos de dados interativos em Python. Ele tem a finalidade de gerenciar inscrições para práticas integradoras de alunos em diferentes turmas.

1. **Autenticação e acesso ao Google Drive**: O código utiliza a biblioteca `gspread` para autenticar-se e acessar uma planilha no Google Drive, onde provavelmente estão armazenados os dados das inscrições.
2. **Conversão da planilha em DataFrame**: Os dados da planilha são obtidos e convertidos em um DataFrame do Pandas para manipulação e análise.
3. **Configuração da interface com o Streamlit**: Define o layout da página e ajustes visuais.
4. **Menu e seleção de páginas**: Define um menu lateral com duas opções de páginas: "Inscrições - Práticas integradoras" e "Outras".
5. **Página de inscrições**: Se o usuário selecionar a página "Inscrições - Práticas integradoras", ele poderá escolher a turma e o nome do estudante para realizar a inscrição em diferentes atividades nas semanas do mês.
   - Os dados são coletados através de widgets interativos como dropdowns e botões.
   - Após a inscrição, os dados são atualizados na planilha do Google Sheets e exibidos na tela.

Ele também faz uso das bibliotecas `pandas` para manipulação de dados, `gspread` para acesso ao Google Sheets, e `streamlit` para construção da interface web.
