#imports das classes de negócio
from Curso import Curso
from Aluno import Aluno
from Professor import Professor
import sys

#inicialização de variáveis e objetos
lista_opcoes = [   "0-) Sair \n"
                  ,"1-) Ver lista de alunos"
                  ,"2-) Incluir um novo aluno"
                  ,"3-) Excluir um aluno existente"
                  ,"4-) Ver um aluno"
                  ,"5-) Ver lista de professor"
                  ,"6-) Incluir um novo professor"
                  ,"7-) Excluir um professor existente"
                  ,"8-) Ver um professor"
                  ,"9-) Ver lista de cursos"
                  ,"10-) Incluir um novo curso"
                  ,"11-) Excluir um curso existente"
                  ,"12-) Ver um curso"]

lista_professores = []
lista_alunos = []
lista_cursos = []

#Iteração com o usuário e dar as boas vindas
nome_login = input("Olá! Por favor entre com o nome de usuário...\n")

#Loop para manter na memória
while True:
    #Mostrar as boas vindas e as opções
    print(f"Olá! Seja bem-vinde {nome_login}! Escolha uma opção:")
    for opcao in lista_opcoes:
        print(opcao)
    opcao_selecionada = int(input("Escolha uma opção \n"))
    #condicionais para controlar a navegação do programa
    if opcao_selecionada == 0: #Sai do programa
        print("Você saiu do sistema.")
        sys.exit()
    elif opcao_selecionada == 1: #Ver lista de alunos
        for aluno in lista_alunos:
            print(f"{aluno.nome} - {aluno.matricula}")
    elif opcao_selecionada == 2: #Incluir um novo aluno
        
        while True:
            nome_aluno = input("Digite o nome do Aluno\n")
            matricula_aluno = input("Digite a matrícula do Aluno\n")
            documento_aluno = input("Digite o número do documento\n")
            aluno = Aluno(nome=nome_aluno,documento=documento_aluno,matricula=matricula_aluno) #Incluindo o documento no momento do construtor
            lista_alunos.append(aluno) #Insere um aluno na lista
            print(f"O aluno {aluno.nome} foi inserido!")  #Mostra para o usuário que o append foi feito      
            
            #Solicitando a saída para o usuário    
            controle_insert = input("Deseja incluir mais um aluno? (Digite 'n' ou 'N' para sair) \n")
            if len(controle_insert) == 1:
                if controle_insert == "n" or controle_insert == "N" or controle_insert == "S" or controle_insert == "s":
                    if controle_insert.upper() == "N":
                        print("Saíndo da inclusão de alunos...")
                        break
        
    elif opcao_selecionada == 3: #Excluir um aluno existente
        
        while True:
            iterador_alunos = 0 
            max_alunos = len(lista_alunos)
            while iterador_alunos < max_alunos: #Outra forma de fazer loop em lista
                print(f"Índice - {iterador_alunos} - {lista_alunos[iterador_alunos].nome}")
                iterador_alunos += 1
            input_do_usuario = input("Digite um valor para a exclusão do aluno \n")
            
            if input_do_usuario.isnumeric():
                aluno_selecionado = int(input_do_usuario) #Solicite para o usuário o índice
                if aluno_selecionado in range(0, max_alunos):
                    aluno_excluido = lista_alunos.pop(aluno_selecionado) #pop para excluir o aluno e retornar o objeto excluído
                    print(f"O aluno {aluno_excluido.nome} foi excluído") #mostra para o usuário
                   
                    #Solicitando a saída para o usuário    
                    controle_exclusao = input("Deseja sair da exclusão? (Digite 's' ou 'S' para sair) \n")
                    if len(controle_exclusao) == 1:
                        if controle_exclusao == "n" or controle_exclusao == "N" or controle_exclusao == "S" or controle_exclusao == "s":
                            if controle_exclusao.upper() == "S":
                                print("Saíndo da exclusão de alunos...")
                                break
                else:
                    print("Esse valor não existe")
            else:
                print("Esse valor deve ser um número")
                    
    elif opcao_selecionada == 4: #Ver um aluno
        while True:
            nome_aluno_pesquisado = input("Digite o nome do aluno a ser pesquisado \n")
            controle_iteracao = 0
            for aluno in lista_alunos:
                if nome_aluno_pesquisado.upper() in aluno.nome.upper():
                    print(f"O aluno {aluno.nome} com a {aluno.matricula} e o documento {aluno.documento} consta na lista.")
                    controle_iteracao += 1
            if controle_iteracao == 0:
                print("O aluno não foi encontrado")

            #Solicitando a saída para o usuário    
            controle_pesquisa = input("Deseja sair da pesquisa? (Digite 's' ou 'S' para sair) \n")
            if len(controle_pesquisa) == 1:
                if controle_pesquisa == "n" or controle_pesquisa == "N" or controle_pesquisa == "S" or controle_pesquisa == "s":
                    if controle_pesquisa.upper() == "S":
                        print("Saíndo da pesquisa de alunos...")
                        break
            
    elif opcao_selecionada == 5: #Ver lista de professor
        for professor in lista_professores:
            print(f'{professor.nome} - {professor.disciplina}')

    elif opcao_selecionada == 6: #Incluir um novo professor  
        while True:
            nome_professor = input("Digite o nome do Professor\n")
            disciplina_professor = input("Digite a disciplina do professor: ")
            professor = Professor(nome=nome_professor,disciplina=disciplina_professor) #Incluindo o documento no momento do construtor
            lista_professores.append(professor) #Insere um professor na lista
            print(f"O professor {professor.nome} foi inserido!")  #Mostra para o usuário que o append foi feito      
            
            #Solicitando a saída para o usuário    
            controle_insert = input("Deseja incluir mais um professor? (Digite 'n' ou 'N' para sair) \n")
            if len(controle_insert) == 1:
                if controle_insert == "n" or controle_insert == "N" or controle_insert == "S" or controle_insert == "s":
                    if controle_insert.upper() == "N":
                        print("Saíndo da inclusão de professores...")
                        break


    elif opcao_selecionada == 7: #Excluir um professor existente
        while True:
            iterador_professores = 0 
            max_professores = len(lista_professores)
            while iterador_professores < max_professores: #Outra forma de fazer loop em lista
                print(f"Índice - {iterador_professores} - {lista_professores[iterador_professores].nome}")
                iterador_professores += 1
            input_do_usuario = input("Digite um valor para a exclusão do professor \n")
            
            if input_do_usuario.isnumeric():
                professor_selecionado = int(input_do_usuario) #Solicite para o usuário o índice
                if professor_selecionado in range(0, max_professores):
                    professor_excluido = lista_professores.pop(professor_selecionado) #pop para excluir o professor e retornar o objeto excluído
                    print(f"O Professor {professor_excluido.nome} foi excluído") #mostra para o usuário

                    #Solicitando a saída para o usuário    
                    controle_exclusao = input("Deseja sair da exclusão? (Digite 's' ou 'S' para sair) \n")
                    if len(controle_exclusao) == 1:
                        if controle_exclusao == "n" or controle_exclusao == "N" or controle_exclusao == "S" or controle_exclusao == "s":
                            if controle_exclusao.upper() == "S":
                                print("Saíndo da exclusão de alunos...")
                                break
                else:
                    print("Esse valor não existe")
            else:
                print("Esse valor deve ser um número")
                    

    elif opcao_selecionada == 8: #Ver um professor
        while True:
            nome_professor_pesquisado = input("Digite o nome do professor a ser pesquisado \n")
            controle_iteracao = 0
            for professor in lista_professores:
                if nome_professor_pesquisado.upper() in professor.nome.upper():
                    print(f"O professor {professor.nome} da disciplina {professor.disciplina} consta na lista.")
                    controle_iteracao += 1
            if controle_iteracao == 0:
                print("O professor não foi encontrado")

                #Solicitando a saída para o usuário    
            controle_pesquisa = input("Deseja sair da pesquisa? (Digite 's' ou 'S' para sair) \n")
            if len(controle_pesquisa) == 1:
                if controle_pesquisa == "n" or controle_pesquisa == "N" or controle_pesquisa == "S" or controle_pesquisa == "s":
                    if controle_pesquisa.upper() == "S":
                        print("Saíndo da pesquisa de alunos...")
                        break

    elif opcao_selecionada == 9: #Ver lista de cursos
        pass
    elif opcao_selecionada == 10: #Incluir um novo curso
        pass
    elif opcao_selecionada == 11: #Excluir um curso existente
        pass
    elif opcao_selecionada == 12: #Ver um curso
        pass











