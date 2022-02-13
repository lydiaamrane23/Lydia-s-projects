
## Serveur-de-discussion-Internet-Relay-Chatou-IRC

![liliserveur](https://user-images.githubusercontent.com/96254332/153772385-adcdbb07-15f8-4721-bd9f-c899dd70c6ea.png)


Le but de ce mini-projet est de realiser un service de discussion en ligne (Internet Relay Chatou IRC) en Python. Il s’agit d’un systeme client/serveur permettant à des utilisateurs de discuter en direct en s’envoyant des messages. Les utilisateurs peuvent discuter en groupe à travers descanaux de discussion, mais egalement deux-a-deux de maniere privee. Le principe est assez simple : des utilisateurs se connectent à un serveur IRC en utilisant un programme client,tape des commandes et le serveur execute ces commandes. Le reseau IRC est constitue de serveurs connect ́es entre eux, sans topologie particuliere.
Chaque client se connecte a un des serveurs et les commandes (ou messages) qu’il tape sont communiquees par son serveur de rattachement aux autres serveurs, jusqu’aux clients destinataires. Les commandes ont la forme suivante/commande , ou represente une liste d’arguments (cette liste pouvant etre vide).
Dans ce projet, j'ai implementé un petit sous-ensemble de commandes.
Chaque client est identifie par un surnom (nickname).
Les noms de canaux commencent par un symbole#. Les commandes deja implimenté sont: /away [message]: Signale son absence quand on nous envoie un message en prive(en reponse un message peut ˆetre envoye).Une nouvelle commande/away reactive l’utilisateur.

1. /help: Affiche la liste des commandes disponibles
2. /invite : Invite un utilisateur sur le canal ou on se trouve
3. /join [cle]: Permet de rejoindre un canal (protege eventuellement par une cle).Le canal est cree s’il n’existe pas.
4. /list : Affiche la liste des canaux sur IRC
5. /msg [canal|nick] message : Pour envoyer un message a un utilisateur ou sur un canal (ou on est present ou pas). Les arguments canal ou nick sont optionnels.
6. /names [channel] : Affiche les utilisateurs connectes a un canal. Si le canal n’est pas specifie, affiche tous les utilisateurs de tous les canaux.
7. /quit[canal] : Pour quitter un canal definitivement


![interface_SD](https://user-images.githubusercontent.com/96254332/153772567-5f40621e-160e-4d65-8fa2-eee7214dd099.png)


Pour le serveur :
## python Serveur.py 8000

D’un point de vue utilisateur, un client IRC sera lance sur la ligne de commande a l’aide du programme client.py dela maniere suivante :
## python client.py lydia 8000



ou nickname est le nom du client qui souhaite se connecter sur le serveur IRCservername. Par exemple, cette commande lancera une interface graphique.

![liliiiiiiii](https://user-images.githubusercontent.com/96254332/153772395-13de1c42-5659-4c53-9227-ab42b2d1898b.png)
