dados = {}
funcionarios = []
try:
    # Menu
    def menu() :
        print("=-=-"*11)
        print("********  Cadastro de Funcionários  *******")
        option = int(input(" [1] - Cadastrar um funcionário \n [2] - Listar o(s) funcionário(s) \n [3] - Editar Funcionário \n [4] - Excluir um funcionário \n [5] - Adicionar aumento salarial \n [6] - Sair do programa \n Digite a opção: "))
        print("*******************************************")
        
        return option
    # Cadastro de dados dos funcionários 
    def cadastra_funcionario():
        import random
        codigo = random.randint(1, 100)
        if codigo in dados:
            print("O Funcionário já está cadastrado !")
        else:
            nome = input("Nome do funcionário :")
            email = input("Email do funcionário :")
            dataDeAdmissao = input("Data de admissão do funcionário ---> dd/mm/aaaa :")
            salario = int(input("Salário do funcionário :"))
            funcionariosdados = [codigo, nome, email, dataDeAdmissao, salario]
            funcionarios.append(funcionariosdados)
            dados[codigo] = [nome,email,dataDeAdmissao,salario]
            print("=-=-"*11)
            print("Funcionário cadastrados com sucesso")
            
            #print(dados)
            #print(funcionarios)

    # Listar funcionários 
    def mostrar_funcionarios() :
        for funcionario in funcionarios:
            
            print(f" Código do funcionário: {funcionario[0]} Nome: {funcionario[1]} E-mail: {funcionario[2]} Data Admissão: {funcionario[3]} Salário R$: {funcionario[4]}")
            
    # Deletar funcionários
    def remover():
        codigo=int(input("Digite o código do funcionário :"))
        if codigo in dados:
            del dados [codigo]
            for funcionario in funcionarios:
                funcionarios.remove(funcionario)
            print("=-=-"*11)
            print("Funcionario removido com sucesso!")
            
        else:
            print("=-=-"*11)
            print("Funcionário não encontrado. Tentar novamente!")
            
    # Editar os funcionários
    def edit():
        codigo=int(input("Digite o codigo do funcionario:"))
        if codigo in dados:
            for funcionario in funcionarios:
                funcionarios.remove(funcionario)
                import random
                codigo = random.randint(1, 100)
                nome = input("Nome do funcionário :")
                email = input("E-mail do funcionário :")
                dataDeAdmissao = input("Data de admissão do funcionário--->dd/mm/aaaa :")
                salario = input("Salário do funcionário :")
                funcionariosdados = [codigo, nome, email, dataDeAdmissao, salario]
                funcionarios.append(funcionariosdados)
                dados[codigo] = [nome,email,dataDeAdmissao,salario]
                #dados[codigo] = [nome,email,dataDeAdmissao,salario]
                #dados.append(funcionarios)
                print("=-=-"*11)
                print("Alterações feitas com sucesso!")
                print("=-=-"*11)
                #print(dados[func][3])
                print(dados)
        else:
            print("=-=-"*11)
            print("ERRO ao alterar - REPETIR PROCESSO!")
            print("=-=-"*11)
    
    # Modificando o salário        
    def editsalario():
        for funcionario in funcionarios:
            print(f" Código do funcionário: {funcionario[0]} Nome: {funcionario[1]} E-mail: {funcionario[2]} Data Admissão: {funcionario[3]} Salário R$: {funcionario[4]}")
            print("=-=-"*11)
            func = int(input("Digite o código do funcionário :"))
            dados[func][3]= dados[func][3] + (int(input("Digite o valor a ser adicionado ao salário do funcionário :")))
            print(funcionarios)
            funcionarios[0][4]= dados[func][3]
            print("=-=-"*11)
            print("Valor adicionado com sucesso")
            #print(dados[func][3])
            #print(dados)

#Funções e variáveis
    def programa() :

        while True:
            option = menu()

            if option == 1 :
                cadastra_funcionario()
            if option == 2 :
                mostrar_funcionarios()
            if option == 3 :
                edit()
            if option == 4 :
                remover()
            if option == 5 :
                editsalario()
            elif option == 6 :
                print("Até breve. Volte sempre!")    
                break
            print("=-=-"*11)
            
    programa()
except:
    print("=-=-"*11)
    print("ERRO. Verificar dados inseridos")
    print("=-=-"*11)