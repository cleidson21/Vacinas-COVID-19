#Autor: Cleidson Ramos de Carvalho
#Componente Curricular: MI - Algoritmos I
#Concluido em: 20/03/2021
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

#Programa para cadastro e relatorio de vacinação Covid-19 em Feira de Santana

print('\nBem vindo ao programa de cadastro de vacinados Covid-19 em Feira de Santana!\n')
local = input('Informe o local da vacinação: ')
data = input('Informe a data da vacinação (dd/mm/aaaa): ')
nomeT = 0
sexoM = 0
sexoF = 0
sexoO = 0
grupoI = 0
grupoO = 0
turnoM = 0
turnoT = 0
vacinaC = 0
vacinaO = 0
doseC1 = 0
doseC2 = 0
doseA1 = 0
doseA2 = 0
funcao = input('Informe a operação que deseja realizar:\n[1] Novo Cadastro \n[2] Relatórios \n[3] Sair \n')
while (funcao != '3'):
    if (funcao == '1'):
        print('\n*CADASTRO!\n')
        nome = input('Digite o nome do vacinado: ')
        nomeT += 1
        cpf = input('Informe o CPF do vacinado: ')
        vacina = (input('Informe o fabricante da vacina tomada: \n[1] CORONAVAC; \n[2] ASTRAZENECA, \n'))
        while True: #Optei por utilizar o "True" como condicional, pois a entrada neste loop é obrigatoria e fiz a utilização do "break" para saida
            if vacina == '1':
                vacinaC += 1
                dose = input('Informe a dose: \n[1] Primeira dose; \n[2] Segunda dose \n')
                while True:
                    #Caso for a primeiro dose os dados pessoais do vacinado é pedido
                    if dose == '1':
                        doseC1 += 1
                        sexo = input('Informe o genero: [1] para masculino e [2] para feminino e [3] para outros: ')
                        while True:
                            if sexo == '1':
                                sexoM += 1
                                break #Saída do loop do sexo
                            elif sexo == '2':
                                sexoF += 1
                                break #Saída do loop do sexo
                            elif sexo == '3':
                                sexoO += 1
                                break #Saída do loop do sexo
                            print('Opção invalida!')
                            sexo = input('Informe o genero: [1] para masculino e [2] para feminino: ')
                        grupo = input('Informe o Grupo Prioritário: \n[1] para Idosos acima de 60 anos; \n[2] Outros; ')
                        while True:
                            if grupo == '1':
                                grupoI += 1
                                break #Saída do loop do grupo
                            elif grupo == '2':
                                grupoO += 1
                                break #Saída do loop do grupo
                            print('Opção invalida!')
                            grupo = input('Informe o Grupo Prioritário: \n[1] para Idosos acima de 60 anos;; \n[2] Outros; ')
                        turno = input('Informe o turno da vacinação: [1] para manhã e [2] para tarde: ')
                        while True:
                            if turno == '1':
                                turnoM += 1
                                break #Saída do loop do turno
                            elif turno == '2':
                                turnoT += 1
                                break #Saída do loop do turno
                            print('Turno invalido!')
                            turno = input('Informe o turno da vacinação: [1] para manhã e [2] para tarde: ')
                        break #Saída do loop da dose 1 CORONAVAC
                    # Caso for a segunda dose, apenas o horario da vacina é pedido
                    elif dose == '2':
                        doseC2 += 1
                        print('\nDados pessoais do Usuario já cadastrado!\n')
                        turno = input('Informe o turno da vacinação: [1] para manhã e [2] para tarde: ')
                        while True:
                            if turno == '1':
                                turnoM += 1
                                break #Saída do loop do turno
                            elif turno == '2':
                                turnoT += 1
                                break #Saída do loop do turno
                        break #Saída do loop da dose 2 CORONAVAC
                    print('Opção invalida!')
                    dose = input('Informe a dose: \n[1] Primeira dose; \n[2] Segunda dose \n')
                break #Saída do loop da vacina CORONAVAC
            elif vacina == '2':# Incio das condicionais da vacina ASTRAZENICA
                vacinaO += 1
                dose = input('Informe a dose: \n[1] Primeira dose; \n[2] Segunda dose \n')
                while True:
                    #Caso for a primeiro dose os dados pessoais do vacinado é pedido
                    if dose == '1':
                        doseA1 += 1
                        sexo = input('Informe o genero: [1] para masculino e [2] para feminino e [3] para outros: ')
                        while True:
                            if sexo == '1':
                                sexoM += 1
                                break #Saída do loop do sexo
                            elif sexo == '2':
                                sexoF += 1
                                break #Saída do loop do sexo
                            elif sexo == '3':dff
                                sexoO += 1
                                break #Saída do loop do sexo
                            print('Opção invalida!')
                            sexo = input('Informe o genero: [1] para masculino e [2] para feminino e [3] para outros: ')
                        grupo = input('Informe o Grupo Prioritário: \n[1] para Idosos acima de 60 anos;; \n[2] Outros; ')
                        while True:
                            if grupo == '1':
                                grupoI += 1
                                break #Saída do loop do grupo
                            elif grupo == '2':
                                grupoO += 1
                                break #Saída do loop do grupo
                            print('Opção invalida!')
                            grupo = input('Informe o Grupo Prioritário: \n[1] para Idosos acima de 60 anos; \n[2] Outros; ')
                        turno = input('Informe o turno da vacinação: [1] para manhã e [2] para tarde: ')
                        while True:
                            if turno == '1':
                                turnoM += 1
                                break #Saída do loop do turno
                            elif turno == '2':
                                turnoT += 1
                                break #Saída do loop do turno
                            print('Turno invalido!')
                            turno = input('Informe o turno da vacinação: [1] para manhã e [2] para tarde: ')
                        break #Saída do loop da dose 1 ASTRAZENECA

                    elif dose == '2': # Caso for a segunda dose, apenas o horario da vacina é pedido
                        doseA2 += 1
                        print('\nDados pessoais do Usuario já cadastrado!\n')
                        turno = input('Informe o turno da vacinação: [1] para manhã e [2] para tarde: ')
                        while True:
                            if turno == '1':
                                turnoM += 1
                                break
                            elif turno == '2':
                                turnoT += 1
                                break
                        break #Saída do loop da dose 2 ASTRAZENECA
                    print('Opção invalida!')
                    dose = input('Informe a dose: \n[1] Primeira dose; \n[2] Segunda dose \n')
                break #Saída do loop da vacina ASTRAZENECA
            print('Opção invalida!')
            vacina = (input('Informe o fabricante da vacina tomada: \n[1] CORONAVAC; \n[2] ASTRAZENECA, \n'))
        registro = input('Informe o registro da vacina: ')
        print('\n*CADASTRO EFETUADO COM SUCESSO!\n') #Fim do cadastro dos vacinados   
    elif (funcao == '2'): #Inicio dos relatorios
        if doseC1 == 0 and doseA1 == 0 : #condicional necessaria para evitar erro de divisão por 0.
            print('\nDados insuficientes para todos os relatorios!\n')
        else:
            totalvacinado = doseC1 + doseA1 #total de vacinados no dia,(as segundas doses não são inclusas por ficar entendido que já tomou a primeira dose)
            totaldose = vacinaC + vacinaO # Total de vacinas idependentes de qual dose tomou
            dose1 = doseC1 + doseA1 # Total da Primeira dose das vacinas
            dose2 = doseC2 + doseA2 # Total da Segunda dose das vacinas
            porcCoro = (100 * vacinaC)/ totaldose #Percentual da vacina CORONAVAC
            porcAstra = (100 * vacinaO)/ totaldose #Percentual da vacina ASTRAZENECA
            porcIdoso = (100 * grupoI) / totalvacinado #Percentual de idosos por vacinados do dia
            porcManha = (100 * turnoM) / totaldose #Percentual de vacinados pela manha do dia
            porcTarde = (100 * turnoT) / totaldose #Percentual de vacinados pela tarde do dia
            porcHomem = (100 * sexoM) / totalvacinado #Percentual de vacinados do sexo masculino
            porcMulher = (100 * sexoF) / totalvacinado #Percentual de vacinados do sexo feminino
            porcOutro = (100 * sexoO) / totalvacinado #Percentual de vacinados de outro definição do sexo
            print('\nRelatório no %s, no dia %s. \n' % (local,data))
            print('Total de pessoas vacinadas é de %d e foram aplicadas %d doses.\n' % (totalvacinado, totaldose))
            print('Pessoas vacinadas na primeira dose: %d \nPessoas vacinadas na segunda dose: %d\n' % (dose1, dose2))
            print('Percentual de vacinados por vacina: CORONAVAC %0.2f %%,  ASTRAZENECA %0.2f %%\n' % (porcCoro, porcAstra))
            print('Percentual de idosos vacinados é %0.2f %%\n' % porcIdoso)
            print('Percentual de vacinados por Horario: Manhã %0.2f %%, Tarde %0.2f %%\n' % (porcManha, porcTarde))
            print('Percentual de vacinados por Sexo: Masculino %0.2f %%, Feminino %0.2f %%, Outro %0.2f %%\n' % (porcHomem, porcMulher, porcOutro))
            print('FIM DOS RELATORIOS!\n')         
    else:
        print('\n*Opção invalida!\n')
    funcao = input('Informe a operação que deseja realizar:\n[1] Novo Cadastro \n[2] Relatórios \n[3] Sair \n')
print('\n*SAINDO...\n') 
      
