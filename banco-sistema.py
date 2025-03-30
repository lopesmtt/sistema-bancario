import os

# Função para limpar a tela dependendo do sistema operacional
def limpar_tela():
    sistema = os.name
    if sistema == 'posix':
        os.system('clear')  # Para sistemas Unix/Mac
    elif sistema == 'nt':
        os.system('cls')  # Para sistemas Windows

# Função para pausar a execução e pedir ao usuário para pressionar Enter
def pausar():
    input("\nPressione Enter para continuar...")

# Início do programa
print('Bem-vindo ao seu programa de riqueza pessoal, iremos avaliar seu perfil e ajudar você na sua busca por excelência!')

# Parte 1: Solicitar as pontuações
dinheiro = int(input('Digite um valor de 0 a 10 para a pontuação que você acha que tem sobre sua vida financeira: '))
saude = int(input('Digite um valor de 0 a 10 para a pontuação que você acha que tem sobre sua saúde: '))
conhecimento = int(input('Digite um valor de 0 a 10 para a pontuação que você considera seu nível de conhecimento: '))
tempo = int(input('Digite um valor de 0 a 10 para a pontuação que você considera sua qualidade de tempo: '))
emocoes = int(input('Digite um valor de 0 a 10 para a pontuação que você considera a qualidade da sua vida emocional: '))

# Pausa antes de calcular a pontuação
pausar()

# Parte 2: Calcular pontuação
pontuacao_total = (dinheiro * saude * conhecimento * tempo * emocoes)
media = (dinheiro + saude + conhecimento + tempo + emocoes) / 5

# Limpar a tela após cálculo
limpar_tela()

# Exibir pontuação
print(f'\nSua pontuação total foi {pontuacao_total}')
print(f'Sua média geral foi {media:.2f}\n')

# Pausa para mostrar a avaliação
pausar()

# Parte 3: Avaliação baseada na pontuação
if pontuacao_total == 10000:
    print('Você chegou à excelência máxima, parabéns!')
elif pontuacao_total >= 5000:
    print('Ótimo, você está no caminho certo, continue!')
elif pontuacao_total >= 100:
    print('Você tem potencial, mas pode melhorar em algumas áreas.')
else:
    print('Há espaço para evolução, identifique os pontos e trabalhe neles.')

# Pausa para mostrar os pontos fracos
pausar()

# Parte 4: Mostrar pontos fracos
pontos_fracos = []
if dinheiro < 5:
    pontos_fracos.append("Vida Financeira")
if saude < 5:
    pontos_fracos.append("Saúde")
if conhecimento < 5:
    pontos_fracos.append("Conhecimento")
if tempo < 5:
    pontos_fracos.append("Qualidade de Tempo")
if emocoes < 5:
    pontos_fracos.append("Vida Emocional")

# Exibe os pontos fracos
if pontos_fracos:
    print("\nPontos fracos:", pontos_fracos)
    print("\nSugestões para seu desenvolvimento:")
    for ponto in pontos_fracos:
        print(f'Trabalhe mais em sua {ponto}')
    
    # Pergunta ao usuário se ele quer dicas
    resposta = input("\nVocê gostaria de receber dicas para melhorar esses pontos? (sim/não): ").strip().lower()

    if resposta == 'sim':
        print("\nAqui estão as dicas para melhorar seus pontos fracos:")
        if "Vida Financeira" in pontos_fracos:
            print("Para melhorar sua vida financeira, crie um orçamento mensal, reduza gastos desnecessários e busque investimentos inteligentes.")
        if "Saúde" in pontos_fracos:
            print("Para melhorar sua saúde, adote uma alimentação equilibrada, pratique exercícios físicos regularmente e cuide da sua mente.")
        if "Conhecimento" in pontos_fracos:
            print("Para aumentar seu conhecimento, leia livros, faça cursos e mantenha-se sempre aprendendo algo novo.")
        if "Qualidade de Tempo" in pontos_fracos:
            print("Para gerenciar melhor seu tempo, crie uma rotina organizada, elimine distrações e estabeleça prioridades.")
        if "Vida Emocional" in pontos_fracos:
            print("Para melhorar sua vida emocional, pratique a gratidão, medite e fortaleça seus relacionamentos com pessoas positivas.")
    else:
        print("\nTudo bem! Continue sua jornada de evolução no seu ritmo.")
else:
    print("\nParabéns! Você está equilibrado em várias áreas.")

# Parte 5: Finalização
pausar()
limpar_tela()
print('\nObrigado por usar nosso programa, continue evoluindo!')