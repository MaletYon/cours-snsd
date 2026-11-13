import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h import *

SPEC = [
    T("Jour 7 / 15 · Séance de 2 heures", "Cadrer et gouverner la démarche", "« Ce qui n'est pas écrit au départ se discute à l'arrivée. » Principe du cours", "Partie IV · Chapitre C08"),
    R("Jour 6 · Contexte national", ["La **SND30** est en vigueur, le plan 2026-2030 est **déposé, en validation**", "Le **conseil** approuve, la loi n° 2018/012 distingue engagements et paiements",
        "Le code des marchés impose des **délais** et interdit de nommer un produit", "La **carte d'applicabilité** se date"]),
    A([("20 min", "**Six questions**, une note de cadrage"), ("15 min", "**Périmètre, horizon, ambition**"), ("20 min", "**Les instances** et la présidence"),
       ("20 min", "**Parties prenantes** et responsabilités"), ("15 min", "**Calendrier, livrables, communication**"), ("30 min", "**Exercice** en séance · synthèse")]),
    C("C08", "Chapitre 8", "PARTIE IV · MÉTHODE", "Cadrer et gouverner la démarche", "« Qui préside ? »"),
    O(["Répondre par écrit aux **six questions** du cadrage", "Définir un périmètre par **trois listes** et des exclusions", "Composer les **instances** d'une démarche",
       "Placer les parties prenantes sur une grille **pouvoir-intérêt**", "Dresser une **matrice des responsabilités**", "Rédiger une **note de cadrage**"]),
    TB("Les six questions du cadrage", "Tableau 8.1 du livre", ["Question", "Ce qu'il faut écrire", "Réponse de l'ANPP"], [2.2, 4.6, 4.6], [
        ["Pourquoi", "Le fait qui déclenche la démarche", "Document échu, panne de mars 2024"], ["Pour qui", "Le commanditaire et l'organe qui approuve", "Directeur général, conseil"],
        ["Sur quoi", "Le périmètre", "Siège, dix antennes, 47 applications"], ["Jusqu'où", "L'horizon et l'ambition", "2025-2029, aligner"],
        ["Avec qui", "Les instances", "Trois instances"], ["Pour quand", "Le calendrier et les livrables", "14 janvier au 26 juin 2025"]]),
    K("Trois niveaux d'ambition", "Le commanditaire choisit avant le diagnostic", [("1", "Remettre à niveau", "Rattraper un retard."), ("2", "Aligner", "Servir le plan stratégique de l'organisation. C'est le choix de l'ANPP."),
        ("3", "Transformer", "Changer la manière de rendre le service.")]),
    TB("Les trois instances de la mission", "Tableau 8.2 du livre", ["Instance", "Composition à l'ANPP", "Rythme", "Rôle"], [2.6, 4.8, 2.2, 1.8], [
        ["Comité de pilotage", "Directeur général, quatre directeurs, cheffe de la division informatique", "Fin de phase", "Décide"],
        ["Équipe projet", "Mme NGO BIYONG, deux agents, le cabinet", "Chaque semaine", "Produit"], ["Groupes de travail", "Un par métier, dont un chef d'antenne", "Selon la phase", "Informe"]]),
    D("La présidence", "La règle la plus souvent enfreinte", [("La règle", "Le comité de pilotage est présidé par **celui qui arbitre les budgets**. S'il délègue, c'est à un directeur de métier, jamais à l'informatique."),
        ("Le conseil", "Il n'est pas une instance de la démarche. Il est **informé du lancement** et il **approuve** le document.")]),
    TB("La grille des parties prenantes", "Tableau 8.3 du livre", ["Position", "Exemple à l'ANPP", "Conduite"], [3.6, 4.2, 3.6], [
        ["Pouvoir fort, intérêt fort", "Directeur général, directeur financier", "Associer à chaque décision"], ["Pouvoir fort, intérêt faible", "Tutelle, conseil d'administration", "Informer à dates fixes"],
        ["Pouvoir faible, intérêt fort", "Chefs d'antenne, agents de guichet", "Consulter, restituer"], ["Pouvoir faible, intérêt faible", "Fournisseurs sortants", "Surveiller"]]),
    P("Qui fait quoi", "La matrice des responsabilités", ["Le **réalisateur** produit", "L'**approbateur** décide et il est **seul**", "Le **consulté** donne un avis avant", "L'**informé** reçoit le résultat",
        "À l'ANPP, la direction générale approuve chaque livrable. Le directeur financier est réalisateur associé du plan de financement"]),
    TB("Les six phases de la mission", "Tableau 8.5 du livre", ["N°", "Phase", "Dates en 2025", "Livrable"], [0.8, 3.4, 3.4, 3.8], [
        ["1", "Cadrage", "12 au 31 janvier", "Note de cadrage"], ["2", "Diagnostic", "3 février au 21 mars", "Rapport de diagnostic"], ["3", "Cible", "24 mars au 25 avril", "Dossier de cible"],
        ["4", "Portefeuille et trajectoire", "28 avril au 23 mai", "Portefeuille, feuille de route"], ["5", "Chiffrage et financement", "26 mai au 13 juin", "Plan de financement"], ["6", "Validation", "14 au 26 juin", "Schéma directeur"]]),
    P("Trois règles de conduite", "Chapitre 8, sections 8.6 et 8.7", ["Une phase **non approuvée** n'est pas terminée", "Le document est plafonné à **60 pages** hors annexes, avec une synthèse de quatre pages pour le conseil",
        "Les chefs d'antenne reçoivent le diagnostic **avant** le comité de pilotage", "Les bénéficiaires ne siègent nulle part : deux réunions avec leurs associations"]),
    SC("« Qui préside ? »", "Mission ANPP · 16 janvier 2025", ["Le cahier des charges prévoyait que Mme NGO BIYONG préside le comité de pilotage.",
        "Elle refuse la première : « Si je préside, ce sera encore le plan de l'informatique. »", "M. BEYALA pose une question à M. OWONA : « Qui, dans cette salle, peut retirer un milliard à une direction pour le donner à une autre ? »"],
        "Le directeur général préside."),
    METIERS3(("Directeur général", "Présider le comité de pilotage. Signer la note de cadrage. Dire l'ambition avant le diagnostic."),
             ("Consultant", "Refuser de commencer sans note signée. Tenir le plafond de pages."),
             ("Directeur des systèmes d'information", "Animer l'équipe projet sans présider. Ouvrir ses contrats et ses comptes.")),
    EX("La grille", "25 minutes, en binôme", "Placez six parties prenantes de l'ANPP sur la grille pouvoir-intérêt et justifiez en une ligne.",
       ["Le président du conseil · le syndicat des agents", "L'éditeur d'e-PRESTATIONS · l'ANTIC", "Les associations de bénéficiaires · le contrôleur financier"],
       "Corrigé indicatif. Président du conseil et contrôleur financier : pouvoir fort, intérêt faible. Syndicat, associations, éditeur : intérêt fort. ANTIC : à informer."),
    SY(["Cadrer, c'est répondre par écrit à **six questions**", "Le périmètre tient en **trois listes** et des exclusions datées", "Le comité de pilotage est présidé par **celui qui arbitre les budgets**",
        "Chaque livrable a **un seul approbateur**", "La note de cadrage est **signée** avant le diagnostic"]),
    M(["Chapitre C08 en entier", "Exercices 8.1 (six questions pour LiZbiZ) et 8.4 (le cadrage sans enveloppe)"]),
    F("Jour 8 · Diagnostiquer l'existant", ["Cinq regards", "Deux notes par application", "Fonctionnement et projets"]),
]
