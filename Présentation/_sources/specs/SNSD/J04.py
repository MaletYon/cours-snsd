import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h import *

SPEC = [
    T("Jour 4 / 15 · Séance de 2 heures", "Normes et référentiels", "« Un cadre volontaire se déclare, une norme se certifie, un texte oblige. »", "Partie II · Chapitre C04"),
    R("Jour 3 · L'alignement et la valeur", ["**McFarlan** : quatre familles d'applications, quatre conduites", "**Quatre perspectives** d'alignement, dont celle du numérique",
        "La valeur vient de l'**usage**, non de l'outil", "Un bénéfice a un **propriétaire** dans le métier"]),
    A([("15 min", "**Quatre natures** de référentiel"), ("20 min", "**ISO/IEC 38500** : le rôle du conseil"), ("20 min", "**COBIT 2019** : six objectifs pour le schéma directeur"),
       ("20 min", "**TOGAF, ITIL 4**, normes de portefeuille"), ("15 min", "**Choisir** et déclarer ses référentiels"), ("30 min", "**Exercice** en séance · synthèse")]),
    C("C04", "Chapitre 4", "PARTIE II · LE CONTEXTE INTERNATIONAL", "Normes et référentiels", "« Notre schéma directeur est conforme à COBIT, ITIL et TOGAF. »"),
    O(["Distinguer **texte, norme certifiable, cadre volontaire, norme de recommandation**", "Énoncer les **trois tâches** de l'ISO/IEC 38500",
       "Citer les **six objectifs** de COBIT 2019 qui portent le schéma directeur", "Dire ce que **TOGAF** et **ITIL 4** apportent",
       "Distinguer **portefeuille, programme, projet**", "**Déclarer** les référentiels d'un schéma directeur"]),
    TB("Quatre natures de référentiel", "Tableau 4.1 du livre", ["Nature", "Force", "Exemple", "Preuve attendue"], [2.8, 3.0, 2.8, 2.8], [
        ["Texte obligatoire", "S'impose, sous sanction", "Code des marchés publics", "Conformité à l'article"], ["Norme certifiable", "Volontaire, vérifiée par un tiers", "ISO/IEC 27001", "Certificat, périmètre, date"],
        ["Cadre volontaire", "Volontaire, déclaré", "COBIT 2019, TOGAF", "Usage déclaré et documenté"], ["Norme de recommandation", "Volontaire, non certifiable", "ISO/IEC 38500, ISO 31000", "Usage déclaré"]]),
    ST("ISO/IEC 38500 : trois tâches du conseil", "Troisième édition, février 2024, alignée sur l'ISO 37000 de 2021", [("Évaluer", "L'usage actuel et futur des technologies."),
        ("Diriger", "La préparation des stratégies et des politiques."), ("Surveiller", "La conformité et la performance.")]),
    P("Ce que la norme change pour le schéma directeur", "Elle s'adresse à l'organe de gouvernance", ["Le conseil **ne rédige pas** le document",
        "Il le **demande**, l'**approuve** et en **surveille l'exécution**", "À l'ANPP, le conseil a approuvé sans surveiller : **deux tâches sur trois** manquaient",
        "Une norme ne devient contraignante que si un **texte** y renvoie, si un **contrat** l'exige ou si l'organisation s'y **engage**"]),
    TB("Six objectifs de COBIT 2019", "Quarante objectifs, un domaine de gouvernance, quatre de gestion", ["Objectif", "Intitulé", "Apport au schéma directeur"], [1.6, 4.4, 5.4], [
        ["EDM01", "Cadre de gouvernance", "Qui décide du schéma directeur"], ["EDM02", "Livraison des bénéfices", "Suivi de la valeur des investissements"],
        ["APO02", "Stratégie gérée", "Diagnostic, cible, feuille de route"], ["APO03", "Architecture d'entreprise gérée", "Cible d'architecture et plan de migration"],
        ["APO05", "Portefeuille géré", "Sélection et arbitrage des projets"], ["APO06", "Budget et coûts gérés", "Chiffrage et suivi financier"]]),
    K("Dessiner, servir", "TOGAF, ISO/IEC/IEEE 42010, ITIL 4", [("T", "TOGAF, 10e édition, 2022", "La vision donne les **principes**. Les phases d'architecture donnent l'existant et la cible. La migration donne les **architectures de transition**."),
        ("V", "ISO/IEC/IEEE 42010", "Une architecture se décrit par des **points de vue** qui répondent aux préoccupations des parties prenantes."),
        ("S", "ITIL 4", "Un projet livré devient un **service à exploiter**. Son coût de fonctionnement figure à la trajectoire.")]),
    TB("Portefeuille, programme, projet", "Le projet fait bien les choses, le portefeuille choisit les bonnes choses à faire", ["Niveau", "Question", "Référence"], [2.4, 6.0, 3.0], [
        ["Portefeuille", "Quels projets, dans quel ordre, avec quels moyens ?", "ISO 21504"], ["Programme", "Comment obtenir un bénéfice par plusieurs projets liés ?", "ISO 21503"],
        ["Projet", "Comment livrer dans les délais, le coût et la qualité ?", "ISO 21502"]]),
    ST("Déclarer les référentiels d'un schéma directeur", "Procédure du chapitre", [("Textes", "Recenser les textes obligatoires qui s'appliquent."), ("Contrats", "Recenser ce qu'exigent un contrat, un bailleur, un superviseur."),
        ("Choix", "Pour chaque besoin restant, **un seul** référentiel volontaire."), ("Écriture", "Lister l'édition et l'usage de chacun."), ("Formule", "Jamais « conforme à ». Écrire « **établi selon** ».")]),
    SC("Trois noms sur une couverture", "BANQUE SANAGA · 21 octobre 2026", ["Le schéma directeur remis au superviseur en 2024 portait la mention « **conforme à COBIT, ITIL et TOGAF** ».",
        "Mme EWANE, responsable du contrôle de second niveau, a cherché sur quoi reposait la phrase. Ni liste des objectifs retenus, ni édition, ni évaluation.",
        "Après la panne, le superviseur a posé la même question. La banque n'a rien pu produire."], "On est conforme à un texte ou certifié selon une norme, sur un périmètre et à une date."),
    METIERS3(("Administrateur", "Demander chaque année ce qui a été évalué, ce qui a été décidé, ce qui a été constaté."),
             ("Directeur des systèmes d'information", "Tenir la liste des référentiels employés, avec leur édition."),
             ("Consultant", "Choisir peu de référentiels et les employer vraiment.")),
    EX("Quelle nature", "20 minutes, en binôme", "Rangez chaque référence dans l'une des quatre natures.", ["COBIT 2019 · ISO/IEC 27001 · le code des marchés publics", "ISO 31000 · TOGAF · ISO 22301", "Un règlement du superviseur bancaire · ITIL 4"],
       "Corrigé. Texte : code des marchés, règlement du superviseur. Certifiable : 27001, 22301. Cadre volontaire : COBIT, TOGAF, ITIL 4. Recommandation : 31000."),
    SY(["Un cadre volontaire **se déclare**, une norme **se certifie**, un texte **oblige**", "ISO/IEC 38500 : le conseil **évalue, dirige, surveille**",
        "COBIT 2019 : EDM01, EDM02, APO02, APO03, APO05, APO06", "TOGAF donne la cible et les architectures de transition", "ISO 21504 pour le portefeuille, ISO 21502 pour le projet"]),
    M(["Chapitre C04 en entier", "Exercices 4.2 (trois tâches) et 4.3 (la couverture)"]),
    F("Jour 5 · Doctrines et stratégies numériques", ["OCDE, Nations Unies, Union africaine", "L'infrastructure publique numérique", "RACINES, urbanisation, souveraineté, sobriété"]),
]
