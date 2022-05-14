#Mostre cada palavra e seu significado em uma saída, formate a saída de uma forma bem elegante.\
# Por exemplo: você pode exibir a palavra seguida de dois-pontos e depois o seu significado,\
# ou apresentar a palavra em uma linha e então exibir seu significado identado em uma segunda linha.\
# Utilize o caractere de quebra de linha (\n) para inserir uma linha em branco entre cada par palavra-significado em sua saída.


linguagens = {'html': 'uma linguagem de marcação!', 'python': 'a melhor linguagem!', 'java': 'um terror!', 'sql': 'um banco de dados!', 'vscode':"um editor de código!" }
for k, v in linguagens.items():
    print(f'O {k} é {v}\n')
