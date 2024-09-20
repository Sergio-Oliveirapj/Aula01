CONSTANTE_BONUS = 1000

# Solicita ao usuario que digite seu nome:
nome_usuario = input ("Digite o seu nome:")

# Solite ao usuario que digite seu salario:
salario_usuario = float( input ( "Digite o seu salario:" ) )

# Solicite ao usuario que digite seu bonus:
bonus_usuario = float ( input ( "Digite o seu bonus:" ) )

# Calcule o valor final do bonus:
valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# Resultado
print ( f"O usuario {nome_usuario} tem o bonus de R$ {valor_do_bonus}")