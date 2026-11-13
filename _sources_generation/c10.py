# -*- coding: utf-8 -*-
from ch import *
corps = sec("De la Stratégie à la Cible", "sec:c10-chaine") + r"""
La cible décrit le système d'information voulu à la fin de la période. Elle se déduit, elle ne s'invente pas.
La chaîne compte quatre maillons~: les objectifs de l'organisation, les capacités qu'ils demandent, les
principes qui guideront les choix, l'architecture qui en résulte.

""" + tab("L{4.6cm}L{7.4cm}", ["Objectif du plan stratégique 2024-2028", "Capacité demandée au système d'information"], [
    ["Payer chaque prestation à date fixe", "Liquider et payer sans interruption, y compris en cas de sinistre"],
    ["Ne payer que les ayants droit", "Tenir un fichier unique des bénéficiaires, rapproché de l'état civil"],
    ["Rapprocher l'Agence des bénéficiaires", "Recevoir et suivre une demande depuis une antenne ou un téléphone"],
    ["Rendre compte de chaque franc", "Produire la dépense par programme et par antenne"]],
    "Des quatre objectifs de l'ANPP aux capacités", "10.1") + r"""

Une capacité se formule par un verbe et un résultat. Elle ne nomme ni un logiciel ni une technique. « Disposer
d'un progiciel intégré » n'est pas une capacité. « Produire la dépense par programme » en est une.

""" + sec("Les Principes Directeurs", "sec:c10-principes") + r"""
Un \termecle{principe directeur} est une règle durable qui tranche d'avance une famille de décisions. Le cadre
TOGAF demande de l'écrire en quatre parties~: un nom, un énoncé, une justification, des
conséquences~\cite{togaf10}. Les conséquences font la valeur du principe. Un principe qui ne gêne personne ne
décide rien.

""" + tab("L{3.2cm}L{4.4cm}L{4.4cm}", ["Nom", "Énoncé", "Conséquence acceptée"], [
    ["Donnée unique", "Un bénéficiaire est enregistré une seule fois", "Les antennes renoncent à leurs fichiers locaux"],
    ["Acheter avant de construire", "Un besoin commun se couvre par un produit du marché", "Le métier adapte ses usages au produit"],
    ["Secours d'abord", "Aucune application clé sans reprise éprouvée", "Un projet sans budget de secours n'est pas lancé"],
    ["Propriétaire désigné", "Chaque application a un responsable côté métier", "Un directeur signe pour chaque application"],
    ["Ouverture", "Les échanges emploient des formats publics", "Certains produits sont écartés"],
    ["Sobriété", "On retire avant d'ajouter", "Tout projet nomme ce qu'il remplace"]],
    "Les six principes directeurs de l'ANPP", "10.2") + r"""

Six à dix principes suffisent. Le comité de pilotage les approuve un par un, avec leurs conséquences. À l'ANPP,
le principe de la donnée unique a demandé une heure de débat. Les chefs d'antenne tenaient à leurs fichiers.

""" + sec("Les Quatre Plans de l'Architecture", "sec:c10-plans") + r"""
La norme ISO/IEC/IEEE~42010 décrit une architecture par des vues adaptées aux préoccupations de chaque
partie~\cite{iso42010}. La pratique française de l'urbanisation en retient quatre~\cite{longepe2001}. TOGAF en
retient quatre aussi, en regroupant données et applications~\cite{togaf10}.

""" + tab("L{2.6cm}L{4.4cm}L{5.0cm}", ["Plan", "Contenu", "Qui le lit"], [
    ["Métier", "Processus, acteurs, événements", "Les directions de métier"],
    ["Fonctionnel", "Blocs de fonctions, indépendants des logiciels", "L'équipe projet"],
    ["Applicatif", "Logiciels, données, échanges", "La fonction informatique"],
    ["Technique", "Serveurs, réseaux, sites, hébergement", "L'exploitation"]],
    "Les quatre plans", "10.3") + r"""

Le plan fonctionnel est le plus utile au schéma directeur. Il découpe le système en \termecle{zones}, en
quartiers et en blocs, à la manière d'un plan de ville. Chaque fonction appartient à un seul bloc. Chaque
donnée a un seul bloc maître.

\begin{boxscenario}{Mission ANPP. Le plan fonctionnel cible, 11 avril 2025}
Le plan cible de l'ANPP compte cinq zones.
\begin{enumerate}
    \item \textbf{Référentiels.} Bénéficiaires, employeurs, barèmes. Zone maîtresse des données communes.
    \item \textbf{Production.} Immatriculation, liquidation, paiement, recouvrement.
    \item \textbf{Relation.} Guichet, téléphone, demandes en ligne, réclamations.
    \item \textbf{Soutien.} Comptabilité, budget, ressources humaines, achats.
    \item \textbf{Pilotage.} Tableaux de bord, statistiques, contrôle.
\end{enumerate}
Les 47 applications du diagnostic se placent sur ce plan. Sept blocs sont couverts par deux applications ou
plus. Quatre blocs ne sont couverts par aucune, dont le référentiel des bénéficiaires.
\end{boxscenario}

Un bloc couvert deux fois signale une redondance à réduire. Un bloc vide signale un besoin. Le rapprochement
du plan fonctionnel et de l'inventaire donne la liste brute des chantiers.

""" + sec("L'Analyse des Écarts", "sec:c10-ecarts") + r"""
Pour chaque capacité, l'analyse des écarts compare l'existant à la cible et qualifie la distance.

""" + tab("L{4.0cm}L{3.6cm}L{2.2cm}L{2.2cm}", ["Capacité", "Existant", "Écart", "Chantier"], [
    ["Liquider et payer sans interruption", "Site unique, application de 2004", "Fort", "Refonte, secours"],
    ["Fichier unique des bénéficiaires", "Onze fichiers", "Fort", "Référentiel"],
    ["Recevoir une demande à distance", "Guichet seul", "Moyen", "Guichet unique"],
    ["Dépense par programme", "Comptabilité générale seule", "Moyen", "Comptabilité analytique"]],
    "L'analyse des écarts de l'ANPP", "10.4") + r"""

""" + sec("Comparer des Scénarios", "sec:c10-scenarios") + r"""
Une seule cible ne se discute pas, elle s'accepte ou se refuse. Le cabinet en présente donc deux ou trois, qui
atteignent les mêmes capacités par des voies différentes. Chaque scénario est décrit de la même manière~: ce
qu'il fait, ce qu'il coûte en ordre de grandeur, ce qu'il demande à l'organisation, ce qu'il risque.

""" + tab("L{2.8cm}L{3.0cm}L{3.0cm}L{3.2cm}", ["", "A. Consolider", "B. Refondre par étapes", "C. Remplacer d'un bloc"], [
    ["Principe", "Sécuriser l'existant, différer la refonte", "Secours puis refonte de la production en trois lots", "Progiciel intégré unique"],
    ["Ordre de grandeur", "1,9 milliard", "4,2 milliards", "7,5 milliards"],
    ["Capacités atteintes en 2029", "1 sur 4", "4 sur 4", "4 sur 4"],
    ["Effort interne", "Faible", "Soutenu", "Très fort"],
    ["Risque principal", "L'application de 2004 cède", "Coexistence de l'ancien et du nouveau", "Échec d'un projet unique"]],
    "Les trois scénarios présentés au comité de pilotage", "10.5") + r"""

Le choix se fait sur une grille de critères pondérés, fixée avant de noter. Le comité de pilotage de l'ANPP a
retenu quatre critères.

""" + tab("L{4.4cm}cccc", ["Critère", "Poids", "A", "B", "C"], [
    ["Contribution aux quatre objectifs", "40~\\%", "2", "4", "5"],
    ["Soutenabilité financière", "25~\\%", "5", "3", "1"],
    ["Capacité de l'Agence à conduire", "20~\\%", "5", "3", "1"],
    ["Maîtrise du risque", "15~\\%", "2", "4", "2"],
    ["Note pondérée", "", "3,35", "3,55", "2,75"]],
    "La notation des scénarios (notes de 1 à 5)", "10.6") + r"""

Le calcul pour le scénario~B~: $0{,}40 \times 4 + 0{,}25 \times 3 + 0{,}20 \times 3 + 0{,}15 \times 4 = 3{,}55$.
L'écart entre A et B est mince. Le comité a retenu B le 25~avril après avoir constaté que A laissait trois
objectifs du plan stratégique sans réponse. La grille éclaire. Elle ne décide pas à la place du comité.

\begin{boxalert}
\textbf{Violation typique.} Présenter trois scénarios dont deux sont faits pour être écartés.

\smallskip
\textbf{Règle~:} chaque scénario doit pouvoir être choisi par un dirigeant raisonnable. Sinon le cabinet a
décidé seul et le comité n'a fait qu'entériner.
\end{boxalert}

""" + sec("Décrire la Cible Retenue", "sec:c10-decrire") + r"""
Le dossier de cible tient en quinze pages. Il contient les capacités, les principes, le plan fonctionnel, le
scénario retenu avec ses motifs et la liste des chantiers. Il ne contient pas de calendrier ni de budget
détaillé. Ils viennent aux deux phases suivantes.

La cible porte aussi sur l'organisation. Celle de l'ANPP prévoit trois changements~: un responsable de la
sécurité rattaché au directeur général, une cellule des données de trois agents, un propriétaire désigné pour
chaque application.

""" + lecture("Le dossier de cible de l'ANPP, 25 avril 2025", [
    ("Chaque capacité se rattache à un objectif du plan stratégique", "O", "Tableau 10.1"),
    ("Les principes sont approuvés avec leurs conséquences", "O", "Procès-verbal du 11 avril"),
    ("Le plan fonctionnel situe toutes les applications", "O", "47 applications placées"),
    ("Chaque donnée commune a un bloc maître", "O", "Zone des référentiels"),
    ("Deux scénarios au moins étaient éligibles", "O", "A et B, écart de 0,20"),
    ("Les critères et les poids ont été fixés avant la notation", "O", "Procès-verbal du 11 avril"),
    ("L'ordre de grandeur de chaque scénario est justifié", "N", "Scénario C estimé par analogie seule"),
    ("La cible d'organisation est décrite", "O", "Section 5 du dossier"),
    ("Aucun produit n'est nommé", "O", "Relecture du dossier")],
    r"""Huit \OUI{} sur neuf. Le \NON{} porte sur le scénario écarté. Il affaiblit peu la décision, puisque C
était aussi dernier sur la capacité à conduire. Le dossier respecte la règle du Chapitre~\ref{chap:droit}~:
aucune marque n'y figure.""") + r"""
"""
chapitre("partie4/P04_C10_cible.tex", 10, "Fixer la Cible", "chap:cible", "Fixer la cible",
 "« Il n'est pas de vent favorable\\\\\n    pour celui qui ne sait où il va. »", "Sénèque, \\textit{Lettres à Lucilius}, lettre 71",
 "Intermédiaire", "Chapitres~\\ref{chap:normes} et \\ref{chap:diagnostic}",
 ["Déduire des capacités à partir d'objectifs stratégiques.", "Rédiger un principe directeur avec ses conséquences.",
  "Décrire une architecture sur quatre plans.", "Rapprocher un plan fonctionnel d'un inventaire.",
  "Conduire une analyse des écarts.", "Comparer des scénarios sur une grille pondérée."],
 "« il nous faut un progiciel intégré »", r"""
Yaoundé, lundi 24~mars~2025. Premier jour de la phase de cible. M.~ABDOULAYE arrive avec une plaquette. Un
éditeur lui a présenté un progiciel qui couvre « toute la gestion d'un organisme de protection sociale ». Il
propose d'en faire la cible. « Le diagnostic a montré que tout est à refaire. Refaisons tout d'un coup. »

M.~BEYALA ne dit pas non. Il demande quelle capacité du plan stratégique ce produit apporte, ce qu'il coûte sur
cinq ans et qui, à l'Agence, saurait conduire un projet de cette taille. Le produit devient le scénario~C. Il
sera noté comme les autres.

\begin{boxalert}
\textbf{Violation typique.} Partir d'une solution et chercher ensuite les besoins qu'elle couvre.

\smallskip
\textbf{Règle~:} la cible part des objectifs de l'organisation. Une solution proposée en cours de route
devient un scénario parmi d'autres.
\end{boxalert}
""", corps,
 [("Architecte d'entreprise", "Tenir le plan fonctionnel. Refuser qu'une fonction appartienne à deux blocs."),
  ("Directeur de métier", "Formuler des capacités, non des logiciels. Accepter par écrit les conséquences des principes."),
  ("Consultant", "Présenter des scénarios tous éligibles. Faire fixer les critères avant de noter.")],
 ["La cible se déduit~: objectifs, capacités, principes, architecture.", "Une capacité se formule par un verbe et un résultat.",
  "Un principe directeur vaut par ses conséquences.", "Quatre plans~: métier, fonctionnel, applicatif, technique.",
  "Le rapprochement du plan fonctionnel et de l'inventaire révèle redondances et manques.", "Deux ou trois scénarios éligibles, notés sur une grille fixée d'avance.",
  "Le dossier de cible ne nomme aucun produit."],
 ["traduire un objectif en capacités", "écrire un principe en quatre parties", "placer des applications sur un plan fonctionnel", "calculer la note pondérée d'un scénario"],
 [("Capacité ou solution", 1, "Dites si chaque formule est une capacité ou une solution, puis reformulez les solutions~: « avoir un entrepôt de données », « connaître chaque jour les paiements en attente », « passer au nuage », « payer sur compte mobile », « identifier un bénéficiaire en moins d'une minute »."),
  ("Recalculer", 2, "Recalculez les notes pondérées du Tableau~10.6 avec les poids 30~\\%, 30~\\%, 20~\\%, 20~\\%. Le classement change-t-il~? Qu'en concluez-vous sur la solidité de la décision~?"),
  ("Un principe", 2, "Rédigez en quatre parties un principe directeur sur l'hébergement des données de l'ANPP, en tenant compte de la loi n°~2024/017. Écrivez deux conséquences qui gêneront quelqu'un."),
  ("La cible de LiZbiZ", 3, "LiZbiZ veut répondre à la jeune pousse qui lui a pris 9~\\% des livraisons urbaines. Déduisez trois capacités de cette situation, proposez deux scénarios éligibles et les critères pour les départager. Justifiez les poids.")],
 ["TOGAF, phases A à D~\\cite{togaf10}.", "Longépé sur l'urbanisation~\\cite{longepe2001}.", "Ross, Weill et Robertson sur le modèle opérationnel~\\cite{ross2006}."],
 "La cible est choisie. Elle ne dit pas encore par quels projets l'atteindre ni dans quel ordre. C'est l'objet du Chapitre~\\ref{chap:portefeuille}.")
