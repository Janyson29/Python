#Declaração
nome_completo = "Janyson Silva"

nome_completo_aspas = """Janyson
Silva"""

nome_completo_quebra = "Janyson \
Silva"

nome = "Janyson"
Sobrenome = "Silva"

#Formatação
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma): " + nome_completo)
print("Nome completo (3a forma): " + "Janyson " + "Silva")
print("Nome completo (4a forma): " + "Janyson", "Silva")
print("Nome completo (5a forma): ", nome_completo_aspas)
print("Nome completo (6a forma): ", nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (8a forma): %s %s" %(nome, Sobrenome))
print(f"Nome completo (9a forma): {nome} {Sobrenome}")
print("Nome completo (10a forma): {} {}". format(nome, Sobrenome))
