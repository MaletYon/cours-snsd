# -*- coding: utf-8 -*-
from ch import *
corps = sec("La Chaîne des Documents d'Orientation", "sec:c06-chaine") + r"""
""" + tab("L{4.0cm}L{2.4cm}L{5.6cm}", ["Document", "Date", "Place du numérique"], [
    ["Cameroun Vision 2035~\\cite{vision2035}", "2009", "Cadre de long terme~: devenir un pays émergent, démocratique et uni dans sa diversité"],
    ["Document de stratégie pour la croissance et l'emploi", "2009, pour 2010-2019", "Première phase de la Vision"],
    ["Plan stratégique Cameroun numérique 2020~\\cite{camnum2020}", "Mai 2016", "Premier document national consacré à l'économie numérique"],
    ["Stratégie nationale de développement, SND30~\\cite{snd30}", "2020, pour 2020-2030", "Deuxième phase de la Vision. Le numérique parmi les sous-secteurs retenus"],
    ["Stratégie nationale d'intelligence artificielle~\\cite{snia2025}", "Juillet 2025", "Sept piliers, dont la gouvernance et la souveraineté"],
    ["Plan stratégique national de santé numérique~\\cite{psnsn2026}", "Mars 2026, pour 2026-2030", "Stratégie d'un secteur, huit axes, 29~milliards de FCFA"]],
    "Les documents d'orientation du Cameroun", "6.1") + r"""

La Vision 2035 a été élaborée par le ministère chargé de l'économie et de la planification. Elle se met en œuvre
par phases de dix ans. La Stratégie nationale de développement 2020-2030, dite SND30, en est la deuxième phase.
Elle vise une transformation structurelle de l'économie et compte le numérique parmi les sous-secteurs sur
lesquels elle s'appuie. Elle demande la modernisation de l'administration et le développement de la
gouvernance électronique.

Tout schéma directeur d'une administration camerounaise se rattache donc à la SND30. C'est le premier maillon de
la démonstration d'alignement~: la mission de l'organisation découle d'un programme, qui découle d'une stratégie
sectorielle, qui découle de la SND30.

""" + sec("Cameroun Numérique 2020, son Bilan et sa Suite", "sec:c06-plan") + r"""
Le Plan stratégique Cameroun numérique 2020 a été publié par le ministère des Postes et Télécommunications en
mai~2016. Sa vision était de faire du Cameroun un pays numérique à l'horizon 2020. Il s'organisait autour du
développement des infrastructures à large bande, de la production de contenus numériques, de la transformation
numérique de l'administration et des entreprises, de la confiance numérique et des compétences.

Son exécution a été partielle. La SND30 relève elle-même que le niveau d'utilisation des technologies reste
faible malgré les investissements. Le plan a pourtant installé un vocabulaire et des acteurs que l'on retrouve
dans tous les documents suivants.

\begin{boxinfo}
\textbf{Le plan 2026-2030.} Le Plan de développement de l'économie numérique au Cameroun 2026-2030, édition
2025~\cite{pden2026}, est finalisé et déposé. À la date de ce cours, il est en cours de validation dans les
services du Premier ministre et n'a pas encore reçu son approbation. Il n'est donc pas en cours de mise en
œuvre. Un schéma directeur rédigé aujourd'hui le mentionne dans ces termes exacts, se rattache à la SND30, qui
est en vigueur, et prévoit de se réviser à l'approbation du plan. La section~\ref{sec:c06-projet} en décrit le
contenu.
\end{boxinfo}

Cette situation est fréquente et il faut savoir la traiter. Un document d'orientation attendu ne se cite pas
comme une source en vigueur. Il ne s'ignore pas non plus. Le schéma directeur écrit ce qui est établi, ce qui est
attendu et ce qui changera.

\subsection{Le projet d'accélération de la transformation numérique}

Le Projet d'accélération de la transformation numérique du Cameroun, le PATNUC, est conduit par le ministère des
Postes et Télécommunications avec l'appui d'un bailleur. Il comprend un volet de connectivité des zones rurales
et un volet d'appui au cadre stratégique, dont est issue la stratégie d'intelligence artificielle. Une
administration qui prépare son schéma directeur vérifie si l'un de ses projets peut s'y inscrire.

""" + sec("La Stratégie d'Intelligence Artificielle", "sec:c06-ia") + r"""
La Stratégie nationale d'intelligence artificielle a été présentée lors de la deuxième édition des Concertations
nationales sur l'intelligence artificielle, à Yaoundé, les 7 et 8~juillet~2025. Elle repose sur sept piliers,
parmi lesquels la gouvernance de l'intelligence artificielle et la souveraineté numérique, les données et
l'infrastructure, et une intelligence artificielle multilingue et inclusive. Elle annonce une loi sur
l'intelligence artificielle et une autorité compétente.

Pour un schéma directeur, deux conséquences. Tout projet d'intelligence artificielle se rattache à cette
stratégie. Tout projet doit prévoir qu'un cadre légal viendra~: on documente dès maintenant les données
employées, les décisions prises et les contrôles humains (Chapitre~\ref{chap:donnees}).

""" + sec("Les Acteurs", "sec:c06-acteurs") + r"""
""" + tab("L{3.6cm}L{8.4cm}", ["Acteur", "Rôle pour un schéma directeur"], [
    ["Ministère des Postes et Télécommunications", "Politique du secteur, plans nationaux, tutelle des agences du numérique"],
    ["ANTIC", "Agence nationale des technologies de l'information et de la communication. Sécurité des systèmes d'information, audits de sécurité, expertise auprès des administrations, interopérabilité"],
    ["ART", "Agence de régulation des télécommunications. Opérateurs, licences, qualité de service"],
    ["CAMTEL et opérateurs", "Infrastructures, connectivité, services de paiement par téléphone"],
    ["Ministère chargé de l'économie et de la planification", "SND30, programmation des investissements publics"],
    ["Ministère des Finances", "Budget, cadre de dépenses à moyen terme, systèmes financiers de l'État"],
    ["Ministère des Marchés publics et ARMP", "Passation et régulation des marchés"],
    ["Autorité de protection des données", "Prévue par la loi n°~2024/017. Autorisations et contrôle des traitements"],
    ["Contrôle supérieur de l'État", "Contrôle des projets et de la gestion publics"]],
    "Les acteurs publics du numérique", "6.2") + r"""

L'ANTIC est régie par le décret n°~2019/150 du 22~mars~2019~\cite{decret2019150}, qui a remplacé le décret
n°~2012/180 du 10~avril~2012~\cite{decret2012180}. Le texte de 2012 la chargeait déjà de favoriser
l'interopérabilité entre les systèmes d'information et de fournir son expertise aux administrations pour la
conception de leurs outils. Elle conduit les audits de sécurité obligatoires prévus par le décret
n°~2012/1643/PM~\cite{decret20121643}.

\begin{boxinfo}
\textbf{Qui impose un schéma directeur~?} Aucun texte général n'impose un schéma directeur à toute
administration. L'obligation figure dans les textes organiques. Celui de la Présidence de la République charge
sa direction de l'informatique d'élaborer et de mettre en œuvre le schéma directeur d'informatisation des
services. Beaucoup de ministères ont une disposition voisine. Le schéma directeur 2020-2024 d'un ministère,
publié en ligne, se réfère aux prescriptions de l'ANTIC pour ses achats~\cite{minepded2020sdi}. Le consultant
cherche donc le texte organique de l'organisation avant d'écrire que le schéma directeur est obligatoire.
\end{boxinfo}

""" + sec("Les Stratégies Sectorielles", "sec:c06-secteurs") + r"""
La santé donne l'exemple le plus abouti. Un premier plan stratégique de santé numérique couvrait 2020-2024. Le
second, pour 2026-2030, a été lancé le 4~mars~2026. Il compte huit axes, dont la gouvernance, le cadre
juridique, les ressources humaines, les infrastructures et l'interopérabilité. Son budget est d'environ
29~milliards de francs CFA. Le ministère y reconnaît un niveau de maturité limité.

Un hôpital public qui rédige son schéma directeur se rattache à ce plan avant de se rattacher à la SND30. La
règle est générale~: le document le plus proche d'abord, puis la chaîne jusqu'à la stratégie nationale.

""" + sec("Le Projet de Plan 2026-2030", "sec:c06-projet") + r"""
Le projet de plan s'ouvre par un état des lieux. Il y constate que le plan Cameroun numérique 2020 a connu un
taux d'exécution très faible et il en donne cinq causes~: un cadre institutionnel et réglementaire inadapté,
des ressources financières insuffisantes, des ressources humaines qualifiées insuffisantes, une faible
coordination des activités transversales et une prise en compte insuffisante des questions de genre. Le
prologue de ce cours a fait le même constat à l'échelle d'une agence. Un plan national et un schéma directeur
d'organisme échouent pour les mêmes raisons.

Le document se compose de quatre parties~: un état des lieux, un diagnostic, un plan d'actions assorti d'un
plan d'actions prioritaires, un dispositif de mise en œuvre et de suivi-évaluation. Il se termine par une
déclaration de politique.

""" + tab("L{3.6cm}L{8.4cm}", ["Élément", "Contenu du projet de plan"], [
    ["Objectif global", "Développer l'économie numérique au Cameroun"],
    ["Cinq piliers", "Infrastructures des communications électroniques, plateformes numériques, services financiers numériques, entrepreneuriat numérique, compétences numériques"],
    ["Quatre axes", "Amélioration de la gouvernance~; renforcement du cadre juridique et institutionnel~; exploitation de l'économie numérique~; utilisation du numérique"],
    ["Mise en œuvre", "À court terme, un comité interministériel de l'économie numérique. À moyen terme, la création d'une agence nationale de l'économie numérique"],
    ["Suivi-évaluation", "Suivi des actions, évaluation de l'impact, tableau de bord"],
    ["Financement", "Un fonds d'investissement pour l'économie numérique, des partenariats public-privé, des alliances internationales et des fonds de garantie, un programme de subventions pour l'inclusion numérique"]],
    "Le projet de Plan de développement de l'économie numérique 2026-2030", "6.3") + r"""

Trois enseignements pour un schéma directeur. Le plan se rattache lui-même au premier pilier de la SND30, la
transformation structurelle de l'économie~: la chaîne de rattachement de ce chapitre est donc la bonne. Il
prévoit de réviser des textes, dont la loi de 2010 sur la cybersécurité~: la carte d'applicabilité du
Chapitre~\ref{chap:droit} devra être relue à son approbation. Il annonce des institutions nouvelles~: la liste
des acteurs du Tableau~6.2 changera.

Tant que l'approbation n'est pas donnée, aucun de ces éléments n'oblige. Le schéma directeur de l'ANPP les
note comme des évolutions attendues et n'en tire aucun projet.

""" + sec("Rattacher un Schéma Directeur", "sec:c06-rattacher") + r"""
\begin{boxprocedure}
\textbf{Établir le rattachement stratégique.}
\begin{enumerate}
    \item Trouver le texte qui crée l'organisation et fixe ses missions.
    \item Trouver le programme budgétaire auquel elle contribue.
    \item Trouver la stratégie de son secteur, si elle existe, avec sa période.
    \item Citer la SND30 et l'objectif concerné.
    \item Noter les documents attendus et non approuvés, avec leur état exact.
    \item Écrire le tout en une page, en tête du schéma directeur.
\end{enumerate}
\end{boxprocedure}

\begin{boxscenario}{Mission ANPP. Le rattachement stratégique, 7 février 2025}
\textbf{Constatations.} Le décret de création de l'Agence fixe trois missions~: liquider les prestations, les
payer, tenir le fichier des bénéficiaires. L'Agence contribue à un programme budgétaire de protection sociale.
Son secteur n'a pas de stratégie numérique propre. Le plan stratégique 2024-2028 de l'Agence, adopté en
décembre~2023, compte quatre objectifs.

\textbf{Analyse} (confiance élevée). Le rattachement se fait à quatre niveaux~: missions, plan stratégique de
l'Agence, programme budgétaire, SND30. Le plan national appelé à succéder à Cameroun numérique 2020 est noté comme attendu. L'absence de
stratégie sectorielle est écrite~: elle explique que l'Agence doive fixer seule ses principes d'interopérabilité.
\end{boxscenario}

""" + lecture("Le rattachement stratégique de l'ANPP", [
    ("Les missions sont tirées d'un texte cité", "O", "Décret de création"),
    ("Un plan stratégique de l'organisation est en vigueur", "O", "Plan 2024-2028"),
    ("Le programme budgétaire est identifié", "O", "Loi de finances"),
    ("La stratégie du secteur est citée", "K", "Aucune stratégie sectorielle"),
    ("Le lien avec la SND30 est écrit", "N", "Absent du plan de l'Agence"),
    ("Les documents attendus sont notés avec leur état", "N", "Aucune mention")],
    r"""Le socle existe~: trois \OUI{} portent sur des textes en vigueur. Le \NEK{} est de critère, puisqu'il
n'y a pas de stratégie sectorielle à citer. Les deux \NON{} se corrigent en une page. C'est le premier livrable
de la mission.""") + r"""
"""
chapitre("partie3/P03_C06_strategie_cameroun.tex", 6, "La Stratégie Numérique du Cameroun", "chap:cameroun", "Stratégie du Cameroun",
 "« Un plan attendu ne se cite pas comme un plan en vigueur.\\\\\n    Il ne s'ignore pas non plus. »", "Principe du cours",
 "Fondamental", "Chapitre~\\ref{chap:doctrines}",
 ["Situer la Vision 2035, la SND30 et le plan Cameroun numérique 2020.", "Dire l'état exact du plan Cameroun numérique 2026-2030.",
  "Présenter la stratégie nationale d'intelligence artificielle et une stratégie sectorielle.", "Nommer les acteurs publics du numérique et leur rôle.",
  "Établir le rattachement stratégique d'un schéma directeur."],
 "« conformément au plan Cameroun numérique »", r"""
Yaoundé, jeudi 15~octobre~2026. La cellule de portefeuille de l'ANPP prépare la révision annuelle du schéma
directeur. Le projet de préambule qu'un agent soumet à Mme~NGO BIYONG commence ainsi~: « Conformément au plan
Cameroun numérique 2026-2030, l'ANPP poursuit sa transformation. » Elle demande où il a lu ce plan. Il en a
entendu parler dans un séminaire.

Elle lui fait chercher le texte d'approbation. Il n'y en a pas. Le plan est finalisé et déposé. Le Premier
ministre ne l'a pas encore approuvé. La phrase est donc fausse~: on ne se conforme pas à un texte
qui n'est pas en vigueur.

\begin{boxalert}
\textbf{Violation typique.} Rattacher un schéma directeur à un document d'orientation que l'on n'a pas lu ou
qui n'est pas approuvé.

\smallskip
\textbf{Règle~:} chaque document cité l'est avec sa date, son auteur et son état~: en vigueur, échu ou
attendu. Le rattachement se fait sur ce qui est en vigueur.
\end{boxalert}
""", corps,
 [("Consultant", "Vérifier l'état de chaque document d'orientation à la date de la mission. Garder la preuve de la vérification."),
  ("Dirigeant d'administration", "Faire inscrire dans le schéma directeur une clause de révision à l'approbation des plans nationaux attendus."),
  ("Directeur des systèmes d'information", "Prendre l'attache de l'ANTIC au début de la démarche, pour la sécurité et l'interopérabilité.")],
 ["La Vision 2035 date de 2009. La SND30 en est la deuxième phase, pour 2020-2030.", "Cameroun numérique 2020 date de mai~2016. Son exécution a été partielle.",
  "Le plan 2026-2030 est finalisé et déposé, sans approbation du Premier ministre à ce jour.", "La stratégie d'intelligence artificielle a été présentée les 7 et 8~juillet~2025.",
  "L'ANTIC est régie par le décret n°~2019/150 du 22~mars~2019.", "Aucun texte général n'impose un schéma directeur. L'obligation vient des textes organiques."],
 ["dire sur quel document en vigueur une administration se rattache", "énoncer l'état du plan 2026-2030", "citer quatre acteurs publics et leur rôle"],
 [("En vigueur, échu, attendu", 1, "Classez~: Vision 2035, Cameroun numérique 2020, SND30, Cameroun numérique 2026-2030, plan de santé numérique 2020-2024, plan de santé numérique 2026-2030, stratégie d'intelligence artificielle de 2025."),
  ("Une page", 2, "Rédigez la page de rattachement stratégique de l'ANPP, selon la démarche en six points."),
  ("Qui saisir", 2, "L'ANPP veut ouvrir un paiement sur compte mobile. Quels acteurs du Tableau~6.2 sont concernés et pour quoi~?"),
  ("Texte organique", 3, "Cherchez le texte organique d'un ministère ou d'un organisme public de votre choix. Dit-il qui élabore le schéma directeur~? Qui l'approuve~? Rédigez votre constat en séparant ce que le texte dit de ce que la pratique ajoute.")],
 ["La SND30~\\cite{snd30}.", "Le plan Cameroun numérique 2020~\\cite{camnum2020}.", "Le plan de santé numérique 2026-2030~\\cite{psnsn2026}.", "Le décret n°~2019/150 sur l'ANTIC~\\cite{decret2019150}."],
 "Les orientations disent où aller. Le droit dit comment une organisation a le droit d'y aller~: acheter, financer, décider, protéger. Le Chapitre~\\ref{chap:droit} dresse le cadre juridique d'un schéma directeur.")
