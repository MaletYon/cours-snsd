import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h import *

SPEC = [
    T("Jour 9 / 15 · Séance de 2 heures", "Fixer la cible", "« Il n'est pas de vent favorable pour celui qui ne sait où il va. » Sénèque", "Partie IV · Chapitre C10"),
    R("Jour 8 · Diagnostiquer l'existant", ["**47 applications** trouvées pour 31 déclarées", "**Quatorze** à refondre, **neuf** à retirer", "**22 %** de la dépense va aux projets", "Un constat : le fait, la pièce, la conséquence"]),
    A([("20 min", "**Des objectifs aux capacités**"), ("20 min", "**Les principes directeurs**"), ("20 min", "**Les quatre plans** et le plan fonctionnel"),
       ("10 min", "**L'analyse des écarts**"), ("20 min", "**Comparer des scénarios**"), ("30 min", "**Exercice** en séance · synthèse")]),
    C("C10", "Chapitre 10", "PARTIE IV · MÉTHODE", "Fixer la cible", "« Il nous faut un progiciel intégré. »"),
    O(["Déduire des **capacités** à partir d'objectifs", "Rédiger un **principe directeur** avec ses conséquences", "Décrire une architecture sur **quatre plans**",
       "Rapprocher un **plan fonctionnel** d'un inventaire", "Conduire une **analyse des écarts**", "Comparer des **scénarios** sur une grille pondérée"]),
    TB("Des objectifs aux capacités", "Tableau 10.1 du livre", ["Objectif du plan stratégique 2024-2028", "Capacité demandée au système d'information"], [4.6, 6.8], [
        ["Payer chaque prestation à date fixe", "Liquider et payer sans interruption, y compris en cas de sinistre"], ["Ne payer que les ayants droit", "Tenir un fichier unique des bénéficiaires, rapproché de l'état civil"],
        ["Rapprocher l'Agence des bénéficiaires", "Recevoir et suivre une demande depuis une antenne ou un téléphone"], ["Rendre compte de chaque franc", "Produire la dépense par programme et par antenne"]],
        note="Une capacité se formule par un verbe et un résultat. Elle ne nomme ni un logiciel ni une technique."),
    TB("Six principes directeurs", "Tableau 10.2 du livre · un principe vaut par ses conséquences", ["Nom", "Énoncé", "Conséquence acceptée"], [2.8, 4.4, 4.2], [
        ["Donnée unique", "Un bénéficiaire est enregistré une seule fois", "Les antennes renoncent à leurs fichiers"], ["Acheter avant de construire", "Un besoin commun se couvre par le marché", "Le métier adapte ses usages"],
        ["Secours d'abord", "Aucune application clé sans reprise éprouvée", "Pas de projet sans budget de secours"], ["Propriétaire désigné", "Chaque application a un responsable métier", "Un directeur signe"],
        ["Ouverture", "Les échanges emploient des formats publics", "Certains produits sont écartés"], ["Sobriété", "On retire avant d'ajouter", "Tout projet nomme ce qu'il remplace"]], 14),
    TB("Les quatre plans", "Tableau 10.3 du livre", ["Plan", "Contenu", "Qui le lit"], [2.4, 5.0, 4.0], [
        ["Métier", "Processus, acteurs, événements", "Les directions de métier"], ["Fonctionnel", "Blocs de fonctions, indépendants des logiciels", "L'équipe projet"],
        ["Applicatif", "Logiciels, données, échanges", "La fonction informatique"], ["Technique", "Serveurs, réseaux, sites, hébergement", "L'exploitation"]]),
    K("Le plan fonctionnel cible de l'ANPP", "Cinq zones · 11 avril 2025", [("1", "Référentiels", "Bénéficiaires, employeurs, barèmes. Zone maîtresse des données communes."), ("2", "Production", "Immatriculation, liquidation, paiement, recouvrement."),
        ("3", "Relation", "Guichet, téléphone, demandes en ligne, réclamations."), ("4", "Soutien", "Comptabilité, budget, ressources humaines, achats."), ("5", "Pilotage", "Tableaux de bord, statistiques, contrôle."),
        ("!", "Le rapprochement", "Sept blocs couverts deux fois ou plus. Quatre blocs vides, dont le référentiel des bénéficiaires.")]),
    TB("Trois scénarios", "Tableau 10.5 du livre", ["", "A. Consolider", "B. Refondre par étapes", "C. Remplacer d'un bloc"], [2.8, 2.8, 3.0, 3.0], [
        ["Principe", "Sécuriser, différer la refonte", "Secours, puis refonte en trois lots", "Progiciel intégré unique"], ["Ordre de grandeur", "1,9 milliard", "4,2 milliards", "7,5 milliards"],
        ["Capacités en 2029", "1 sur 4", "4 sur 4", "4 sur 4"], ["Risque principal", "L'application de 2004 cède", "Coexistence ancien et nouveau", "Échec d'un projet unique"]], 14),
    TB("La notation des scénarios", "Tableau 10.6 du livre · critères et poids fixés avant de noter", ["Critère", "Poids", "A", "B", "C"], [5.0, 1.4, 1.4, 1.4, 1.4], [
        ["Contribution aux quatre objectifs", "40 %", "2", "4", "5"], ["Soutenabilité financière", "25 %", "5", "3", "1"], ["Capacité de l'Agence à conduire", "20 %", "5", "3", "1"],
        ["Maîtrise du risque", "15 %", "2", "4", "2"], ["Note pondérée", "", "3,35", "3,55", "2,75"]],
        note="Le comité retient B le 25 avril : A laissait trois objectifs sans réponse. La grille éclaire, elle ne décide pas."),
    P("Le dossier de cible", "Quinze pages", ["Les capacités, les principes, le plan fonctionnel, le scénario retenu et ses motifs, la liste des chantiers",
        "Ni calendrier ni budget détaillé : ils viennent aux deux phases suivantes", "La cible porte aussi sur l'**organisation** : un responsable de la sécurité, une cellule des données, un propriétaire par application",
        "**Aucun produit** n'y est nommé"]),
    SC("« Refaisons tout d'un coup »", "Mission ANPP · 24 mars 2025", ["M. ABDOULAYE arrive avec la plaquette d'un éditeur : un progiciel qui couvre « toute la gestion d'un organisme de protection sociale ».",
        "M. BEYALA ne dit pas non. Il demande quelle capacité ce produit apporte, ce qu'il coûte sur cinq ans et qui saurait conduire un projet de cette taille.", "Le produit devient le **scénario C**. Il sera noté comme les autres."],
        "La cible part des objectifs. Une solution proposée en route devient un scénario parmi d'autres."),
    METIERS3(("Architecte d'entreprise", "Tenir le plan fonctionnel. Refuser qu'une fonction appartienne à deux blocs."), ("Directeur de métier", "Formuler des capacités, non des logiciels."),
             ("Consultant", "Présenter des scénarios tous éligibles. Faire fixer les critères avant de noter.")),
    EX("Recalculer", "25 minutes, en binôme", "Recalculez les notes pondérées avec les poids 30 %, 30 %, 20 %, 20 %.", ["Quelle note pour A, pour B, pour C ?", "Le classement change-t-il ?", "Qu'en concluez-vous sur la solidité de la décision ?"],
       "Corrigé. A 3,50, B 3,50, C 2,40. A et B à égalité : la décision tient à l'argument du comité, non à la grille seule."),
    SY(["La cible **se déduit** : objectifs, capacités, principes, architecture", "Une capacité : **un verbe et un résultat**", "Un principe directeur vaut par ses **conséquences**",
        "Le plan fonctionnel révèle **redondances et manques**", "Deux ou trois scénarios **éligibles**, notés sur une grille fixée d'avance"]),
    M(["Chapitre C10 en entier", "Exercices 10.1 (capacité ou solution) et 10.3 (un principe)"]),
    F("Jour 10 · Portefeuille et trajectoire", ["Quarante projets, tous prioritaires", "Trier, équilibrer, ordonner", "Le profil annuel de dépense"]),
]
