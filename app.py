import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

st.title("Better Ranking European Football Teams")

data = pd.read_csv("data_clean.csv")
data.drop("Unnamed: 0", inplace=True, axis = 1)
results = pd.read_csv("data_ranked.csv")
results.drop("Unnamed: 0", inplace=True, axis = 1)


def color_champ(val):
    if val == "ESP":
        color = '#ffed75'
    elif val == "FRA":
        color = "#78c8eb"
    elif val == "ITA":
        color = "#6bcf96"
    elif val == "ANG":
        color = "#f27278"
    else :
        color = ""
    return f'background-color: {color}'

st.write("## Notre Classement :")


st.write("### Données initiales après le Scraping")
st.dataframe(data)
st.markdown("ici figurent tous les critères que nous utiliserons dans notre analyse.")

st.markdown("### Equipes classées selon nos citères")
st.dataframe(results.style.applymap(color_champ, subset=['Championnat']))
st.markdown("Voici les résultats de notre classement final. On remarque que ce sont principalement les équipes espagnoles et anglaises qui figurent dans le haut du tableau, ce qui corrèle avec les coefficients.")
st.markdown("Au contraire, le bas du tableau est beaucoup plus hétérogène avec des équipes des 4 championnats.")
st.markdown("Les poids des coefficients de l'UEFA sont très lourds, on retrouve ainsi certaines équipes avec des performances décevantes comme le PSG qui ne figure pas dans le top 20.")


st.write("## Analyse des performance théoriques :")

df = data.copy()
df_agg = df.groupby("Championnat").mean()
df_agg.reset_index(inplace=True)

fig = px.scatter(df, x="ATT", y="DEF", color="Championnat", hover_name="Squad")
st.write("### Valeurs offensive et défensives théoriques des équipes")
st.plotly_chart(fig)
st.write("Dans ce premier graph on a plot le niveau théorique d'attaque et de défense des équipes. Les couleurs représentent les différents championnats. On remarque que les équipes françaises sont globalement moins fortes, et que les équipes anglaises ont en général une meilleure défense.")

fig = px.bar(df_agg, x="Championnat", y=["DEF", "ATT"])
st.write("### Valeurs offensive et défensives théoriques moyennes des championnats")
st.plotly_chart(fig)
st.write("On confirme les tendances remarquées en étudiant le niveau moyen des équipes par championnat : le championnat français est globalement en dessous, et le championnat anglais s'impose en attaque comme en défense.")


st.write("## Analyse du fair-play :")

fig = px.scatter(df, x="Fls", y="pts", color="Championnat", hover_name="Squad")
st.write("### Relation entre les nombre de points et le nombre de fautes commises par équipe")
st.plotly_chart(fig)
st.write("Ici on a plot en y le nombre de points récolté par une équipe, et en x le nombre de fautes commises. De manière générale, plus une équipe a de points, moins elle commet de fautes. On remarque également une différence au niveau des championnats : les équipes anglaises commettent moins de fautes.")

fig = px.bar(df_agg, x="Championnat", y=["CrdY", "Fls"])
st.write("### Nombre moyen de cartons jaunes reçus et de fautes commises par équipe par championnat")
st.plotly_chart(fig)
st.write("Ici on observe la quantité moyenne de fautes (rouge) et de cartons jaunes (bleu) par équipe pour chaque championnat. \nEst-ce que les équipes anglaises commettent moins de fautes car elles sont meilleures \? On ne peut pas dire ça. La raison la plus probable est l\'arbitrage en Angleterre est plus laxiste, c\'est un championnats physique où les fautes sont moins susceptibles d\'être sifflées. ")


st.write("## Analyse de notre classement :")

fig = px.scatter(results, x="rank_avg", y="rank_pts", color="Championnat", hover_name="Squad")
fig.update_layout(
    shapes=[
        {
            'type': 'line',
            'x0': 1,
            'y0': 1,
            'x1': 20,
            'y1': 20,
            'line': {
                'color': 'black',
                'width': 1.5
            }
        }
    ])
st.write("### Comparaison entre le rang moyen que nous avons calculé et le rang réel des équipes")
st.plotly_chart(fig)
st.write("Ici on compare la moyenne des classements que nous avons établi par rapport aux classements réels des équipes. La ligne noire est la ligne directrice, une équipe sur cette ligne a le même classement moyen des 7 critères, que son classement réel. \nOn remarque que les meilleures équipes sont sous la ligne directrice, à l'inverse des moins bonnes équipes qui se trouvent au dessus. Sela signifie que notre classement a tendance à tirer vers le haut les moins bonnes équipes et les rapprocher des meilleures.")

fig = px.scatter(results, x="rating_adj/20", y="rank_pts", color="Championnat", hover_name="Squad")
st.write("### Comparaison entre le rang réel des équipes et notre note ajustée")
st.plotly_chart(fig)
st.write("Il est intéressant de voir que la tendance est corrélée, mais aussi que certains championnats sont plus en dessous de la moyenne, comme le championnat français. Cela est dû aux coefficients.")
