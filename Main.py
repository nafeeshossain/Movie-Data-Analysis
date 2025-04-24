import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('/content/movie_metadata.csv')

# Clean the data
df_clean = df[['movie_title', 'genres', 'title_year', 'imdb_score']].copy()
df_clean.dropna(inplace=True)
df_clean['title_year'] = df_clean['title_year'].astype(int)

# Top 10 rated movies
top_movies = df_clean.sort_values(by='imdb_score', ascending=False).head(10)

# Plot 1: Top 10 movies by rating
plt.figure(figsize=(10, 6))
sns.barplot(x='imdb_score', y='movie_title', data=top_movies, palette='magma')
plt.title('Top 10 Rated Movies on IMDb')
plt.xlabel('IMDb Score')
plt.ylabel('Movie Title')
plt.tight_layout()
plt.show()

# Plot 2: Genre distribution
plt.figure(figsize=(12, 6))
genre_counts = df_clean['genres'].str.split('|').explode().value_counts().head(10)
sns.barplot(x=genre_counts.values, y=genre_counts.index, palette='viridis')
plt.title('Top 10 Most Common Genres')
plt.xlabel('Number of Movies')
plt.ylabel('Genre')
plt.tight_layout()
plt.show()

# Plot 3: IMDb Rating distribution
plt.figure(figsize=(10, 5))
sns.histplot(df_clean['imdb_score'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of IMDb Ratings')
plt.xlabel('IMDb Rating')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Plot 4: Ratings vs Release Year
plt.figure(figsize=(12, 6))
sns.scatterplot(x='title_year', y='imdb_score', data=df_clean, alpha=0.6)
plt.title('IMDb Rating vs Release Year')
plt.xlabel('Release Year')
plt.ylabel('IMDb Rating')
plt.tight_layout()
plt.show()
