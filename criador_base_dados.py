
import zlib # para descompactar o arquivo zip
import sys # soluções de encoding utf8 do texto
import sqlite3 #abrir arquivo como csv e salvar como base de dados sqlite3
import timeit #informa o tempo de execução da pesquisa
import winsound # aviso sonoro no final da execução do script
import os
import suprocess
###########################################################################################

# é necessario atualizar o arquivo sqlite3.dll para um que permite fts3. basta copiar o arquivo correto para a pasta do python. ex: C:\anaconda3\DLLs

###########################################################################################

# download do site pelo modulo homura

print ("________________________________________________________________________________")
print ("CRIADOR DE BASE DE DADOS PARA CARGOS TCE-PB. 05.04.2017")
print ("Aperte CTRL+C para cancelar o programa, ou feche a janela")
print ("________________________________________________________________________________\n")

start_time = timeit.default_timer()


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

filename = "aria2c.exe"
filename_opcoes = " --file-allocation=none --conditional-get=true --lowest-speed-limit=4k  --max-tries=20 "
#--conditional-get=true --lowest-speed-limit=4k 
arquivo_municipal = "http://dados.tce.pb.gov.br/TCE-PB-SAGRES-Folha_Pessoal_Esfera_Municipal.txt.gz"
arquivo_estadual = 'http://dados.tce.pb.gov.br/TCE-PB-SAGRES-Folha_Pessoal_Esfera_Estadual.txt.gz'

print('###########################################')
print('Fazendo download: ',arquivo_municipal)
print('###########################################')

execucao = filename +  filename_opcoes + arquivo_municipal
download = os.system(resource_path(execucao))

print('\n\n')
print('###########################################')
print('Fazendo download: ',arquivo_estadual)
print('###########################################')
execucao = filename +  filename_opcoes + arquivo_estadual
download = os.system(resource_path(execucao))
print('')
print('')
print('  Download completo.')

print("--- %s minutos ---" % "{0:.3f}".format(float((timeit.default_timer() - start_time))/60))

# decompacta arquivos

start_time = timeit.default_timer()
CHUNKSIZE=1024
           
d = zlib.decompressobj(16+zlib.MAX_WBITS)
fm = open('TCE-PB-SAGRES-Folha_Pessoal_Esfera_Municipal.txt.gz', 'rb')            
fm_out = open('TCE-PB-SAGRES-Folha_Pessoal_Esfera_Municipal.txt','wb')
print ('\n\nIniciando descompressão Folha Municipal.....')
buffer=fm.read(CHUNKSIZE)

while buffer:
  outstr = d.decompress(buffer)
  fm_out.write(outstr)
  buffer=fm.read(CHUNKSIZE)

outstr = d.flush()


fm.close()
fm_out.close()
print ('Iniciando descompressão Folha Municipal.....ok!')
print("--- %s minutos ---" % "{0:.3f}".format(float((timeit.default_timer() - start_time))/60))
start_time = timeit.default_timer()
print ('Iniciando descompressão Folha Estadual.....')

fe = open('TCE-PB-SAGRES-Folha_Pessoal_Esfera_Estadual.txt.gz', 'rb')            
fe_out = open('TCE-PB-SAGRES-Folha_Pessoal_Esfera_Estadual.txt','wb')

buffer1=fe.read(CHUNKSIZE)
d1 = zlib.decompressobj(16+zlib.MAX_WBITS) # não é uma configuração, ele cria um stream de dados. É necessário um novo stream porque é um arquivo diferente.
while buffer1:
  outstr = d1.decompress(buffer1)
  fe_out.write(outstr)
  buffer1=fe.read(CHUNKSIZE)

outstr = d.flush()

fe.close()
fe_out.close()

print ('Iniciando descompressão Folha Estadual.....ok!')
print("--- %s minutos ---" % "{0:.3f}".format(float((timeit.default_timer() - start_time))/60))
# cria base de dados

start_time = timeit.default_timer()

print ('\n\nCriando base de dados (arquivo folhapessoal.db).... \n\n')
print ('Inserindo Folha do Município (12 minutos) na base de dados....')

try: os.remove('Folhapessoal.db')
except: pass

conn = sqlite3.connect("Folhapessoal.db")
curs = conn.cursor()


#modifiquei ordem das colunas para que fique similar ao arquivo do municipio. retirei a coluna cd_udgestora por ser desnecessário.
subprocess.call(['sqlite3.exe','FolhaPessoal.db','.separator','|','.import','TCE-PB-SAGRES-Folha_Pessoal_Esfera_municipal.txt','Folhamunicipio'])

print ('Inserindo Folha do Município (12 minutos) na base de dados....ok!!!')
print("--- %s minutos ---" % "{0:.3f}".format(float((timeit.default_timer() - start_time))/60))

start_time = timeit.default_timer()

print ('Inserindo Folha do Estado(8 minutos) na base de dados....')

subprocess.call(['sqlite3.exe','FolhaPessoal.db','.separator','|','.import','TCE-PB-SAGRES-Folha_Pessoal_Esfera_estadual.txt','Folhaestado'])

print ('Inserindo Folha do Estado(8 minutos) na base de dados... ok!!!')
print("--- %s minutos ---" % "{0:.3f}".format(float((timeit.default_timer() - start_time))/60))


start_time = timeit.default_timer()

print ('Criando tabela FTS3 Município (12 minutos)....')


# cria indexes para as tabelas (retirado em razão da desnecessidade por conta do fts3)
#curs.execute('CREATE INDEX cpfmunicipio on folhamunicipio(cpf);')
#curs.execute('CREATE INDEX cpfestado on folhaestado(cpf);')
# cria modulo para as tabelas



curs.execute('CREATE VIRTUAL TABLE pesquisamunicipio USING fts3(servidor, cpf, cargo, natureza, mesanoreferencia, poder, orgao, tokenize=unicode61);')
curs.execute('CREATE VIRTUAL TABLE pesquisaestado USING fts3(servidor, cpf, cargo, natureza, mesanoreferencia, poder, orgao, dataadmissao, tokenize=unicode61);')
# insere dados

curs.execute('INSERT INTO pesquisamunicipio SELECT servidor, cpf, cargo, natureza, mesanoreferencia, municipio, orgao FROM folhamunicipio;')
print ('Criando tabela FTS3 Município (12 minutos)....ok!')
print("--- %s minutos ---" % "{0:.3f}".format(float((timeit.default_timer() - start_time))/60))

start_time = timeit.default_timer()
print ('Criando tabela FTS3 Estado (8 minutos)....')

curs.execute('INSERT INTO pesquisaestado SELECT servidor, cpf, cargo, natureza, mesanoreferencia, poder, orgao, dataadmissao FROM folhaestado;')
conn.commit()
conn.close()
print ('Criando tabela FTS3 Estado (8 minutos)....ok!')
print("--- %s minutos ---" % "{0:.3f}".format(float((timeit.default_timer() - start_time))/60))


winsound.Beep(500,300)
winsound.Beep(600,500)

input('Encerrado! Pressione Enter para sair do programa')


            
            
