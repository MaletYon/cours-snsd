# -*- coding: utf-8 -*-
from ch import *
corps = sec("Trois Moments, Trois Questions", "sec:c16-moments") + r"""
Un schéma directeur s'audite à trois moments. Chacun pose une question différente et s'appuie sur des pièces
différentes.

""" + tab("L{2.6cm}L{4.4cm}L{5.0cm}", ["Moment", "Question", "Pièces"], [
    ["Avant l'approbation", "Le document est-il exécutable~?", "Document, note de cadrage, diagnostic, fiches, plan de financement"],
    ["Pendant l'exécution", "Est-il exécuté et piloté~?", "Procès-verbaux, tableau de bord, registres, marchés"],
    ["À l'échéance", "A-t-il produit ce qu'il promettait~?", "Mesures de départ et d'arrivée des bénéfices, comptes"]],
    "Les trois audits d'un schéma directeur", "16.1") + r"""

Le prologue a pratiqué le troisième sur le document de 2021. Les chapitres de méthode ont pratiqué le premier
sur chaque livrable de 2027. Ce chapitre donne la méthode complète.

""" + sec("L'Objet, le Critère, la Preuve", "sec:c16-objet") + r"""
L'Auditologie, que l'auteur développe dans un autre ouvrage~\cite{minka2026auditologie}, pose qu'un audit
compare un objet à un critère au moyen d'une preuve et qu'il rend compte de ce qu'il n'a pas pu établir. Trois
exigences en découlent.

\begin{enumerate}
    \item \textbf{L'objet est délimité.} On audite un document daté, une période, un périmètre.
    \item \textbf{Le critère préexiste.} Il vient d'un texte, d'une norme, d'un engagement de l'organisation
          ou d'une règle de l'art reconnue. L'auditeur ne l'invente pas en cours de route.
    \item \textbf{La preuve est une pièce.} Un document, un enregistrement, une observation consignée. Une
          déclaration orale n'est une preuve que de ce qui a été déclaré.
\end{enumerate}

Chaque exigence reçoit l'une de trois cotes. \OUI{}~: la preuve montre que l'exigence est satisfaite.
\NON{}~: la preuve montre qu'elle ne l'est pas. \NEK{}~: l'auditeur ne peut pas conclure. Le \NEK{} est de
preuve quand la pièce manque. Il est de critère quand l'exigence ne s'applique pas ou ne peut pas être
formulée pour cet objet.

\begin{boxalert}
\textbf{Violation typique.} Coter \NON{} faute de pièce, ou \OUI{} sur la foi d'une déclaration.

\smallskip
\textbf{Règle~:} l'absence de preuve n'est pas la preuve de l'absence. Sans pièce, la cote est \NEK{}.
\end{boxalert}

""" + sec("Le Référentiel d'Exigences", "sec:c16-referentiel") + r"""
Le référentiel d'audit d'un schéma directeur rassemble des exigences de cinq sources. L'Annexe~D donne celui de
la mission ANPP. Il compte 48~exigences réparties en huit domaines, un par chapitre de méthode.

""" + tab("L{3.4cm}L{5.4cm}c", ["Source", "Exemple d'exigence", "Exigences"], [
    ["Textes", "Le document est approuvé par l'organe compétent", "9"],
    ["Normes de gouvernance", "L'organe de gouvernance surveille l'exécution", "8"],
    ["Engagements de l'organisation", "Chaque projet sert un objectif du plan stratégique", "7"],
    ["Règles de l'art", "Chaque projet affiche son coût annuel après mise en service", "19"],
    ["Cohérence interne", "Le total des fiches égale le total du plan de financement", "5"]],
    "Les cinq sources du référentiel de l'ANPP", "16.2") + r"""

Une exigence bien écrite est vérifiable par une pièce. « Le schéma directeur est aligné sur la stratégie » ne
se vérifie pas. « Chaque projet retenu cite un objectif du plan stratégique » se vérifie fiche par fiche.

""" + sec("Trois Mesures", "sec:c16-mesures") + r"""
Les cotes se résument par trois nombres. Soit $n$ le nombre d'exigences, $n_O$, $n_N$ et $n_K$ les effectifs
des trois cotes.

\begin{equation}
    \mu = \frac{n_O}{n} \qquad\qquad U = \frac{n_K}{n} \qquad\qquad
    H = -\sum_{c \in \{O,N,K\}} \frac{n_c}{n} \log_2 \frac{n_c}{n}
\end{equation}

$\mu$ est la part des exigences dont la satisfaction est prouvée. $U$ est la part de ce que l'auditeur ignore.
$H$ est l'entropie de Shannon de la répartition~\cite{shannon1948}. Elle vaut 0 quand toutes les cotes sont
identiques et atteint son maximum, $\log_2 3 \approx 1{,}58$, quand les trois cotes sont à égalité. Un terme
dont l'effectif est nul ne compte pas.

Les trois nombres se lisent ensemble. Un $\mu$ de 0,60 avec un $U$ de 0,05 décrit un objet connu et
moyennement conforme. Le même $\mu$ avec un $U$ de 0,35 décrit un objet mal connu~: il peut être très bon ou
médiocre. La conclusion n'est pas la même. Dans le second cas, la première recommandation est d'obtenir les
pièces.

\begin{boxscenario}{Audit du schéma directeur 2027-2031 de l'ANPP avant approbation, 18 juin 2027}
Le directeur général demande à l'auditeur interne de l'Agence un avis avant le conseil du 24~juin. L'auditeur
applique les 48~exigences de l'Annexe~D. Il obtient 37~\OUI{}, 7~\NON{} et 4~\NEK{}.

\[ \mu = \frac{37}{48} = 0{,}771 \qquad U = \frac{4}{48} = 0{,}083 \]
\[ H = -(0{,}771 \log_2 0{,}771 + 0{,}146 \log_2 0{,}146 + 0{,}083 \log_2 0{,}083) = 0{,}99 \]

Le document est connu à 92~\%. Plus des trois quarts des exigences sont prouvées. Les sept \NON{} se
concentrent dans deux domaines~: le chiffrage, avec trois exigences, et la maîtrise des risques dans les
fiches, avec deux. Les quatre \NEK{} sont tous de preuve.
\end{boxscenario}

""" + sec("Lire par Domaine", "sec:c16-domaines") + r"""
Une moyenne cache les écarts. La lecture se fait donc aussi par domaine.

""" + tab("L{4.0cm}ccccc", ["Domaine", "Exigences", "\\OUI{}", "\\NON{}", "\\NEK{}", "$\\mu$"], [
    ["Cadrage", "6", "5", "0", "1", "0,83"],
    ["Diagnostic", "6", "5", "1", "0", "0,83"],
    ["Cible", "6", "6", "0", "0", "1,00"],
    ["Portefeuille", "6", "5", "1", "0", "0,83"],
    ["Chiffrage et financement", "7", "3", "3", "1", "0,43"],
    ["Pilotage", "6", "5", "0", "1", "0,83"],
    ["Maîtrise des risques", "6", "4", "2", "0", "0,67"],
    ["Cadre juridique", "5", "4", "0", "1", "0,80"],
    ["Ensemble", "48", "37", "7", "4", "0,77"]],
    "Les résultats de l'audit par domaine", "16.3") + r"""

Le chiffrage est le point faible. C'est aussi là que le document de 2021 avait failli. L'avis de l'auditeur
tient en trois phrases~: le document peut être soumis au conseil, sous réserve que le total des fiches et celui du plan
de financement soient mis en accord et que le conseil soit informé de la hausse du fonctionnement. Les quatre pièces manquantes
doivent être produites avant la première revue.

""" + sec("Mesurer l'Alignement", "sec:c16-alignement") + r"""
Le Chapitre~\ref{chap:alignement} a présenté le modèle de Henderson et Venkatraman~\cite{henderson1993} et la
mesure de Luftman~\cite{luftman2000}. Luftman note six critères sur cinq niveaux, du processus initial au
processus optimisé. Sa mesure repose sur l'opinion de dirigeants interrogés. Elle capte une perception.

L'audit par exigences capte autre chose~: des faits prouvés. Les deux se complètent. On peut dériver du
référentiel un \termecle{indice d'alignement prouvé} en ne gardant que les exigences qui relient le système
d'information à la stratégie.

""" + tab("L{8.4cm}cL{2.6cm}", ["Exigence d'alignement", "Cote", "Preuve"], [
    ["Chaque capacité se rattache à un objectif du plan stratégique", "\\OUI{}", "Dossier de cible"],
    ["Chaque projet retenu cite un objectif", "\\OUI{}", "22 fiches"],
    ["Chaque objectif est servi par un projet au moins", "\\OUI{}", "Table de correspondance"],
    ["Chaque projet a un responsable dans le métier", "\\OUI{}", "22 fiches"],
    ["Le comité qui arbitre est présidé par la direction générale", "\\OUI{}", "Note de cadrage"],
    ["Chaque bénéfice a un propriétaire et une mesure de départ", "\\NON{}", "Deux bénéfices sans mesure"],
    ["Le tableau de bord contient un indicateur de résultat métier", "\\OUI{}", "Tableau de bord"],
    ["La révision annuelle précède la préparation du budget", "\\NEK{}", "Calendrier non arrêté"]],
    "L'indice d'alignement prouvé de l'ANPP, juin 2027", "16.4") + r"""

Six \OUI{} sur huit~: l'indice vaut 0,75. Appliquée au document de 2021, la même grille donnait un \OUI{} sur
huit, soit 0,125. La mesure ne dit pas que le système d'information de l'ANPP est aligné. Elle dit que le
dispositif qui doit produire l'alignement existe et qu'il est prouvé.

""" + sec("Le Rapport", "sec:c16-rapport") + r"""
Le rapport d'audit d'un schéma directeur tient en dix pages. Il suit un ordre constant.

\begin{enumerate}
    \item L'objet, le périmètre, la date, le référentiel employé.
    \item Les trois mesures, pour l'ensemble et par domaine.
    \item Les \NON{}, chacun avec le fait, la pièce, la conséquence et une recommandation.
    \item Les \NEK{}, chacun avec la pièce attendue et la personne qui doit la produire.
    \item L'avis.
    \item En annexe, la table complète des cotes.
\end{enumerate}

Les \NEK{} sont publiés. C'est la marque de la méthode. Un rapport qui les tait laisse croire que l'auditeur a
tout vu.

\begin{boxprocedure}
\textbf{Auditer un schéma directeur.}
\begin{enumerate}
    \item Délimiter l'objet et le moment.
    \item Arrêter le référentiel avec le commanditaire avant de voir les pièces.
    \item Demander les pièces par écrit. Tenir un registre de ce qui est reçu.
    \item Coter chaque exigence. Écrire la référence de la pièce.
    \item Calculer $\mu$, $U$ et $H$, pour l'ensemble et par domaine.
    \item Faire valider les faits par l'audité. Les cotes ne se négocient pas.
    \item Rédiger le rapport. Publier les \NEK{}.
\end{enumerate}
\end{boxprocedure}

""" + sec("Pistes de Recherche", "sec:c16-recherche") + r"""
Le cours ouvre plus de questions qu'il n'en ferme. Quatre d'entre elles peuvent nourrir un mémoire.

\begin{enumerate}
    \item \textbf{Le devenir des schémas directeurs.} Combien de documents adoptés par des organismes publics
          de la sous-région sont exécutés à plus de moitié~? Aucune mesure publiée n'existe. La grille du
          prologue permet de la produire.
    \item \textbf{Perception et preuve.} L'indice d'alignement prouvé et la maturité de Luftman
          classent-ils les organisations dans le même ordre~?
    \item \textbf{Le paradoxe de la productivité.} La question de Solow~\cite{solow1987} et de
          Brynjolfsson~\cite{brynjolfsson1993} a été posée pour des économies industrielles. Elle reste
          ouverte pour les administrations d'Afrique centrale.
    \item \textbf{L'informatique hors contrôle.} Quelle part de l'activité réelle des administrations repose
          sur des outils non recensés~? Seize applications sur 47 à l'ANPP est un cas, non une statistique.
\end{enumerate}

""" + lecture("L'audit du 18 juin 2027 jugé selon sa propre méthode", [
    ("L'objet et la date sont délimités", "O", "Version du 11 juin 2027"),
    ("Le référentiel a été arrêté avant l'examen des pièces", "O", "Courriel du 2 juin"),
    ("Chaque cote renvoie à une pièce", "O", "Table des cotes"),
    ("Les mesures sont données par domaine", "O", "Tableau 16.3"),
    ("Les NEK sont publiés avec la pièce attendue", "O", "Section 4 du rapport"),
    ("Les faits ont été validés par l'audité", "O", "Réunion du 17 juin"),
    ("L'auditeur est indépendant de l'objet audité", "N", "Il a siégé au groupe de travail finances"),
    ("L'avis distingue les réserves des recommandations", "O", "Section 5")],
    r"""Sept \OUI{} sur huit. Le \NON{} est sérieux. L'auditeur interne a participé au groupe de travail dont il
contrôle ensuite le produit. Le domaine du chiffrage, où il siégeait, est aussi le plus mal coté, ce qui plaide
pour sa bonne foi. La règle demeure~: on n'audite pas son propre travail. Le rapport le signale en première
page.""") + r"""
"""
chapitre("partie6/P06_C16_auditer.tex", 16, "Auditer un Schéma Directeur, Mesurer l'Alignement", "chap:audit", "Auditer",
 "« Ce qui est affirmé sans preuve\\\\\n    peut être nié sans preuve. »", "Adage latin, \\textit{quod gratis asseritur, gratis negatur}",
 "Avancé", "Tous les chapitres précédents",
 ["Distinguer les trois moments d'audit d'un schéma directeur.", "Écrire une exigence vérifiable par une pièce.", "Coter OUI, NON ou NEK et qualifier un NEK.",
  "Calculer et lire ensemble $\\mu$, $U$ et $H$.", "Lire des résultats par domaine.", "Calculer un indice d'alignement prouvé.", "Structurer un rapport d'audit."],
 "« donnez-moi une note sur vingt »", r"""
Yaoundé, vendredi 18~juin~2027. Six jours avant le conseil d'administration. M.~TCHUENTE, son président, reçoit
l'auditeur interne. Il a lu la synthèse de quatre pages. Il veut savoir si le document est bon. « Donnez-moi une
note sur vingt. »

L'auditeur ne donne pas de note sur vingt. Il pose trois nombres sur la table. Trente-sept exigences sur
quarante-huit sont prouvées. Sept ne sont pas satisfaites, dont trois sur le chiffrage. Quatre n'ont pas pu
être vérifiées. « Je peux vous dire ce qui est établi, ce qui manque et ce que j'ignore. Une note unique
mélangerait les trois. »

\begin{boxalert}
\textbf{Violation typique.} Résumer un audit par une note unique.

\smallskip
\textbf{Règle~:} un audit rend trois informations~: ce qui est conforme, ce qui ne l'est pas, ce qui n'a pas
pu être établi. Les fondre en un nombre détruit la troisième.
\end{boxalert}
""", corps,
 [("Auditeur interne", "Arrêter le référentiel avant les pièces. Publier les NEK. Se récuser s'il a participé aux travaux."),
  ("Président du conseil d'administration", "Demander un avis indépendant avant d'approuver. Lire les NEK avant les NON."),
  ("Consultant", "Livrer avec le document la table des pièces qui prouvent chaque exigence."),
  ("Chercheur", "Employer la grille sur un échantillon d'organisations pour produire les mesures qui manquent.")],
 ["Trois moments d'audit~: avant l'approbation, pendant l'exécution, à l'échéance.", "Un audit compare un objet à un critère au moyen d'une preuve.",
  "Trois cotes~: OUI, NON, NEK. Le NEK est de preuve ou de critère.", "$\\mu$ mesure le prouvé, $U$ l'ignoré, $H$ la dispersion des cotes.",
  "Les résultats se lisent par domaine.", "L'indice d'alignement prouvé complète la mesure de perception de Luftman.",
  "Le rapport publie les NEK.", "On n'audite pas son propre travail."],
 ["écrire dix exigences vérifiables", "coter un document et calculer les trois mesures", "rédiger un constat et sa recommandation", "donner un avis en trois phrases"],
 [("Trois mesures", 1, "Un audit de 20~exigences donne 12~OUI, 5~NON et 3~NEK. Calculez $\\mu$, $U$ et $H$."),
  ("Réécrire", 2, "Réécrivez chaque exigence pour qu'une pièce puisse la vérifier~: « la gouvernance est efficace », « les utilisateurs sont impliqués », « le budget est réaliste », « la sécurité est prise en compte »."),
  ("Deux objets", 2, "Deux schémas directeurs obtiennent $\\mu = 0{,}60$. Le premier a $U = 0{,}05$, le second $U = 0{,}35$. Rédigez pour chacun l'avis en trois phrases."),
  ("Vérifier le tableau", 2, "Recalculez le $\\mu$ de chaque domaine du Tableau~16.3 et l'entropie de l'ensemble. Quel domaine a l'entropie la plus forte~? Qu'est-ce que cela signifie~?"),
  ("L'audit à l'échéance", 3, "Nous sommes en 2032. Concevez l'audit à l'échéance du schéma directeur 2027-2031 de l'ANPP~: douze exigences, les pièces à demander, les mesures de départ dont vous aurez besoin et que vous devez donc faire conserver dès 2027.")],
 ["Minka, \\textit{Auditologie}~\\cite{minka2026auditologie}.", "Luftman~\\cite{luftman2000}.", "Henderson et Venkatraman~\\cite{henderson1993}.", "Shannon~\\cite{shannon1948}."],
 "Le cours s'achève où il a commencé~: devant un document de schéma directeur, avec une grille et des pièces. Les annexes rassemblent les outils~: glossaire, modèles, textes, référentiel d'exigences.")
