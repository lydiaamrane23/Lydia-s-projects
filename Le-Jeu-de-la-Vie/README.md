# Le-Jeu-de-la-Vie

 Le jeu  de  la  vie de Conway represente l’ ́evolution d’une population de cellules contenue dans un tableau bidi-mensionnel. 
 Chaque case du tableau contient 0 ou 1 cellule et on simule l’ ́evolution de la population en divisant le temps en une suite d’instants et en calculant (suivant des regles d ́ecrites plus loin) la population `a chaque instant.
Regles d’evolution : Pour savoir l’etat d’une case a l’etape n+ 1, on regarde son etat et celui de ses 8 voisines a l’instant n.
1. —  Si elle est vide et qu’elle a exactement 3 cases voisines occupees, elle devient occupee par une nouvelle cellule. Sinon elle reste vide.
2. —  Si elle est occupee et qu’elle a exactement 2 ou 3 cases voisines egalement occupees, la cellule qui occupe la case survit. Sinon le cellule disparaıt.

file: sequetiel.py : un programme qui simule l’evolution d’une population de cellules de dimension n×n`a l’aide d’un programme séquentiel, l’initialisation de la population est  de maniere aleatoire, la boucle principale du programme consistera `a afficher puis `a calculer la nouvelle population

file: Barriere.py : On remarque que le calcul de l’ ́etat d’une case `a l’ ́etape suivante est independant du calcul des autres cases.c'est pour cela je modifié mon  programme afin d’effectuer ces calculs `a l’aide de threads independantes.
Plutot que de creer n×n threads a chaque iteration, on va creer n×n threads qui calculent en  boucle l’ ́etat  de  leur  case  respective. 
La  difficult ́e  consiste a synchroniser les threads entre  elles  pour qu’aucune ne commence `a calculer l’ ́etape n+ 2 si d’autres n’ont pas encore fini de calculer l’etap en+ 1 (il faudra donc utiliser une ## barriere de synchronisation)
