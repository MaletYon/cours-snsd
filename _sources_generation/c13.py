# -*- coding: utf-8 -*-
from ch import *
corps = sec("Qui Suit l'Exécution", "sec:c13-instances") + r"""
Les instances de la mission se dissolvent le jour de l'approbation. D'autres les remplacent pour cinq ans. La
norme ISO/IEC~38500 confie à l'organe de gouvernance la tâche de surveiller~\cite{iso38500}. Weill et Ross
ajoutent que chaque type de décision doit avoir un titulaire connu~\cite{weillross2004}.

""" + tab("L{3.2cm}L{3.6cm}L{2.0cm}L{3.2cm}", ["Instance", "Composition", "Rythme", "Décide de"], [
    ["Conseil d'administration", "Administrateurs", "Chaque année", "Révision, budget"],
    ["Comité de portefeuille", "Directeur général, directeurs", "Chaque trimestre", "Lancement, arrêt, arbitrage entre projets"],
    ["Comité de projet", "Responsable métier, chef de projet, fournisseur", "Chaque mois", "Conduite d'un projet"],
    ["Cellule de portefeuille", "Deux agents auprès du directeur général", "En continu", "Rien. Elle instruit et alerte"]],
    "Les instances d'exécution à l'ANPP", "13.1") + r"""

La \termecle{cellule de portefeuille} est l'instance la plus modeste et la plus utile. Elle tient les fiches à
jour, prépare le comité, vérifie les chiffres des chefs de projet. Elle n'est pas rattachée à la division
informatique. À l'ANPP, elle est créée par une décision du 2~juillet~2027.

""" + sec("Le Tableau de Bord", "sec:c13-tableau") + r"""
Kaplan et Norton ont proposé en 1992 de suivre une organisation sur quatre axes plutôt que sur le seul résultat
financier~\cite{kaplannorton1992}. Transposés au schéma directeur, ils donnent une douzaine d'indicateurs au
plus.

""" + tab("L{2.8cm}L{4.8cm}L{4.4cm}", ["Axe", "Indicateur", "Cible de l'ANPP pour 2031"], [
    ["Bénéficiaires", "Prestations payées à la date prévue", "99~\\%"],
    ["Bénéficiaires", "Délai de traitement d'une demande", "15~jours"],
    ["Finances", "Part des projets dans la dépense", "35~\\%"],
    ["Finances", "Écart de coût du portefeuille", "Moins de 10~\\%"],
    ["Processus", "Projets livrés à la date prévue", "70~\\%"],
    ["Processus", "Applications sans responsable", "0"],
    ["Capacités", "Postes du plan de dotation pourvus", "8 sur 8"],
    ["Capacités", "Applications clés avec reprise éprouvée", "Toutes"]],
    "Le tableau de bord du schéma directeur", "13.2") + r"""

Un indicateur se définit par cinq éléments~: une formule, une source, un responsable de la mesure, une
fréquence, une cible. Un indicateur sans source ne sera pas produit. Un indicateur sans cible ne dit rien.

\begin{boxalert}
\textbf{Violation typique.} Suivre l'avancement des projets et jamais leurs effets.

\smallskip
\textbf{Règle~:} le tableau de bord contient au moins un indicateur de résultat pour le bénéficiaire du
service. Vingt-deux projets livrés à l'heure sans que les paiements arrivent à date fixe sont un échec.
\end{boxalert}

""" + sec("Mesurer l'Avancement", "sec:c13-avancement") + r"""
Le pourcentage d'avancement déclaré par un chef de projet est peu fiable. La méthode de la valeur acquise
compare trois montants à une date donnée~: ce qui devait être fait, ce qui est fait, ce qui a été dépensé. La
norme ISO~21502 la range parmi les pratiques de maîtrise~\cite{iso21502}.

\begin{equation}
    \mathrm{IP_d} = \frac{\mathrm{VA}}{\mathrm{VP}} \qquad\qquad \mathrm{IP_c} = \frac{\mathrm{VA}}{\mathrm{CR}}
\end{equation}

VP est la valeur planifiée, budget des travaux prévus à la date. VA est la valeur acquise, budget des travaux
réellement achevés. CR est le coût réel. $\mathrm{IP_d}$ mesure le respect des délais, $\mathrm{IP_c}$ le
respect des coûts. Au-dessous de 1, le portefeuille est en retard ou trop cher.

\begin{boxscenario}{ANPP. La première revue, 30 juin 2028}
Le profil du Tableau~11.5 prévoyait 380~millions en 2027 et la moitié de 1~050 au premier semestre 2028. La
valeur planifiée au 30~juin~2028 est donc de $380 + 525 = 905$~millions. La cellule de portefeuille établit que
les travaux achevés représentent 540~millions de budget et que 610~millions ont été payés.

\[ \mathrm{IP_d} = \frac{540}{905} = 0{,}60 \qquad \mathrm{IP_c} = \frac{540}{610} = 0{,}89 \]

Le portefeuille a réalisé 60~\% de ce qui était prévu. Chaque franc dépensé a produit 89~centimes de travaux
prévus. Le retard vient de deux marchés~: le site de secours, relancé après une première procédure
infructueuse, le référentiel, notifié avec quatre mois de retard.
\end{boxscenario}

""" + sec("Suivre les Bénéfices", "sec:c13-benefices") + r"""
Un projet livré n'a encore rien rapporté. Ward et Daniel demandent de désigner pour chaque bénéfice un
\termecle{propriétaire}, de le mesurer avant le projet, puis de le mesurer après~\cite{warddaniel2006}. Sans
mesure de départ, aucun progrès ne se prouve.

""" + tab("L{3.6cm}L{2.8cm}L{2.6cm}L{2.6cm}", ["Bénéfice attendu", "Propriétaire", "Mesure de départ", "Cible"], [
    ["Paiement à date fixe", "Directeur des prestations", "91~\\% en 2026", "99~\\% en 2031"],
    ["Fin des doubles paiements", "Directeur financier", "2~340 cas en 2026", "Moins de 200"],
    ["Délai de traitement", "Chefs d'antenne", "47~jours", "15~jours"],
    ["Économie de contrats", "Cheffe de division", "0", "85~millions par an"]],
    "Le registre des bénéfices (extrait)", "13.3") + r"""

Le bénéfice appartient au métier. La fonction informatique livre un outil. Le directeur des prestations
obtient, ou n'obtient pas, le paiement à date fixe. Cela suppose qu'il change l'organisation du travail autour
de l'outil. Le Chapitre~\ref{chap:alignement} l'a montré~: la valeur vient de l'usage.

""" + sec("Faire Adopter", "sec:c13-adopter") + r"""
Rogers a décrit comment une nouveauté se répand dans un groupe~: quelques pionniers, une majorité qui suit, des
retardataires~\cite{rogers1962}. Davis a montré que l'usage d'un système dépend de deux perceptions, son
utilité et sa facilité~\cite{davis1989}. Ces deux travaux fondent trois gestes simples.

\begin{enumerate}
    \item Choisir des antennes pilotes parmi les volontaires, non parmi les plus proches du siège.
    \item Montrer aux agents ce que l'outil leur épargne avant de montrer ce qu'il permet de contrôler.
    \item Former au poste de travail, sur des dossiers réels, la semaine de la mise en service.
\end{enumerate}

Le budget de formation et d'accompagnement figure dans chaque fiche de projet. À l'ANPP il représente 9~\% de
l'investissement. Une fiche sans ce budget est renvoyée à son auteur.

""" + sec("Accueillir l'Imprévu", "sec:c13-imprevu") + r"""
Entre 2021 et 2025, onze projets de l'ANPP se sont faits hors du schéma directeur. Mintzberg appelle cela la
stratégie émergente~\cite{mintzberg1985}. L'interdire est vain. Il faut une porte d'entrée.

\begin{boxprocedure}
\textbf{Instruire une demande hors portefeuille.}
\begin{enumerate}
    \item Le demandeur remplit une fiche de projet, comme pour les autres.
    \item La cellule de portefeuille la note sur la grille de valeur et vérifie le plan fonctionnel.
    \item Le comité de portefeuille décide~: rejet, attente de la révision annuelle ou entrée immédiate.
    \item Une entrée immédiate nomme le projet qu'elle décale ou la ressource nouvelle qui la finance.
    \item La décision est inscrite au registre du portefeuille.
\end{enumerate}
\end{boxprocedure}

Une réserve pour projets non prévus facilite la règle. Les 242~millions de provision pour aléas ne servent pas
à cela. L'ANPP a choisi de ne pas créer de réserve et d'appliquer la règle du décalage.

""" + sec("Réviser", "sec:c13-reviser") + r"""
Un schéma directeur de cinq ans rédigé une fois est faux au bout de dix-huit mois. Il se révise chaque année, à
date fixe, avant la préparation du budget. La révision répond à quatre questions.

\begin{enumerate}
    \item Les objectifs de l'organisation ont-ils changé~?
    \item Qu'a-t-on livré, dépensé, obtenu~?
    \item Les hypothèses de financement tiennent-elles~?
    \item Que faut-il avancer, décaler, retirer, ajouter~?
\end{enumerate}

La révision produit un document court, approuvé par le conseil. Elle peut glisser l'horizon d'un an. On parle
alors de \termecle{schéma directeur glissant}. La cible ne se révise pas chaque année. Si elle doit changer,
c'est qu'un fait majeur est survenu~: une réforme, une fusion, une rupture technique. On rouvre alors une
démarche complète.

\begin{boxinfo}
\textbf{Arrêter un projet.} Le comité de portefeuille a le pouvoir d'arrêter. C'est sa décision la plus
difficile, parce que l'argent déjà dépensé pèse sur le jugement. La question à poser est simple~: sachant ce
que nous savons, lancerions-nous ce projet aujourd'hui pour ce qu'il reste à payer~? Entre 2021 et 2025, quatre
projets de l'ANPP ont été arrêtés sans qu'aucune instance ne l'ait décidé. Ils se sont éteints.
\end{boxinfo}

""" + lecture("Le dispositif de pilotage de l'ANPP, revue du 30 juin 2028", [
    ("Un comité de portefeuille se réunit chaque trimestre", "O", "Quatre procès-verbaux"),
    ("La cellule de portefeuille est indépendante de l'informatique", "O", "Décision du 2 juillet 2027"),
    ("Chaque indicateur a une source et une cible", "O", "Fiches d'indicateur"),
    ("Le tableau de bord contient un indicateur de résultat", "O", "Paiements à date"),
    ("L'avancement est mesuré par la valeur acquise", "O", "Note de la cellule"),
    ("Chaque bénéfice a un propriétaire et une mesure de départ", "N", "Deux bénéfices sans mesure de départ"),
    ("Les demandes hors portefeuille passent par la procédure", "N", "Un projet lancé par une direction en mars 2028"),
    ("La révision annuelle est approuvée par le conseil", "K", "Conseil prévu en septembre"),
    ("Les projets en retard ont un plan de rattrapage", "O", "Deux plans joints")],
    r"""Six \OUI{} sur neuf. Le dispositif existe et fonctionne. Les deux \NON{} montrent que les habitudes
résistent~: une direction a encore lancé son projet seule. Le comité l'a régularisé au lieu de l'instruire. Le
\NEK{} est de preuve et il est normal à cette date.""") + r"""
"""
chapitre("partie5/P05_C13_piloter.tex", 13, "Piloter l'Exécution", "chap:piloter", "Piloter",
 "« Aucun plan ne résiste au premier contact. »", "D'après Helmuth von Moltke, 1871",
 "Intermédiaire", "Chapitres~\\ref{chap:portefeuille} et \\ref{chap:financer}",
 ["Composer les instances d'exécution d'un schéma directeur.", "Construire un tableau de bord sur quatre axes.", "Calculer les indices de délai et de coût par la valeur acquise.",
  "Tenir un registre des bénéfices.", "Instruire une demande hors portefeuille.", "Conduire une révision annuelle."],
 "« tout avance normalement »", r"""
Yaoundé, vendredi 30~juin~2028. Première revue annuelle. Les chefs de projet présentent leurs fiches. Toutes
portent la mention « avancement conforme ». M.~OWONA s'en réjouit.

La cellule de portefeuille distribue ensuite une page. Elle a compté ce qui est réellement achevé. Sur
905~millions de travaux prévus à cette date, 540 sont faits. Le site de secours n'a pas de fournisseur. Le
référentiel a quatre mois de retard. Le directeur général demande pourquoi personne ne l'a dit. « Chaque projet
avance, répond l'un des agents de la cellule. C'est le portefeuille qui est en retard. »

\begin{boxalert}
\textbf{Violation typique.} Piloter un portefeuille par l'addition des déclarations des chefs de projet.

\smallskip
\textbf{Règle~:} l'avancement se mesure par une instance qui ne conduit aucun projet, avec une méthode
identique pour tous.
\end{boxalert}
""", corps,
 [("Directeur général", "Présider le comité de portefeuille. Arrêter les projets qui doivent l'être."),
  ("Responsable de la cellule de portefeuille", "Mesurer sans conduire. Alerter par écrit. Tenir le registre des décisions."),
  ("Directeur de métier", "Mesurer le bénéfice avant le projet. En répondre après."),
  ("Auditeur interne", "Vérifier chaque année un échantillon d'indicateurs en remontant à leur source.")],
 ["Quatre instances~: conseil, comité de portefeuille, comités de projet, cellule de portefeuille.", "Un indicateur a une formule, une source, un responsable, une fréquence, une cible.",
  "La valeur acquise donne deux indices~: délai et coût.", "Un bénéfice a un propriétaire dans le métier et une mesure de départ.",
  "Une demande hors portefeuille entre par une procédure qui nomme ce qu'elle décale.", "Le schéma directeur se révise chaque année avant le budget.",
  "Le comité de portefeuille peut arrêter un projet."],
 ["définir un indicateur en cinq éléments", "calculer les deux indices de la valeur acquise", "remplir une ligne du registre des bénéfices", "préparer une révision annuelle"],
 [("Deux indices", 1, "À une date donnée, un portefeuille présente une valeur planifiée de 1~200~millions, une valeur acquise de 900 et un coût réel de 1~000. Calculez les deux indices et commentez."),
  ("Un indicateur", 2, "Définissez en cinq éléments l'indicateur « applications clés avec reprise éprouvée ». Dites ce que signifie « éprouvée » et quelle pièce le prouve."),
  ("Le projet de mars", 2, "Une direction de l'ANPP a lancé seule un projet en mars 2028. Rédigez la décision que le comité de portefeuille aurait dû prendre, selon la procédure de ce chapitre."),
  ("Arrêter", 3, "À la revue de 2029, le lot~1 de la refonte a consommé 80~\\% de son budget pour 45~\\% de ses travaux. Calculez l'indice de coût, estimez le coût final si la tendance se prolonge et rédigez la note d'options au comité~: poursuivre, redéfinir, arrêter.")],
 ["Kaplan et Norton~\\cite{kaplannorton1992}.", "Ward et Daniel~\\cite{warddaniel2006}.", "ISO~21502~\\cite{iso21502} et ISO~21504~\\cite{iso21504}.", "Weill et Ross~\\cite{weillross2004}."],
 "Piloter suppose que rien de grave n'arrive. Le Chapitre~\\ref{chap:maitriser} traite de ce qui peut arriver.")
