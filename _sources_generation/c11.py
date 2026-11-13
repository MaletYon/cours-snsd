# -*- coding: utf-8 -*-
from ch import *
corps = sec("Du Chantier au Projet", "sec:c11-projet") + r"""
La cible a donné des chantiers. Le portefeuille les découpe en projets. Un projet a un résultat livrable, un
responsable, un coût et une durée. La norme ISO~21504 appelle \termecle{portefeuille} l'ensemble des projets et
des programmes réunis pour atteindre des objectifs stratégiques~\cite{iso21504}. Gérer un portefeuille, c'est
choisir, ordonner et réviser.

Chaque projet candidat tient sur une \termecle{fiche de projet} d'une page. L'Annexe~B en donne le modèle.

""" + tab("L{3.4cm}L{8.6cm}", ["Rubrique", "Contenu"], [
    ["Résultat", "Ce qui existera à la fin, en une phrase vérifiable"],
    ["Objectif servi", "L'objectif du plan stratégique et la capacité visée"],
    ["Responsable", "Un directeur de métier, nommé"],
    ["Coût", "Investissement et coût annuel après mise en service"],
    ["Durée", "En mois, passation du marché comprise"],
    ["Dépendances", "Les projets qui doivent être finis avant"],
    ["Ce qu'il remplace", "Les applications retirées"],
    ["Risque principal", "Un seul, avec sa parade"]],
    "La fiche de projet", "11.1") + r"""

À l'ANPP, les groupes de travail ont produit 40~fiches. Leur coût cumulé atteint 6,8~milliards de FCFA.
L'enveloppe indiquée par le directeur général après le choix du scénario~B est de 4,2~milliards sur cinq ans.
Il faut choisir.

""" + sec("Trier", "sec:c11-trier") + r"""
Le tri sépare d'abord les projets \termecle{obligatoires}. Un projet est obligatoire s'il répond à un texte, à
une injonction ou à un risque que l'organisation ne peut pas porter. Ils ne se notent pas, ils s'inscrivent. On
vérifie seulement que le mot n'est pas employé par commodité.

L'ANPP en compte cinq~: le site de secours et le plan de continuité, l'audit de sécurité, la mise en conformité
à la loi sur les données personnelles, le remplacement des onduleurs, la sortie d'un système dont l'éditeur
cesse la maintenance en 2026. Ils pèsent 1~150~millions.

Les 35~autres se notent. La note de valeur, sur 100, reprend les critères du choix de scénario. Le rapport de
la valeur au coût donne un rang.

""" + tab("L{0.9cm}L{4.4cm}ccc", ["N°", "Projet", "Valeur", "Coût (millions)", "Valeur par million"], [
    ["P15", "Tableau de bord des paiements", "55", "60", "0,92"],
    ["P38", "Refonte du site d'information", "20", "45", "0,44"],
    ["P21", "Comptabilité analytique", "60", "150", "0,40"],
    ["P12", "Guichet unique des demandes", "70", "180", "0,39"],
    ["P07", "Référentiel des bénéficiaires", "90", "340", "0,26"],
    ["P33", "Application mobile des agents", "30", "120", "0,25"]],
    "Six projets classés par valeur rapportée au coût", "11.2") + r"""

Le classement ne suffit pas. Le référentiel des bénéficiaires arrive cinquième, pourtant la refonte de la
liquidation en dépend. Le site d'information arrive deuxième avec une valeur de 20. Le ratio favorise les
petits projets. On le corrige par deux règles~: un seuil de valeur, fixé à 40 à l'ANPP, en dessous duquel un
projet n'est pas retenu, puis l'examen des dépendances.

\begin{boxalert}
\textbf{Violation typique.} Qualifier d'obligatoire un projet que l'on veut soustraire à l'arbitrage.

\smallskip
\textbf{Règle~:} un projet obligatoire cite le texte, l'injonction ou le risque qui l'impose. Sans cette
référence, il se note comme les autres.
\end{boxalert}

""" + sec("Équilibrer", "sec:c11-equilibrer") + r"""
Un portefeuille se juge aussi dans son ensemble. La grille de McFarlan, vue au Chapitre~\ref{chap:alignement},
sert de contrôle~: un portefeuille tout entier consacré au soutien ne prépare rien, un portefeuille tout entier
stratégique néglige ce qui tourne. On regarde aussi la répartition par objectif, par direction et par niveau de
risque.

""" + tab("L{4.6cm}cr", ["Domaine", "Projets", "Montant (millions)"], [
    ["Obligatoires~: secours, sécurité, conformité", "5", "1 150"],
    ["Refonte de la production", "6", "1 820"],
    ["Référentiels et données", "3", "520"],
    ["Relation avec les bénéficiaires", "4", "410"],
    ["Soutien et pilotage", "4", "280"],
    ["Total retenu", "22", "4 180"]],
    "Le portefeuille retenu par l'ANPP", "11.3") + r"""

Vingt-deux projets sont retenus pour 4~180~millions. Sur les dix-huit autres, onze sont différés après 2029
avec leur fiche conservée, sept sont rejetés. La liste des projets écartés figure au schéma directeur avec le
motif. Elle évite que les mêmes demandes reviennent chaque année par une autre porte.

""" + sec("Ordonner", "sec:c11-ordonner") + r"""
Trois contraintes fixent l'ordre. Les \termecle{dépendances}~: on ne refond pas la liquidation avant d'avoir le
référentiel des bénéficiaires, on ne migre rien avant d'avoir un secours. La \termecle{capacité à faire}~:
l'ANPP ne peut pas conduire plus de six projets à la fois avec ses chefs de projet et ses directions. Les
\termecle{délais de droit public}, vus au Chapitre~\ref{chap:droit}~: inscription budgétaire, programmation,
passation.

La refonte de la production est découpée en trois lots. Chaque lot livre un résultat utilisable seul.

""" + tab("L{4.2cm}ccccc", ["Projet ou lot", "2025", "2026", "2027", "2028", "2029"], [
    ["Onduleurs, audit de sécurité", "X", "", "", "", ""],
    ["Site de secours, continuité", "X", "X", "", "", ""],
    ["Référentiel des bénéficiaires", "X", "X", "", "", ""],
    ["Lot 1. Immatriculation", "", "X", "X", "", ""],
    ["Lot 2. Liquidation", "", "", "X", "X", ""],
    ["Lot 3. Paiement, recouvrement", "", "", "", "X", "X"],
    ["Guichet unique", "", "X", "X", "", ""],
    ["Comptabilité analytique", "", "", "X", "X", ""],
    ["Retrait de neuf applications", "X", "X", "", "", ""]],
    "La trajectoire 2025-2029 (extrait)", "11.4") + r"""

\begin{boxdef}
\textbf{Trajectoire.} Ordre daté des projets retenus, avec pour chaque année ce qui démarre, ce qui est livré
et ce qui est retiré. Elle se lit année par année~: à la fin de chacune, l'organisation dispose d'un système
qui fonctionne.
\end{boxdef}

""" + sec("Montrer des Résultats Tôt", "sec:c11-tot") + r"""
Un schéma directeur qui ne livre rien la première année perd ses soutiens. Le portefeuille réserve donc
quelques projets courts, peu coûteux, visibles. À l'ANPP, le tableau de bord des paiements coûte 60~millions
et sera livré en six mois. Le retrait de neuf applications ne coûte presque rien et libère 85~millions par an de
contrats.

Ces résultats rapides ne doivent pas contredire la cible. Un tableau de bord branché sur l'application de 2004
sera rebranché en 2027. Le coût de ce rebranchement est écrit dans la fiche.

""" + sec("Les Paiements par Année", "sec:c11-annees") + r"""
La trajectoire donne un profil de dépense. Il se compare à ce que l'organisation peut payer chaque année.

""" + tab("L{3.4cm}rrrrrr", ["", "2025", "2026", "2027", "2028", "2029", "Total"], [
    ["Paiements (millions)", "380", "1 050", "1 180", "940", "630", "4 180"],
    ["Projets en cours", "5", "6", "6", "5", "4", ""]],
    "Le profil de dépense de la trajectoire", "11.5") + r"""

L'année 2025 est faible. Les marchés ne seront notifiés qu'au second semestre. Le pic de 2027 dépasse d'un
facteur huit la moyenne annuelle des projets de la période passée, qui était de 136~millions. La trajectoire
n'est donc crédible que si le financement change d'échelle. C'est la question du chapitre suivant.

\begin{boxprocedure}
\textbf{Construire un portefeuille et sa trajectoire.}
\begin{enumerate}
    \item Réunir une fiche par projet candidat.
    \item Isoler les obligatoires, référence à l'appui.
    \item Noter les autres, appliquer le seuil de valeur, classer.
    \item Retenir dans la limite de l'enveloppe. Écrire le motif de chaque rejet.
    \item Vérifier l'équilibre par objectif, par domaine, par risque.
    \item Ordonner selon les dépendances, la capacité à faire et les délais de droit.
    \item Découper les grands projets en lots utilisables seuls.
    \item Tracer le profil annuel et le comparer aux moyens.
\end{enumerate}
\end{boxprocedure}

""" + lecture("Le portefeuille de l'ANPP, 23 mai 2025", [
    ("Chaque projet retenu a une fiche complète", "O", "22 fiches"),
    ("Chaque projet a un responsable côté métier", "O", "Rubrique renseignée sur 22 fiches"),
    ("Chaque projet obligatoire cite sa référence", "O", "Cinq références"),
    ("Le total retenu tient dans l'enveloppe", "O", "4 180 pour 4 200"),
    ("Les projets écartés sont listés avec leur motif", "O", "Annexe du portefeuille"),
    ("Les dépendances sont respectées par la trajectoire", "O", "Tableau 11.4"),
    ("Le nombre de projets simultanés reste dans la capacité", "O", "Six au plus"),
    ("Chaque projet nomme ce qu'il remplace", "N", "Sept fiches muettes"),
    ("Le coût après mise en service est chiffré", "N", "Neuf fiches sans coût annuel"),
    ("Une provision pour aléas est prévue", "N", "Marge de 20 millions seulement")],
    r"""Sept \OUI{} sur dix. Les trois \NON{} vont dans le même sens~: le portefeuille est bien choisi et mal
bordé. Sans coût annuel, le fonctionnement de 2029 est inconnu. Avec 20~millions de marge sur 4,2~milliards, le
premier dépassement oblige à retirer un projet. Le comité de pilotage a approuvé le portefeuille sous réserve
que la phase de chiffrage lève ces trois points.""") + r"""
"""
chapitre("partie4/P04_C11_portefeuille.tex", 11, "Portefeuille et Trajectoire", "chap:portefeuille", "Portefeuille",
 "« Gouverner, c'est choisir. »", "Pierre Mendès France, discours à l'Assemblée nationale, 3~juin~1953",
 "Intermédiaire", "Chapitre~\\ref{chap:cible}",
 ["Rédiger une fiche de projet.", "Distinguer un projet obligatoire d'un projet arbitrable.", "Classer des projets par valeur rapportée au coût et corriger le classement.",
  "Vérifier l'équilibre d'un portefeuille.", "Ordonner des projets selon trois contraintes.", "Tracer un profil annuel de dépense."],
 "« quarante projets, tous prioritaires »", r"""
Yaoundé, lundi 28~avril~2025. Les groupes de travail remettent leurs fiches. Il y en a quarante. Chaque
direction a écrit « priorité~1 » en tête des siennes. Le total fait 6,8~milliards. M.~OWONA a dit 4,2.

Le directeur des prestations propose de tout garder et d'étaler sur huit ans. M.~ABDOULAYE propose de réduire
chaque projet de 40~\%. Mme~EKANI fait remarquer qu'un site de secours à 60~\% ne secourt rien. Il faudra
retirer des projets entiers. Personne ne veut retirer les siens.

\begin{boxalert}
\textbf{Violation typique.} Tenir dans l'enveloppe en rabotant tous les projets du même pourcentage.

\smallskip
\textbf{Règle~:} un portefeuille se réduit en retirant des projets, non en les amputant. Un projet sous-financé
coûte son budget et ne livre pas son résultat.
\end{boxalert}
""", corps,
 [("Directeur de métier", "Signer comme responsable de ses projets. Accepter par écrit le rejet des autres."),
  ("Responsable de portefeuille", "Tenir les fiches à jour. Présenter chaque trimestre l'état des 22 projets sur une page."),
  ("Directeur financier", "Rapprocher le profil annuel du cadre de dépenses. Exiger le coût après mise en service."),
  ("Consultant", "Faire écrire les motifs de rejet. Refuser les obligatoires sans référence.")],
 ["Un projet tient sur une fiche d'une page.", "Les obligatoires s'inscrivent d'abord, référence à l'appui.", "Les autres se notent. Le ratio se corrige par un seuil de valeur et par les dépendances.",
  "Un portefeuille se réduit en retirant des projets entiers.", "Trois contraintes d'ordre~: dépendances, capacité à faire, délais de droit.",
  "Les grands projets se découpent en lots utilisables seuls.", "Le profil annuel se compare aux moyens."],
 ["remplir une fiche de projet", "classer dix projets et justifier les corrections", "tracer une trajectoire qui respecte des dépendances", "dresser le profil annuel de dépense"],
 [("Classer", 1, "Calculez la valeur par million des projets suivants et classez-les~: valeur 80 pour 400~millions, valeur 45 pour 90, valeur 35 pour 50, valeur 65 pour 260. Appliquez ensuite le seuil de valeur de 40."),
  ("L'enveloppe", 2, "Avec les six projets du Tableau~11.2 et une enveloppe de 600~millions, composez le meilleur portefeuille sachant que P12 dépend de P07. Donnez le total de valeur obtenu et comparez-le à celui d'un choix par ratio seul."),
  ("Obligatoire ou non", 2, "Dites si chaque projet de l'ANPP peut être qualifié d'obligatoire et sur quelle référence~: le plan de continuité, le renouvellement des postes de travail, l'audit de sécurité, la refonte du site d'information, le registre des traitements de données personnelles."),
  ("La trajectoire contrainte", 3, "Le marché du site de secours est déclaré infructueux en 2025 et relancé. Il glisse d'un an. Reprenez le Tableau~11.4, déterminez les projets qui glissent avec lui et ceux qui peuvent avancer. Proposez une trajectoire révisée qui tient dans six projets simultanés.")],
 ["ISO~21504~\\cite{iso21504}.", "McFarlan sur le portefeuille d'applications~\\cite{mcfarlan1984}.", "Weill et Ross sur les décisions d'investissement~\\cite{weillross2004}."],
 "Le portefeuille est choisi et ordonné. Il reste à le chiffrer complètement, à le financer, à l'acheter et à trouver les personnes. C'est l'objet du Chapitre~\\ref{chap:financer}.")
