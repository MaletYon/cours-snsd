# -*- coding: utf-8 -*-
from ch import *
corps = sec("Cinq Regards sur l'Existant", "sec:c09-regards") + r"""
Le diagnostic décrit l'existant sans le juger d'avance. Il porte cinq regards. Chacun a ses sources et son
livrable.

""" + tab("L{2.6cm}L{4.6cm}L{4.8cm}", ["Regard", "Question", "Sources"], [
    ["Métier", "Que fait l'organisation, que veut-elle faire~?", "Plan stratégique, entretiens de direction"],
    ["Applications", "Quels logiciels, pour quels métiers, dans quel état~?", "Inventaire, contrats, entretiens d'utilisateurs"],
    ["Infrastructures", "Sur quoi tout cela tourne-t-il~?", "Inventaire technique, visites de salles"],
    ["Organisation", "Qui s'en occupe, avec quelles compétences~?", "Organigramme, fiches de poste"],
    ["Finances", "Combien cela coûte-t-il, pour quoi~?", "Comptes des cinq derniers exercices, marchés"]],
    "Les cinq regards du diagnostic", "9.1") + r"""

Le diagnostic ne propose rien. Les idées de solution qui viennent pendant les entretiens se notent dans un
carnet à part. Elles serviront à la phase de cible.

""" + sec("Collecter", "sec:c09-collecter") + r"""
Trois moyens se complètent. Les documents disent ce qui a été décidé. Les entretiens disent ce qui se fait.
L'observation dit ce qui se passe.

À l'ANPP, le cabinet a demandé 34~documents le premier jour. Il en a reçu 21 en deux semaines. Il a conduit
38~entretiens d'une heure~: les directeurs, les chefs de service, six chefs d'antenne, les agents de la division
informatique. Il a passé une journée au guichet de l'antenne de Bafoussam et une journée à celle de Garoua.

\begin{boxprocedure}
\textbf{Conduire un entretien de diagnostic.}
\begin{enumerate}
    \item Envoyer trois questions la veille. Pas davantage.
    \item Commencer par le travail de la personne, non par l'informatique.
    \item Demander ce qui se passe quand le système est arrêté.
    \item Demander à voir~: un écran, un fichier, un registre.
    \item Noter les faits, les chiffres et leur source. Séparer les opinions.
    \item Envoyer le compte rendu sous trois jours et le faire valider.
\end{enumerate}
\end{boxprocedure}

Un document manquant est une information. Treize des 34~documents demandés n'existent pas à l'ANPP, dont
l'inventaire des applications, le plan de secours et la liste des habilitations. Le rapport de diagnostic les
énumère.

""" + sec("L'Inventaire des Applications", "sec:c09-inventaire") + r"""
L'inventaire est une liste où chaque application occupe une ligne. La \termecle{fiche d'application} en donne
le détail. Elle répond à dix questions~: nom, métier servi, responsable côté métier, nombre d'utilisateurs,
éditeur ou auteur, année de mise en service, technologie, contrat de maintenance, coût annuel, données
personnelles traitées.

La division informatique de l'ANPP croyait gérer 31~applications. Le cabinet en a trouvé 47. Les seize autres
sont des classeurs, des bases bureautiques ou des services en ligne souscrits par une direction avec sa
carte. Trois d'entre elles servent à calculer des droits.

\begin{boxdef}
\textbf{Informatique hors contrôle.} Ensemble des outils numériques employés dans une organisation sans que la
fonction informatique les ait fournis ni recensés. Elle signale presque toujours un besoin que l'offre
officielle ne couvre pas.
\end{boxdef}

""" + sec("Deux Notes par Application", "sec:c09-notes") + r"""
Chaque application reçoit deux notes de 1 à 5. La \termecle{valeur pour le métier} mesure le service rendu. La
\termecle{santé technique} mesure la capacité à durer. Chaque note se calcule sur quatre critères notés de 1 à 5
dont on prend la moyenne.

""" + tab("L{5.6cm}L{6.4cm}", ["Valeur pour le métier", "Santé technique"], [
    ["Contribution aux objectifs du plan stratégique", "Technologie encore maintenue par son éditeur"],
    ["Part de l'activité qui en dépend", "Compétences disponibles pour la faire évoluer"],
    ["Satisfaction des utilisateurs", "Nombre d'incidents sur douze mois"],
    ["Absence d'alternative manuelle", "Documentation et sauvegardes vérifiées"]],
    "Les huit critères de notation d'une application", "9.2") + r"""

Le seuil est fixé à 3. Le croisement des deux notes donne quatre décisions.

""" + tab("L{3.0cm}L{3.0cm}L{2.4cm}L{3.6cm}", ["Valeur", "Santé", "Décision", "Applications de l'ANPP"], [
    ["3 ou plus", "3 ou plus", "Investir", "6"],
    ["3 ou plus", "Moins de 3", "Refondre", "14"],
    ["Moins de 3", "3 ou plus", "Conserver", "18"],
    ["Moins de 3", "Moins de 3", "Retirer", "9"]],
    "Les quatre décisions et le résultat pour les 47 applications", "9.3") + r"""

Quatorze applications à refondre~: c'est le cœur du prochain schéma directeur. Elles comprennent la liquidation
des droits, écrite en 2004 dans un langage que deux agents seulement savent lire. Neuf applications à retirer~:
c'est une économie immédiate si l'on résilie leurs contrats.

\begin{boxalert}
\textbf{Violation typique.} Noter les applications en réunion, à main levée.

\smallskip
\textbf{Règle~:} chaque note renvoie à une pièce. Le nombre d'incidents vient du registre, la satisfaction
d'une enquête, la date de fin de maintenance du contrat. Une note sans pièce est une opinion.
\end{boxalert}

""" + sec("Les Infrastructures et la Sécurité", "sec:c09-infra") + r"""
Le regard technique recense les salles, les serveurs, le réseau, les postes, les sauvegardes. Il vérifie quatre
points qui commandent la continuité~: l'alimentation électrique, la climatisation, le lien entre les sites,
l'existence d'un site de secours.

À l'ANPP, la salle du siège abrite tous les serveurs. Les antennes y accèdent par un lien unique. La panne de
mars~2024 a duré quatre jours parce qu'un onduleur a cédé et que la dernière sauvegarde restaurable datait de
onze jours. Le diagnostic ne refait pas l'audit de sécurité. Il en reprend les constats et note s'il existe.
À l'ANPP, l'audit obligatoire n'a pas été réalisé depuis 2020.

""" + sec("L'Organisation et les Compétences", "sec:c09-organisation") + r"""
La division informatique de l'ANPP compte 19~agents pour 412~agents de l'Agence. Le référentiel européen des
compétences numériques, la norme EN~16234-1~\cite{ecf}, sert de grille. On y repère les compétences tenues, les
compétences tenues par une seule personne et les compétences absentes.

""" + tab("L{4.6cm}cL{5.6cm}", ["Domaine", "Agents", "Constat"], [
    ["Exploitation et assistance", "11", "Effectif suffisant, astreinte non organisée"],
    ["Développement et maintenance", "5", "Deux agents seuls à connaître la liquidation"],
    ["Réseau et sécurité", "2", "Aucun responsable de la sécurité désigné"],
    ["Pilotage, projets, achats", "1", "La cheffe de division, seule"],
    ["Données", "0", "Compétence absente"]],
    "La division informatique de l'ANPP par domaine", "9.4") + r"""

""" + sec("Les Finances", "sec:c09-finances") + r"""
Le regard financier reconstitue la dépense informatique réelle des cinq derniers exercices. Elle ne se lit pas
dans une seule ligne du budget. Il faut y ajouter les achats faits par les autres directions, les contrats
portés par les moyens généraux et la masse salariale de la division.

La dépense se partage en deux. Le \termecle{fonctionnement} maintient l'existant~: salaires, maintenance,
licences, liaisons, énergie. Le \termecle{projet} crée du nouveau. Le rapport entre les deux dit la marge de
manœuvre.

""" + tab("L{4.2cm}rr", ["Nature", "Montant 2019-2023 (millions de FCFA)", "Part"], [
    ["Fonctionnement", "2 418", "78~\\%"],
    ["Projets", "682", "22~\\%"],
    ["Total", "3 100", "100~\\%"]],
    "La dépense informatique de l'ANPP sur cinq ans", "9.5") + r"""

Avec 78~\% de fonctionnement, l'ANPP consacre aux projets 136~millions par an en moyenne. Le schéma directeur de
2019 annonçait 6,3~milliards. L'écart était lisible dès le premier jour pour qui avait fait ce tableau.

""" + sec("Restituer", "sec:c09-restituer") + r"""
Le rapport de diagnostic tient en trente pages. Il s'ouvre par dix constats au plus, rangés par ordre de
gravité. Chaque constat suit la même forme~: le fait, la pièce, la conséquence pour le métier. Une synthèse en
quatre cases, forces, faiblesses, occasions, menaces, peut le clore. Elle résume, elle ne remplace pas les
constats.

\begin{boxscenario}{Mission ANPP. Les cinq premiers constats, 21 mars 2025}
\begin{enumerate}
    \item La liquidation des droits repose sur une application de 2004 que deux agents savent maintenir.
    \item Aucun site de secours. La dernière panne a suspendu les paiements quatre jours.
    \item Seize applications sur 47 échappent à la division informatique. Trois calculent des droits.
    \item Les projets reçoivent 22~\% de la dépense, soit 136~millions par an.
    \item Treize documents de référence n'existent pas, dont l'inventaire et le plan de secours.
\end{enumerate}
\end{boxscenario}

Le comité de pilotage valide le diagnostic. Les directeurs y lisent parfois des faits qui les gênent. Le
consultant ne retire pas un constat prouvé. Il peut en revoir la formulation.

""" + lecture("Le diagnostic de la mission ANPP, 21 mars 2025", [
    ("L'inventaire couvre toutes les applications trouvées", "O", "47 fiches"),
    ("Chaque application a un responsable côté métier", "N", "19 fiches sans responsable"),
    ("Chaque note renvoie à une pièce", "O", "Registre des pièces du diagnostic"),
    ("La dépense de cinq exercices est reconstituée", "O", "Tableau 9.5"),
    ("La dépense des autres directions est incluse", "K", "Trois directions n'ont pas répondu"),
    ("Les compétences critiques sont repérées", "O", "Tableau 9.4"),
    ("Les comptes rendus d'entretien sont validés", "O", "38 validations"),
    ("Le rapport est approuvé par le comité de pilotage", "O", "Procès-verbal du 21 mars")],
    r"""Six \OUI{} sur huit. Le \NON{} n'est pas une faute du cabinet. Il est un constat~: dix-neuf applications
n'ont pas de propriétaire. Le \NEK{} est de preuve. Tant que trois directions n'ont pas transmis leurs achats,
le total de 3,1~milliards est un plancher.""") + r"""
"""
chapitre("partie4/P04_C09_diagnostiquer.tex", 9, "Diagnostiquer l'Existant", "chap:diagnostic", "Diagnostiquer",
 "« On ne gère bien que ce que l'on a d'abord compté. »", "Principe du cours",
 "Intermédiaire", "Chapitre~\\ref{chap:cadrer}",
 ["Porter cinq regards sur l'existant.", "Conduire un entretien de diagnostic.", "Tenir un inventaire et une fiche d'application.",
  "Noter une application sur sa valeur et sa santé.", "Reconstituer la dépense informatique et la partager entre fonctionnement et projets.",
  "Rédiger un constat en trois temps."],
 "« nous avons trente et une applications »", r"""
Yaoundé, lundi 10~février~2025. Mme~NGO BIYONG remet au cabinet la liste des applications de l'Agence. Elle en
compte 31. Le même jour, Mme~EKANI revient de la direction des prestations avec une clé contenant un classeur
de calcul. Un chef de service l'a construit en 2017 pour corriger les pensions de réversion que l'application
officielle calcule mal. Il traite 4~200 dossiers par an. Personne à la division informatique ne le connaît.

En trois semaines, le cabinet trouve seize outils de cette sorte. Le consultant junior propose de les appeler
« applications pirates ». M.~BEYALA corrige~: « Ce sont des besoins que personne n'a écoutés. Vous les
inventoriez comme les autres. »

\begin{boxalert}
\textbf{Violation typique.} Établir l'inventaire à partir de la seule liste de la fonction informatique.

\smallskip
\textbf{Règle~:} l'inventaire se construit depuis les métiers. On demande à chaque service avec quoi il
travaille, puis on rapproche de la liste officielle.
\end{boxalert}
""", corps,
 [("Consultant", "Demander les documents le premier jour. Noter la source de chaque chiffre. Tenir un registre des pièces."),
  ("Directeur des systèmes d'information", "Fournir l'inventaire qu'il a, sans le maquiller. Accepter que le diagnostic en trouve davantage."),
  ("Contrôleur de gestion", "Reconstituer la dépense par nature et par direction. Signaler les achats hors budget informatique."),
  ("Auditeur", "Reprendre les notes d'un échantillon d'applications et remonter aux pièces.")],
 ["Le diagnostic porte cinq regards~: métier, applications, infrastructures, organisation, finances.", "Un document manquant est un constat.",
  "L'inventaire se construit depuis les métiers.", "Chaque application reçoit une note de valeur et une note de santé, d'où quatre décisions~: investir, refondre, conserver, retirer.",
  "La dépense se partage entre fonctionnement et projets.", "Un constat s'écrit en trois temps~: le fait, la pièce, la conséquence.",
  "Le diagnostic ne propose pas de solution."],
 ["conduire un entretien et en rédiger le compte rendu", "remplir une fiche d'application", "calculer les deux notes d'une application et en tirer la décision", "reconstituer la part des projets dans la dépense"],
 [("Deux notes", 1, "Une application de l'ANPP obtient 4, 5, 2, 4 sur les critères de valeur et 1, 2, 3, 2 sur les critères de santé. Calculez les deux notes et donnez la décision."),
  ("La dépense", 2, "Sur un exercice, une organisation dépense 310~millions de salaires informatiques, 240 de maintenance et de licences, 90 de liaisons et 160 de projets. Calculez la part des projets. Elle veut la porter à 35~\\% sans augmenter le total. De combien doit baisser le fonctionnement~?"),
  ("Trois constats", 2, "Rédigez en trois temps les constats correspondant aux faits suivants~: l'audit de sécurité n'a pas été fait depuis 2020, la division n'a aucun agent chargé des données, dix-neuf applications n'ont pas de responsable côté métier."),
  ("Les seize", 3, "Proposez une conduite pour les seize applications hors contrôle de l'ANPP. Distinguez celles qui calculent des droits des autres. Dites ce que le schéma directeur doit prévoir pour que le phénomène ne se reproduise pas, sans l'interdire par principe.")],
 ["Peppard et Ward sur l'évaluation du portefeuille existant~\\cite{wardpeppard2016}.", "COBIT~2019 pour les niveaux de capacité~\\cite{cobit2019}.", "La norme EN~16234-1~\\cite{ecf}."],
 "L'existant est connu. Reste à dire où aller. C'est l'objet du Chapitre~\\ref{chap:cible}.")
