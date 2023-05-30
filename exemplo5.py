import pandas as pd

prof = pd.read_excel('professores.xlsx')

linhas = len(prof)
prof.loc[linhas+1, 'siape'] = int(input("ID: "))
prof.loc[linhas+1, 'nome'] = input("nome: ")
prof.loc[linhas+1, 'formacao'] = input("formação: ")

prof.to_excel('professores.xlsx', index=False)