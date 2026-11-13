# -*- coding: utf-8 -*-
from ch import *
import re, os
R = '/home/claude/cours-snsd/'
def ecrire(f, s):
    s = re.sub(r',(\s+)et(\s)', r'\1et\2', s)
    assert '’' not in s and '—' not in s
    open(R + f, 'w').write(s); print(f, s.count('\n'))
G = "\\providecommand{\\gardetitre}{\\par\\vskip 0pt plus 9\\baselineskip\\penalty-300\\vskip 0pt plus -9\\baselineskip}\n"
# ---------------------------------------------------------------- A
gl = [
 ("Alignement stratégique", "Accord entre la stratégie de l'organisation, celle de son système d'information et leurs organisations respectives", "alignement"),
 ("Analyse des écarts", "Comparaison, capacité par capacité, de l'existant et de la cible", "cible"),
 ("Autorisation d'engagement", "Limite supérieure des dépenses pouvant être engagées, y compris sur plusieurs années", "droit"),
 ("Bénéfice", "Avantage mesurable ou observable obtenu par le métier grâce à un projet. Il a un propriétaire et une mesure de départ", "piloter"),
 ("Bilan d'impact sur l'activité", "Étude qui fixe, pour chaque activité, l'interruption et la perte de données admissibles", "maitriser"),
 ("Cadrage", "Phase qui répond par écrit aux six questions préalables et se clôt par une note signée", "cadrer"),
 ("Capacité", "Aptitude attendue du système d'information, formulée par un verbe et un résultat, sans nommer de solution", "cible"),
 ("Carte d'applicabilité", "Tableau daté qui dit, texte par texte, s'il s'applique à l'organisation et sous quelle condition", "droit"),
 ("Cellule de portefeuille", "Petite équipe indépendante des projets qui tient les fiches, mesure l'avancement et alerte", "piloter"),
 ("Cible", "Description du système d'information voulu à la fin de la période", "cible"),
 ("Comité de pilotage", "Instance qui décide pendant la démarche, présidée par celui qui arbitre les budgets", "cadrer"),
 ("Comité de portefeuille", "Instance qui lance, arrête et arbitre les projets pendant l'exécution", "piloter"),
 ("Constat", "Énoncé en trois temps~: le fait, la pièce, la conséquence pour le métier", "diagnostic"),
 ("Coût complet de possession", "Somme de l'investissement, du fonctionnement, du renouvellement et de la sortie sur une période", "financer"),
 ("Crédit de paiement", "Limite supérieure des dépenses pouvant être payées dans l'année", "droit"),
 ("Donnée de référence", "Donnée partagée par plusieurs processus, dotée d'un propriétaire et d'un système maître", "donnees"),
 ("Durée maximale d'interruption admissible", "Délai au-delà duquel l'arrêt d'une activité cause un dommage inacceptable", "maitriser"),
 ("Exigence", "Énoncé vérifiable par une pièce, tiré d'un texte, d'une norme, d'un engagement ou d'une règle de l'art", "audit"),
 ("Facteur clé de succès", "Domaine où les résultats doivent être bons pour que l'organisation réussisse", "alignement"),
 ("Fiche d'application", "Description d'une application en dix rubriques", "diagnostic"),
 ("Fiche de projet", "Description d'un projet candidat en une page et huit rubriques", "portefeuille"),
 ("Gouvernance du système d'information", "Système par lequel l'usage du numérique est dirigé et contrôlé. Trois tâches~: évaluer, diriger, surveiller", "normes"),
 ("Indice d'alignement prouvé", "Part des exigences d'alignement dont la satisfaction est prouvée par une pièce", "audit"),
 ("Informatique hors contrôle", "Outils employés sans que la fonction informatique les ait fournis ni recensés", "diagnostic"),
 ("Interopérabilité", "Aptitude de systèmes distincts à échanger des données et à les employer", "donnees"),
 ("Lot", "Partie d'un grand projet qui livre un résultat utilisable seul", "portefeuille"),
 ("NEK", "Cote donnée quand l'auditeur ne peut pas conclure. De preuve si la pièce manque, de critère si l'exigence ne peut pas s'appliquer", "audit"),
 ("Note de cadrage", "Document de dix pages, signé du commanditaire, qui fixe la démarche", "cadrer"),
 ("Perte de données maximale admissible", "Ancienneté maximale des données que l'on accepte de retrouver après un sinistre", "maitriser"),
 ("Plan fonctionnel", "Découpage du système en zones, quartiers et blocs, indépendant des logiciels", "cible"),
 ("Portefeuille", "Ensemble des projets réunis pour atteindre des objectifs stratégiques", "portefeuille"),
 ("Principe directeur", "Règle durable qui tranche d'avance une famille de décisions. Elle vaut par ses conséquences", "cible"),
 ("Projet obligatoire", "Projet imposé par un texte, une injonction ou un risque que l'organisation ne peut pas porter", "portefeuille"),
 ("Provision pour aléas", "Montant réservé pour couvrir l'incertitude des estimations", "financer"),
 ("Registre de conformité", "Liste des exigences applicables avec leur responsable, leur état et leur pièce", "maitriser"),
 ("Réversibilité", "Obligation faite à un prestataire de restituer les données et d'assister la reprise en fin de contrat", "financer"),
 ("Scénario de repli", "Portefeuille réduit prévu d'avance pour le cas où une ressource manquerait", "financer"),
 ("Schéma directeur", "Document approuvé par l'organe de gouvernance qui fixe pour plusieurs années la cible du système d'information, les projets, leur ordre, leur coût et leur pilotage", "vocabulaire"),
 ("Schéma directeur glissant", "Schéma directeur dont l'horizon est repoussé d'un an à chaque révision annuelle", "piloter"),
 ("Stratégie numérique", "Choix par lesquels une organisation emploie le numérique pour atteindre ses objectifs ou les redéfinir", "vocabulaire"),
 ("Trajectoire", "Ordre daté des projets retenus, lisible année par année", "portefeuille"),
 ("Urbanisation", "Démarche qui organise le système d'information en blocs aux frontières stables, à la manière d'un plan de ville", "cible"),
 ("Valeur acquise", "Budget des travaux réellement achevés à une date. Elle se compare à la valeur planifiée et au coût réel", "piloter"),
 ("Valeur actuelle nette", "Somme des flux d'un projet ramenés à la date de départ, investissement déduit", "financer"),
]
gl.sort(key=lambda x: x[0].lower().replace('é','e').replace('è','e'))
A = "\\chapter{Glossaire}\n\\label{ann:glossaire}\n\nCe glossaire reprend sous une forme abrégée les définitions des chapitres. Le renvoi indique le chapitre où le terme est défini et employé.\n\n\\begin{description}\n"
for t, d, c in gl:
    A += "    \\item[%s] %s (Ch.~\\ref{chap:%s}).\n" % (t, d, c)
A += "\\end{description}\n"
ecrire('annexes/Ann_A_glossaire.tex', A)
# ---------------------------------------------------------------- B
B = G + r"""\chapter{Modèles}
\label{ann:modeles}

Ces modèles sont ceux de la mission ANPP. Ils se recopient et s'adaptent. Aucun ne dépasse une page une fois
rempli, sauf la note de cadrage et le schéma directeur lui-même.

\gardetitre
\section*{B1. Note de cadrage (Chapitre~\ref{chap:cadrer})}

""" + tab("cL{4.0cm}L{7.4cm}", ["N°", "Section", "Contenu"], [
 ["1", "Fait déclencheur", "Trois lignes~: ce qui s'est passé, à quelle date"],
 ["2", "Commanditaire et approbation", "Qui commande, quel organe approuve, par quel acte"],
 ["3", "Périmètre", "Entités, métiers, objets. Liste des exclusions datées et motivées"],
 ["4", "Horizon et ambition", "Années couvertes. Remettre à niveau, aligner ou transformer"],
 ["5", "Instances", "Composition nominative, présidence, rythme"],
 ["6", "Parties prenantes", "Grille pouvoir-intérêt, conduite pour chaque groupe"],
 ["7", "Responsabilités", "Matrice par livrable, un seul approbateur"],
 ["8", "Calendrier et livrables", "Phases, dates, comités, plafond de pages"],
 ["9", "Communication", "À qui, quoi, quand, par quel moyen"],
 ["10", "Signature", "Commanditaire, date"]]) + r"""

\gardetitre
\section*{B2. Fiche d'application (Chapitre~\ref{chap:diagnostic})}

""" + tab("L{4.4cm}L{7.6cm}", ["Rubrique", "Exemple~: liquidation des droits"], [
 ["Nom et métier servi", "LIQUID, direction des prestations"],
 ["Responsable côté métier", "Directeur des prestations"],
 ["Utilisateurs", "64 agents, siège et antennes"],
 ["Éditeur ou auteur", "Développement interne"],
 ["Mise en service", "2004"],
 ["Technologie", "Langage et base qui ne sont plus maintenus"],
 ["Maintenance", "Deux agents de la division"],
 ["Coût annuel", "38~millions, salaires compris"],
 ["Données personnelles", "Oui~: identité, carrière, droits"],
 ["Notes", "Valeur 4,5. Santé 1,5. Décision~: refondre"]]) + r"""

\gardetitre
\section*{B3. Fiche de projet (Chapitre~\ref{chap:portefeuille})}

""" + tab("L{4.4cm}L{7.6cm}", ["Rubrique", "Exemple~: P07, référentiel des bénéficiaires"], [
 ["Résultat", "Un fichier unique des 186~000 bénéficiaires, maître pour toutes les applications"],
 ["Objectif servi", "Ne payer que les ayants droit"],
 ["Responsable", "Directeur des prestations"],
 ["Investissement", "340~millions (60 en 2025, 280 en 2026)"],
 ["Coût annuel ensuite", "48~millions à partir de 2027"],
 ["Durée", "20~mois, passation comprise"],
 ["Dépendances", "Aucune en amont. Les trois lots de la refonte en dépendent"],
 ["Ce qu'il remplace", "Onze fichiers de bénéficiaires"],
 ["Risque principal", "Reprise des données défaillante. Parade~: fiabilisation préalable"],
 ["Sécurité, continuité, données", "Analyse de risque, reprise sur le site de secours, formalités de la loi n°~2024/017"],
 ["Jalon d'arrêt", "Fin de la fiabilisation~: moins de 1~\\% de doublons, sinon report"]]) + r"""

\gardetitre
\section*{B4. Fiche d'indicateur (Chapitre~\ref{chap:piloter})}

""" + tab("L{4.4cm}L{7.6cm}", ["Rubrique", "Exemple~: paiements à date"], [
 ["Formule", "Prestations payées au plus tard à la date prévue, divisées par les prestations dues"],
 ["Source", "Journal des paiements"],
 ["Responsable de la mesure", "Cellule de portefeuille"],
 ["Fréquence", "Chaque mois"],
 ["Mesure de départ", "91~\\% en 2024"],
 ["Cible", "99~\\% en 2029"]]) + r"""

\gardetitre
\section*{B5. Sommaire type d'un schéma directeur}

Soixante pages au plus, hors annexes. Une synthèse de quatre pages l'accompagne pour l'organe qui approuve.

""" + tab("cL{5.0cm}cL{4.6cm}", ["N°", "Partie", "Pages", "Chapitre du cours"], [
 ["1", "Synthèse pour décision", "4", "Tous"],
 ["2", "Mandat, périmètre, gouvernance de la démarche", "4", "\\ref{chap:cadrer}"],
 ["3", "Stratégie de l'organisation et cadre de référence", "5", "\\ref{chap:cameroun} et \\ref{chap:droit}"],
 ["4", "Diagnostic~: dix constats", "8", "\\ref{chap:diagnostic}"],
 ["5", "Cible~: capacités, principes, plan fonctionnel, scénario retenu", "10", "\\ref{chap:cible}"],
 ["6", "Portefeuille et trajectoire", "10", "\\ref{chap:portefeuille}"],
 ["7", "Financement, achats, dotation", "8", "\\ref{chap:financer}"],
 ["8", "Pilotage et révision", "5", "\\ref{chap:piloter}"],
 ["9", "Risques, sécurité, continuité, conformité", "6", "\\ref{chap:maitriser}"],
 ["", "Annexes~: fiches, inventaire, registres, projets écartés", "", ""]]) + r"""

\gardetitre
\section*{B6. Page de décision pour un comité}

Chaque comité reçoit trois jours avant une page par décision. Elle contient cinq lignes~: la décision demandée,
les faits et leurs pièces, les options avec leur coût, la recommandation, ce qui se passe si l'on ne décide pas.
"""
ecrire('annexes/Ann_B_modeles.tex', B)
# ---------------------------------------------------------------- C
def fam(titre, rows):
    return "\\gardetitre\n\\section*{%s}\n\n" % titre + tab("L{6.4cm}L{5.6cm}", ["Texte", "Intérêt pour le schéma directeur"], rows) + "\n\n"
C = G + r"""\chapter{Textes et documents de référence}
\label{ann:textes}

Cette annexe liste les textes cités dans le cours, par famille. Chaque ligne renvoie à la bibliographie, qui
donne la référence complète. La liste est arrêtée au 13~novembre~2026. Les textes changent~: la carte
d'applicabilité d'une mission se date et se relit (Chapitre~\ref{chap:droit}).

""" + fam("C1. Lois camerounaises", [
 ["Loi n°~2010/012 du 21~décembre~2010, cybersécurité et cybercriminalité~\\cite{loi2010012}", "Protection des systèmes, audit de sécurité obligatoire"],
 ["Loi n°~2010/013 du 21~décembre~2010, communications électroniques~\\cite{loi2010013}", "Réseaux et services"],
 ["Loi n°~2010/021 du 21~décembre~2010, commerce électronique~\\cite{loi2010021}", "Activités commerciales en ligne"],
 ["Loi-cadre n°~2011/012 du 6~mai~2011, protection du consommateur~\\cite{loi2011012}", "Services aux particuliers"],
 ["Loi n°~2017/010 du 12~juillet~2017, établissements publics~\\cite{loi2017010}", "Organe qui approuve"],
 ["Loi n°~2017/011 du 12~juillet~2017, entreprises publiques~\\cite{loi2017011}", "Organe qui approuve"],
 ["Loi n°~2018/011 du 11~juillet~2018, transparence et bonne gouvernance~\\cite{loi2018011}", "Reddition des comptes"],
 ["Loi n°~2018/012 du 11~juillet~2018, régime financier de l'État~\\cite{loi2018012}", "Programmes, engagements, paiements"],
 ["Loi n°~2023/009 du 25~juillet~2023, protection des enfants en ligne~\\cite{loi2023009}", "Services ouverts au public"],
 ["Loi n°~2024/017 du 23~décembre~2024, données personnelles~\\cite{loi2024017}", "Formalités, sécurité, transferts"]]) + fam("C2. Décrets camerounais", [
 ["Décret n°~2011/1521/PM du 15~juin~2011~\\cite{decret20111521}", "Application de la loi sur le commerce électronique"],
 ["Décret n°~2012/180 du 10~avril~2012~\\cite{decret2012180}", "Ancien texte de l'ANTIC"],
 ["Décret n°~2012/1643/PM~\\cite{decret20121643}", "Audit de sécurité obligatoire"],
 ["Décret n°~2018/355 du 12~juin~2018~\\cite{decret2018355}", "Marchés des entreprises publiques"],
 ["Décret n°~2018/366 du 20~juin~2018~\\cite{decret2018366}", "Code des marchés publics"],
 ["Décret n°~2019/150 du 22~mars~2019~\\cite{decret2019150}", "Organisation de l'ANTIC"]]) + fam("C3. Documents d'orientation du Cameroun", [
 ["Vision 2035~\\cite{vision2035}", "Cap de long terme"],
 ["Stratégie nationale de développement 2020-2030~\\cite{snd30}", "Document de rattachement des administrations"],
 ["Plan stratégique Cameroun numérique 2020~\\cite{camnum2020}", "Échu. Référence historique"],
 ["Stratégie nationale d'intelligence artificielle~\\cite{snia2025}", "Sept piliers, présentée en juillet 2025"],
 ["Plan stratégique national de santé numérique 2026-2030~\\cite{psnsn2026}", "Exemple de stratégie sectorielle"],
 ["Schéma directeur informatique 2020-2024 du MINEPDED~\\cite{minepded2020sdi}", "Exemple de schéma directeur ministériel"]]) + r"""\begin{boxinfo}
\textbf{Le plan 2026-2030.} Le Plan de développement de l'économie numérique au Cameroun 2026-2030, édition
2025~\cite{pden2026}, est finalisé et déposé. Il est en cours de validation dans les services du Premier
ministre et n'est donc pas en cours de mise en œuvre. Il ne figure pas dans la liste des documents en vigueur.
Un schéma directeur le mentionne comme attendu (Chapitre~\ref{chap:cameroun}, section~\ref{sec:c06-projet}).
\end{boxinfo}

""" + fam("C4. Textes de la CEMAC, de la COBAC et de l'OHADA", [
 ["Règlement n°~04/08/CEMAC/UMAC/COBAC du 6~octobre~2008~\\cite{cemac200804}", "Gouvernement d'entreprise des établissements de crédit"],
 ["Règlement COBAC R-2008/01~\\cite{cobac200801}", "Plan de continuité des activités"],
 ["Règlement COBAC R-2016/04~\\cite{cobac201604}", "Contrôle interne"],
 ["Règlement n°~03/16/CEMAC/UMAC/CM du 21~décembre~2016~\\cite{cemac2016paiement}", "Systèmes, moyens et incidents de paiement"],
 ["Règlement n°~04/18/CEMAC/UMAC/COBAC du 21~décembre~2018~\\cite{cemac2018paiement}", "Services de paiement"],
 ["Lettre circulaire LC-COB/04 du 21~janvier~2022~\\cite{cobac2022lc}", "Audit et politique de sécurité"],
 ["Rapport annuel 2024 de la COBAC~\\cite{cobac2024rapport}", "Règlement sur le risque informatique"],
 ["Acte uniforme OHADA du 26~janvier~2017~\\cite{ohada2017audcif}", "Droit comptable, conservation dix ans"]]) + fam("C5. Textes africains et internationaux", [
 ["Convention de Malabo, 27~juin~2014~\\cite{malabo2014}", "Cybersécurité et données personnelles"],
 ["Stratégie de transformation numérique pour l'Afrique 2020-2030~\\cite{ua2020dts}", "Cap continental"],
 ["Cadre stratégique de l'Union africaine sur les données, 2022~\\cite{ua2022donnees}", "Gouvernance des données"],
 ["Stratégie continentale sur l'intelligence artificielle, 2024~\\cite{ua2024ia}", "Usage responsable"],
 ["Pacte numérique africain, 2024~\\cite{ua2024pacte}", "Position commune"],
 ["Protocole de la ZLECAf sur le commerce numérique, 2024~\\cite{zlecaf2024}", "Échanges numériques"],
 ["Pacte numérique mondial, A/RES/79/1, 22~septembre~2024~\\cite{onu2024pacte}", "Cadre des Nations unies"],
 ["Recommandation de l'OCDE sur les stratégies numériques gouvernementales, 2014~\\cite{ocde2014}", "Doctrine de l'administration numérique"]]) + fam("C6. Normes et référentiels", [
 ["ISO/IEC~38500:2024~\\cite{iso38500}", "Gouvernance du numérique"],
 ["ISO~37000:2021~\\cite{iso37000}", "Gouvernance des organisations"],
 ["COBIT~2019~\\cite{cobit2019}", "Objectifs de gouvernance et de gestion"],
 ["TOGAF, 10\\textsuperscript{e}~édition~\\cite{togaf10}", "Architecture d'entreprise"],
 ["ISO/IEC/IEEE~42010~\\cite{iso42010}", "Description d'architecture"],
 ["ITIL~4~\\cite{itil4}", "Gestion des services"],
 ["ISO~21502 et ISO~21504~\\cite{iso21502,iso21504}", "Projets et portefeuilles"],
 ["ISO~31000~\\cite{iso31000}", "Management du risque"],
 ["ISO/IEC~27001~\\cite{iso27001}", "Sécurité de l'information"],
 ["ISO~22301~\\cite{iso22301}", "Continuité d'activité"],
 ["ISO/IEC~42001~\\cite{iso42001}", "Management de l'intelligence artificielle"],
 ["ISO~56002~\\cite{iso56002}", "Management de l'innovation"],
 ["EN~16234-1~\\cite{ecf}", "Compétences numériques"]])
ecrire('annexes/Ann_C_textes.tex', C)
# ---------------------------------------------------------------- D
S = {'T': 'Texte', 'N': 'Norme', 'E': 'Engagement', 'R': 'Règle de l\'art', 'C': 'Cohérence'}
D = [
 ("D1. Cadrage", "cadrer", [
  ("La note de cadrage est signée par le commanditaire", 'R', 'O', "Signature du 31~janvier"),
  ("Le périmètre du diagnostic est celui de la note de cadrage", 'C', 'O', "Rapprochement des deux documents"),
  ("L'organe d'approbation est le conseil d'administration", 'T', 'O', "Section 2 de la note"),
  ("Le comité de pilotage est présidé par la direction générale", 'N', 'O', "Composition du comité"),
  ("L'horizon couvre le plan stratégique de l'Agence", 'E', 'O', "2025-2029 pour un plan 2024-2028"),
  ("La tutelle a été informée du lancement", 'R', 'K', "Copie du courrier non remise. \\textit{Preuve}")]),
 ("D2. Diagnostic", "diagnostic", [
  ("L'inventaire est construit depuis les métiers", 'R', 'O', "47~fiches, dont 16 hors liste officielle"),
  ("Chaque application a un responsable côté métier", 'R', 'N', "19~fiches sans responsable"),
  ("Chaque note renvoie à une pièce", 'R', 'O', "Registre des pièces"),
  ("La dépense de cinq exercices est reconstituée", 'R', 'O', "Tableau 9.5"),
  ("Le total de la dépense égale la somme par nature", 'C', 'O', "2~418 + 682 = 3~100"),
  ("Le rapport est approuvé par le comité de pilotage", 'R', 'O', "Procès-verbal du 21~mars")]),
 ("D3. Cible", "cible", [
  ("Chaque capacité se rattache à un objectif du plan stratégique", 'E', 'O', "Tableau 10.1"),
  ("Chaque objectif est servi par une capacité et par un projet au moins", 'E', 'O', "Table de correspondance"),
  ("Les principes directeurs sont approuvés avec leurs conséquences", 'N', 'O', "Procès-verbal du 11~avril"),
  ("L'architecture est décrite par des vues adaptées aux lecteurs", 'N', 'O', "Quatre plans"),
  ("Toutes les applications de l'inventaire sont situées sur le plan fonctionnel", 'C', 'O', "47 sur 47"),
  ("Deux scénarios éligibles ont été comparés sur des critères fixés d'avance", 'R', 'O', "Tableau 10.6")]),
 ("D4. Portefeuille", "portefeuille", [
  ("Chaque projet a une fiche et un responsable dans le métier", 'R', 'O', "22~fiches"),
  ("Chaque projet retenu cite un objectif du plan stratégique", 'E', 'O', "22~fiches"),
  ("La sélection suit des critères écrits et les projets écartés sont motivés", 'N', 'O', "Annexe du portefeuille"),
  ("Le total des projets retenus tient dans l'enveloppe fixée", 'E', 'O', "4~180 pour 4~200"),
  ("La trajectoire respecte les dépendances", 'C', 'O', "Tableau 11.4"),
  ("Chaque projet nomme ce qu'il remplace", 'R', 'N', "Sept fiches muettes")]),
 ("D5. Chiffrage et financement", "financer", [
  ("Chaque projet affiche son investissement et son coût annuel", 'R', 'O', "22~fiches complétées"),
  ("Une provision pour aléas est chiffrée", 'R', 'O', "242~millions"),
  ("Chaque projet est présenté en engagements et en paiements", 'T', 'O', "Tableaux du plan"),
  ("Le total des fiches égale le total du plan de financement", 'C', 'N', "4~180 d'un côté, 4~422 de l'autre"),
  ("Chaque bénéfice a un propriétaire et une mesure de départ", 'R', 'N', "Deux bénéfices sans mesure"),
  ("Le fonctionnement à terme est porté à la connaissance du conseil", 'E', 'N', "Absent de la synthèse de quatre pages"),
  ("Chaque ressource est qualifiée par un acte", 'R', 'K', "Projet de convention non transmis. \\textit{Preuve}")]),
 ("D6. Pilotage", "piloter", [
  ("L'organe de gouvernance surveille l'exécution chaque année", 'N', 'O', "Revue annuelle inscrite au document"),
  ("Un comité de portefeuille trimestriel est institué", 'R', 'O', "Section 8"),
  ("Une méthode unique de mesure de l'avancement est fixée", 'N', 'O', "Valeur acquise"),
  ("Le tableau de bord contient un indicateur de résultat du plan stratégique", 'E', 'O', "Paiements à date"),
  ("Une procédure traite les demandes hors portefeuille", 'R', 'O', "Section 8"),
  ("La révision annuelle précède la préparation du budget", 'R', 'K', "Calendrier non arrêté. \\textit{Preuve}")]),
 ("D7. Maîtrise des risques", "maitriser", [
  ("Un registre des risques existe avec des propriétaires", 'N', 'O', "Registre du 13~juin"),
  ("Le secours est dimensionné par un bilan d'impact sur l'activité", 'N', 'O', "Tableau 14.2"),
  ("L'audit de sécurité obligatoire est programmé", 'T', 'O', "Projet obligatoire n°~2"),
  ("Les traitements de données personnelles sont recensés et leurs formalités programmées", 'T', 'O', "Projet obligatoire n°~3"),
  ("Chaque fiche porte les rubriques sécurité, continuité, données", 'R', 'N', "Rubriques absentes de huit fiches"),
  ("Chaque projet a un jalon d'arrêt", 'R', 'N', "Neuf fiches sans jalon")]),
 ("D8. Cadre juridique", "droit", [
  ("Une carte d'applicabilité datée est jointe", 'T', 'O', "Annexe du document"),
  ("Aucun produit ni aucune marque n'est nommé", 'T', 'O', "Relecture"),
  ("Les délais de passation des marchés sont comptés dans la trajectoire", 'T', 'O', "Plan d'achat"),
  ("Chaque projet est rattaché à un programme budgétaire", 'T', 'O', "22~fiches"),
  ("Les transferts de données hors du Cameroun sont identifiés", 'T', 'K', "Contrats d'hébergement non transmis. \\textit{Preuve}")]),
]
tot = {'O': 0, 'N': 0, 'K': 0}; src = {k: 0 for k in S}; n = 0
body = ''
for titre, lab, rows in D:
    body += "\\gardetitre\n\\section*{%s (Chapitre~\\ref{chap:%s})}\n\n" % (titre, lab)
    rr = []
    for e, s, c, p in rows:
        n += 1; tot[c] += 1; src[s] += 1
        rr.append([str(n), e, S[s], COTE[c], p])
    body += tab("cL{4.9cm}L{1.8cm}cL{3.3cm}", ["N°", "Exigence", "Source", "Cote", "Preuve, nature du NEK"], rr) + "\n\n"
print(n, tot, src)
assert n == 48 and tot == {'O': 37, 'N': 7, 'K': 4} and src == {'T': 9, 'N': 8, 'E': 7, 'R': 19, 'C': 5}
Dx = G + r"""\chapter{Les quarante-huit exigences de la mission ANPP}
\label{ann:exigences}

Cette annexe réunit le référentiel employé le 20~juin~2025 pour l'audit du schéma directeur 2025-2029 de l'ANPP
avant son approbation (Chapitre~\ref{chap:audit}). Elle permet de refaire chaque calcul~: 6 + 6 + 6 + 6 + 7 +
6 + 6 + 5 = 48 exigences, 37~\OUI{}, 7~\NON{}, 4~\NEK{}. La colonne Source indique d'où vient l'exigence~: un
texte, une norme, un engagement de l'Agence, une règle de l'art ou la cohérence interne du document. Les
quatre \NEK{} sont de preuve.

Les cotes sont celles du 20~juin~2025. Elles diffèrent parfois de celles des encadrés de lecture des chapitres,
établies à d'autres dates sur des livrables intermédiaires.

""" + body + r"""\gardetitre
\section*{Récapitulatif}

""" + tab("L{4.4cm}ccccc", ["Domaine", "Exigences", "\\OUI{}", "\\NON{}", "\\NEK{}", "$\\mu$"],
 [[t.split('. ')[1], str(len(r)), str(sum(1 for x in r if x[2] == 'O')), str(sum(1 for x in r if x[2] == 'N')), str(sum(1 for x in r if x[2] == 'K')), fr(sum(1 for x in r if x[2] == 'O') / len(r))] for t, l, r in D]
 + [["Ensemble", "48", "37", "7", "4", "0,77"]]) + r"""

\hfill\lecture{0{,}771}{0{,}083}{0{,}99}
"""
ecrire('annexes/Ann_D_exigences.tex', Dx)
