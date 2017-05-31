# Cargos_tcepb
Scripts em Python para consulta dos cargos de servidores municipais e estaduais fornecidos pelo Tribunal de Contas do Estado da Paraíba. Tais dados podem ser salvos em uma planilha excel.

Os dados estão disponíveis no site dados.tce.pb.gov.br.

A base de dados é montada com full text search fts4 com tokenizer unicode61. Isso quer dizer que:
1. Acentos são ignorados
2. Maisúculo/minúsculo é ignorado
3. Operadores podem ser utilizados. A exemplo de * ? OR NEAR NOT.

Para mais informações, vide:  http://www.sqlite.org/fts3.html

Atenção!Antes de tudo:
a) Verifique se você possui pelo menos 12gb de espaço em seu HD
b) Se estiver utilizando um proxy, vc deverá configurá-lo no prompt de comando digitando: SET HTTP_PROXY=http://login.senha@proxy:porta
c) Preferencialmente instale o libroffice versão 32bits.
d) O script foi projetado para windows. Se você utilizar linux você tem condições de adaptá-lo para suas necessidades :)

# como criar a base de dados:
1. Instale python anaconda em: https://www.continuum.io/downloads
  Em caso de dúvidas, opte pela versão 32bits.
2. Baixe o repositório no canto superior direito (download zip)

3. No prompt de comando digite: 
pip install homura
pip install winsound

3. Execute o script criador_base_dados.py.  Ele baixará os arquivos do site dados.tce.pb.gov.br e iniciará a criação da base de dados folhapessoal.db.
3a. Para executá-lo, você poderá fazer seguir este roteiro: clicar duas vezes -> mais aplicativos -> Procurar outro aplicativo neste PC.
  Depois, vá na pasta do usuário -> anaconda 3 -> Selecione python.exe
  Ele poderá falhar. Clique duas vezes novamente e vai funcionar.
3a. Se alguma falha ocorreu, repita a operação. Algumas vezes os arquivos do dados.tce.pb.gov.br não baixam completamente.

# como consultar
1. Se você executou o item 3a duas vezes, na hora de criar a base de dados, clique duas vezes no arquivo cargostce.py
