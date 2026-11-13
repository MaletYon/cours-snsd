import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h import *

SPEC = [
    T("Jour 10 / 15 · Séance de 2 heures", "Portefeuille et trajectoire", "« Gouverner, c'est choisir. » Pierre Mendès France, 1953", "Partie IV · Chapitre C11"),
    R("Jour 9 · Fixer la cible", ["La cible **se déduit** des objectifs", "Six **principes directeurs**, chacun avec sa conséquence", "Le scénario **B** est retenu : secours, puis refonte en trois lots", "Ordre de grandeur : **4,2 milliards**"]),
    A([("15 min", "**Du chantier au projet** : la fiche d'une page"), ("25 min", "**Trier** : obligatoires, valeur, seuil"), ("15 min", "**Équilibrer** le portefeuille"),
       ("25 min", "**Ordonner** : dépendances, capacité, délais de droit"), ("10 min", "**Le profil annuel**"), ("30 min", "**Exercice** en séance · synthèse")]),
    C("C11", "Chapitre 11", "PARTIE IV · MÉTHODE", "Portefeuille et trajectoire", "« Quarante projets, tous prioritaires. »"),
    O(["Rédiger une **fiche de projet**", "Distinguer un projet **obligatoire** d'un projet arbitrable", "**Classer** par valeur rapportée au coût et corriger le classement",
       "Vérifier l'**équilibre** d'un portefeuille", "**Ordonner** selon trois contraintes", "Tracer un **profil annuel** de dépense"]),
    TB("La fiche de projet", "Tableau 11.1 du livre · une page", ["Rubrique", "Contenu"], [3.2, 8.2], [
        ["Résultat", "Ce qui existera à la fin, en une phrase vérifiable"], ["Objectif servi", "L'objectif du plan stratégique et la capacité visée"], ["Responsable", "Un directeur de métier, nommé"],
        ["Coût", "Investissement et coût annuel après mise en service"], ["Durée", "En mois, passation du marché comprise"], ["Dépendances", "Les projets qui doivent être finis avant"],
        ["Ce qu'il remplace", "Les applications retirées"], ["Risque principal", "Un seul, avec sa parade"]], 14),
    S4("L'état des demandes", "28 avril 2025", [("40", "fiches remises par les groupes de travail"), ("6,8", "milliards de coût cumulé"), ("4,2", "milliards d'enveloppe"), ("5", "projets obligatoires pour 1 150 millions")]),
    D("Le projet obligatoire", "Il ne se note pas, il s'inscrit", [("La définition", "Un projet est obligatoire s'il répond à **un texte**, à **une injonction** ou à **un risque** que l'organisation ne peut pas porter."),
        ("Le garde-fou", "Il cite sa référence. Sans elle, il se note comme les autres. À l'ANPP : secours, audit de sécurité, données personnelles, onduleurs, fin de maintenance.")]),
    TB("Classer par valeur rapportée au coût", "Tableau 11.2 du livre", ["N°", "Projet", "Valeur", "Coût", "Valeur par million"], [1.0, 5.0, 1.4, 1.4, 2.4], [
        ["P15", "Tableau de bord des paiements", "55", "60", "0,92"], ["P38", "Refonte du site d'information", "20", "45", "0,44"], ["P21", "Comptabilité analytique", "60", "150", "0,40"],
        ["P12", "Guichet unique des demandes", "70", "180", "0,39"], ["P07", "Référentiel des bénéficiaires", "90", "340", "0,26"], ["P33", "Application mobile des agents", "30", "120", "0,25"]],
        note="Le ratio favorise les petits projets. Deux corrections : un seuil de valeur à 40, puis l'examen des dépendances."),
    TB("Le portefeuille retenu", "Tableau 11.3 du livre", ["Domaine", "Projets", "Montant (millions)"], [6.4, 2.0, 3.0], [
        ["Obligatoires : secours, sécurité, conformité", "5", "1 150"], ["Refonte de la production", "6", "1 820"], ["Référentiels et données", "3", "520"],
        ["Relation avec les bénéficiaires", "4", "410"], ["Soutien et pilotage", "4", "280"], ["Total retenu", "22", "4 180"]],
        note="Onze projets différés, sept rejetés. La liste des projets écartés figure au document, avec le motif."),
    K("Trois contraintes d'ordre", "Chapitre 11, section 11.4", [("D", "Les dépendances", "On ne refond pas la liquidation avant le référentiel. On ne migre rien avant le secours."),
        ("C", "La capacité à faire", "L'ANPP ne conduit pas plus de **six projets** à la fois."), ("L", "Les délais de droit public", "Inscription budgétaire, programmation, passation.")]),
    TB("La trajectoire 2025-2029", "Tableau 11.4 du livre (extrait)", ["Projet ou lot", "2025", "2026", "2027", "2028", "2029"], [4.8, 1.3, 1.3, 1.3, 1.3, 1.3], [
        ["Site de secours, continuité", "X", "X", "", "", ""], ["Référentiel des bénéficiaires", "X", "X", "", "", ""], ["Lot 1. Immatriculation", "", "X", "X", "", ""],
        ["Lot 2. Liquidation", "", "", "X", "X", ""], ["Lot 3. Paiement, recouvrement", "", "", "", "X", "X"], ["Retrait de neuf applications", "X", "X", "", "", ""]],
        note="Chaque lot livre un résultat utilisable seul. À la fin de chaque année, l'Agence dispose d'un système qui fonctionne."),
    TB("Le profil de dépense", "Tableau 11.5 du livre · millions de FCFA", ["", "2025", "2026", "2027", "2028", "2029", "Total"], [2.8, 1.4, 1.4, 1.4, 1.4, 1.4, 1.6], [
        ["Paiements", "380", "1 050", "1 180", "940", "630", "4 180"], ["Projets en cours", "5", "6", "6", "5", "4", ""]],
        note="Le pic de 2027 vaut environ huit fois la moyenne passée des projets, 136 millions par an. Le financement doit changer d'échelle."),
    SC("« Tous prioritaires »", "Mission ANPP · 28 avril 2025", ["Chaque direction a écrit « priorité 1 » en tête de ses fiches. Le total fait 6,8 milliards.", "M. ABDOULAYE propose de réduire chaque projet de 40 %.",
        "Mme EKANI : « Un site de secours à 60 % ne secourt rien. »"], "Un portefeuille se réduit en retirant des projets entiers, non en les amputant."),
    METIERS3(("Directeur de métier", "Signer comme responsable de ses projets. Accepter par écrit le rejet des autres."), ("Responsable de portefeuille", "Tenir les fiches à jour. Présenter l'état des 22 projets sur une page."),
             ("Directeur financier", "Rapprocher le profil annuel du cadre de dépenses. Exiger le coût après mise en service.")),
    EX("L'enveloppe", "25 minutes, en binôme", "Avec les six projets du tableau et 600 millions, composez le meilleur portefeuille. P12 dépend de P07.",
       ["Que donne le choix par ratio seul ?", "Que devient-il si l'on respecte la dépendance ?", "Et si l'on applique le seuil de valeur de 40 ?"],
       "Corrigé. Ratio seul : 555 millions, valeur réelle 165. Avec la dépendance : P07, P15, P21, P38 pour 595 millions et 225 points. Avec le seuil : P07, P12, P15 pour 580 millions et 215 points."),
    SY(["Un projet tient sur **une fiche d'une page**", "Les **obligatoires** s'inscrivent d'abord, référence à l'appui", "Le ratio se corrige par un **seuil de valeur** et par les **dépendances**",
        "Un portefeuille se réduit en retirant des **projets entiers**", "Trois contraintes d'ordre et un **profil annuel** comparé aux moyens"]),
    M(["Chapitre C11 en entier", "Exercices 11.3 (obligatoire ou non) et 11.4 (la trajectoire contrainte)"]),
    F("Jour 11 · Chiffrer, financer, acheter, doter", ["Le coût complet", "Engagements, paiements, scénario de repli", "Faire, acheter, louer"]),
]
