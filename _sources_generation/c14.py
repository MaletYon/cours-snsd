# -*- coding: utf-8 -*-
from ch import *
corps = sec("Deux Sortes de Risques", "sec:c14-deux") + r"""
Le schéma directeur rencontre le risque deux fois. Il y a les risques \emph{du} schéma directeur~: ce qui peut
empêcher de l'exécuter. Il y a les risques que le schéma directeur \emph{traite}~: ceux qui pèsent sur le
système d'information et que les projets doivent réduire. Les premiers se gèrent dans le pilotage. Les seconds
commandent une partie du portefeuille.

La norme ISO~31000 définit le risque comme l'effet de l'incertitude sur les objectifs et décrit un processus en
cinq temps~: établir le contexte, identifier, analyser, évaluer, traiter~\cite{iso31000}. S'y ajoutent deux
activités continues, communiquer et surveiller.

""" + sec("Le Registre des Risques du Schéma Directeur", "sec:c14-registre") + r"""
Chaque risque s'écrit en trois parties~: une cause, un événement, une conséquence sur un objectif. Il reçoit
une probabilité et un impact notés de 1 à 5. Leur produit donne la criticité. Un propriétaire en répond.

""" + tab("L{0.7cm}L{4.6cm}cccL{3.2cm}", ["N°", "Risque", "P", "I", "C", "Traitement"], [
    ["R1", "Subvention non inscrite en loi de finances", "4", "4", "16", "Scénario de repli"],
    ["R2", "Reprise des onze fichiers de bénéficiaires défaillante", "4", "4", "16", "Fiabilisation avant reprise"],
    ["R3", "Départ des deux agents de la liquidation", "3", "5", "15", "Documentation, binômes"],
    ["R4", "Marché du site de secours infructueux", "3", "4", "12", "Consultation préalable du marché"],
    ["R5", "Postes du plan de dotation non autorisés", "3", "4", "12", "Saisine de la tutelle, assistance externe"],
    ["R6", "Refus du fichier unique par les antennes", "3", "3", "9", "Antennes pilotes, accompagnement"]],
    "Le registre des risques du schéma directeur de l'ANPP (extrait)", "14.1") + r"""

Le seuil d'attention de l'ANPP est fixé à 12. Cinq risques l'atteignent. Chacun a un traitement, un
propriétaire et une date de revue. Quatre traitements sont possibles~: éviter, réduire, transférer, accepter.
Accepter est une décision. Elle se signe.

\begin{boxalert}
\textbf{Violation typique.} Un registre des risques rempli une fois, annexé au document, jamais rouvert.

\smallskip
\textbf{Règle~:} le registre est relu à chaque comité de portefeuille. Un risque dont la note n'a pas bougé en
un an n'a pas été regardé.
\end{boxalert}

""" + sec("La Sécurité", "sec:c14-securite") + r"""
La norme ISO/IEC~27001 demande un système de management de la sécurité de l'information~: une politique, une
appréciation des risques, des mesures, des contrôles, une amélioration~\cite{iso27001}. La loi n°~2010/012
impose de protéger les systèmes et de les faire auditer~\cite{loi2010012,decret20121643}. La lettre circulaire
de la COBAC demande aux banques une politique fondée sur les normes internationales~\cite{cobac2022lc}.

Le schéma directeur ne remplace pas la politique de sécurité. Il lui donne quatre choses.

\begin{enumerate}
    \item \textbf{Une organisation.} Un responsable de la sécurité qui ne dépend pas de celui qu'il contrôle.
          À l'ANPP, il est rattaché au directeur général.
    \item \textbf{Un budget.} Une ligne propre, distincte des projets. L'ANPP y consacre 6~\% de sa dépense
          informatique annuelle à partir de 2026.
    \item \textbf{Une règle de projet.} Chaque fiche comporte une analyse de risque de sécurité et son coût.
    \item \textbf{Un calendrier.} L'audit obligatoire, les tests d'intrusion, les revues d'habilitations sont
          programmés sur cinq ans.
\end{enumerate}

""" + sec("La Continuité", "sec:c14-continuite") + r"""
La norme ISO~22301 traite de la continuité d'activité~\cite{iso22301}. Sa démarche part du métier. Un
\termecle{bilan d'impact sur l'activité} demande à chaque direction combien de temps elle peut travailler sans
son système et combien de données elle peut accepter de perdre.

\begin{boxdef}
\textbf{Durée maximale d'interruption admissible.} Délai au-delà duquel l'arrêt d'une activité cause un
dommage inacceptable. Elle fixe le temps laissé pour redémarrer.

\smallskip
\textbf{Perte de données maximale admissible.} Ancienneté maximale des données que l'on accepte de retrouver
après un sinistre. Elle fixe la fréquence des sauvegardes ou de la réplication.
\end{boxdef}

""" + tab("L{3.4cm}L{2.6cm}L{2.6cm}L{3.4cm}", ["Activité de l'ANPP", "Interruption admissible", "Perte admissible", "Constat de mars 2024"], [
    ["Paiement des prestations", "4 heures", "1 heure", "4 jours, 11 jours de données"],
    ["Encaissement (e-PRESTATIONS)", "8 heures", "1 heure", "Aucun secours"],
    ["Liquidation des droits", "2 jours", "1 jour", "4 jours"],
    ["Comptabilité", "5 jours", "1 jour", "4 jours"]],
    "Le bilan d'impact sur l'activité de l'ANPP", "14.2") + r"""

L'écart entre les besoins et le constat dimensionne le projet de secours. Une interruption admissible de quatre
heures impose un second site prêt à prendre le relais et une réplication des données. Elle exclut une simple
sauvegarde sur bande. Voilà pourquoi le site de secours coûte 620~millions.

Un plan de continuité qui n'a pas été essayé n'existe pas. Le schéma directeur programme un exercice par an et
en fait un indicateur du tableau de bord. Pour une banque, le règlement COBAC~R-2008/01 fait du plan de
continuité une obligation~\cite{cobac200801}.

""" + sec("La Conformité", "sec:c14-conformite") + r"""
La carte d'applicabilité du Chapitre~\ref{chap:droit} devient un \termecle{registre de conformité}. Chaque
exigence y reçoit un responsable, un état et une pièce.

""" + tab("L{3.6cm}L{3.2cm}L{2.2cm}L{3.0cm}", ["Exigence", "Source", "État en 2025", "Projet qui la traite"], [
    ["Audit de sécurité", "Loi n°~2010/012", "Non réalisé depuis 2020", "Obligatoire n°~2"],
    ["Formalités préalables des traitements", "Loi n°~2024/017", "Non engagées", "Obligatoire n°~3"],
    ["Engagements et paiements", "Loi n°~2018/012", "Conforme", "Plan de financement"],
    ["Programmation des marchés", "Décret n°~2018/366", "Conforme pour 2025", "Plan d'achat"],
    ["Approbation par le conseil", "Loi n°~2017/010", "Conforme", "Délibération du 26~juin"]],
    "Le registre de conformité du schéma directeur (extrait)", "14.3") + r"""

La conformité se construit dans les projets. Le registre impose que la fiche de tout projet touchant des
données personnelles porte une tâche d'analyse et de formalité, avec son délai. La même logique vaut pour la
sécurité et la continuité. On parle de prise en compte \termecle{dès la conception}.

""" + sec("Les Projets Eux-Mêmes", "sec:c14-projets") + r"""
Les projets informatiques échouent d'une manière connue~: ils dépassent leur budget, glissent ou livrent moins
que prévu. Quatre parades relèvent du schéma directeur et non du chef de projet.

\begin{enumerate}
    \item \textbf{La taille.} Aucun lot ne dépasse deux ans ni 800~millions à l'ANPP. Le lot~2 de la refonte,
          à 780~millions, est à la limite.
    \item \textbf{Le jalon d'arrêt.} Chaque projet a un point où le comité décide de poursuivre ou non.
    \item \textbf{La coexistence.} L'ancien système reste en service jusqu'à la recette du nouveau. Son coût
          pendant la période est chiffré.
    \item \textbf{Le regard extérieur.} Les trois projets les plus lourds font l'objet d'une revue
          indépendante chaque année.
\end{enumerate}

\begin{boxprocedure}
\textbf{Intégrer la maîtrise des risques au schéma directeur.}
\begin{enumerate}
    \item Dresser le registre des risques du schéma directeur. Désigner les propriétaires.
    \item Faire le bilan d'impact sur l'activité avec les directions.
    \item En déduire les projets obligatoires de sécurité et de continuité.
    \item Tirer le registre de conformité de la carte d'applicabilité.
    \item Ajouter à la fiche de projet les rubriques sécurité, continuité, données personnelles.
    \item Programmer les audits, les exercices et les revues sur toute la période.
\end{enumerate}
\end{boxprocedure}

""" + lecture("La maîtrise des risques dans le schéma directeur 2025-2029 de l'ANPP", [
    ("Un registre des risques existe avec des propriétaires", "O", "Registre du 13 juin 2025"),
    ("Chaque risque au-dessus du seuil a un traitement", "O", "Cinq traitements"),
    ("Un bilan d'impact sur l'activité a été conduit", "O", "Tableau 14.2"),
    ("Le secours est dimensionné sur ce bilan", "O", "Fiche du projet de secours"),
    ("Un exercice de continuité annuel est programmé", "O", "Calendrier 2026-2029"),
    ("Le responsable de la sécurité est indépendant de l'informatique", "O", "Cible d'organisation"),
    ("La sécurité a une ligne budgétaire propre", "O", "6~\\% à partir de 2026"),
    ("Chaque fiche de projet porte les rubriques de risque", "N", "Rubriques absentes de huit fiches"),
    ("Le registre de conformité est tenu", "O", "Tableau 14.3"),
    ("Le registre des risques a été relu depuis l'approbation", "K", "Aucun procès-verbal fourni")],
    r"""Huit \OUI{} sur dix. Le document de 2025 fait ce que celui de 2019 ignorait. Le \NON{} est facile à
lever. Le \NEK{} est de preuve et il est le plus instructif~: un registre bien fait à la date d'approbation ne
prouve rien sur sa vie ensuite. La cote dépendra des procès-verbaux du comité de portefeuille.""") + r"""
"""
chapitre("partie5/P05_C14_maitriser.tex", 14, "Risques, Sécurité, Continuité, Conformité", "chap:maitriser", "Maîtriser",
 "« Tout ce qui est susceptible d'aller mal\\\\\n    finira par aller mal. »", "Loi dite de Murphy",
 "Intermédiaire", "Chapitres~\\ref{chap:droit} et \\ref{chap:piloter}",
 ["Distinguer les risques du schéma directeur des risques qu'il traite.", "Écrire un risque en trois parties et le coter.", "Dire ce que le schéma directeur apporte à la sécurité.",
  "Conduire un bilan d'impact sur l'activité.", "Tirer un registre de conformité d'une carte d'applicabilité.", "Citer quatre parades à l'échec des projets."],
 "« quatre jours »", r"""
Yaoundé, mars~2024. Un onduleur de la salle des serveurs cède un mardi à 14~heures. Les serveurs s'arrêtent sans
précaution. Au redémarrage, la base des paiements est corrompue. La dernière sauvegarde utilisable date de onze
jours. Il faut la restaurer, puis ressaisir onze jours d'opérations à partir des bordereaux des antennes.

Les paiements du mois partent avec quatre jours de retard. Pour 186~000~bénéficiaires, quatre jours sont longs.
Le ministre de tutelle convoque le directeur général. Le schéma directeur 2019-2023 prévoyait bien un « plan de
secours ». C'était le projet n°~17. Il n'avait jamais démarré, faute de budget. Personne n'avait écrit ce que
coûterait son absence.

\begin{boxalert}
\textbf{Violation typique.} Mettre la continuité et la sécurité en concurrence avec les autres projets lors de
l'arbitrage.

\smallskip
\textbf{Règle~:} les projets qui répondent à un risque que l'organisation ne peut pas porter sont
obligatoires. Ils se financent avant les autres.
\end{boxalert}
""", corps,
 [("Responsable de la sécurité", "Tenir la politique, programmer les audits, viser les fiches de projet."),
  ("Responsable de la continuité", "Conduire le bilan d'impact avec les métiers. Organiser l'exercice annuel et en rendre compte."),
  ("Directeur de métier", "Dire combien de temps il peut tenir sans son système. Signer sa réponse."),
  ("Auditeur", "Demander le dernier exercice de continuité et les procès-verbaux de relecture du registre.")],
 ["Deux sortes de risques~: ceux du schéma directeur, ceux qu'il traite.", "Un risque s'écrit~: cause, événement, conséquence. Il a un propriétaire.",
  "Quatre traitements~: éviter, réduire, transférer, accepter.", "Le schéma directeur donne à la sécurité une organisation, un budget, une règle de projet, un calendrier.",
  "Le bilan d'impact fixe l'interruption et la perte de données admissibles.", "Un plan de continuité non essayé n'existe pas.",
  "La carte d'applicabilité devient un registre de conformité."],
 ["écrire et coter six risques", "conduire un bilan d'impact pour une activité", "dresser un registre de conformité", "ajouter les rubriques de risque à une fiche de projet"],
 [("Coter", 1, "Écrivez en trois parties puis cotez le risque suivant pour LiZbiZ~: son client principal, qui pèse 38~\\% du chiffre d'affaires, exige un suivi des colis en temps réel que le système actuel ne fournit pas."),
  ("Le bilan d'impact", 2, "Pour l'activité « paiement des prestations », expliquez pourquoi une interruption admissible de quatre heures et une perte admissible d'une heure excluent la sauvegarde quotidienne. Quelles solutions restent~?"),
  ("Accepter", 2, "Le comité de l'ANPP veut accepter le risque~R6. Rédigez la décision d'acceptation~: motif, limite, signataire, date de revue."),
  ("La banque", 3, "Dressez le registre de conformité du schéma directeur de la BANQUE SANAGA pour la sécurité et la continuité, à partir des textes du Chapitre~\\ref{chap:droit}. Cinq lignes au moins, avec la pièce attendue par le superviseur.")],
 ["ISO~31000~\\cite{iso31000}.", "ISO/IEC~27001~\\cite{iso27001} et ISO~22301~\\cite{iso22301}.", "Le règlement COBAC~R-2008/01~\\cite{cobac200801}."],
 "La méthode est complète, de la commande à l'exécution. La dernière partie regarde ce qui la bouscule aujourd'hui, puis la manière de la contrôler. Le Chapitre~\\ref{chap:donnees} commence par les données.")
