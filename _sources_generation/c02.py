# -*- coding: utf-8 -*-
from ch import *
corps = sec("Lire l'Environnement : Porter", "sec:c02-porter") + r"""
Michael Porter publie en 1980 une méthode d'analyse d'un secteur~\cite{porter1980}. La rentabilité d'une
entreprise dépend de cinq forces~: la rivalité entre concurrents, la menace des nouveaux entrants, la menace
des produits de substitution, le pouvoir des fournisseurs et celui des clients.

""" + tab("L{3.4cm}L{4.0cm}L{4.6cm}", ["Force", "Question", "Chez LiZbiZ"], [
    ["Rivalité", "Combien de concurrents, de quelle taille~?", "Six transporteurs nationaux, prix proches"],
    ["Nouveaux entrants", "Est-il facile d'entrer~?", "Une jeune pousse livre à moto avec une application"],
    ["Substituts", "Le besoin peut-il être servi autrement~?", "Points de retrait tenus par des commerçants"],
    ["Fournisseurs", "Peuvent-ils imposer leurs prix~?", "Carburant et pièces, prix subis"],
    ["Clients", "Peuvent-ils partir ou négocier~?", "Un client pèse 38~\\% du chiffre d'affaires"]],
    "Les cinq forces appliquées à LiZbiZ", "2.1") + r"""

En 1985, Porter ajoute la \termecle{chaîne de valeur}~\cite{porter1985}. L'entreprise est découpée en activités
principales (logistique d'approvisionnement, production, logistique de distribution, vente, service) et en
activités de soutien (infrastructure, ressources humaines, technologie, achats). L'avantage naît de la manière
dont ces activités sont exécutées et reliées.

La même année, Porter et Millar montrent que l'information traverse toute la chaîne~\cite{portermillar1985}.
Chaque activité produit et consomme de l'information. Les technologies peuvent donc abaisser un coût,
différencier une offre ou changer les règles d'un secteur. Ce texte est le premier à faire du système
d'information une arme stratégique et non un centre de coût.

\begin{boxinfo}
\textbf{Trois stratégies génériques.} Porter distingue la domination par les coûts, la différenciation et la
concentration sur un segment. Une entreprise qui poursuit les trois à la fois reste « enlisée au milieu ». Le
système d'information ne sert pas les trois de la même manière~: l'automatisation sert les coûts, la
connaissance du client sert la différenciation.
\end{boxinfo}

\textbf{Limite.} Les cinq forces supposent un secteur aux frontières nettes. Les plateformes numériques
brouillent ces frontières~: un opérateur de téléphonie devient un concurrent des banques.

""" + sec("Regarder au-dedans : Ressources et Capacités", "sec:c02-ressources") + r"""
La théorie des ressources renverse le regard. L'avantage ne vient pas d'abord de la position sur un marché. Il
vient de ce que l'entreprise possède et que les autres ne peuvent pas copier. Wernerfelt l'énonce en
1984~\cite{wernerfelt1984}. Barney en donne en 1991 les conditions~\cite{barney1991}~: une ressource fonde un
avantage durable si elle a de la valeur, si elle est rare, si elle est difficile à imiter et si rien ne la
remplace. La grille VRIO, qui en découle, ajoute que l'organisation doit savoir l'exploiter.

""" + tab("L{4.2cm}ccccL{3.0cm}", ["Ressource de LiZbiZ", "Valeur", "Rare", "Inimitable", "Exploitée", "Conclusion"], [
    ["Postes de travail neufs", "Oui", "Non", "Non", "Oui", "Parité"],
    ["Logiciel de gestion d'entrepôt du marché", "Oui", "Non", "Non", "En partie", "Parité"],
    ["Dix ans de données de tournées", "Oui", "Oui", "Oui", "Non", "Avantage inexploité"],
    ["Réseau de 40 correspondants en zone rurale", "Oui", "Oui", "Oui", "Oui", "Avantage durable"]],
    "Grille VRIO de quatre ressources", "2.2") + r"""

La grille dit quelque chose d'utile au schéma directeur. Le matériel que tout le monde peut acheter ne donne
aucun avantage. Les données que seule l'entreprise détient en donnent un, à condition de les exploiter.

En 1997, Teece, Pisano et Shuen ajoutent les \termecle{capacités dynamiques}~\cite{teece1997}~: l'aptitude à
recomposer ses ressources quand l'environnement change. Pour un schéma directeur, cela justifie des dépenses qui
ne rapportent rien dans l'immédiat, comme une architecture qui permet de changer de fournisseur ou une équipe
capable d'intégrer vite un nouveau service.

""" + sec("La Stratégie se Fait aussi en Marchant", "sec:c02-mintzberg") + r"""
Mintzberg et Waters observent en 1985 que la stratégie réalisée diffère presque toujours de la stratégie
voulue~\cite{mintzberg1985}. Une partie de la stratégie \textit{délibérée} n'est jamais exécutée. Une stratégie
\textit{émergente} apparaît, faite de décisions prises au fil des événements.

Le bilan de l'ANPP en est l'illustration. Six projets délibérés ont abouti. Onze projets émergents se sont
ajoutés. Mintzberg n'y voit pas un échec en soi. L'échec est de ne pas s'en apercevoir. Un schéma directeur doit
donc prévoir comment un projet non prévu y entre et comment un projet prévu en sort.

""" + sec("Rupture, Plateformes et Coûts de Transaction", "sec:c02-numerique") + r"""
Christensen décrit en 1997 l'\termecle{innovation de rupture}~\cite{christensen1997}. Un nouvel entrant propose
un produit moins bon et moins cher à des clients que les entreprises en place négligent. Il s'améliore, puis
remonte vers leur clientèle. Les entreprises établies ne le voient pas venir parce qu'elles écoutent leurs
meilleurs clients.

Rochet et Tirole formalisent en 2003 les \termecle{marchés bifaces}~\cite{rochettirole2003}. Une plateforme
sert deux groupes qui ont besoin l'un de l'autre. La valeur pour chaque groupe croît avec la taille de l'autre.
Le paiement par téléphone mobile en est l'exemple le plus proche~: plus il y a de commerçants qui l'acceptent,
plus les porteurs l'utilisent. Parker, Van Alstyne et Choudary en ont tiré une méthode~\cite{parker2016}.

La théorie des coûts de transaction éclaire le choix de faire ou de faire faire. Coase demande en 1937 pourquoi
les entreprises existent~\cite{coase1937}. Williamson précise en 1975 qu'il vaut mieux faire soi-même quand
l'actif est très spécifique, quand l'incertitude est forte et quand l'échange est fréquent~\cite{williamson1975}.

""" + tab("L{4.4cm}L{3.6cm}L{4.0cm}", ["Activité informatique", "Spécificité", "Tendance"], [
    ["Messagerie", "Faible", "Faire faire"],
    ["Hébergement standard", "Faible", "Faire faire"],
    ["Application de calcul des prestations", "Forte", "Garder la maîtrise"],
    ["Référentiel des bénéficiaires", "Forte", "Garder la maîtrise"]],
    "Faire ou faire faire à l'ANPP", "2.3") + r"""

""" + sec("Relier Objectifs et Mesures", "sec:c02-bsc") + r"""
Kaplan et Norton proposent en 1992 le \termecle{tableau de bord prospectif}~\cite{kaplannorton1992}. La
performance se lit sur quatre axes~: finances, clients, processus internes, apprentissage. Chaque objectif reçoit
une mesure, une cible et une initiative. Le modèle sera repris au Chapitre~\ref{chap:piloter} pour piloter
l'exécution du schéma directeur.

""" + sec("Dans une Administration", "sec:c02-public") + r"""
Ces théories sont nées dans l'entreprise. Leur transposition demande trois précautions.

\begin{enumerate}
    \item \textbf{La mission remplace le marché.} L'ANPP n'a pas de concurrent. Les cinq forces se relisent en
          parties prenantes~: tutelle, bailleurs, bénéficiaires, opérateurs de paiement, fournisseurs.
    \item \textbf{La valeur est publique.} Elle se mesure en délai, en accès, en confiance et non en marge.
    \item \textbf{Les ressources sont contraintes.} Une agence ne recrute ni n'achète librement. La grille VRIO
          reste utile pour repérer ce qu'elle détient d'unique, par exemple son fichier des bénéficiaires.
\end{enumerate}

\begin{boxscenario}{Mission LiZbiZ. La note stratégique du 6 février 2025}
\textbf{Constatations.} Le plan HORIZON~3 vise le doublement du chiffre d'affaires. Un client pèse 38~\% des
ventes. Une jeune pousse a pris 9~\% des livraisons urbaines à Douala en dix-huit mois. LiZbiZ détient dix ans
de données de tournées qu'elle n'exploite pas.

\textbf{Analyse} (confiance moyenne). La menace vient d'un nouvel entrant de rupture sur le segment urbain.
L'avantage de LiZbiZ est ailleurs~: son réseau rural et ses données. La stratégie numérique doit défendre le
premier par le suivi des colis et exploiter les secondes pour optimiser les tournées. La fibre n'est qu'un
moyen.
\end{boxscenario}
"""
chapitre("partie1/P01_C02_theories_strategie.tex", 2, "Les Théories de la Stratégie", "chap:strategie", "Théories de la stratégie",
 "« L'essence de la stratégie est de choisir\\\\\n    ce qu'il ne faut pas faire. »", "D'après Michael Porter",
 "Fondamental", "Chapitre~\\ref{chap:vocabulaire}",
 ["Appliquer les cinq forces et la chaîne de valeur à une organisation.", "Utiliser la grille VRIO pour qualifier une ressource informatique.",
  "Distinguer stratégie délibérée et stratégie émergente.", "Reconnaître une rupture et un marché biface.",
  "Raisonner un choix de faire ou de faire faire.", "Transposer ces théories à une administration."],
 "« le concurrent livre à moto »", r"""
Douala, mardi 4~février~2025. Le directeur commercial de LiZbiZ ne s'inquiète pas. La jeune pousse qui livre à
moto dans la ville « ne fait pas le même métier ». Elle ne transporte que des petits colis, elle n'a pas
d'entrepôt et ses prix ne couvrent sans doute pas ses coûts.

Mme~EKANI demande les chiffres. En dix-huit mois, ce concurrent a pris 9~\% des livraisons urbaines. Ses clients
sont de petits commerçants en ligne que LiZbiZ ne démarche pas. Il leur donne le suivi du colis en temps réel.
Deux grands comptes de LiZbiZ viennent de demander le même service.

\begin{boxalert}
\textbf{Violation typique.} Juger un nouvel entrant sur la qualité de son offre du moment.

\smallskip
\textbf{Règle~:} une rupture commence par le bas du marché. La question utile n'est pas « fait-il aussi bien
que nous~? » mais « à qui suffit ce qu'il fait et à quelle vitesse progresse-t-il~? »
\end{boxalert}
""", corps,
 [("Consultant", "Citer une théorie avec son auteur et sa date. Dire ce qu'elle explique et ce qu'elle n'explique pas."),
  ("Directeur des systèmes d'information", "Passer chaque grand poste de dépense à la grille VRIO. Ce qui n'est ni rare ni inimitable se standardise ou s'achète."),
  ("Dirigeant", "Demander une fois par an quels projets sont nés hors du plan. Leur nombre dit ce que le plan n'avait pas vu.")],
 ["Porter~: cinq forces, chaîne de valeur, trois stratégies génériques. L'information traverse toute la chaîne.",
  "Barney~: une ressource fonde un avantage si elle a de la valeur, si elle est rare, inimitable et exploitée.",
  "Teece~: les capacités dynamiques justifient d'investir dans l'aptitude à changer.",
  "Mintzberg~: la stratégie réalisée mêle le délibéré et l'émergent.",
  "Christensen, Rochet et Tirole, Williamson~: rupture, plateformes, faire ou faire faire.",
  "Dans une administration, la mission remplace le marché et la valeur est publique."],
 ["nommer les cinq forces", "énoncer les quatre conditions de Barney", "donner un exemple local de marché biface", "dire quand il vaut mieux faire soi-même"],
 [("Cinq forces", 1, "Appliquez les cinq forces à une banque de détail camerounaise face au paiement par téléphone mobile. Une ligne par force."),
  ("VRIO", 2, "Passez à la grille VRIO quatre ressources de l'ANPP~: le fichier des bénéficiaires, le centre de données, l'application e-PRESTATIONS, le réseau des dix antennes."),
  ("Délibéré, émergent", 2, "Classez les onze projets hors schéma directeur de l'ANPP en trois familles possibles~: réponse à une urgence, opportunité de financement, demande de la tutelle. Que doit prévoir le nouveau document pour chacune~?"),
  ("Faire ou faire faire", 3, "La BANQUE SANAGA envisage de confier l'exploitation de son système central à un prestataire. Appliquez les trois critères de Williamson. Concluez, puis dites ce que le superviseur exigera.")],
 ["Porter~\\cite{porter1980,porter1985} et Porter et Millar~\\cite{portermillar1985}.", "Barney~\\cite{barney1991} et Teece et al.~\\cite{teece1997}.", "Mintzberg et Waters~\\cite{mintzberg1985}.", "Christensen~\\cite{christensen1997}."],
 "Ces théories disent comment une organisation choisit sa route. Elles ne disent pas comment le système d'information la suit. C'est la question de l'alignement et de la valeur, objet du Chapitre~\\ref{chap:alignement}.")
