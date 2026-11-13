# -*- coding: utf-8 -*-
from ch import *
corps = sec("Trois Natures de Référentiel", "sec:c04-natures") + r"""
""" + tab("L{2.8cm}L{3.0cm}L{2.8cm}L{3.4cm}", ["Nature", "Force", "Exemple", "Preuve attendue"], [
    ["Texte obligatoire", "S'impose, sous sanction", "Code des marchés publics", "Conformité à l'article"],
    ["Norme certifiable", "Volontaire, vérifiée par un tiers", "ISO/IEC~27001", "Certificat, périmètre, date"],
    ["Cadre volontaire", "Volontaire, déclaré", "COBIT 2019, TOGAF", "Usage déclaré et documenté"],
    ["Norme de recommandation", "Volontaire, non certifiable", "ISO/IEC~38500, ISO~31000", "Usage déclaré"]],
    "Quatre natures de référentiel", "4.1") + r"""

Une norme ou un cadre ne devient contraignant que de trois manières~: un texte y renvoie, un contrat l'exige ou
l'organisation s'y engage par une décision de son organe délibérant. Hors de ces cas, c'est une référence que
l'on emprunte et que l'on déclare.

""" + sec("Gouverner : ISO/IEC 38500 et ISO 37000", "sec:c04-38500") + r"""
L'ISO/IEC~38500 traite de la gouvernance des technologies de l'information~\cite{iso38500}. Sa troisième édition
date de février~2024 et s'aligne sur l'ISO~37000 de 2021, qui traite de la gouvernance des
organismes~\cite{iso37000}. Elle s'adresse à l'organe de gouvernance, c'est-à-dire au conseil, et non à la
direction informatique.

Son modèle tient en trois tâches que le conseil exerce sur l'usage des technologies~: \textbf{évaluer} l'usage
actuel et futur, \textbf{diriger} la préparation des stratégies et des politiques, \textbf{surveiller} la
conformité et la performance. Elle énonce des principes de bonne gouvernance, parmi lesquels la responsabilité,
la stratégie, l'acquisition, la performance, la conformité et le comportement humain.

\begin{boxinfo}
\textbf{Portée pour le schéma directeur.} La norme place le schéma directeur du bon côté de la table. Le conseil
ne rédige pas le document. Il le demande, l'approuve et en surveille l'exécution. Le bilan de l'ANPP au prologue
montre un conseil qui a approuvé sans surveiller~: deux tâches sur trois manquaient.
\end{boxinfo}

""" + sec("Gouverner et Gérer : COBIT 2019", "sec:c04-cobit") + r"""
COBIT~2019 est le cadre de l'ISACA~\cite{cobit2019}. Il compte quarante objectifs, répartis en un domaine de
gouvernance et quatre domaines de gestion. Le cours de gouvernance (UE MSN-2S3-MSI03) l'a présenté. Six
objectifs concernent directement le schéma directeur.

""" + tab("L{1.6cm}L{4.2cm}L{6.2cm}", ["Objectif", "Intitulé résumé", "Usage pour le schéma directeur"], [
    ["EDM01", "Cadre de gouvernance", "Qui décide du schéma directeur"],
    ["EDM02", "Livraison des bénéfices", "Suivi de la valeur des investissements"],
    ["APO02", "Stratégie gérée", "Diagnostic, cible, feuille de route"],
    ["APO03", "Architecture d'entreprise gérée", "Cible d'architecture et plan de migration"],
    ["APO05", "Portefeuille géré", "Sélection et arbitrage des projets"],
    ["APO06", "Budget et coûts gérés", "Chiffrage et suivi financier"]],
    "Six objectifs de COBIT 2019 pour le schéma directeur", "4.2") + r"""

COBIT propose aussi une \termecle{cascade des objectifs}~: des besoins des parties prenantes aux objectifs de
l'entreprise, puis aux objectifs d'alignement, puis aux objectifs de gouvernance et de gestion. C'est un outil
commode pour démontrer l'alignement pièce par pièce.

""" + sec("Dessiner la Cible : TOGAF, ISO 42010, ArchiMate", "sec:c04-togaf") + r"""
TOGAF est la norme d'architecture d'entreprise de l'Open Group, dont la dixième édition date de
2022~\cite{togaf10}. Sa méthode de développement de l'architecture parcourt des phases~: vision, architecture
métier, architecture des systèmes d'information (données et applications), architecture technique, opportunités
et solutions, planification de la migration, gouvernance de la mise en œuvre, gestion du changement. Le cours
d'architecture (UE MSN-2S3-MSI02) la détaille.

Pour le schéma directeur, trois phases comptent. La vision donne les principes. Les phases d'architecture donnent
l'existant et la cible. La planification de la migration donne les \textit{architectures de transition}, qui
sont les étapes de la trajectoire.

L'ISO/IEC/IEEE~42010 fixe la manière de décrire une architecture~\cite{iso42010}~: des parties prenantes ont
des préoccupations, auxquelles répondent des points de vue. ArchiMate est le langage de modélisation de l'Open
Group, organisé en couches métier, application et technologie.

""" + sec("Servir : ITIL 4 et ISO/IEC 20000", "sec:c04-itil") + r"""
ITIL~4 décrit un \termecle{système de valeur des services}~\cite{itil4}. La demande y entre, la valeur en sort.
Le système réunit des principes directeurs, une gouvernance, une chaîne de valeur des services, des pratiques et
une amélioration continue. ITIL~4 comporte un module consacré à la stratégie numérique et informatique.

Pour le schéma directeur, ITIL apporte une idée que les documents oublient~: un projet livré devient un service à
exploiter. Le coût de fonctionnement, les compétences d'exploitation et les niveaux de service doivent figurer à
la trajectoire. L'ISO/IEC~20000-1 est la norme certifiable de gestion des services.

""" + sec("Arbitrer : les Normes de Portefeuille", "sec:c04-portefeuille") + r"""
L'ISO~21502 traite du management de projet~\cite{iso21502}. L'ISO~21504 traite du management de
portefeuille~\cite{iso21504}. La distinction est celle du cours~: le projet fait bien les choses, le portefeuille
choisit les bonnes choses à faire.

""" + tab("L{2.6cm}L{4.4cm}L{5.0cm}", ["Niveau", "Question", "Référentiels"], [
    ["Portefeuille", "Quels projets, dans quel ordre, avec quels moyens~?", "ISO~21504, MoP, COBIT APO05"],
    ["Programme", "Comment obtenir un bénéfice par plusieurs projets liés~?", "MSP, ISO~21503"],
    ["Projet", "Comment livrer dans les délais, le coût et la qualité~?", "ISO~21502, PMBOK, PRINCE2"]],
    "Portefeuille, programme, projet", "4.3") + r"""

""" + sec("Maîtriser : Risque, Sécurité, Continuité, Intelligence Artificielle", "sec:c04-maitrise") + r"""
""" + tab("L{3.8cm}L{4.0cm}L{4.2cm}", ["Norme", "Objet", "Place dans le schéma directeur"], [
    ["ISO~31000:2018~\\cite{iso31000}", "Gestion du risque, lignes directrices", "Risques du schéma directeur lui-même"],
    ["ISO/IEC~27001:2022~\\cite{iso27001}", "Sécurité de l'information, certifiable", "Volet sécurité de la cible"],
    ["ISO~22301:2019~\\cite{iso22301}", "Continuité d'activité, certifiable", "Secours et reprise"],
    ["ISO/IEC~42001:2023~\\cite{iso42001}", "Système de management de l'IA, certifiable", "Projets d'intelligence artificielle"],
    ["ISO~56002:2019~\\cite{iso56002}", "Management de l'innovation", "Expérimentations"],
    ["EN~16234-1:2019~\\cite{ecf}", "Référentiel européen des compétences numériques", "Volet compétences"]],
    "Normes de maîtrise utiles au schéma directeur", "4.4") + r"""

""" + sec("Choisir ses Référentiels", "sec:c04-choisir") + r"""
\begin{boxprocedure}
\textbf{Déclarer les référentiels d'un schéma directeur.}
\begin{enumerate}
    \item Recenser les textes obligatoires qui s'appliquent à l'organisation (Chapitre~\ref{chap:droit}).
    \item Recenser les référentiels exigés par un contrat, un bailleur ou un superviseur.
    \item Choisir, pour chaque besoin restant, un seul référentiel volontaire.
    \item Écrire dans le document la liste retenue, l'édition de chaque référentiel et son usage.
    \item Ne jamais écrire « conforme à » pour un cadre volontaire. Écrire « établi selon ».
\end{enumerate}
\end{boxprocedure}

\begin{boxscenario}{Mission ANPP. Les référentiels retenus, 28 janvier 2025}
\textbf{Constatations.} Le cahier des charges du conseil cite « les bonnes pratiques » sans les nommer. Le
bailleur qui finance une partie des projets demande un suivi de portefeuille. La division informatique compte
deux agents certifiés ITIL et aucun architecte.

\textbf{Analyse} (confiance élevée). L'équipe retient l'ISO/IEC~38500 pour le rôle du conseil, COBIT~2019 pour
les six objectifs du Tableau~4.2, l'ISO~21504 pour le portefeuille et l'ISO~31000 pour les risques. TOGAF n'est
pas retenu comme méthode complète, faute d'architecte~: la cible sera décrite par des cartographies simples.
Ce choix est écrit dans la note de cadrage.
\end{boxscenario}

""" + lecture("Les référentiels à l'ANPP avant la mission", [
    ("Les référentiels employés sont nommés avec leur édition", "N", "Schéma directeur 2019"),
    ("Le conseil exerce les trois tâches de l'ISO/IEC~38500", "N", "Approuve sans surveiller"),
    ("Un processus de portefeuille existe", "N", "Aucune procédure"),
    ("Un registre des risques informatiques est tenu", "O", "Registre de 2024"),
    ("La gestion des services suit un cadre déclaré", "K", "Pratiques ITIL non documentées"),
    ("Une certification est détenue sur un périmètre", "N", "Aucune")],
    r"""Un seul \OUI{}. Le registre des risques existe depuis la panne de mars~2024. Le \NEK{} est de preuve~:
deux agents appliquent ITIL sans procédure écrite. L'Agence n'a pas besoin de certificat à ce stade. Elle a
besoin de nommer ce qu'elle emploie.""") + r"""
"""
chapitre("partie2/P02_C04_normes_referentiels.tex", 4, "Normes et Référentiels", "chap:normes", "Normes et référentiels",
 "« Le conseil ne rédige pas le schéma directeur.\\\\\n    Il le demande, l'approuve et le surveille. »", "D'après l'ISO/IEC 38500",
 "Fondamental", "Chapitre~\\ref{chap:alignement}~; COBIT et ITIL (UE MSN-2S3-MSI03)~; architecture d'entreprise (UE MSN-2S3-MSI02)",
 ["Distinguer texte obligatoire, norme certifiable et cadre volontaire.", "Décrire les trois tâches de l'ISO/IEC~38500.",
  "Citer les objectifs de COBIT~2019 qui portent le schéma directeur.", "Situer TOGAF, ITIL~4 et l'ISO~21504.",
  "Déclarer les référentiels d'un schéma directeur."],
 "« conforme à COBIT »", r"""
Douala, mercredi 21~octobre~2026. Le schéma directeur que la BANQUE SANAGA\footnote{La BANQUE SANAGA est fictive.
Sa panne de 2026 et l'Opération WOURI qui a suivi figurent dans d'autres cours de l'auteur.} avait remis à son
superviseur en 2024 portait en couverture la mention « conforme à COBIT, ITIL et TOGAF ». Mme~NKENG, responsable
du contrôle de second niveau, a cherché sur quoi reposait cette phrase. Elle n'a trouvé ni liste des objectifs
retenus, ni édition des référentiels, ni évaluation.

Le superviseur a posé la même question après la panne. La banque n'a rien pu produire. Mme~NKENG résume~: « Nous
avons écrit trois noms sur une couverture. »

\begin{boxalert}
\textbf{Violation typique.} Écrire « conforme à » devant le nom d'un cadre volontaire.

\smallskip
\textbf{Règle~:} on est conforme à un texte ou certifié selon une norme, sur un périmètre et à une date. Un
cadre volontaire s'emploie et se déclare~: lesquels de ses éléments, dans quelle édition, pour quel usage.
\end{boxalert}
""", corps,
 [("Administrateur", "Demander chaque année trois choses sur les technologies~: ce qui a été évalué, ce qui a été décidé, ce qui a été constaté."),
  ("Directeur des systèmes d'information", "Tenir la liste des référentiels employés, avec leur édition. Retirer de tout document les mentions qui ne reposent sur aucune pièce."),
  ("Consultant", "Choisir peu de référentiels et les employer vraiment. Quatre référentiels déclarés et suivis valent mieux que dix cités.")],
 ["Un cadre volontaire se déclare, une norme se certifie, un texte oblige.", "ISO/IEC~38500:2024~: le conseil évalue, dirige et surveille.",
  "COBIT~2019~: EDM01, EDM02, APO02, APO03, APO05 et APO06 portent le schéma directeur.", "TOGAF donne la cible et les architectures de transition.",
  "ITIL~4 rappelle qu'un projet livré devient un service à exploiter.", "L'ISO~21504 traite le portefeuille, l'ISO~21502 le projet."],
 ["nommer les trois tâches de l'ISO/IEC~38500", "dire quand un cadre volontaire devient contraignant", "distinguer portefeuille, programme et projet"],
 [("Quelle nature", 1, "Classez dans le Tableau~4.1~: COBIT~2019, ISO/IEC~27001, le code des marchés publics, ISO~31000, TOGAF, ISO~22301, un règlement du superviseur bancaire, ITIL~4."),
  ("Trois tâches", 2, "Reprenez le bilan du prologue. Pour chacune des trois tâches de l'ISO/IEC~38500, dites ce que le conseil de l'ANPP a fait et ce qu'il aurait dû faire."),
  ("La couverture", 2, "Réécrivez la mention de couverture du schéma directeur de la BANQUE SANAGA pour qu'elle soit exacte. Dites quelles pièces doivent l'accompagner."),
  ("Cascade", 3, "Appliquez la cascade des objectifs de COBIT à l'objectif « payer chaque bénéficiaire à date fixe ». Donnez un objectif d'alignement et deux objectifs de gestion. Indiquez la pièce qui prouverait chacun.")],
 ["L'ISO/IEC~38500~\\cite{iso38500} et l'ISO~37000~\\cite{iso37000}.", "COBIT~2019~\\cite{cobit2019}, objectifs APO02 et APO05.", "La norme TOGAF~\\cite{togaf10}.", "L'ISO~21504~\\cite{iso21504}."],
 "Les normes viennent d'organismes techniques. Les États et les organisations internationales ont aussi leurs doctrines et leurs stratégies numériques. Le Chapitre~\\ref{chap:doctrines} les présente, de l'OCDE à l'Union africaine.")
