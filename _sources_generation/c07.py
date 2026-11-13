# -*- coding: utf-8 -*-
from ch import *
corps = sec("Cinq Familles de Règles", "sec:c07-familles") + r"""
Un schéma directeur rencontre le droit à cinq moments~: quand il traite des données, quand il sécurise, quand il
finance, quand il achète et quand il fait décider.

""" + tab("L{2.8cm}L{5.0cm}L{4.2cm}", ["Famille", "Textes principaux", "Question pour le schéma directeur"], [
    ["Numérique", "Lois n°~2010/012, 2010/013, 2010/021, 2023/009 et 2024/017", "Que peut-on traiter, échanger, mettre en ligne~?"],
    ["Finances", "Lois n°~2018/011 et 2018/012", "Comment inscrire une dépense sur plusieurs années~?"],
    ["Organisation", "Lois n°~2017/010 et 2017/011", "Qui approuve le document~?"],
    ["Achat", "Décrets n°~2018/366 et 2018/355", "Comment acquérir~?"],
    ["Secteur", "Règlements de la CEMAC et de la COBAC, droit OHADA", "Que demande le superviseur ou le droit des affaires~?"]],
    "Cinq familles de règles", "7.1") + r"""

""" + sec("Les Lois du Numérique", "sec:c07-numerique") + r"""
Trois lois ont été promulguées le même jour, le 21~décembre~2010.

La loi n°~2010/012 relative à la cybersécurité et à la cybercriminalité~\cite{loi2010012} impose aux exploitants
de systèmes d'information de les protéger, prévoit un audit de sécurité obligatoire, que le décret
n°~2012/1643/PM organise~\cite{decret20121643}, et protège la vie privée dans les communications. Pour le schéma
directeur, elle fonde le volet sécurité et le budget de l'audit.

La loi n°~2010/013 régissant les communications électroniques, modifiée par la loi n°~2015/006 du
20~avril~2015~\cite{loi2010013}, encadre les réseaux et les services. Une organisation qui veut exploiter son
propre réseau entre ses sites, ou qui achète de la connectivité, s'y réfère.

La loi n°~2010/021 régissant le commerce électronique~\cite{loi2010021}, précisée par le décret n°~2011/1521/PM
du 15~juin~2011~\cite{decret20111521}, encadre les activités commerciales en ligne. Elle intéresse LiZbiZ dès
qu'elle vend ou contracte par voie électronique.

S'y ajoutent la loi-cadre n°~2011/012 du 6~mai~2011 sur la protection du consommateur~\cite{loi2011012} et la
loi n°~2023/009 du 25~juillet~2023 portant charte de protection des enfants en ligne~\cite{loi2023009}.

\begin{boxjuris}
\textbf{\loicam{n°~2024/017} du 23~décembre~2024 relative à la protection des données à caractère
personnel}~\cite{loi2024017}.

\smallskip
\textbf{Portée pour le schéma directeur.} La loi soumet les traitements à une autorisation préalable, encadre
les transferts hors du Cameroun, impose des mesures de sécurité et prévoit une évaluation d'impact pour les
traitements à risque élevé. Tout projet qui crée ou modifie un traitement de données personnelles porte donc
une tâche de conformité, un délai et un coût. Un schéma directeur qui ne les prévoit pas sous-estime chaque
projet. Le cours d'audit de protection des données (UE MSN-2S4-SEC02) en donne le détail.
\end{boxjuris}

""" + sec("Les Finances Publiques", "sec:c07-finances") + r"""
La loi n°~2018/012 du 11~juillet~2018 fixe le régime financier de l'État et des autres entités
publiques~\cite{loi2018012}. Elle organise le budget en programmes dotés d'objectifs et d'indicateurs et
distingue les \termecle{autorisations d'engagement}, qui permettent de s'engager sur plusieurs années, des
\termecle{crédits de paiement}, qui limitent ce qui peut être payé dans l'année. La loi n°~2018/011 du même jour
porte code de transparence et de bonne gouvernance~\cite{loi2018011}.

Deux conséquences. Un projet pluriannuel se chiffre en engagement total et en paiements annuels. Les deux
tableaux figurent au schéma directeur. Ensuite, un projet se rattache à un programme et à ses indicateurs. Un
projet qui ne contribue à aucun indicateur de programme a peu de chances d'être financé.

\begin{boxinfo}
\textbf{Le cadre de dépenses à moyen terme.} L'administration programme ses dépenses sur trois ans. La première
année du schéma directeur se cale sur le budget voté. Les deux suivantes se calent sur ce cadre. Au-delà, la
trajectoire est indicative, ce que le document doit écrire.
\end{boxinfo}

""" + sec("Qui Approuve", "sec:c07-organes") + r"""
La loi n°~2017/010 du 12~juillet~2017 porte statut général des établissements publics~\cite{loi2017010}. La loi
n°~2017/011 du même jour porte statut général des entreprises publiques~\cite{loi2017011}. Elles ont remplacé la
loi de 1999. Dans les deux cas, un conseil d'administration définit les orientations et approuve les budgets et
les plans, et un directeur général exécute.

Le schéma directeur engage l'organisation sur plusieurs exercices. Il relève donc du conseil. Un document
approuvé par le seul directeur général, ou par la seule direction informatique, n'engage pas les budgets à
venir. C'est l'une des causes du sort du document de 2019 à l'ANPP~: le conseil l'avait approuvé, mais aucune
délibération n'en tirait de conséquence budgétaire.

""" + sec("Acheter", "sec:c07-marches") + r"""
Le décret n°~2018/366 du 20~juin~2018 porte code des marchés publics~\cite{decret2018366}. Il s'applique à
l'État, aux collectivités et aux établissements publics. Les entreprises publiques relèvent du décret
n°~2018/355 du 12~juin~2018, qui fixe des règles communes à leurs marchés~\cite{decret2018355}.

Le code pèse sur le schéma directeur de quatre manières.

\begin{enumerate}
    \item \textbf{Le délai.} Entre la décision de lancer un projet et la notification d'un marché, il s'écoule
          plusieurs mois. La trajectoire doit les compter.
    \item \textbf{L'allotissement.} Découper un projet en lots change la concurrence et le calendrier. Le
          fractionnement destiné à éviter une procédure est interdit.
    \item \textbf{La programmation.} Les marchés de l'année sont programmés à l'avance. Un projet absent de la
          programmation ne peut pas être lancé.
    \item \textbf{La définition du besoin.} Le besoin est décrit par ses fonctions et ses performances, non par
          une marque. Le schéma directeur ne nomme donc pas de produit.
\end{enumerate}

\begin{boxalert}
\textbf{Violation typique.} Inscrire au schéma directeur le nom d'un éditeur ou d'un matériel.

\smallskip
\textbf{Règle~:} le schéma directeur décrit des besoins et des exigences. Le choix du produit résulte de la
mise en concurrence. Un document qui nomme la solution prépare un contentieux.
\end{boxalert}

""" + sec("Le Secteur Bancaire", "sec:c07-banque") + r"""
Un établissement de crédit de la CEMAC est supervisé par la Commission bancaire de l'Afrique centrale, la COBAC.
Cinq textes concernent son système d'information.

""" + tab("L{5.2cm}L{6.8cm}", ["Texte", "Exigence pour le système d'information"], [
    ["Règlement n°~04/08/CEMAC/UMAC/COBAC du 6~octobre~2008~\\cite{cemac200804}", "Gouvernement d'entreprise~: rôle du conseil d'administration"],
    ["Règlement COBAC R-2008/01~\\cite{cobac200801}", "Plan de continuité des activités"],
    ["Règlement COBAC R-2016/04~\\cite{cobac201604}", "Contrôle interne, y compris les activités externalisées"],
    ["Règlement n°~04/18/CEMAC/UMAC/COBAC du 21~décembre~2018~\\cite{cemac2018paiement}", "Services de paiement, en vigueur depuis le 1\\textsuperscript{er}~janvier~2019"],
    ["Lettre circulaire LC-COB/04 du 21~janvier~2022~\\cite{cobac2022lc}", "Audit indépendant de la sécurité, politique de sécurité selon les normes internationales"]],
    "Textes communautaires pour le système d'information d'une banque", "7.2") + r"""

La lettre circulaire de 2022 demandait aux établissements de faire auditer leur système d'information par des
experts indépendants avant le 30~juin~2022 et de se doter d'une politique de sécurité fondée sur les normes
internationales. Le rapport annuel 2024 de la COBAC signale l'adoption d'un règlement relatif à la gestion du
risque informatique~\cite{cobac2024rapport}. Pour la BANQUE SANAGA, le schéma directeur n'est donc pas un choix.
Il répond à un superviseur qui lit le document et vérifie son exécution.

Le règlement n°~03/16/CEMAC/UMAC/CM du 21~décembre~2016 sur les systèmes, moyens et incidents de
paiement~\cite{cemac2016paiement} et le règlement de 2018 sur les services de paiement s'appliquent aussi aux
opérateurs de paiement par téléphone. L'ANPP les rencontre si elle paie des prestations sur compte mobile.

""" + sec("Le Droit des Affaires", "sec:c07-ohada") + r"""
LiZbiZ est une société anonyme régie par les Actes uniformes de l'OHADA. L'Acte uniforme relatif au droit
comptable et à l'information financière, adopté à Brazzaville le 26~janvier~2017~\cite{ohada2017audcif},
intéresse le schéma directeur à deux titres. Il fixe les conditions dans lesquelles une dépense informatique
s'inscrit à l'actif ou en charge, ce qui commande la présentation du budget. Il impose de conserver dix ans les
livres comptables et les pièces justificatives, ce qui commande l'archivage et la réversibilité des systèmes
comptables.

""" + sec("La Carte d'Applicabilité", "sec:c07-carte") + r"""
""" + tab("L{4.4cm}ccc", ["Texte", "ANPP", "LiZbiZ", "BANQUE SANAGA"], [
    ["Loi n°~2010/012, sécurité", "Oui", "Oui", "Oui"],
    ["Loi n°~2024/017, données personnelles", "Oui", "Oui", "Oui"],
    ["Loi n°~2010/021, commerce électronique", "Non", "Oui", "Oui"],
    ["Loi n°~2018/012, régime financier", "Oui", "Non", "Non"],
    ["Loi n°~2017/010, établissements publics", "Oui", "Non", "Non"],
    ["Décret n°~2018/366, marchés publics", "Oui", "Non", "Non"],
    ["Actes uniformes de l'OHADA", "Non", "Oui", "Oui"],
    ["Règlements de la COBAC", "Non", "Non", "Oui"],
    ["Règlements de paiement de la CEMAC", "Si paiement mobile", "Non", "Oui"]],
    "Carte d'applicabilité des textes aux trois organisations", "7.3") + r"""

\begin{boxprocedure}
\textbf{Dresser la carte d'applicabilité d'une organisation.}
\begin{enumerate}
    \item Qualifier l'organisation~: administration, établissement public, entreprise publique, société privée,
          établissement supervisé.
    \item Lister les textes de chaque famille du Tableau~7.1.
    \item Pour chacun, répondre oui, non ou sous condition, et écrire la condition.
    \item Pour chaque oui, noter l'exigence qui touche le schéma directeur et la pièce qui la prouvera.
    \item Dater la carte. Les textes changent.
\end{enumerate}
\end{boxprocedure}

""" + lecture("Le cadre juridique dans le schéma directeur 2019 de l'ANPP", [
    ("Le document est approuvé par le conseil", "O", "Délibération du 17 décembre 2018"),
    ("Une délibération en tire les conséquences budgétaires", "N", "Aucune"),
    ("Les projets sont chiffrés en engagements et en paiements", "N", "Total unique"),
    ("Chaque projet est rattaché à un programme budgétaire", "N", "Aucun rattachement"),
    ("Les délais de passation des marchés sont comptés", "N", "Calendrier sans procédure"),
    ("Aucun produit n'est nommé", "N", "Onze marques citées"),
    ("L'audit de sécurité obligatoire est prévu", "N", "Absent"),
    ("Les traitements de données personnelles sont recensés", "K", "Loi postérieure au document")],
    r"""Un \OUI{} sur huit. Le document de 2019 était approuvé et inapplicable. Le \NEK{} est de critère~: la
loi sur les données personnelles date de 2024 et ne pouvait pas être citée en 2018. Les six \NON{} tiennent à
l'ignorance du droit public par ses rédacteurs. Aucun n'est technique.""") + r"""
"""
chapitre("partie3/P03_C07_cadre_juridique.tex", 7, "Le Cadre Juridique d'un Schéma Directeur", "chap:droit", "Cadre juridique",
 "« Une administration n'achète pas, ne finance pas\\\\\n    et ne décide pas comme une entreprise. »", "Principe du cours",
 "Fondamental", "Chapitre~\\ref{chap:cameroun}",
 ["Citer les lois du numérique et dire ce que chacune impose au schéma directeur.", "Distinguer autorisations d'engagement et crédits de paiement.",
  "Dire quel organe approuve un schéma directeur.", "Énoncer quatre effets du code des marchés publics sur une trajectoire.",
  "Citer les textes communautaires applicables au système d'information d'une banque.", "Dresser une carte d'applicabilité."],
 "« nous lancerons le projet en mars »", r"""
Yaoundé, mercredi 12~février~2025. Le directeur des prestations veut un tableau de bord des paiements « pour
mars ». Mme~EKANI demande à M.~ABDOULAYE, directeur financier, si la dépense est inscrite au budget 2025. Elle ne
l'est pas. Elle demande si le marché figure à la programmation de l'année. Il n'y figure pas.

M.~ABDOULAYE fait le compte. Il faut une inscription au budget, donc une délibération du conseil. Il faut ensuite
un dossier d'appel d'offres, un délai de publication, une commission, une attribution, une notification. « Votre
mars est un mars 2026. » Le directeur des prestations découvre que le calendrier d'un projet public commence
bien avant le premier jour de travail.

\begin{boxalert}
\textbf{Violation typique.} Bâtir la trajectoire d'une administration avec des délais d'entreprise.

\smallskip
\textbf{Règle~:} dans une organisation soumise au droit public, la trajectoire compte trois délais avant le
démarrage d'un projet~: l'inscription budgétaire, la programmation du marché et la passation.
\end{boxalert}
""", corps,
 [("Directeur financier", "Fournir au consultant le budget voté, le cadre de dépenses à moyen terme et la programmation des marchés. Sans ces trois pièces, la trajectoire est une fiction."),
  ("Consultant", "Dresser la carte d'applicabilité avant le diagnostic. Elle dit quelles pièces demander et à qui."),
  ("Directeur des systèmes d'information", "Écrire les besoins par leurs fonctions. Tenir un calendrier des marchés à côté du calendrier des projets.")],
 ["Trois lois du 21~décembre~2010~: cybersécurité, communications électroniques, commerce électronique.", "La loi n°~2024/017 ajoute à chaque projet une tâche de conformité.",
  "La loi n°~2018/012 distingue autorisations d'engagement et crédits de paiement.", "Le conseil d'administration approuve le schéma directeur (lois n°~2017/010 et 2017/011).",
  "Le code des marchés publics (décret n°~2018/366) impose des délais et interdit de nommer un produit.", "Une banque répond à la COBAC~: continuité, contrôle interne, audit de sécurité.",
  "L'Acte uniforme comptable de l'OHADA impose dix ans de conservation."],
 ["dire pourquoi un schéma directeur ne nomme pas de produit", "expliquer la différence entre engagement et paiement", "citer trois textes de la COBAC ou de la CEMAC", "dresser la carte d'applicabilité d'une organisation"],
 [("Quelle famille", 1, "Rangez dans les cinq familles du Tableau~7.1~: le décret n°~2018/366, la loi n°~2018/012, la loi n°~2024/017, le règlement COBAC R-2008/01, la loi n°~2017/010, la loi n°~2010/021, l'Acte uniforme comptable."),
  ("Engagement et paiement", 2, "Un projet de l'ANPP coûte 900~millions sur trois ans~: 200, 450 puis 250. Dressez le tableau des autorisations d'engagement et des crédits de paiement. Que se passe-t-il si les crédits de la deuxième année sont réduits à 300~?"),
  ("Carte d'une université", 2, "Dressez la carte d'applicabilité d'une université d'État qui veut un schéma directeur numérique. Notez pour trois textes l'exigence et la pièce."),
  ("La banque sous-traite", 3, "La BANQUE SANAGA veut confier son hébergement à un prestataire étranger. Listez les textes concernés dans chacune des cinq familles et les questions que le superviseur posera. Séparez ce que les textes exigent de ce que la prudence recommande.")],
 ["La loi n°~2018/012~\\cite{loi2018012}.", "Le code des marchés publics~\\cite{decret2018366}.", "Les lois n°~2017/010 et 2017/011~\\cite{loi2017010,loi2017011}.", "La lettre circulaire LC-COB/04~\\cite{cobac2022lc}."],
 "Le contexte est posé~: théories, normes, orientations, droit. La méthode peut commencer. Son premier temps est le cadrage, objet du Chapitre~\\ref{chap:cadrer}.")
