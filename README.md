# Web_Scraping_S9
Projet réalisé par Sara VIDAL et Constantin TESTU

Dans ce projet nous allons tenter d'étudier les équipes de football des meilleurs championnats européens. L'objectif est d'établir un classement européens. En effet il n'existe pas de classement précis qui compare les équipes des différents championnats car ces dernières ne s'affrontent pas entre elles pour la plupart. 

### Extraction des données : *data_extraction.ipynb*

Nous allons analyser les performances des équipes anglaises, françaises, espagnoles, et italiennes. Nous étudierons les données de la saison 2021-2022 étant la dernière saison complète ayant eu lieu.

Afin de déterminer un nouveau classement, nous allons scraper les données depuis 3 sites différents : 
- lequipe.fr pour les classements des équipes dans chaque championnat
- fifaindex.com pour les valeurs théoriques des différentes équipes
- fbref.com pour des données plus complémentaires sur les performances des équipes

Sur chaque site nous scrapons 4 pages, une pour chaque championnat, et nous en tirons des tableaux de données.

Une fois les données extraite, nous devons merge les 12 tableaux de données ensemble. Il nous faut par ailleur faire en sorte que tous les noms d'équipes concordent.
Nous nettoyons également les données en supprimant les colonnes inutiles, et en calculant de nouvelles colonnes à partir de celles extraites.

### Traitement et Analyse des données : *processing.ipynb*

Nous avons orienté notre analyse et classification des équipes selon 3 grands axes : 

Les performances réalisées (l'équipe & fbref)
- points
- buts marqués
- buts encaissés
- différence de buts
- pourcentage de duels aériens gagnés
Les performances théoriques (FIFA)
- Note moyenne de l'équipe (moyenne de attaquants, milieux, et défenseurs
Le fair-play de l'équipe (fbref)
- Nombre de cartons jaunes
- nombre de fautes commises

Nous pouvions alors comparer les performances théoriques et réelles. Quant au fair-play, il n'est pas présent pour récompenser les équipes fair-play, mais c'est un bon indicateur de performances :

une équipe en difficulté et souvent en défense commettra plus de fautes (les catons jaunes nous informe sur la gravité des fautes

Chaque indicateur peut possèder des biais, par exemple, une équipe peut être très bien classée au niveau des points sans pour autant marquer beaucoup de buts si elle se contente de petites victoires (1-0).
Ainsi, en multipliant les indicateurs nous réduisons les biais

Comment avons nous classé les équipes : 

Pour chaque indicateur, nous avons établi un classement des équipes, par championnat, puis nous avons calculé la moyenne des classements.

Ensuite nous calculons une note avec la formule suivante :
*(20-rank_avg) x coeff_championnat*

Nous soustrayons à 20 car il y a 20 équipes par championnat. Le coefficient du championnat est donné par l'UEFA : 

FRA  0.59497
ITA  0.71497
ESP 0.88855
ANG 1.03141


### Produit final : *app.py*

Pour un rendu final esthétique et ergonomique, nous avons développé une application avec streamlit. Cette dernière nous sert comme d'un dashboard pour afficher nos classements et nos visualisations.

![image](https://user-images.githubusercontent.com/61684044/214178503-3a5facc4-62c4-4a48-a5ac-0bd5ff5dfcb1.png)

![image](https://user-images.githubusercontent.com/61684044/214178565-fec0e26d-3b9a-48c3-810a-09674d6e0fd4.png)


Toutes les analyses des graphiques peuvent êtres retrouvées dans nos slides ou dans l'application développée. Nous vous recommandons d'aller les trouver dans l'application car les graphiques y sont interactifs.  
