import pandas as pd

# Carregando os csv em dataframes
filmes1 = pd.read_csv("tmdb_5000_movies.csv")
filmes2 = pd.read_csv("tmdb_5000_credits.csv")

# Combinando os dataframes usando a coluna "id"
filmes = pd.merge(filmes1, filmes2, left_on='id', right_on='movie_id')

# Selecionando as colunas relevantes
filmes_atores = filmes[['title_x', 'cast']]

# Criando um novo dataframe para organizar os atores por filme
filmeAtor = pd.DataFrame(columns=['Filme', 'Atores'])

# Preenchendo o dataframe com os pares de filme e ator
for index, row in filmes_atores.iterrows():
    filme = row['title_x']
    atores = [ator['name'] for ator in eval(row['cast'])]
    filmeAtor = pd.concat([filmeAtor, pd.DataFrame({'Filme': [filme], 'Atores': [', '.join(atores)]})])

# Exibindo alguns pares de filme e ator, com linhas em branco entre eles
print("\nPares de filme e ator:")
for index, row in filmeAtor.sample(5).iterrows():
    print(f"{row['Filme']} | {row['Atores']}\n")
