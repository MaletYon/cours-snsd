import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h import *

SPEC = [
    T("Jour 14 / 15 · Séance de 2 heures", "Données, intelligence artificielle,\nplateformes, sobriété", "« Une donnée sans propriétaire n'est tenue par personne. » Principe du cours", "Partie VI · Chapitre C15"),
    R("Jour 13 · Risques, sécurité, continuité, conformité", ["Le registre des risques se **relit** à chaque comité de portefeuille", "Quatre heures d'interruption admissible imposent **un second site**",
        "Un plan non **essayé** n'existe pas", "La conformité se construit **dès la conception**"]),
    A([("10 min", "**Quatre forces** qui élargissent la méthode"), ("25 min", "**Les données**"), ("25 min", "**L'intelligence artificielle**"),
       ("15 min", "**Les plateformes** et l'interopérabilité"), ("15 min", "**Le nuage et la sobriété**"), ("30 min", "**Exercice** en séance · synthèse")]),
    C("C15", "Chapitre 15", "PARTIE VI · DÉFIS ET RECHERCHE", "Données, intelligence artificielle, plateformes, sobriété", "« Mettons de l'intelligence artificielle. »"),
    O(["Répondre aux **cinq questions** de gouvernance d'une donnée", "Juger un cas d'usage d'intelligence artificielle sur **cinq conditions**", "Lister les **échanges** avec l'extérieur et leurs dépendances",
       "Formuler une **doctrine d'hébergement** par classe de données", "Chiffrer un levier de **sobriété**"]),
    TB("Gouverner une donnée", "Tableau 15.1 du livre · cadre de l'Union africaine, 2022", ["Question", "Réponse attendue", "À l'ANPP, pour le bénéficiaire"], [3.0, 3.8, 4.6], [
        ["À qui appartient-elle ?", "Un propriétaire dans le métier", "Directeur des prestations"], ["Où est sa référence ?", "Un seul système maître", "Référentiel des bénéficiaires"],
        ["Que vaut-elle ?", "Une mesure de qualité", "Taux de doublons"], ["Qui y accède ?", "Des règles d'habilitation", "Par antenne, par fonction"], ["Combien de temps ?", "Une durée et un sort final", "Registre des traitements"]]),
    S4("La qualité du fichier", "Rapprochement d'un échantillon", [("11", "fichiers de bénéficiaires"), ("5 000", "dossiers rapprochés"), ("7,4 %", "de doublons probables"), ("13 800", "dossiers à examiner sur 186 000")],
        "Le projet de référentiel commence par un chantier de fiabilisation, qui n'est pas un chantier informatique."),
    TB("Cinq conditions pour un cas d'usage", "Tableau 15.2 du livre", ["Condition", "Question"], [2.6, 8.8], [
        ["Objectif", "Quel objectif du plan stratégique ce cas sert-il, avec quelle mesure ?"], ["Données", "Existent-elles, en quantité et en qualité, et a-t-on le droit de les employer ?"],
        ["Décision", "Qui décide à la fin : la machine ou un agent ? Qui répond d'une erreur ?"], ["Preuve", "Peut-on expliquer un résultat à la personne concernée ?"], ["Exploitation", "Qui surveillera la dérive du modèle, avec quel budget ?"]]),
    P("L'intelligence artificielle dans le schéma directeur", "Stratégie continentale 2024, stratégie nationale 2025, ISO/IEC 42001", ["Ce n'est **pas un projet** : c'est une famille de techniques au service d'un objectif",
        "Un cas d'usage se nomme par **la décision qu'il aide à prendre**", "Il entre au portefeuille **après** le projet qui lui fournit des données fiables",
        "Les assistants conversationnels sont une nouvelle informatique hors contrôle : une **règle d'usage** dit ce qui n'y est jamais saisi"]),
    SC("Le cas des paiements indus", "ANPP · révision de 2026", ["La direction financière propose un modèle qui signale les dossiers à risque : bénéficiaire décédé, double immatriculation, droit éteint.",
        "Le comité applique les cinq conditions. L'objectif est clair. Les données ne sont pas prêtes avant la fin de 2026.", "Le modèle **signale**, un agent **instruit**, aucune suspension automatique. Chaque signalement indique ses motifs."],
        "Le projet entre au portefeuille pour 2027, pour 95 millions. Il décale un projet de soutien."),
    TB("Les échanges avec l'extérieur", "Tableau 15.3 du livre", ["Échange", "Partenaire", "État en 2025", "Dépend de l'ANPP ?"], [2.4, 4.0, 2.8, 2.4], [
        ["Décès", "État civil", "Courrier mensuel", "Non"], ["Carrières", "Employeurs", "Bordereaux papier", "En partie"], ["Paiements", "Banques, opérateurs de paiement", "Fichiers déposés", "Oui"], ["Identité", "Fichier national d'identité", "Aucun", "Non"]],
        note="Un échange qui dépend d'un tiers s'inscrit comme une hypothèse, avec une solution d'attente."),
    CP("Le nuage et la sobriété", "Deux sujets que le plan de financement porte", "Le nuage", ["**Où** sont les données ?", "**Qui** peut y accéder ?", "**Comment** en sortir ?", "Une doctrine par classe de données : bénéficiaires au Cameroun, gestion dans la sous-région"],
       "La sobriété", ["Retirer avant d'ajouter", "Durée de vie des postes : de quatre à six ans", "380 postes à 450 000 FCFA : **14,25 millions** économisés par an", "La consommation de la salle des serveurs se mesure"]),
    TB("Ce qui change dans le document", "Tableau 15.4 du livre", ["Force", "Ajout au schéma directeur"], [3.2, 8.2], [
        ["Données", "Données de référence, propriétaires, indicateurs de qualité, cellule des données"], ["Intelligence artificielle", "Grille des cinq conditions, règle d'usage, registre des cas d'usage"],
        ["Plateformes", "Tableau des échanges, hypothèses et solutions d'attente"], ["Nuage", "Doctrine d'hébergement par classe de données"], ["Sobriété", "Durées de vie, plan de retrait, indicateur de consommation"]]),
    METIERS3(("Responsable des données", "Mesurer la qualité. Refuser un modèle sur des données non fiabilisées."), ("Directeur de métier", "Rester propriétaire de ses données et des décisions prises avec l'aide d'un modèle."),
             ("Consultant", "Ramener toute demande de technique à une capacité et à une mesure.")),
    EX("Cinq conditions", "25 minutes, en binôme", "La BANQUE SANAGA veut un modèle qui note les demandes de crédit des particuliers.", ["Appliquez les cinq conditions", "Laquelle vous paraît la plus difficile à remplir ?", "Que doit dire la fiche de projet ?"],
       "Corrigé indicatif. La preuve est la plus difficile : expliquer une note à la personne concernée. La fiche nomme qui décide et qui surveille la dérive."),
    SY(["Quatre forces : **données, intelligence artificielle, plateformes, sobriété**", "Une donnée de référence a un **propriétaire** et un **système maître**", "Un cas d'usage se juge sur **cinq conditions**",
        "Les **données viennent avant les modèles**", "Un échange qui dépend d'un tiers est une **hypothèse**"]),
    M(["Chapitre C15 en entier", "Exercices 15.1 (les doublons) et 15.4 (LiZbiZ plateforme)"]),
    F("Jour 15 · Auditer un schéma directeur, mesurer l'alignement", ["L'objet, le critère, la preuve", "µ, U, H", "L'indice d'alignement prouvé"]),
]
