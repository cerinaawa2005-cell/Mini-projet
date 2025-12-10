import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Pour que les graphiques s'affichent bien dans Streamlit
sns.set_style("whitegrid")

# 1. Charger les données (avec cache pour ne pas recharger tout le temps)
@st.cache_data
def load_data():
    df = pd.read_csv("../Data/netflix_titles.csv")
    return df

df = load_data()

# 2. Titre et description
st.title("Mini-projet Netflix")
st.write(
    "Application interactive pour explorer le catalogue Netflix : "
    "répartition films/séries, genres, pays et évolution des ajouts."
)

# 3. Petit aperçu du dataset
st.subheader("Aperçu du dataset")
st.dataframe(df.head())

# 4. Répartition Films vs Séries
st.subheader("Répartition des films et des séries")

type_counts = df["type"].value_counts()

fig1, ax1 = plt.subplots(figsize=(4, 3))
sns.barplot(x=type_counts.index, y=type_counts.values, ax=ax1)
ax1.set_xlabel("Type de contenu")
ax1.set_ylabel("Nombre de titres")
ax1.set_title("Films vs Séries sur Netflix")
st.pyplot(fig1)

# 5. Top 10 des genres
st.subheader("Top 10 des genres les plus populaires")

all_genres = df["listed_in"].str.split(", ")
genres_flat = [genre for row in all_genres.dropna() for genre in row]
genres_series = pd.Series(genres_flat)
top_genres = genres_series.value_counts().head(10)

fig2, ax2 = plt.subplots(figsize=(6, 4))
sns.barplot(x=top_genres.values, y=top_genres.index, ax=ax2)
ax2.set_xlabel("Nombre de titres")
ax2.set_ylabel("Genre")
ax2.set_title("Top 10 des genres")
st.pyplot(fig2)

# 6. Évolution des ajouts par année
st.subheader("Évolution des ajouts de contenus sur Netflix")

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["year_added"] = df["date_added"].dt.year

year_added_counts = df["year_added"].value_counts().sort_index()

fig3, ax3 = plt.subplots(figsize=(8, 4))
sns.lineplot(x=year_added_counts.index, y=year_added_counts.values, ax=ax3)
ax3.set_xlabel("Année d'ajout")
ax3.set_ylabel("Nombre de titres")
ax3.set_title("Nombre de titres ajoutés par année")
st.pyplot(fig3)

st.write("Fin de l'exploration – tu peux jouer avec les graphiques et scroller !")
