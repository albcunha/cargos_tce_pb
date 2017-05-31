from time import time as time_time #informa o tempo de execução da pesquisa
import os.path #verifica se os arquivos estão na pasta 
from sys import argv as sys_argv # relacionado aos acentos
from sqlite3 import connect as sqlite3_connect# consulta da base de dados folhapessoal.db em sqlite3
from pandas import DataFrame as pd_dataframe #serve para salva o arquivos em formao xlsx
from pandas import concat as pd_concat
from pandas import ExcelWriter as pd_excelwriter

import xlsxwriter # altera a planilha para ficar mais agradável

print("________________________________________________________________________________")
print("CONSULTA CARGOS TCE-PB. 25.08.2015") 
print("________________________________________________________________________________\n")

WD = os.path.dirname(os.path.realpath(sys_argv[0]))
os.path.realpath(os.path.dirname(sys_argv[0]))


while True:
    if os.path.isfile('folhapessoal.db') is False:     
        pergunta1 = input("O arquivo folhapessoal.db não existe existe! Tentar novamente (S/N))?: ")
        if pergunta1.upper() == 'S' : 
            if os.path.isfile('folhapessoal.db') is True :
                break
            else: 
                print("O arquivo folhapessoal.db ainda não está na pasta. Precisa copiá-lo. Tente Novamente.")
                continue
        if pergunta1.upper() == 'N' :
            print("Saindo do programa....")
            input('ENTER para sair')
            sys.exit()
            
        else:
            continue
    if os.path.isfile('folhapessoal.db') is True:      
        break



print("________________________________________________________________________________")
print("Olá! \nA Pesquisa a pesquisa pode ser feita por Ente, CPF(sem pontuação) e nome. \nAbra o arquivo leia-me.txt para entender como funciona a consulta.  ") 
print("________________________________________________________________________________\n")


while True :
    while True:
        db = sqlite3_connect('folhapessoal.db') #abre base de dados
        cursor = db.cursor()        
        criterio_pesquisa = input('Pesquisa: ') 
        pergunta = criterio_pesquisa.replace(".","").replace("-","")
        pergunta = pergunta.strip()
        try:
            pergunta = str(int(pergunta))
            pass
        except:
            pass          
        if len(pergunta) == 0 : continue
           
        start_time = time_time()
        print()
        print("Pesquisando.... BASE MUNICIPAL E ESTADUAL")
        print()
        print()
        sql = "SELECT * FROM pesquisamunicipio WHERE pesquisamunicipio match ?"
        #atentar pra a virgula depois do input do usuario(pergunta), para torná-lo em tuple
        cursor.execute(sql,(pergunta,))
        municipio = pd_dataframe.from_dict(cursor.fetchall()) 
        if len(municipio) == 0:
            print()
            print('Municipio... Sem resultado')
            print()
        else:
            print(municipio[5], municipio[2],municipio[0])
            
        print()        
        print("terminado.""")
        print(("--- %s segundos ---" % (time_time() - start_time)))
        sql = "SELECT * FROM pesquisaestado WHERE pesquisaestado match ?"
        #consulta municipal
        #atentar pra a virgula depois do input do usuario(pergunta), para torná-lo em tuple
        cursor.execute(sql,(pergunta,))
        estado = pd_dataframe.from_dict(cursor.fetchall()) 
        if len(estado) == 0:
            print()
            print('Estado... Sem resultado')
            print()
        else:
            print(estado[6],estado[2],estado[0])
            
        resultado = pd_dataframe() 
        resultado = pd_concat([municipio,estado]) # retirei , ignore_index=True pra ver fica com a numeração da linha
        try : resultado.columns =['SERVIDOR', 'CPF', 'CARGO','NATUREZA', 'MES_ANO', 'PODER ESTADUAL_MUNICIPIO','ORGAO','ADMISSAO']
        except: pass
        try : resultado.columns =['SERVIDOR', 'CPF', 'CARGO','NATUREZA', 'MES_ANO', 'PODER ESTADUAL_MUNICIPIO','ORGAO']
        except: pass       
        print("terminado.""")
        print()        
        print('Linhas com os critérios selecionados nos Municípios: ',len(municipio.index), 'linhas')
        print('Linhas com os critérios selecionados no Estado: ',len(estado.index), 'linhas')
        print(("--- %s segundos ---" % (time_time() - start_time)))

           
    
        
    
 
        if resultado.empty:
            pass
        while True:
            pergunta2 = input('\nSalvar?(S/N)?: ')
            if pergunta2.upper() == 'S' :       
                pergunta = input('Nome do arquivo?: ')
                if len(pergunta) == 0:
                    print()
                    print("Arquivo invalido. Informe um nome para o arquivo....")
                    continue
                arquivosaida = str(pergunta) + '.xlsx'
                print("Salvando arquivo....",arquivosaida)
                if os.path.isfile(arquivosaida) is False:
                    with open(arquivosaida, 'w') as f:
                        writer = pd_excelwriter(arquivosaida, engine='xlsxwriter')
                        resultado.to_excel(writer, sheet_name='Folha de Pessoal TCE')                       
                        workbook  = writer.book
                        worksheet = writer.sheets['Folha de Pessoal TCE']                    
                        format = workbook.add_format({'border':1, 'text_wrap': True, 'valign':'top','align':'center'})                                    
                        format0 = workbook.add_format({'border':1, 'text_wrap': True, 'valign':'top', 'center_across':'left'})                                    
                        format1 = workbook.add_format({'border':1, 'num_format':'dd/mm/yyyy', 'align':'center'})      
                        #format2 = workbook.add_format({'border':1, 'align':'center','bg_color':'808080', 'pattern':1}) #não está funcionando.                                   
                        worksheet.set_column('B:B',35, format0)
                        worksheet.set_column('C:C',12, format)
                        worksheet.set_column('D:D',17, format0)
                        worksheet.set_column('E:E',15, format)
                        worksheet.set_column('F:F',9, format)
                        worksheet.set_column('G:G',35, format0)
                        worksheet.set_column('H:H',20, format)
                        worksheet.set_column('I:I',11, format1)                                    
                        #worksheet.set_row(0, 20, format2) # não está funcionando
                        writer.save()
                        writer.close()
                        f.close()
                        print()
                        print()
                        break
                try:
                    os.path.isfile(arquivosaida) is True     
                    pergunta1 = input("O arquivo já existe! Gravar por cima (S/N))?: ") 
                    if pergunta1.upper() == 'S' : 
                        try:
                            fresult = open(arquivosaida,'w') is True #testa pra ver se dá pra recriar o arquivo
                            with open(arquivosaida, 'w') as f:
                                writer = pd_excelwriter(arquivosaida, engine='xlsxwriter')
                                resultado.to_excel(writer, sheet_name='Folha de Pessoal TCE')                       
                                workbook  = writer.book
                                worksheet = writer.sheets['Folha de Pessoal TCE']                    
                                format = workbook.add_format({'border':1, 'text_wrap': True, 'valign':'top','align':'center'})                                    
                                format0 = workbook.add_format({'border':1, 'text_wrap': True, 'valign':'top', 'center_across':'left'})                                    
                                format1 = workbook.add_format({'border':1, 'num_format':'dd/mm/yyyy', 'align':'center'})      
                                #format2 = workbook.add_format({'border':1, 'align':'center','bg_color':'808080', 'pattern':1}) #não está funcionando.                                   
                                worksheet.set_column('B:B',35, format0)
                                worksheet.set_column('C:C',12, format)
                                worksheet.set_column('D:D',17, format0)
                                worksheet.set_column('E:E',15, format)
                                worksheet.set_column('F:F',9, format)
                                worksheet.set_column('G:G',35, format0)
                                worksheet.set_column('H:H',20, format)
                                worksheet.set_column('I:I',11, format1)                                    
                                #worksheet.set_row(0, 20, format2) # não está funcionando
                                writer.save()
                                writer.close()
                                f.close()                          
                                print("Salvando arquivo....",arquivosaida)
                                print()
                                print()
                        except:
                            print("O arquivo está aberto. Precisa Fechá-lo. Tente Novamente.")
                            break
                    break            
                    if pergunta1.upper() == 'N' :
                        break
                    else:
                        continue           
                except:  
                    pass
            if pergunta2.upper() == 'N' :
                break
            
            else: continue

    
 


