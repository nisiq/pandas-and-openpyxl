import pandas as pd

arq = pd.read_excel('professores.xlsx')

profs = arq.loc[arq['cargo'] == 'PROFESSOR DO MAGISTERIO SUPERIOR']
x = profs['nome']
print(x)

