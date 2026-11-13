# -*- coding: utf-8 -*-
from ch import *
corps = sec("Quatre Forces qui Bousculent la Méthode", "sec:c15-forces") + r"""
La méthode des chapitres précédents a été conçue pour des applications et des projets. Quatre forces
l'obligent à s'élargir. Les données deviennent un actif à part. L'intelligence artificielle change ce qu'un
système peut faire et ce qu'il peut rater. Les plateformes déplacent la frontière de l'organisation. La
sobriété impose de compter autre chose que des francs.

Aucune ne rend la méthode caduque. Chacune ajoute un chapitre au schéma directeur.

""" + sec("Les Données", "sec:c15-donnees") + r"""
Le Cadre stratégique de l'Union africaine en matière de données, adopté en février~2022, demande aux États de
traiter les données comme une ressource à gouverner et à faire circuler~\cite{ua2022donnees}. Pour une
organisation, gouverner ses données revient à répondre à cinq questions pour chaque donnée importante.

""" + tab("L{3.2cm}L{4.4cm}L{4.4cm}", ["Question", "Réponse attendue", "À l'ANPP, pour le bénéficiaire"], [
    ["À qui appartient-elle~?", "Un propriétaire dans le métier", "Directeur des prestations"],
    ["Où est sa référence~?", "Un seul système maître", "Référentiel des bénéficiaires"],
    ["Que vaut-elle~?", "Une mesure de qualité", "Taux de doublons, taux d'identifiants vérifiés"],
    ["Qui y accède~?", "Des règles d'habilitation", "Par antenne, par fonction"],
    ["Combien de temps~?", "Une durée et un sort final", "Durée fixée par le registre des traitements"]],
    "Cinq questions de gouvernance pour une donnée", "15.1") + r"""

Le diagnostic a trouvé onze fichiers de bénéficiaires à l'ANPP. Le rapprochement d'un échantillon de
5~000~dossiers a donné 7,4~\% de doublons probables. Sur 186~000~bénéficiaires, cela représente près de
13~800~dossiers à examiner. Le projet de référentiel commence donc par un chantier de fiabilisation, qui n'est
pas un chantier informatique.

\begin{boxdef}
\textbf{Donnée de référence.} Donnée partagée par plusieurs processus et qui décrit un objet stable de
l'activité~: une personne, un employeur, un barème. Elle a un propriétaire, un système maître et une règle de
mise à jour.
\end{boxdef}

Le schéma directeur comporte désormais un volet données~: la liste des données de référence, leurs
propriétaires, les indicateurs de qualité, la cellule qui les suit. La loi n°~2024/017 y ajoute ses propres
exigences pour les données personnelles~\cite{loi2024017}.

""" + sec("L'Intelligence Artificielle", "sec:c15-ia") + r"""
La Stratégie continentale de l'Union africaine sur l'intelligence artificielle date de
juillet~2024~\cite{ua2024ia}. Le Cameroun a présenté sa stratégie nationale en juillet~2025~\cite{snia2025}. La
norme ISO/IEC~42001 décrit un système de management de l'intelligence artificielle~\cite{iso42001}.

Pour le schéma directeur, l'intelligence artificielle n'est pas un projet. C'est une famille de techniques qui
peut servir un objectif. La question reste celle du Chapitre~\ref{chap:cible}~: quelle capacité~? Un cas
d'usage se juge sur cinq conditions avant d'entrer au portefeuille.

""" + tab("L{3.0cm}L{9.0cm}", ["Condition", "Question"], [
    ["Objectif", "Quel objectif du plan stratégique ce cas sert-il, avec quelle mesure~?"],
    ["Données", "Les données existent-elles, en quantité et en qualité suffisantes, et a-t-on le droit de les employer~?"],
    ["Décision", "Qui décide à la fin~: la machine ou un agent~? Qui répond d'une erreur~?"],
    ["Preuve", "Peut-on expliquer un résultat à la personne concernée~?"],
    ["Exploitation", "Qui surveillera la dérive du modèle, avec quel budget~?"]],
    "Cinq conditions pour un cas d'usage d'intelligence artificielle", "15.2") + r"""

\begin{boxscenario}{ANPP. Le cas des paiements indus, révision de 2026}
La direction financière propose un modèle qui signale les dossiers à risque de paiement indu~: bénéficiaire
décédé, double immatriculation, droit éteint. Le comité de portefeuille applique les cinq conditions.

L'objectif est clair~: ne payer que les ayants droit. Les données ne sont pas prêtes~: le référentiel ne sera
fiabilisé qu'à la fin de 2026. La décision est fixée~: le modèle signale, un agent instruit, aucune suspension
automatique. La preuve est exigée~: chaque signalement indique ses motifs. L'exploitation est confiée à la
cellule des données.

Le projet entre au portefeuille pour 2027, après le référentiel. Il coûte 95~millions. Il décale un projet de
soutien, selon la règle du Chapitre~\ref{chap:piloter}.
\end{boxscenario}

\begin{boxalert}
\textbf{Violation typique.} Inscrire au schéma directeur « un projet d'intelligence artificielle » sans dire
pour quoi faire.

\smallskip
\textbf{Règle~:} un cas d'usage se nomme par la décision qu'il aide à prendre. Il n'entre au portefeuille
qu'après le projet qui lui fournit des données fiables.
\end{boxalert}

Les assistants conversationnels du commerce posent une autre question. Les agents les emploient déjà, sans
attendre le schéma directeur. C'est une forme nouvelle d'informatique hors contrôle. Une règle d'usage, courte,
dit quelles données ne doivent jamais y être saisies. À l'ANPP, aucune donnée de bénéficiaire.

""" + sec("Les Plateformes", "sec:c15-plateformes") + r"""
Le Chapitre~\ref{chap:strategie} a présenté les marchés bifaces~\cite{rochettirole2003} et la logique de
plateforme~\cite{parker2016}. Une plateforme crée de la valeur en mettant en relation des tiers. Elle oblige le
schéma directeur à regarder hors des murs.

Pour LiZbiZ, la question est offensive. L'entreprise possède dix ans de données de tournées et un réseau de
quarante correspondants ruraux. Elle peut rester un transporteur, ou ouvrir son réseau à d'autres expéditeurs
et à d'autres livreurs. Dans le second cas, son système d'information cesse d'être un outil interne. Il devient
le produit.

Pour une administration, la question est celle de l'\termecle{interopérabilité}. L'ANPP a besoin de l'état
civil pour connaître les décès, des employeurs pour les carrières, des opérateurs de paiement pour verser. Les
textes qui régissent l'ANTIC lui confient de favoriser l'interopérabilité entre les systèmes
d'information~\cite{decret2012180,decret2019150}. Le schéma directeur liste donc les échanges attendus, leurs partenaires et leur
état.

""" + tab("L{3.2cm}L{3.2cm}L{2.6cm}L{3.0cm}", ["Échange", "Partenaire", "État en 2025", "Dépend de l'ANPP~?"], [
    ["Décès", "État civil", "Courrier mensuel", "Non"],
    ["Carrières", "Employeurs", "Bordereaux papier", "En partie"],
    ["Paiements", "Banques, opérateurs de paiement", "Fichiers déposés", "Oui"],
    ["Identité", "Fichier national d'identité", "Aucun", "Non"]],
    "Les échanges de l'ANPP avec l'extérieur", "15.3") + r"""

Deux échanges sur quatre ne dépendent pas de l'Agence. Le schéma directeur les inscrit comme des hypothèses,
avec une solution d'attente. Un projet dont le succès dépend d'un tiers qui ne s'est engagé à rien est un
risque à porter au registre.

""" + sec("Le Nuage et la Maîtrise", "sec:c15-nuage") + r"""
Louer des capacités chez un prestataire réduit l'investissement et accélère les projets. La dépendance grandit
en proportion. Trois questions reviennent dans tout schéma directeur.

\begin{enumerate}
    \item \textbf{Où sont les données~?} La loi n°~2024/017 encadre les transferts hors du Cameroun.
    \item \textbf{Qui peut y accéder~?} Le droit du pays du prestataire s'applique aussi.
    \item \textbf{Comment en sortir~?} La réversibilité, vue au Chapitre~\ref{chap:financer}.
\end{enumerate}

Le schéma directeur fixe une doctrine par classe de données. L'ANPP en retient trois~: les données de
bénéficiaires restent sur des sites situés au Cameroun, les données de gestion peuvent être hébergées dans la
sous-région, les données publiques n'ont pas de contrainte. La doctrine est un principe directeur. Elle a des
conséquences de coût, que le plan de financement porte.

""" + sec("La Sobriété", "sec:c15-sobriete") + r"""
Un système d'information consomme de l'énergie, des matériels et de l'attention. Le principe « retirer avant
d'ajouter », adopté au Chapitre~\ref{chap:cible}, en est la traduction. Trois leviers relèvent du schéma
directeur.

\begin{enumerate}
    \item \textbf{La durée de vie.} Allonger d'un an l'usage des postes de travail réduit les achats. L'ANPP
          passe de quatre à six ans.
    \item \textbf{Le retrait.} Une application retirée libère des serveurs, des licences, de l'énergie.
    \item \textbf{L'énergie.} Dans un pays où le réseau électrique connaît des coupures, la salle des serveurs
          tourne une partie du temps sur groupe électrogène. La mesure de sa consommation est un indicateur
          financier autant qu'écologique.
\end{enumerate}

Avec 380~postes de travail à 450~000~FCFA, le renouvellement tous les quatre ans coûte 42,75~millions par an.
Tous les six ans, il coûte 28,5~millions. L'économie annuelle est de 14,25~millions.

""" + sec("Ce qui Change dans le Document", "sec:c15-document") + r"""
""" + tab("L{3.0cm}L{9.0cm}", ["Force", "Ajout au schéma directeur"], [
    ["Données", "Liste des données de référence, propriétaires, indicateurs de qualité, cellule des données"],
    ["Intelligence artificielle", "Grille des cinq conditions, règle d'usage des assistants, registre des cas d'usage"],
    ["Plateformes", "Tableau des échanges avec l'extérieur, hypothèses et solutions d'attente"],
    ["Nuage", "Doctrine d'hébergement par classe de données"],
    ["Sobriété", "Durées de vie, plan de retrait, indicateur de consommation"]],
    "Cinq ajouts au schéma directeur", "15.4") + r"""

""" + lecture("Les défis nouveaux dans le schéma directeur de l'ANPP, révision de 2026", [
    ("Les données de référence sont listées avec leur propriétaire", "O", "Quatre données, quatre propriétaires"),
    ("Un indicateur de qualité est mesuré pour chacune", "N", "Mesure pour les bénéficiaires seuls"),
    ("Chaque cas d'usage d'IA passe la grille des cinq conditions", "O", "Fiche des paiements indus"),
    ("Une règle d'usage des assistants est diffusée", "O", "Note du 3 mars 2026"),
    ("Les échanges avec l'extérieur sont listés avec leur état", "O", "Tableau 15.3"),
    ("Chaque échange dépendant d'un tiers a une solution d'attente", "N", "Rien pour le fichier d'identité"),
    ("Une doctrine d'hébergement par classe de données existe", "O", "Principe directeur n° 7"),
    ("La consommation de la salle des serveurs est mesurée", "K", "Compteur posé, aucun relevé transmis")],
    r"""Cinq \OUI{} sur huit. L'Agence a pris les sujets dans le bon ordre~: les données avant l'intelligence
artificielle. Les deux \NON{} sont des travaux à finir. Le \NEK{} est de preuve.""") + r"""
"""
chapitre("partie6/P06_C15_donnees_ia.tex", 15, "Données, Intelligence Artificielle, Plateformes, Sobriété", "chap:donnees", "Défis",
 "« Une donnée sans propriétaire\\\\\n    n'est tenue par personne. »", "Principe du cours",
 "Avancé", "Chapitres~\\ref{chap:strategie}, \\ref{chap:doctrines} et \\ref{chap:cible}",
 ["Répondre aux cinq questions de gouvernance d'une donnée.", "Juger un cas d'usage d'intelligence artificielle sur cinq conditions.", "Lister les échanges d'une organisation avec l'extérieur et leurs dépendances.",
  "Formuler une doctrine d'hébergement par classe de données.", "Chiffrer un levier de sobriété.", "Dire ce que ces forces ajoutent au schéma directeur."],
 "« mettons de l'intelligence artificielle »", r"""
Yaoundé, mars~2026. Un administrateur revient d'un colloque. Au conseil, il demande pourquoi le schéma directeur
voté neuf mois plus tôt « ne contient pas d'intelligence artificielle ». Il veut un projet avant la fin de
l'année. M.~OWONA transmet à la cellule de portefeuille.

La cellule ne répond ni oui ni non. Elle demande quelle décision de l'Agence on veut améliorer. La direction
financière a une réponse~: repérer les paiements indus. La cellule demande alors sur quelles données. La réponse
est moins assurée. Le fichier compte encore 7,4~\% de doublons probables.

\begin{boxalert}
\textbf{Violation typique.} Ajouter une technique au schéma directeur parce qu'elle est à la mode.

\smallskip
\textbf{Règle~:} une technique entre au portefeuille par un cas d'usage, instruit comme toute demande
nouvelle.
\end{boxalert}
""", corps,
 [("Responsable des données", "Tenir la liste des données de référence. Mesurer leur qualité. Refuser un modèle sur des données non fiabilisées."),
  ("Directeur de métier", "Rester propriétaire de ses données et des décisions prises avec l'aide d'un modèle."),
  ("Délégué à la protection des données", "Viser chaque cas d'usage et la doctrine d'hébergement."),
  ("Consultant", "Ramener toute demande de technique à une capacité et à une mesure.")],
 ["Quatre forces élargissent la méthode~: données, intelligence artificielle, plateformes, sobriété.", "Une donnée de référence a un propriétaire, un système maître, une mesure de qualité.",
  "Un cas d'usage d'intelligence artificielle se juge sur cinq conditions~: objectif, données, décision, preuve, exploitation.", "Les données viennent avant les modèles.",
  "Le schéma directeur liste les échanges avec l'extérieur et les traite comme des hypothèses quand ils dépendent d'un tiers.", "La doctrine d'hébergement se fixe par classe de données.",
  "Retirer avant d'ajouter."],
 ["appliquer les cinq questions à une donnée", "instruire un cas d'usage d'intelligence artificielle", "dresser le tableau des échanges d'une organisation", "chiffrer l'effet d'un allongement de durée de vie"],
 [("Les doublons", 1, "Vérifiez le calcul des dossiers à examiner à l'ANPP. Si un agent en examine 25 par jour, combien de jours de travail faut-il~? Combien d'agents pour finir en six mois de 22~jours ouvrés~?"),
  ("Cinq conditions", 2, "La BANQUE SANAGA veut un modèle qui note les demandes de crédit des particuliers. Appliquez les cinq conditions. Dites laquelle vous paraît la plus difficile à remplir."),
  ("La sobriété", 2, "Refaites le calcul du renouvellement des postes pour 520~postes à 480~000~FCFA, en passant de trois à cinq ans. Citez un coût que cet allongement fait apparaître."),
  ("LiZbiZ plateforme", 3, "Rédigez la note de deux pages au conseil de LiZbiZ sur l'ouverture de son réseau à d'autres expéditeurs. Appuyez-vous sur la théorie des marchés bifaces~: qui sont les deux faces, laquelle subventionner, quel rôle pour les données de tournées, quels risques."),
  ("Question de recherche", 3, "Formulez une question de recherche sur la qualité des données de référence dans les administrations d'Afrique centrale. Proposez une méthode de mesure et dites quelles données il faudrait collecter.")],
 ["Le Cadre de l'Union africaine sur les données~\\cite{ua2022donnees}.", "La Stratégie continentale sur l'intelligence artificielle~\\cite{ua2024ia}.", "ISO/IEC~42001~\\cite{iso42001}.", "Parker, Van Alstyne et Choudary~\\cite{parker2016}."],
 "Le schéma directeur est écrit, exécuté, élargi. Reste une question~: comment savoir s'il est bon~? Le Chapitre~\\ref{chap:audit} y répond.")
