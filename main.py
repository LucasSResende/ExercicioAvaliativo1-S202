import Aula
import classes

aulas = Aula.ControleAulas()

comp1 = True
while(comp1 == True):

    print("1. Criar aula\n"
          "2. Editar aula\n"
          "3. Deletar aula\n"
          "4. Sair")
    op1 = input()

    if(op1 == '1'):
        assunto = input("Assunto da aula: ")
        aula = Aula(assunto)
        nomeProfessor = input("Nome do professor: ")
        especiProfessor = input("Especialidade do professor: ")
        professor = Professor(nomeProfessor,especiProfessor)
        aula.professor = professor
        print("Alunos presentes:")
        comp2 = True
        aula.alunos.clear()

        while(comp2 == True):

            nomeAluno = input("Nome aluno: ")
            matriculaAluno = input("Matricula: ")
            cursoAluno = input("Curso: ")
            periodoAluno = input("Período: ")
            aluno = Aluno(nomeAluno, matriculaAluno, cursoAluno, periodoAluno)
            aula.alunos.append(aluno)
            print("Próximo aluno: \n"
                  "1. Sim \n"
                  "2. Não")
            op2 = input()
            if(op2 == '2'):
                comp1 = False
                aulas.cria_aula(aula.assunto, aula.professor, aula.alunos)
                print("1. Voltar às opções: \n"
                      "2. Sair:")
                op10 = input()
                if(op10 == '2'):
                    comp1 = False


    elif(op1 == '2'):
        comp3 = True
        while(comp3 == True):
            cod = input("Código da aula a editar: ")
            print("Opçções de edição:\n"
                  "1. Assunto da aula\n"
                  "2. Professor da aula\n"
                  "3. Alunos em aula")
            op3 = input()
            if(op3 == '1'):
                print("Novo assunto:")
                novoAssunto = input()
                aulas.assunto_up(cod, novoAssunto)
                print("1. Editar outra aula \n"
                      "2. Voltar ás opções:\n"
                      "3. Sair:")
                op4 = input()
                if(op4 == '2'):
                    comp3 = False
                elif(op4 == '3'):
                    comp3 = False
                    comp1 = False

            elif(op3 == '2'):
                print("Novo professor")
                nomeProfessor = input("Nome: ")
                especiProfessor = input("Especialidade do professor: ")
                professor = Professor(nomeProfessor, especiProfessor)
                aulas.prof_up(cod,professor)
                print("1. Editar outra aula: \n"
                      "2. Voltar ás opções:\n"
                      "3. Sair:")
                op5 = input()
                if (op5 == '2'):
                    comp3 = False
                elif (op5 == '3'):
                    comp3 = False
                    comp1 = False

            elif(op3 == '3'):
                print("1. Alterar lista: \n"
                      "2. Adicionar um novo aluno a aula: \n"
                      "3. Remover um aluno da aula")
                op5 = input()
                if(op5 == '1'):
                    print("Alunos em aula: ")
                    comp4 = True
                    newAlunos: list[Aluno] = []
                    while (comp4 == True):
                        nomeAluno = input("Nome: ")
                        matriculaAluno = input("Matrícula: ")
                        cursoAluno = input("Curso: ")
                        periodoAluno = input("Período")
                        aluno = Aluno(nomeAluno, matriculaAluno, cursoAluno, periodoAluno)
                        newAlunos.append(aluno)
                        print("Entrar com novo aluno:\n"
                              "1. Sim\n"
                              "2. Não")
                        op2 = input()
                        if (op2 == '2'):
                            comp4 = False
                            aulas.turma_up(cod,newAlunos)
                            print("1. Editar outra aula\n"
                                  "2. Voltar ás opções:\n"
                                  "3. Sair:")
                            op6 = input()
                            if (op6 == '2'):
                                comp3 = False
                            elif (op6 == '3'):
                                comp3 = False
                                comp1 = False


                elif(op5 == '2'):
                    matriculaAluno = input("Matricula: ")
                    nomeAluno = input("Nome: ")
                    cursoAluno = input("Curso: ")
                    periodoAluno = input("Período: ")
                    aluno = Aluno(nomeAluno, matriculaAluno, cursoAluno, periodoAluno)
                    aulas.aluno_up(cod,aluno)
                    print("1. Editar novamente:\n"
                          "2. Voltar ás opções:\n"
                          "3. Sair:")
                    op7 = input()
                    if (op7 == '2'):
                        comp3 = False
                    elif (op7 == '3'):
                        comp3 = False
                        comp1 = False

                elif(op5 == '3'):
                    matriculaAluno = input("Código do aluno para remoção: ")
                    aulas.aluno_del(cod,matriculaAluno)
                    print("1. Editar outra aula: \n"
                          "2. Voltar ás opções: \n"
                          "3. Sair: ")
                    op8 = input()
                    if (op8 == '2'):
                        comp3 = False
                    elif (op8 == '3'):
                        comp3 = False
                        comp1 = False

    elif(op1 == '3'):
        comp4 = True
        while (comp4 == True):
            cod = input("Código da aula a remover: ")
            aulas.aula_del(cod)
            print("1. Apagar outra aula\n"
                  "2. Voltar ás opções:\n"
                  "3. Sair:")
            op9 = input()
            if (op9 == '2'):
                comp4 = False
            elif (op9 == '3'):
                comp4 = False
                comp1 = False

    elif(op1 == '4'):
        comp1 = False