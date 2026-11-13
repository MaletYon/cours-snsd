# -*- coding: utf-8 -*-
from ch import *
corps = sec("Mesurer la Maturité : Nolan", "sec:c03-nolan") + r"""
Richard Nolan observe dans les années 1970 que la dépense informatique d'une organisation suit une courbe en S
répétée. Il en tire un modèle en six stades~\cite{nolan1979}~: initiation, contagion, contrôle, intégration,
administration des données, maturité. À chaque stade correspondent un type d'applications, une organisation et
un mode de contrôle des dépenses.

Le modèle a vieilli dans ses détails. Son idée reste juste~: une organisation ne saute pas de stade. Une agence
dont les applications ont proliféré sans contrôle ne peut pas passer d'un coup à la gestion des données. Il lui
faut d'abord reprendre la main sur ses dépenses et son inventaire.

""" + sec("Partir des Besoins des Dirigeants : Rockart", "sec:c03-rockart") + r"""
John Rockart propose en 1979 de partir des \termecle{facteurs clés de succès}~\cite{rockart1979}. Ce sont les
quelques domaines où les résultats doivent être bons pour que l'organisation réussisse. On les obtient par
entretien avec les dirigeants. De chaque facteur on tire les informations nécessaires, puis les applications.

""" + tab("L{4.2cm}L{3.8cm}L{4.0cm}", ["Facteur clé de succès de l'ANPP", "Information nécessaire", "Conséquence pour le SI"], [
    ["Payer à date fixe", "État des paiements par antenne, chaque jour", "Tableau de bord des paiements"],
    ["Ne payer que les ayants droit", "Fichier unique, à jour des décès", "Lien avec l'état civil"],
    ["Rendre compte à la tutelle", "Dépense par programme", "Comptabilité analytique"],
    ["Rester joignable", "Demandes et délais de réponse", "Guichet unique des demandes"]],
    "Des facteurs clés de succès aux applications", "3.1") + r"""

""" + sec("Classer les Applications : McFarlan", "sec:c03-mcfarlan") + r"""
Warren McFarlan publie en 1984 une grille qui classe les applications selon leur importance pour l'activité
d'aujourd'hui et pour celle de demain~\cite{mcfarlan1984}. Peppard et Ward en ont donné la version la plus
employée~\cite{wardpeppard2016}.

""" + tab("L{2.6cm}L{4.4cm}L{5.0cm}", ["Famille", "Rôle", "Conduite à tenir"], [
    ["Stratégique", "Décisive pour la stratégie future", "Investir, innover, garder la maîtrise"],
    ["Opérationnelle clé", "L'activité s'arrête sans elle", "Fiabiliser, sécuriser, ne pas rater"],
    ["À fort potentiel", "Pourrait devenir stratégique", "Expérimenter à petit budget, trancher vite"],
    ["De soutien", "Utile, sans enjeu propre", "Standardiser, acheter, réduire le coût"]],
    "La grille des applications", "3.2") + r"""

La grille interdit de gérer toutes les applications de la même manière. Une application de soutien développée sur
mesure est un gaspillage. Une application opérationnelle clé sans secours est un risque. À l'ANPP, e-RECETTES
est opérationnelle clé et n'avait pas de site de secours.

""" + sec("Le Modèle d'Alignement Stratégique", "sec:c03-sam") + r"""
Henderson et Venkatraman publient en 1993 le modèle qui a donné son nom à l'alignement~\cite{henderson1993}. Il
croise deux axes. Le premier oppose l'affaire et les technologies. Le second oppose l'externe (la stratégie) et
l'interne (l'organisation et les processus).

""" + tab("L{3.0cm}L{4.4cm}L{4.6cm}", ["", "Affaire", "Technologies de l'information"], [
    ["Externe", "Stratégie d'affaire~: offre, compétences distinctives, alliances", "Stratégie des TI~: périmètre technologique, compétences, partenariats"],
    ["Interne", "Organisation~: structure, processus, compétences", "Infrastructure et processus des TI~: architecture, processus, compétences"]],
    "Les quatre domaines du modèle d'alignement", "3.3") + r"""

L'alignement a deux dimensions. L'\textit{adéquation stratégique} relie l'externe et l'interne d'un même côté.
L'\textit{intégration fonctionnelle} relie l'affaire et les technologies. Les auteurs décrivent quatre parcours.

""" + tab("L{3.6cm}L{4.2cm}L{4.2cm}", ["Perspective", "Point de départ", "Rôle du DSI"], [
    ["Exécution de la stratégie", "La stratégie d'affaire commande l'organisation, qui commande le SI", "Exécutant"],
    ["Transformation technologique", "La stratégie d'affaire commande la stratégie des TI", "Architecte"],
    ["Potentiel concurrentiel", "Une technologie ouvre une stratégie d'affaire nouvelle", "Catalyseur"],
    ["Niveau de service", "La stratégie des TI commande le service rendu aux métiers", "Prestataire"]],
    "Quatre perspectives d'alignement", "3.4") + r"""

La plupart des schémas directeurs ne connaissent que la première perspective. La troisième est celle du
numérique~: c'est la technologie qui suggère la stratégie. Le paiement sur compte mobile n'a été pensable pour
l'ANPP que le jour où les opérateurs l'ont offert.

\subsection{Mesurer l'alignement : Luftman}

Jerry Luftman propose en 2000 une mesure de la maturité de l'alignement sur six critères et cinq
niveaux~\cite{luftman2000}~: communication, mesure de la valeur, gouvernance, partenariat, périmètre et
architecture, compétences. Le cours l'emploie sous forme d'exigences cotées, pour rester dans sa convention.

""" + lecture("L'alignement à l'ANPP, 9 février 2027", [
    ("Communication~: la division informatique participe aux réunions de direction", "N", "Feuilles de présence 2026"),
    ("Communication~: les métiers connaissent les projets en cours", "N", "Entretiens, 14 sur 18"),
    ("Valeur~: chaque projet a un bénéfice attendu écrit", "N", "Fiches de projet"),
    ("Valeur~: un bilan est fait après la mise en service", "N", "Aucun bilan"),
    ("Gouvernance~: une instance arbitre les projets", "N", "Aucune instance"),
    ("Gouvernance~: le budget suit les priorités arbitrées", "K", "Clé de répartition non documentée"),
    ("Partenariat~: chaque projet a un responsable métier", "O", "Notes de désignation, 9 sur 11"),
    ("Architecture~: une cartographie applicative est tenue", "N", "Aucune"),
    ("Compétences~: un plan de formation existe", "O", "Plan 2026"),
    ("Compétences~: les postes clés ont un suppléant", "K", "Organigramme incomplet")],
    r"""L'alignement n'est pas établi~: $\mu = 0{,}20$. Six écarts touchent la communication, la valeur, la
gouvernance et l'architecture. Les deux \NEK{} sont de preuve et se lèveront pendant le diagnostic. Le point
d'appui est le partenariat~: les métiers désignent déjà un responsable par projet.""") + r"""

""" + sec("Graduer l'Ambition : Venkatraman", "sec:c03-venkatraman") + r"""
Venkatraman décrit en 1994 cinq niveaux de transformation par les technologies~\cite{venkatraman1994}. Les deux
premiers sont évolutifs~: l'exploitation localisée, puis l'intégration interne. Les trois suivants sont
révolutionnaires~: la refonte des processus, la refonte du réseau d'affaires, la redéfinition du périmètre
d'activité. Les bénéfices croissent avec le niveau, les changements d'organisation aussi.

Un schéma directeur doit dire à quel niveau il se place. Informatiser le guichet d'une antenne relève du niveau
un. Faire payer les prestations par un opérateur de téléphonie relève du niveau quatre et suppose des accords,
des textes et une autre organisation.

""" + sec("La Valeur en Question", "sec:c03-valeur") + r"""
Robert Solow écrit en 1987 que l'on voit des ordinateurs partout sauf dans les statistiques de
productivité~\cite{solow1987}. Brynjolfsson examine ce \termecle{paradoxe de la productivité} en
1993~\cite{brynjolfsson1993} et avance quatre explications~: des erreurs de mesure, des délais d'apprentissage,
une redistribution des gains entre entreprises et une mauvaise gestion des investissements. Ses travaux
ultérieurs montrent que la valeur apparaît quand l'investissement technique s'accompagne d'un changement
d'organisation.

Nicholas Carr soutient en 2003 la thèse adverse~\cite{carr2003}. Les technologies de l'information deviennent
une commodité, comme l'électricité. Ce que tous peuvent acheter ne distingue personne. Il recommande de dépenser
moins, de suivre plutôt que de mener, de gérer les risques plutôt que les opportunités.

\begin{boxinfo}
\textbf{Que retenir de la controverse.} Carr a raison pour l'infrastructure. La théorie des ressources
(Chapitre~\ref{chap:strategie}) dit la même chose. Il a tort pour l'usage~: deux organisations dotées des mêmes
outils n'en tirent pas la même valeur. La valeur vient des données, des processus et des compétences, non du
matériel.
\end{boxinfo}

Ward et Daniel proposent en 2006 la \termecle{gestion des bénéfices}~\cite{warddaniel2006}. Un bénéfice n'est pas
livré par un projet. Il est obtenu par un métier qui change sa manière de travailler. Chaque bénéfice a donc un
propriétaire, une mesure et une date, distincts de ceux du projet.

""" + sec("Gouvernance, Modèle Opérationnel et Fusion des Stratégies", "sec:c03-gouvernance") + r"""
Weill et Ross montrent en 2004 que les organisations les plus performantes ont clarifié qui décide de quoi en
matière de technologies~\cite{weillross2004}. Ils distinguent cinq décisions~: les principes, l'architecture,
l'infrastructure, les besoins applicatifs, l'investissement. Un schéma directeur dit pour chacune qui décide et
qui est consulté.

Ross, Weill et Robertson ajoutent en 2006 le \termecle{modèle opérationnel}~\cite{ross2006}. Une organisation
choisit son degré de standardisation des processus et son degré d'intégration des données. Quatre modèles en
résultent~: diversification, coordination, réplication, unification. L'ANPP, qui applique la même procédure
dans dix antennes sur un même fichier, relève de l'unification. LiZbiZ, dont les sites partagent les clients
mais pas toujours les procédures, relève de la coordination.

Bharadwaj et ses coauteurs proposent en 2013 de ne plus parler d'alignement~\cite{bharadwaj2013}. La stratégie
numérique n'est pas une stratégie fonctionnelle alignée sur la stratégie d'affaire. Elle en est une composante.
Westerman, Bonnet et McAfee croisent en 2014 deux capacités~\cite{westerman2014}~: la capacité numérique (ce que
l'on sait faire avec la technologie) et la capacité de conduite (vision, gouvernance, engagement). Seules les
organisations fortes sur les deux transforment durablement leur activité.
"""
chapitre("partie1/P01_C03_alignement_valeur.tex", 3, "L'Alignement et la Valeur", "chap:alignement", "Alignement et valeur",
 "« Un bénéfice n'est pas livré par un projet.\\\\\n    Il est obtenu par un métier qui change. »", "D'après Ward et Daniel",
 "Fondamental", "Chapitres~\\ref{chap:vocabulaire} et~\\ref{chap:strategie}",
 ["Situer une organisation sur les stades de Nolan.", "Tirer des besoins d'information des facteurs clés de succès.",
  "Classer un portefeuille applicatif dans la grille de McFarlan.", "Décrire le modèle d'alignement stratégique et ses quatre perspectives.",
  "Coter la maturité de l'alignement.", "Discuter le paradoxe de la productivité et la thèse de Carr."],
 "« l'informatique ne suit pas »", r"""
Yaoundé, lundi 8~février~2027. Le directeur des prestations de l'ANPP résume son avis en une phrase~: « L'informatique
ne suit pas. » Il attend depuis deux ans un état quotidien des paiements. Mme~NGO~BIYONG répond qu'elle n'a
jamais reçu cette demande par écrit et qu'elle a appris par hasard la réforme des prestations de 2025.

Chacun a raison. La division informatique n'assiste pas aux réunions de direction. Les métiers ne savent pas quels
projets sont en cours. Personne n'arbitre. Mme~EKANI note que le problème n'est pas technique. Il porte un nom
depuis 1993.

\begin{boxalert}
\textbf{Violation typique.} Traiter un défaut d'alignement par un achat de matériel ou de logiciel.

\smallskip
\textbf{Règle~:} l'alignement est une affaire de décisions et de personnes. Il se construit par une instance
qui arbitre, par des responsables métiers désignés et par une mesure de la valeur obtenue.
\end{boxalert}
""", corps,
 [("Directeur des systèmes d'information", "Tenir la grille des applications à jour et la présenter chaque année. Demander pour chaque projet le nom du métier qui en obtiendra le bénéfice."),
  ("Responsable métier", "Écrire le bénéfice attendu avant le projet et le mesurer après. Sans cela, l'investissement ne se justifie ni ne se défend."),
  ("Dirigeant", "Faire entrer le responsable du système d'information dans les réunions où la stratégie se discute.")],
 ["Nolan~: une organisation ne saute pas de stade de maturité.", "Rockart~: les facteurs clés de succès donnent les besoins d'information.",
  "McFarlan~: quatre familles d'applications, quatre conduites.", "Henderson et Venkatraman~: quatre domaines, deux dimensions, quatre perspectives.",
  "Luftman~: l'alignement se mesure sur six critères.", "La valeur vient de l'usage et du changement d'organisation, non de l'outil.",
  "Weill et Ross~: dire qui décide de quoi. Bharadwaj~: la stratégie numérique est une composante de la stratégie."],
 ["dessiner les quatre domaines du modèle d'alignement", "classer une application dans la grille de McFarlan", "citer deux explications du paradoxe de la productivité", "dire ce qu'est un propriétaire de bénéfice"],
 [("Grille de McFarlan", 1, "Classez~: la paie de l'ANPP, e-RECETTES, un pilote de paiement sur compte mobile dans une antenne, la messagerie, le fichier des bénéficiaires, un site d'information du public."),
  ("Quelle perspective", 2, "Pour chacune des trois organisations du cours, dites quelle perspective du Tableau~3.4 décrit le mieux la situation actuelle et laquelle vous recommandez. Justifiez en trois lignes."),
  ("Lever deux NEK", 2, "Quelles pièces demandez-vous pour lever les deux \\NEK{} de la lecture de l'ANPP~? Recalculez $\\mu$ et $U$ dans le cas le plus favorable et dans le moins favorable."),
  ("Carr à la banque", 3, "Le directeur financier de la BANQUE SANAGA cite Carr pour réduire de 30~\\% le budget informatique. Rédigez une réponse d'une page qui lui donne raison sur un point et tort sur un autre, avec des exemples tirés de la banque.")],
 ["Henderson et Venkatraman~\\cite{henderson1993}.", "Luftman~\\cite{luftman2000}.", "Carr~\\cite{carr2003} et Brynjolfsson~\\cite{brynjolfsson1993}.", "Weill et Ross~\\cite{weillross2004}~; Ross et al.~\\cite{ross2006}."],
 "Les théories donnent des idées. Les normes et les référentiels donnent des critères. Avant de regarder le Cameroun, le Chapitre~\\ref{chap:normes} présente ceux que le monde emploie.")
