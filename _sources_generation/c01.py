# -*- coding: utf-8 -*-
from ch import *
corps = sec("Trois Mots à Séparer", "sec:c01-mots") + r"""
\begin{boxdef}
\textbf{Stratégie.} Ensemble cohérent de choix par lesquels une organisation décide où elle veut aller, ce qu'elle
fera et ce qu'elle renonce à faire, compte tenu de ses moyens et de son environnement.
\end{boxdef}

Une \termecle{stratégie} se reconnaît à ses renoncements. Un texte qui promet tout à tous n'en est pas une. Dans
une entreprise, elle vise un avantage sur des concurrents. Dans une administration, elle vise l'accomplissement
d'une mission fixée par un texte, avec des moyens votés.

\begin{boxdef}
\textbf{Système d'information.} Ensemble organisé de personnes, de processus, de données et de moyens
techniques qui collecte, traite, conserve et diffuse l'information dont une organisation a besoin pour agir.
\end{boxdef}

Le \termecle{système d'information} dépasse l'informatique. Un registre papier tenu dans une antenne régionale
en fait partie. Un schéma directeur qui n'inventorie que des serveurs décrit un parc et non un système
d'information.

\begin{boxdef}
\textbf{Numérique.} Usage des technologies de l'information qui modifie le service rendu, la relation avec
l'usager ou le modèle d'activité lui-même et pas seulement l'outil de travail interne.
\end{boxdef}

La distinction entre informatique et \termecle{numérique} n'est pas de mode. Informatiser, c'est faire plus vite
ce que l'on faisait déjà. Passer au numérique, c'est faire autrement~: le bénéficiaire qui suit son dossier sur
son téléphone ne reçoit pas le même service que celui qui se déplace à un guichet équipé d'un ordinateur.

""" + tab("L{3.0cm}L{4.4cm}L{4.6cm}", ["Notion", "Question à laquelle elle répond", "Exemple à l'ANPP"], [
    ["Stratégie de l'organisation", "Que voulons-nous devenir~?", "Payer chaque bénéficiaire à date fixe, où qu'il vive"],
    ["Stratégie numérique", "Que change le numérique dans notre mission~?", "Paiement sur compte mobile, suivi en ligne"],
    ["Stratégie du SI", "De quelles informations et applications avons-nous besoin~?", "Un référentiel unique des bénéficiaires"],
    ["Stratégie informatique", "Avec quelles techniques et quels moyens~?", "Hébergement, réseau des antennes, compétences"]],
    "Quatre niveaux de stratégie", "1.1") + r"""

La séparation entre stratégie du système d'information et stratégie informatique vient d'Earl et a été reprise par
Peppard et Ward~\cite{wardpeppard2016}. La première dit le \textit{quoi}, tirée des besoins des métiers. La
seconde dit le \textit{comment}. Beaucoup de schémas directeurs ne traitent que la seconde.

""" + sec("Du Plan Informatique à la Stratégie Numérique", "sec:c01-histoire") + r"""
Le vocabulaire a changé avec la place de l'informatique dans l'organisation.

""" + tab("L{2.2cm}L{3.2cm}L{6.6cm}", ["Période", "Document type", "Ce qu'il cherchait"], [
    ["Années 1970", "Plan informatique", "Programmer l'achat des machines et l'automatisation des tâches de masse"],
    ["Années 1980", "Schéma directeur informatique", "Relier les applications aux objectifs de l'organisation. En France, méthode RACINES"],
    ["Années 1990", "Schéma directeur du système d'information", "Aligner le système d'information sur la stratégie. Modèle de Henderson et Venkatraman"],
    ["Années 2000", "Plan d'urbanisation, gouvernance", "Maîtriser la cohérence d'ensemble et les droits de décision"],
    ["Depuis 2010", "Stratégie numérique", "Faire du numérique une composante de la stratégie elle-même"]],
    "Cinq générations de documents", "1.2") + r"""

Ces générations ne se remplacent pas. Elles s'empilent. Une administration qui écrit sa stratégie numérique a
toujours besoin de programmer des achats de matériel. L'erreur est de croire qu'un nouveau mot dispense du
travail de l'ancien.

""" + sec("Ce que Contient un Schéma Directeur", "sec:c01-contenu") + r"""
\begin{boxprocedure}
\textbf{Les six pièces d'un schéma directeur.}
\begin{enumerate}
    \item \textbf{Le rappel de la stratégie} de l'organisation et de ses contraintes.
    \item \textbf{Le diagnostic} de l'existant, avec ses forces et ses écarts.
    \item \textbf{La cible}~: ce que sera le système d'information à l'horizon retenu, avec ses principes.
    \item \textbf{Le portefeuille de projets}, hiérarchisé, avec les dépendances.
    \item \textbf{La trajectoire}~: le calendrier, le budget par année, les moyens humains.
    \item \textbf{La gouvernance}~: qui décide, qui suit, quels indicateurs, quelle révision.
\end{enumerate}
\end{boxprocedure}

Chaque pièce répond à l'une des trois questions du prologue. Les pièces 1 à 3 établissent l'alignement. La
pièce 5 établit le financement. La pièce 6 établit la gouvernance. La pièce 4 les relie.

\subsection{Ce qu'il n'est pas}

""" + tab("L{4.2cm}L{7.8cm}", ["Confusion", "Différence"], [
    ["Un inventaire", "L'inventaire décrit ce qui existe. Le schéma directeur décide de ce qui existera"],
    ["Un cahier des charges", "Le cahier des charges décrit un projet. Le schéma directeur choisit les projets"],
    ["Un plan d'urbanisation", "Le plan d'urbanisation fixe des règles de construction. Le schéma directeur fixe un programme de travaux"],
    ["Un budget", "Le budget autorise une dépense annuelle. Le schéma directeur donne la raison de cette dépense sur plusieurs années"],
    ["Une politique de sécurité", "La politique fixe des règles. Le schéma directeur programme les moyens de les appliquer"]],
    "Cinq confusions fréquentes", "1.3") + r"""

""" + sec("L'Horizon et la Révision", "sec:c01-horizon") + r"""
Un schéma directeur couvre le plus souvent trois à cinq ans. En dessous de trois ans, il ne laisse pas le temps de
conduire un projet structurant. Au-delà de cinq ans, les hypothèses techniques et budgétaires ne tiennent plus.

L'horizon ne dit rien de la fréquence de révision. Un document à cinq ans se révise chaque année. La trajectoire
est précise pour la première année, indicative pour les suivantes. On parle de \termecle{plan glissant}. À
l'ANPP, l'horizon retenu est 2027-2031, calé sur la fin de la Stratégie nationale de développement en 2030 et sur
le cadre budgétaire à moyen terme de l'Agence.

""" + sec("Trois Organisations, Trois Régimes", "sec:c01-cas") + r"""
\begin{boxscenario}{Les trois missions d'AUDIX CONSEIL en 2027}
""" + tab("L{2.6cm}L{3.4cm}L{5.8cm}", ["Organisation", "Nature", "Demande"], [
    ["ANPP", "Établissement public, Yaoundé, 412 agents", "Schéma directeur 2027-2031, après l'échec du précédent"],
    ["LiZbiZ", "Société anonyme de logistique, Douala", "Stratégie numérique à l'appui du plan de croissance HORIZON~3"],
    ["BANQUE SANAGA", "Établissement de crédit, Douala", "Schéma directeur exigé après la panne et l'Opération WOURI"]]) + r"""

\medskip
\textbf{Analyse} (confiance élevée). Les trois demandes portent le même nom et obéissent à trois régimes.
L'Agence achète selon le code des marchés publics et finance selon le régime financier de l'État. L'entreprise
décide seule sous le droit des sociétés. La banque rend compte à un superviseur communautaire. Le
Chapitre~\ref{chap:droit} en tire une carte d'applicabilité.
\end{boxscenario}
"""
chapitre("partie1/P01_C01_vocabulaire.tex", 1, "Stratégie, Système d'Information, Numérique", "chap:vocabulaire", "Vocabulaire",
 "« Informatiser, c'est faire plus vite.\\\\\n    Passer au numérique, c'est faire autrement. »", "Principe du cours",
 "Fondamental", "Prologue~; gouvernance stratégique des SI (UE MSN-2S3-MSI01)",
 ["Définir stratégie, système d'information et numérique.", "Distinguer quatre niveaux de stratégie.",
  "Situer le schéma directeur dans l'histoire des documents de planification.", "Énumérer les six pièces d'un schéma directeur.",
  "Dire ce qu'un schéma directeur n'est pas."],
 "« notre stratégie, c'est la fibre »", r"""
Douala, jeudi 14~janvier~2027. M.~ETEME, directeur général de LiZbiZ, reçoit M.~BEYALA. Son entreprise de
logistique veut doubler son chiffre d'affaires en trois ans. C'est le plan HORIZON~3. « Notre stratégie
numérique est prête. Nous installons la fibre dans les quatre sites et nous changeons tous les postes. »

M.~BEYALA demande ce que les clients verront de différent. M.~ETEME hésite. La fibre accélère les échanges entre
les entrepôts. Elle ne change rien pour le client qui attend un colis. Le concurrent qui vient de s'installer,
lui, envoie un message à chaque étape de la livraison.

\begin{boxalert}
\textbf{Violation typique.} Présenter un programme d'équipement comme une stratégie numérique.

\smallskip
\textbf{Règle~:} une stratégie numérique se formule du point de vue de celui que l'organisation sert. Si rien
ne change pour lui, il s'agit d'une stratégie informatique. Elle est nécessaire. Elle ne suffit pas.
\end{boxalert}
""", corps,
 [("Directeur des systèmes d'information", "Refuser d'écrire seul le schéma directeur. Les pièces 1 et 3 appartiennent aux métiers et à la direction générale."),
  ("Dirigeant", "Dire la stratégie de l'organisation avant de demander celle du système d'information. Sans la première, la seconde est un inventaire."),
  ("Consultant", "Demander à chaque interlocuteur ce qu'il appelle schéma directeur. Trois personnes donnent souvent trois définitions.")],
 ["Une stratégie se reconnaît à ses renoncements.", "Le système d'information comprend des personnes, des processus, des données et des techniques.",
  "Quatre niveaux~: stratégie de l'organisation, stratégie numérique, stratégie du SI, stratégie informatique.",
  "Un schéma directeur réunit six pièces~: stratégie rappelée, diagnostic, cible, portefeuille, trajectoire, gouvernance.",
  "L'horizon est de trois à cinq ans, la révision est annuelle."],
 ["distinguer stratégie numérique et stratégie informatique sur un exemple", "citer les six pièces d'un schéma directeur", "expliquer ce qu'est un plan glissant"],
 [("Classer dix phrases", 1, "Classez dans l'un des quatre niveaux du Tableau~1.1~: (a) migrer la messagerie~; (b) ouvrir un guichet en ligne~; (c) servir les zones rurales~; (d) créer un référentiel des agents~; (e) recruter deux administrateurs de bases de données~; (f) réduire de moitié le délai de paiement~; (g) permettre le suivi d'un dossier par SMS~; (h) remplacer les onduleurs~; (i) partager les données avec l'état civil~; (j) devenir le premier logisticien du pays."),
  ("La stratégie de LiZbiZ", 2, "Réécrivez en dix lignes la stratégie numérique de LiZbiZ du point de vue de ses clients. Dites ensuite ce que devient le projet de fibre dans ce nouveau texte."),
  ("Six pièces", 2, "Reprenez le Tableau~P.1 du prologue. Pour chacune des six pièces d'un schéma directeur, dites si le document de 2021 la contenait, en partie ou pas du tout."),
  ("Horizon", 3, "La BANQUE SANAGA veut un schéma directeur à dix ans « pour ne plus y revenir ». Rédigez la réponse de M.~BEYALA en séparant ce qui peut être fixé à dix ans de ce qui ne le peut pas.")],
 ["Peppard et Ward~\\cite{wardpeppard2016}, chapitres 1 à 3.", "Bharadwaj et al.~\\cite{bharadwaj2013}, sur la fusion des stratégies."],
 "Les mots sont posés. Reste à savoir comment une organisation choisit sa stratégie. Le Chapitre~\\ref{chap:strategie} présente les théories que le consultant doit connaître dans leur texte d'origine.")
