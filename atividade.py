import pandas as pd

# Carregando os csv em dataframes
filmes1 = pd.read_csv("tmdb_5000_movies.csv")
filmes2 = pd.read_csv("tmdb_5000_credits.csv")

# Exibindo as primeiras linhas de cada dataframe
print("Primeiras linhas do dataset 'tmdb_5000_movies.csv':")
print(filmes1.head())

print("\nPrimeiras linhas do dataset 'tmdb_5000_credits.csv':")
print(filmes2.head())
