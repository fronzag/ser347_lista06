import matplotlib.pyplot as plt

estados = [ 'Acre', 'Alagoas', 'Amapá', 'Amazonas',  'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Paraná', 'Paraíba', 'Pará', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'Sergipe', 'São Paulo', 'Tocantins']

pib2017 = [ 14271, 52843, 15480, 93204, 268661, 147890, 244683, 113352, 191899, 89524, 126805, 96372, 576199, 421375, 62387, 155195, 181551, 45359,  671362, 64295, 423151, 43506, 12103, 277192, 40704, 2119854, 34102]


plt.figure(figsize=(10, 8) )
plt.suptitle("PIB das Unidades da Federação brasileiras em 2017", fontsize=16)
plt.bar(estados, pib2017, align='center', color='gray', linewidth=2, edgecolor='black')
plt.xticks(estados, rotation='vertical')
plt.xlabel("Estados")
plt.ylabel("PIB em 2017 (1.000.000 R$)")

plt.subplots_adjust(bottom=0.3)
plt.show()
