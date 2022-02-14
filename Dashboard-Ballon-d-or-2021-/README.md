# Dashboard-Ballon-d-or-2021
  Visualisation des données des nominées au ballon d’or 

Introduction:

Le FIFA Ballon D'Or est un trophée du meilleur footballeur de l'année décerné par France Football. À la fin de chaque année en octobre, une liste de 30 finalistes est dévoilée, tandis que l'annonce du lauréat est prévue fin novembre. 
Le but de notre étude est de visualiser et de comparer les performances individuelles des joueurs nominées au ballon d’or 2021.

Présentation et description des données:

la table de données contient 1540 lignes. De base, elle contient 17 variables(colonnes) , seulement, j'ai choisi de ne retenir que 11 variables qui me semblaient intéressantes pour mon étude. 
Les variables ainsi retenues sont les suivantes :

1. Name : nom du joueur.
2. Date : la date du match disputé par un des joueurs.
3. Result : Le résultat du match.
4. Played position : La  position du joueur durant le match.
5. Goals : Le nombre de buts marqués par le joueur.
6. Assists : le nombre de passes décisives effectuées par le joueur.
7. Yellow : le nombre de cartons jaunes reçus par le joueur.
8. Yellow_X2 : le nombre de cartons jaunes X2 reçus par le joueur.
9. Red  : le nombre de cartons rouges reçus par le joueur le jour du match.
10. Minutes : nombre de minutes jouées par le joueur pendant le match.
11. Compétition : la compétition dans laquelle se déroule le match. 

Librairies et langages informatiques utilisés:
## Python comme langage de programmation pour l’analyse et la visualisation des données et plus exactement les librairies Pandas, Numpy et Sqldf pour le pré-processing et le framework Dash Plotly pour la création des visualisations de manière interactive et dynamique.

Nettoyage des données :

C’est une étape indispensable qui sert principalement à identifier et supprimer les données non pertinentes et dans laquelle je me suis occupés également de la gestion des valeurs manquantes afin d’améliorer la cohérence, la fiabilité et la valeur des données.

## Visualisation des données:

La visualisation des données est un ensemble de méthodes qui désigne la représentation graphique des données pour pouvoir présenter de manière visuelle et pertinente les informations présentes dans un ensemble de données. Pour cette partie, j'ai créé un tableau de bord regroupant différentes visualisations et contenant trois pages qu’on va vous présenter ci-dessous:

## Individual player performances:


![da1](https://user-images.githubusercontent.com/96254332/153503260-1a76bcfb-9ee8-48e7-8677-9344636f6ce4.png)
Cette page contient trois bar charts qui représentent respectivement le temps de jeu, les buts ainsi que les passes décisives de chaque joueur.
on trouve aussi la distribution des positions des nominées ainsi qu’un graphique en courbe décrivant le nombre de cartons( jaunes, 2* jaunes et rouges) reçus par mois.
De plus, j'ai ajouté un filtre sur les joueurs,  un autre sur les compétitions et un dernier sur le mois de l’année. Ces filtres s’appliquent sur les bar charts et les line charts décrits ci-dessus.



## Data distribution:


![da2](https://user-images.githubusercontent.com/96254332/153503301-afd93b61-59c9-40af-bb56-450e48f30be1.png)

Dans cette page, on retrouve une boîte à moustache qui permet de révéler le profil essentiel d'une série statistique quantitative qui est dans notre cas soit les buts, soit les passes décisives ou bien le temps de jeu pour chaque joueur ou encore le mois de l’année.
Ce dernier est accompagné d’un nuage de points qui représente la répartition des buts et passes décisives par rapport au temps de jeu pour chaque compétition.


## Player comparaison:

![da3](https://user-images.githubusercontent.com/96254332/153503320-5ba2993e-41e4-410b-866a-5c913f71e900.png)

Cette dernière page a pour but de faire une comparaison entre deux joueurs, elle contient : 

Un radar chart : qui affiche les données (goals/assists/playing time/yellow) de deux joueurs avec des couleurs différentes sous la forme d'un graphique bidimensionnel de variables quantitatives présentées sur des axes en partant du centre. Pour une meilleure représentation nous avons modifié l’unité de playing_time.
4 kpi (indicateur clé de performance) : Il y a quatre cartes. Chaque carte affiche la médiane(goals/assists/playing time/yellow) par rapport au nombre total de (goals/assists/playing time/yellow) pour l'année 2021. 


Conclusion:
Le dashboard développé dans ce projet a facilité la compréhension et la lecture des performances individuelles de chaque joueur ainsi que les relations entre les différentes colonnes qui nous intéressent afin d' y voir plus clair.
