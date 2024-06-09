from sympy import symbols, Or, And, Not, simplify_logic

def karnaugh_map(text):
    # Convertendo o texto em uma lista de inteiros
    truth_table = eval(text)
    
    # Verificando o número de variáveis na tabela verdade
    num_variables = len(bin(len(truth_table) - 1)[2:])
    
    # Criando símbolos para as variáveis
    variables = symbols(' '.join(chr(65 + i) for i in range(num_variables)))  # A, B, C, D, ...
    
    # Inicializando a expressão lógica
    expression = Or(*[
        And(*[
            (variables[j] if row & (1 << (num_variables - 1 - j)) else Not(variables[j]))
            for j in range(num_variables)
        ])
        for row, value in enumerate(truth_table) if value
    ])
    
    # Simplificando a expressão lógica
    simplified_expression = simplify_logic(expression)
    
    return str(simplified_expression)
