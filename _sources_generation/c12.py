# -*- coding: utf-8 -*-
from ch import *
corps = sec("Le Coût Complet", "sec:c12-cout") + r"""
Le coût d'un projet ne s'arrête pas à sa mise en service. Le \termecle{coût complet de possession} additionne
l'investissement et tout ce que l'organisation paiera ensuite pour faire vivre le résultat.

""" + tab("L{3.0cm}L{9.0cm}", ["Poste", "Contenu"], [
    ["Investissement", "Logiciels, matériels, prestations d'intégration, reprise des données, formation, conduite du changement"],
    ["Charges internes", "Temps des agents du métier et de l'informatique affectés au projet"],
    ["Fonctionnement", "Maintenance, licences ou abonnements, hébergement, liaisons, énergie, exploitation"],
    ["Renouvellement", "Remplacement des matériels, montées de version"],
    ["Sortie", "Reprise des données et retrait en fin de vie"]],
    "Les cinq postes du coût complet", "12.1") + r"""

Le référentiel des bénéficiaires de l'ANPP demande 340~millions d'investissement, payés 60 en 2027 et 280 en
2028. Il coûte ensuite 48~millions par an à partir de 2029. Sur la période du schéma directeur, son coût
complet est de $340 + 3 \times 48 = 484$~millions. La fiche de projet n'affichait que 340.

\begin{boxalert}
\textbf{Violation typique.} Chiffrer un schéma directeur en investissement seul.

\smallskip
\textbf{Règle~:} chaque projet affiche deux montants~: l'investissement et le coût annuel après mise en
service. Le schéma directeur affiche la dépense de fonctionnement de sa dernière année.
\end{boxalert}

""" + sec("Estimer", "sec:c12-estimer") + r"""
Trois méthodes d'estimation se combinent. L'\termecle{analogie} part d'un projet comparable déjà réalisé. Le
\termecle{détail} additionne les éléments un à un. Le \termecle{prix de marché} interroge des fournisseurs sans
les engager. Aucune n'est exacte. Chaque estimation se donne donc avec une fourchette.

La fourchette se resserre avec l'avancement. En phase de schéma directeur, une estimation à plus ou moins
30~\% est honnête. Elle se couvre par une \termecle{provision pour aléas}. L'ANPP avait retenu 20~millions de
marge sur 4,2~milliards, soit moins de 0,5~\%. Le cabinet a proposé 8~\% des projets non obligatoires.

""" + sec("La Valeur d'un Projet", "sec:c12-valeur") + r"""
Quand un projet rapporte ou économise de l'argent, on compare ce qu'il coûte à ce qu'il rapporte, en tenant
compte du temps. Un franc reçu dans cinq ans vaut moins qu'un franc reçu aujourd'hui. La
\termecle{valeur actuelle nette} ramène tous les flux à la date de départ.

\begin{equation}
    \mathrm{VAN} = -I_0 + \sum_{t=1}^{n} \frac{F_t}{(1+r)^t}
\end{equation}

$I_0$ est l'investissement, $F_t$ le flux net de l'année $t$, $r$ le taux d'actualisation, $n$ la durée.

Le guichet unique des demandes coûte 180~millions. Il réduit les déplacements d'agents et les doubles saisies
pour un gain net estimé à 55~millions par an pendant cinq ans. Au taux de 8~\%, la somme actualisée des gains
vaut $55 \times 3{,}993 = 219{,}6$~millions. La valeur actuelle nette est de $219{,}6 - 180 = 39{,}6$~millions.
Le projet se paie.

\begin{boxinfo}
\textbf{Limite dans le secteur public.} La plupart des bénéfices d'une administration ne sont pas des recettes.
Un paiement à date fixe ne rapporte rien à l'Agence. Il évite à un retraité de s'endetter. Ward et Daniel
proposent de classer les bénéfices selon qu'ils sont financiers, quantifiables, mesurables ou seulement
observables~\cite{warddaniel2006}. Un bénéfice observable reste un bénéfice, à condition de dire qui
l'observera et comment.
\end{boxinfo}

""" + sec("Engager et Payer", "sec:c12-aecp") + r"""
Le Chapitre~\ref{chap:droit} a distingué autorisations d'engagement et crédits de paiement. Chaque projet se
présente donc sur deux lignes.

""" + tab("L{4.6cm}rrrr", ["Lot 2. Liquidation (millions)", "2028", "2029", "2030", "Total"], [
    ["Autorisations d'engagement", "780", "", "", "780"],
    ["Crédits de paiement", "150", "420", "210", "780"]],
    "Engagements et paiements d'un lot", "12.2") + r"""

L'engagement est pris en 2028 pour la totalité, sans quoi le marché ne peut pas être signé. Les paiements
suivent les livraisons. Si les crédits de 2029 sont réduits, le fournisseur n'est pas payé à l'échéance, le
projet ralentit et des intérêts moratoires courent.

""" + sec("Financer", "sec:c12-financer") + r"""
Le plan de financement met en face de chaque année une ressource. Il en existe quatre sortes pour un
établissement public~: les ressources propres, la subvention de l'État, le concours d'un partenaire technique et
financier, l'économie dégagée par le schéma directeur lui-même.

""" + tab("L{5.0cm}rL{4.4cm}", ["Ressource", "Montant (millions)", "Condition"], [
    ["Ressources propres de l'Agence", "2 300", "Délibération annuelle du conseil"],
    ["Subvention d'investissement de l'État", "1 200", "Inscription en loi de finances"],
    ["Partenaire technique et financier", "680", "Convention à signer, fléchée sur le secours et le référentiel"],
    ["Total", "4 180", ""]],
    "Le plan de financement de l'ANPP", "12.3") + r"""

Une ressource n'est acquise que lorsqu'un acte l'établit. Le plan distingue donc trois états~: acquise,
demandée, espérée. Au 11~juin~2027, seules les ressources propres de 2027 sont acquises. Le schéma directeur
l'écrit et prévoit ce qui serait retiré si la subvention ou la convention manquait. C'est le
\termecle{scénario de repli}. Celui de l'ANPP ramène le portefeuille à 2~300~millions en conservant les cinq
projets obligatoires, le référentiel et le premier lot de la refonte.

Le fonctionnement change aussi. En 2031, les nouveaux systèmes ajoutent 310~millions de charges annuelles. Le
retrait de neuf applications en retire 85. Le fonctionnement annuel augmente donc de 225~millions. Le conseil
d'administration doit le savoir le jour où il approuve.

""" + sec("Faire, Acheter, Louer", "sec:c12-acheter") + r"""
Pour chaque besoin, trois voies s'ouvrent. Coase puis Williamson ont montré que le choix dépend des coûts de
transaction~\cite{coase1937,williamson1975}~: on garde en interne ce qui est spécifique, incertain et fréquent,
on achète le reste.

""" + tab("L{2.2cm}L{4.6cm}L{5.2cm}", ["Voie", "Convient quand", "Point de vigilance"], [
    ["Faire", "Le besoin est propre à l'organisation et au cœur du métier", "Dépendance à quelques agents"],
    ["Acheter", "Un produit du marché couvre le besoin commun", "Coût des adaptations, dépendance à l'éditeur"],
    ["Louer", "Le besoin varie ou l'investissement est impossible", "Localisation des données, réversibilité, charge récurrente"]],
    "Trois voies d'acquisition", "12.4") + r"""

Louer un service en nuage transforme un investissement en charge de fonctionnement. Pour une administration,
cela déplace la dépense d'une ligne budgétaire à une autre, ce qui n'est pas toujours possible. Cela pose aussi
la question du lieu des données, que la loi n°~2024/017 encadre pour les transferts hors du
Cameroun~\cite{loi2024017}.

Tout contrat prévoit sa fin. La \termecle{réversibilité} oblige le prestataire à restituer les données dans un
format utilisable et à assister la reprise. Elle se négocie à la signature.

Le plan d'achat du schéma directeur liste les marchés, leur type, leur montant estimé et leur date de
lancement. L'ANPP en prévoit quatorze pour ses vingt-deux projets. Le code des marchés publics en fixe la
procédure~\cite{decret2018366}.

""" + sec("Doter", "sec:c12-doter") + r"""
Un portefeuille de 4,2~milliards ne se conduit pas avec une division conçue pour en dépenser 136~millions par
an. Le plan de dotation répond à trois questions~: quelles compétences, combien, par quelle voie.

""" + tab("L{4.6cm}cL{5.4cm}", ["Compétence", "Postes", "Voie"], [
    ["Responsable de la sécurité", "1", "Recrutement en 2027"],
    ["Chefs de projet", "2", "Un recrutement, une mobilité interne"],
    ["Architecte", "1", "Recrutement en 2028"],
    ["Données", "3", "Deux recrutements, une reconversion"],
    ["Acheteur informatique", "1", "Mobilité depuis les marchés"]],
    "Le plan de dotation de l'ANPP~: huit postes", "12.5") + r"""

La division passe de 19 à 27~agents. Les postes sont décrits avec le référentiel européen des
compétences~\cite{ecf}. Le plan prévoit aussi la formation des agents en place et le transfert de compétences
dans chaque marché. Les deux agents qui connaissent la liquidation sont affectés à la refonte. Leur
remplacement à la maintenance est organisé avant.

\begin{boxprocedure}
\textbf{Établir le plan de financement.}
\begin{enumerate}
    \item Compléter chaque fiche~: investissement, coût annuel, fourchette.
    \item Ajouter la provision pour aléas.
    \item Présenter chaque projet en engagements et en paiements.
    \item Additionner par année. Comparer au profil des ressources.
    \item Qualifier chaque ressource~: acquise, demandée, espérée.
    \item Écrire le scénario de repli.
    \item Calculer le fonctionnement de la dernière année.
    \item Joindre le plan d'achat et le plan de dotation.
\end{enumerate}
\end{boxprocedure}

""" + lecture("Le plan de financement de l'ANPP, 11 juin 2027", [
    ("Chaque projet affiche investissement et coût annuel", "O", "22 fiches complétées"),
    ("Une provision pour aléas est chiffrée", "O", "8~\\% des projets non obligatoires"),
    ("Chaque projet est présenté en engagements et en paiements", "O", "Tableaux du plan"),
    ("Chaque ressource est qualifiée", "O", "Tableau 12.3 et colonne d'état"),
    ("Un scénario de repli est écrit", "O", "Portefeuille à 2 300 millions"),
    ("Le fonctionnement de 2031 est calculé", "O", "Hausse de 225 millions par an"),
    ("Le total avec provision tient dans l'enveloppe", "N", "4 422 pour 4 200"),
    ("Le plan d'achat est rapproché de la programmation", "O", "Quatorze marchés"),
    ("Les huit postes sont autorisés", "K", "Demande adressée à la tutelle, réponse attendue")],
    r"""Sept \OUI{} sur neuf. Le \NON{} est le prix de l'honnêteté. La provision de 8~\% porte sur 3~030~millions
de projets non obligatoires, soit 242~millions. Le total atteint 4~422~millions. Le comité de pilotage a deux
voies~: relever l'enveloppe ou retirer un projet. Il a retiré la refonte du site d'information et un projet de
soutien. Le \NEK{} est de preuve et il est grave~: sans les postes, la trajectoire ne tient pas.""") + r"""
"""
chapitre("partie4/P04_C12_financer.tex", 12, "Chiffrer, Financer, Acheter, Doter", "chap:financer", "Financer",
 "« Un plan sans ressources est un vœu. »", "Principe du cours",
 "Intermédiaire", "Chapitres~\\ref{chap:droit} et \\ref{chap:portefeuille}",
 ["Calculer le coût complet d'un projet.", "Donner une estimation avec sa fourchette et sa provision.", "Calculer une valeur actuelle nette et en dire les limites.",
  "Présenter un projet en engagements et en paiements.", "Établir un plan de financement avec un scénario de repli.", "Choisir entre faire, acheter et louer.", "Établir un plan de dotation."],
 "« qui paiera ensuite ? »", r"""
Yaoundé, mardi 25~mai~2027. M.~ABDOULAYE relit les 22~fiches. Il additionne les investissements~: 4~180~millions.
Il cherche ensuite la colonne des coûts annuels. Neuf fiches n'en ont pas. Il appelle Mme~EKANI. « Vous me
demandez d'approuver l'achat de vingt-deux voitures sans me dire ce qu'elles consomment. »

Le cabinet reprend les neuf fiches en une semaine. Le résultat surprend le comité~: en 2031, l'Agence paiera
chaque année 225~millions de plus qu'aujourd'hui pour faire tourner ce qu'elle aura construit. Personne ne
l'avait vu. Le schéma directeur de 2021 ne le disait pas non plus.

\begin{boxalert}
\textbf{Violation typique.} Présenter au conseil un total d'investissement sans la charge récurrente qu'il
crée.

\smallskip
\textbf{Règle~:} l'organe qui approuve un schéma directeur approuve deux chiffres~: l'enveloppe de la période
et le fonctionnement annuel à son terme.
\end{boxalert}
""", corps,
 [("Directeur financier", "Qualifier chaque ressource. Refuser un plan dont tout le financement est espéré."),
  ("Acheteur", "Traduire le portefeuille en marchés. Caler leur lancement sur la programmation. Écrire les clauses de réversibilité."),
  ("Responsable des ressources humaines", "Faire autoriser les postes avant le lancement des projets qui en dépendent."),
  ("Consultant", "Donner des fourchettes. Chiffrer la provision. Écrire le scénario de repli sans attendre qu'on le demande.")],
 ["Le coût complet ajoute à l'investissement le fonctionnement, le renouvellement et la sortie.", "Une estimation se donne avec une fourchette et se couvre par une provision.",
  "La valeur actuelle nette compare des flux ramenés à la date de départ. Elle ne saisit pas les bénéfices non financiers.", "Un projet public se présente en engagements et en paiements.",
  "Une ressource est acquise, demandée ou espérée.", "Le scénario de repli dit ce qui reste si une ressource manque.",
  "Le conseil approuve l'enveloppe et le fonctionnement annuel à terme.", "Le plan de dotation précède les projets."],
 ["calculer le coût complet d'un projet sur cinq ans", "calculer une valeur actuelle nette", "dresser le tableau des engagements et des paiements", "écrire un scénario de repli"],
 [("Coût complet", 1, "Un projet demande 200~millions d'investissement en 2027 et 30~millions par an à partir de 2028. Calculez son coût complet sur 2027-2031."),
  ("Valeur actuelle nette", 2, "Un projet coûte 120~millions et procure un gain net de 40~millions par an pendant quatre ans. Calculez sa valeur actuelle nette au taux de 8~\\%, puis au taux de 15~\\%. Commentez."),
  ("La provision", 2, "Vérifiez les chiffres de la lecture du plan de financement~: montant des projets non obligatoires, provision, total. De combien faut-il réduire le portefeuille pour tenir dans 4~200~millions, provision comprise~?"),
  ("Le repli", 3, "La convention avec le partenaire technique et financier n'est pas signée à la fin de 2027. Rédigez la note au comité de pilotage~: projets touchés, conséquences sur la trajectoire, options, recommandation."),
  ("Louer ou acheter", 3, "La BANQUE SANAGA hésite entre acheter ses serveurs de secours et louer un service d'hébergement hors de la CEMAC. Comparez les deux voies sur cinq critères, dont le regard du superviseur et la réversibilité.")],
 ["Ward et Daniel sur la gestion des bénéfices~\\cite{warddaniel2006}.", "La loi n°~2018/012~\\cite{loi2018012}.", "Williamson sur les coûts de transaction~\\cite{williamson1975}."],
 "Le schéma directeur est complet. Le conseil d'administration l'approuve le 24~juin~2027. Le plus difficile commence~: l'exécuter. C'est l'objet du Chapitre~\\ref{chap:piloter}.")
