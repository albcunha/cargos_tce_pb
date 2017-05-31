<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=windows-1252"/>
	<title></title>
	<meta name="generator" content="LibreOffice 5.3.3.2 (Windows)"/>
	<meta name="created" content="2017-05-30T21:57:03.557000000"/>
	<meta name="changed" content="2017-05-30T21:58:12.102000000"/>
	<style type="text/css">
		@page { margin: 2cm }
		p { margin-bottom: 0.25cm; line-height: 120% }
	</style>
</head>
<body lang="pt-BR" dir="ltr">
<p align="left" style="margin-bottom: 0cm; line-height: 100%"><font size="5" style="font-size: 18pt"><b>Cargos_tcepb<br/>
</b></font>Scripts
em Python para consulta dos cargos de servidores municipais e
estaduais fornecidos pelo Tribunal de Contas do Estado da Para&iacute;ba.
Tais dados podem ser salvos em uma planilha excel.</p>
<p align="left" style="margin-bottom: 0cm; line-height: 100%"><br/>
Os
dados est&atilde;o dispon&iacute;veis no site dados.tce.pb.gov.br.</p>
<p align="left" style="margin-bottom: 0cm; line-height: 100%">A base
de dados &eacute; montada com full text search fts4 com tokenizer
unicode61. Isso quer dizer que:</p>
<p align="left" style="margin-bottom: 0cm; line-height: 100%">1.
Acentos s&atilde;o ignorados</p>
<p align="left" style="margin-bottom: 0cm; line-height: 100%">2.
Mais&uacute;culo/min&uacute;sculo &eacute; ignorado</p>
<p align="left" style="margin-bottom: 0cm; line-height: 100%">3.
Operadores podem ser utilizados. A exemplo de * ? OR NEAR NOT.</p>
<p align="left" style="margin-bottom: 0cm; line-height: 100%"><br/>
<br/>
Para
mais informa&ccedil;&otilde;es, vide: 
http://www.sqlite.org/fts3.html<br/>
<br/>
<b>Aten&ccedil;&atilde;o!Antes
de tudo:<br/>
</b>a) Verifique se voc&ecirc; possui pelo menos 12gb
de espa&ccedil;o em seu HD<br/>
b) Se estiver utilizando um proxy, vc
dever&aacute; configur&aacute;-lo no prompt de comando digitando: SET
HTTP_PROXY=http://login.senha@proxy:porta<br/>
c) Preferencialmente
instale o libroffice vers&atilde;o 32bits.<br/>
d) O script foi
projetado para windows. Se voc&ecirc; utilizar linux voc&ecirc; tem
condi&ccedil;&otilde;es de adapt&aacute;-lo para suas necessidades
:)<br/>
<br/>
<font size="4" style="font-size: 16pt"><b>Como criar a
base de dados:<br/>
</b></font>1. Instale python anaconda em:
https://www.continuum.io/downloads<br/>
  Em caso de d&uacute;vidas,
opte pela vers&atilde;o 32bits.<br/>
2. Baixe o reposit&oacute;rio no
canto superior direito (download zip)<br/>
3. No prompt de comando
digite: <br/>
pip install homura<br/>
pip install winsound<br/>
pip
install xlswriter<br/>
3. Execute o script criador_base_dados.py. 
Ele baixar&aacute; os arquivos do site dados.tce.pb.gov.br e iniciar&aacute;
a cria&ccedil;&atilde;o da base de dados folhapessoal.db.<br/>
3a.
Para execut&aacute;-lo, voc&ecirc; poder&aacute; fazer seguir este
roteiro: clicar duas vezes -&gt; mais aplicativos -&gt; Procurar
outro aplicativo neste PC.<br/>
  Depois, v&aacute; na pasta do
usu&aacute;rio -&gt; anaconda 3 -&gt; Selecione python.exe<br/>
  Ele
poder&aacute; falhar. Clique duas vezes novamente e vai
funcionar.<br/>
3a. Se alguma falha ocorreu, repita a opera&ccedil;&atilde;o.
Algumas vezes os arquivos do dados.tce.pb.gov.br n&atilde;o baixam
completamente.<br/>
<br/>
<font size="4" style="font-size: 16pt"><b>Como
consultar<br/>
</b></font>1. Se voc&ecirc; executou o item 3a duas
vezes, na hora de criar a base de dados, clique duas vezes no arquivo
cargostce.py<br/>
<br/>

</p>
</body>
</html>
