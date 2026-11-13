import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h import *

SPEC = [
    T("Jour 8 / 15 · Séance de 2 heures", "Diagnostiquer l'existant", "« On ne gère bien que ce que l'on a d'abord compté. » Principe du cours", "Partie IV · Chapitre C09"),
    R("Jour 7 · Cadrer et gouverner la démarche", ["**Six questions**, une note de cadrage signée", "Le comité de pilotage est présidé par **celui qui arbitre les budgets**",
        "**Trois ambitions** : remettre à niveau, aligner, transformer", "Six phases, du 14 janvier au 26 juin 2025"]),
    A([("15 min", "**Cinq regards** sur l'existant"), ("20 min", "**Collecter** : documents, entretiens, observation"), ("25 min", "**L'inventaire** et les deux notes par application"),
       ("15 min", "**Organisation et finances**"), ("15 min", "**Restituer** : le constat en trois temps"), ("30 min", "**Exercice** en séance · synthèse")]),
    C("C09", "Chapitre 9", "PARTIE IV · MÉTHODE", "Diagnostiquer l'existant", "« Nous avons trente et une applications. »"),
    O(["Porter **cinq regards** sur l'existant", "Conduire un **entretien** de diagnostic", "Tenir un **inventaire** et une fiche d'application",
       "**Noter** une application sur sa valeur et sa santé", "Partager la dépense entre **fonctionnement et projets**", "Rédiger un **constat** en trois temps"]),
    TB("Les cinq regards", "Tableau 9.1 du livre", ["Regard", "Question", "Sources"], [2.4, 4.6, 4.4], [
        ["Métier", "Que fait l'organisation, que veut-elle faire ?", "Plan stratégique, entretiens de direction"], ["Applications", "Quels logiciels, dans quel état ?", "Inventaire, contrats, utilisateurs"],
        ["Infrastructures", "Sur quoi tout cela tourne-t-il ?", "Inventaire technique, visites"], ["Organisation", "Qui s'en occupe ?", "Organigramme, fiches de poste"], ["Finances", "Combien cela coûte-t-il ?", "Comptes de cinq exercices, marchés"]]),
    ST("Conduire un entretien de diagnostic", "Procédure du chapitre", [("Avant", "Trois questions envoyées la veille."), ("Ouvrir", "Commencer par le **travail** de la personne."), ("Creuser", "Que se passe-t-il quand le système est arrêté ? Demander à **voir**."),
        ("Noter", "Les faits et leur source. Séparer les opinions."), ("Après", "Compte rendu sous **trois jours**, validé.")]),
    S4("La collecte à l'ANPP", "Un document manquant est une information", [("34", "documents demandés le premier jour"), ("21", "reçus en deux semaines"), ("13", "n'existent pas, dont l'inventaire et le plan de secours"), ("38", "entretiens d'une heure")]),
    D("L'informatique hors contrôle", "Chapitre 9, section 9.3", [("Le constat", "La division croyait gérer 31 applications. Le cabinet en a trouvé **47**. Seize sont des classeurs ou des services souscrits par une direction. Trois calculent des droits."),
        ("La lecture", "Ces outils signalent un **besoin que l'offre officielle ne couvre pas**. Ils s'inventorient comme les autres.")]),
    TB("Deux notes, quatre décisions", "Seuil à 3 · Tableau 9.3 du livre", ["Valeur pour le métier", "Santé technique", "Décision", "À l'ANPP"], [3.2, 3.2, 2.6, 2.4], [
        ["3 ou plus", "3 ou plus", "Investir", "6"], ["3 ou plus", "Moins de 3", "Refondre", "14"], ["Moins de 3", "3 ou plus", "Conserver", "18"], ["Moins de 3", "Moins de 3", "Retirer", "9"]],
        note="Chaque note est la moyenne de quatre critères notés de 1 à 5. Chaque critère renvoie à une pièce."),
    TB("La division informatique par domaine", "Tableau 9.4 du livre · 19 agents pour 412", ["Domaine", "Agents", "Constat"], [4.4, 1.4, 5.6], [
        ["Exploitation et assistance", "11", "Effectif suffisant, astreinte non organisée"], ["Développement et maintenance", "5", "Deux agents seuls à connaître la liquidation"],
        ["Réseau et sécurité", "2", "Aucun responsable de la sécurité désigné"], ["Pilotage, projets, achats", "1", "La cheffe de division, seule"], ["Données", "0", "Compétence absente"]]),
    S4("La dépense sur cinq ans", "Tableau 9.5 du livre", [("3 100", "millions de FCFA dépensés de 2019 à 2023"), ("78 %", "de fonctionnement"), ("22 %", "de projets"), ("136", "millions par an pour les projets")],
        "Le schéma directeur de 2019 annonçait 6,3 milliards. L'écart était lisible dès le premier jour."),
    D("Le constat en trois temps", "Chapitre 9, section 9.8", [("La forme", "**Le fait**, **la pièce**, **la conséquence** pour le métier. Dix constats au plus, par ordre de gravité."),
        ("Un exemple", "La liquidation des droits repose sur une application de 2004 que deux agents savent maintenir (fiche d'application) : un départ suspend l'évolution des droits.")]),
    SC("Le classeur de 2017", "Mission ANPP · 10 février 2025", ["Mme NGO BIYONG remet la liste des applications : il y en a 31.", "Le même jour, Mme EKANI revient de la direction des prestations avec un classeur de calcul. Un chef de service l'a construit en 2017 pour corriger les pensions de réversion.",
        "Il traite **4 200 dossiers par an**. Personne à la division informatique ne le connaît."], "L'inventaire se construit depuis les métiers."),
    METIERS3(("Consultant", "Demander les documents le premier jour. Noter la source de chaque chiffre."), ("Directeur des systèmes d'information", "Fournir l'inventaire qu'il a, sans le maquiller."),
             ("Contrôleur de gestion", "Reconstituer la dépense par nature et par direction.")),
    EX("Deux notes", "20 minutes, en binôme", "Calculez les deux notes et donnez la décision.", ["Critères de valeur : 4, 5, 2, 4", "Critères de santé : 1, 2, 3, 2", "Puis rédigez le constat en trois temps"],
       "Corrigé. Valeur 3,75. Santé 2,0. Décision : refondre. Le constat cite la fiche d'application et dit ce que le métier risque."),
    SY(["Cinq regards : **métier, applications, infrastructures, organisation, finances**", "Un document manquant est un **constat**", "Deux notes, quatre décisions : **investir, refondre, conserver, retirer**",
        "La dépense se partage entre **fonctionnement et projets**", "Le diagnostic **ne propose pas** de solution"]),
    M(["Chapitre C09 en entier", "Exercices 9.2 (la dépense) et 9.4 (les seize)"]),
    F("Jour 9 · Fixer la cible", ["Des objectifs aux capacités", "Principes directeurs et plan fonctionnel", "Comparer des scénarios"]),
]
