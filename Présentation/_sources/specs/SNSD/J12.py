import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h import *

SPEC = [
    T("Jour 12 / 15 · Séance de 2 heures", "Piloter l'exécution", "« Chaque projet avance. C'est le portefeuille qui est en retard. »", "Partie V · Chapitre C13"),
    R("Jour 11 · Chiffrer, financer, acheter, doter", ["Le **coût complet** dépasse l'investissement", "Engagements et paiements, **scénario de repli**", "**+225 millions** de fonctionnement annuel en 2029", "Huit postes : la division passe à 27 agents"]),
    A([("15 min", "**Qui suit** l'exécution"), ("20 min", "**Le tableau de bord**"), ("25 min", "**La valeur acquise**"),
       ("15 min", "**Les bénéfices** et l'adoption"), ("15 min", "**L'imprévu** et la révision annuelle"), ("30 min", "**Exercice** en séance · synthèse")]),
    C("C13", "Chapitre 13", "PARTIE V · MISE EN ŒUVRE", "Piloter l'exécution", "« Tout avance normalement. »"),
    O(["Composer les **instances d'exécution**", "Construire un **tableau de bord** sur quatre axes", "Calculer les indices de **délai** et de **coût**",
       "Tenir un **registre des bénéfices**", "Instruire une **demande hors portefeuille**", "Conduire une **révision annuelle**"]),
    TB("Les instances d'exécution", "Tableau 13.1 du livre", ["Instance", "Composition", "Rythme", "Décide de"], [3.0, 3.6, 2.0, 2.8], [
        ["Conseil d'administration", "Administrateurs", "Chaque année", "Révision, budget"], ["Comité de portefeuille", "Directeur général, directeurs", "Chaque trimestre", "Lancement, arrêt, arbitrage"],
        ["Comité de projet", "Responsable métier, chef de projet, fournisseur", "Chaque mois", "Conduite d'un projet"], ["Cellule de portefeuille", "Deux agents auprès du directeur général", "En continu", "Rien : elle instruit et alerte"]], 14),
    TB("Le tableau de bord", "Kaplan et Norton, 1992 · Tableau 13.2 du livre", ["Axe", "Indicateur", "Cible pour 2029"], [2.4, 6.0, 3.0], [
        ["Bénéficiaires", "Prestations payées à la date prévue", "99 %"], ["Bénéficiaires", "Délai de traitement d'une demande", "15 jours"], ["Finances", "Part des projets dans la dépense", "35 %"],
        ["Processus", "Projets livrés à la date prévue", "70 %"], ["Capacités", "Applications clés avec reprise éprouvée", "Toutes"]],
        note="Un indicateur a une formule, une source, un responsable, une fréquence et une cible."),
    D("La valeur acquise", "ISO 21502", [("Trois montants", "**VP**, valeur planifiée : budget des travaux prévus à la date. **VA**, valeur acquise : budget des travaux achevés. **CR**, coût réel."),
        ("Deux indices", "Indice de délai = VA / VP. Indice de coût = VA / CR. Au-dessous de 1, le portefeuille est en retard ou trop cher.")]),
    S4("La première revue", "ANPP · 30 juin 2026", [("905", "millions de travaux prévus à cette date"), ("540", "millions de travaux achevés"), ("0,60", "indice de délai"), ("0,89", "indice de coût")],
        "Le retard vient de deux marchés : le site de secours, relancé, et le référentiel, notifié avec quatre mois de retard."),
    TB("Le registre des bénéfices", "Ward et Daniel, 2006 · Tableau 13.3 du livre", ["Bénéfice attendu", "Propriétaire", "Mesure de départ", "Cible"], [3.8, 3.2, 2.4, 2.2], [
        ["Paiement à date fixe", "Directeur des prestations", "91 % en 2024", "99 %"], ["Fin des doubles paiements", "Directeur financier", "2 340 cas", "Moins de 200"],
        ["Délai de traitement", "Chefs d'antenne", "47 jours", "15 jours"], ["Économie de contrats", "Cheffe de division", "0", "85 millions"]],
        note="Le bénéfice appartient au métier. Sans mesure de départ, aucun progrès ne se prouve."),
    P("Faire adopter", "Rogers 1962, Davis 1989", ["Choisir des antennes pilotes parmi les **volontaires**", "Montrer d'abord ce que l'outil **épargne** aux agents",
        "Former au poste, sur des **dossiers réels**, la semaine de la mise en service", "À l'ANPP, la formation et l'accompagnement représentent **9 %** de l'investissement"]),
    ST("Instruire une demande hors portefeuille", "Procédure du chapitre", [("Fiche", "Le demandeur remplit une fiche de projet."), ("Note", "La cellule la note et vérifie le plan fonctionnel."),
        ("Décision", "Rejet, attente de la révision ou entrée immédiate."), ("Décalage", "Une entrée nomme le projet qu'elle **décale**."), ("Registre", "La décision est inscrite.")]),
    P("Réviser chaque année", "Avant la préparation du budget", ["Les objectifs de l'organisation ont-ils changé ?", "Qu'a-t-on livré, dépensé, obtenu ?", "Les hypothèses de financement tiennent-elles ?",
        "Que faut-il avancer, décaler, retirer, ajouter ?", "Le comité peut **arrêter** un projet : le lancerions-nous aujourd'hui pour ce qu'il reste à payer ?"]),
    SC("« Avancement conforme »", "ANPP · 30 juin 2026", ["Les chefs de projet présentent leurs fiches. Toutes portent la mention « avancement conforme ».",
        "La cellule de portefeuille distribue une page : sur 905 millions de travaux prévus, **540** sont faits. Le site de secours n'a pas de fournisseur.", "Le directeur général demande pourquoi personne ne l'a dit."],
        "L'avancement se mesure par une instance qui ne conduit aucun projet."),
    METIERS3(("Directeur général", "Présider le comité de portefeuille. Arrêter les projets qui doivent l'être."), ("Responsable de la cellule", "Mesurer sans conduire. Alerter par écrit."),
             ("Directeur de métier", "Mesurer le bénéfice avant le projet. En répondre après.")),
    EX("Deux indices", "20 minutes, en binôme", "Valeur planifiée 1 200 millions, valeur acquise 900, coût réel 1 000.", ["Calculez l'indice de délai", "Calculez l'indice de coût", "Rédigez en deux lignes ce que vous dites au comité"],
       "Corrigé. Indice de délai 0,75. Indice de coût 0,90. Le portefeuille est en retard d'un quart et dépense plus que ce qu'il produit."),
    SY(["Quatre instances, dont une **cellule de portefeuille** indépendante", "Un indicateur a une **source** et une **cible**", "La **valeur acquise** donne deux indices",
        "Un bénéfice a un **propriétaire** et une **mesure de départ**", "Le schéma directeur se révise **chaque année**"]),
    M(["Chapitre C13 en entier", "Exercices 13.2 (un indicateur) et 13.4 (arrêter)"]),
    F("Jour 13 · Risques, sécurité, continuité, conformité", ["Le registre des risques", "Le bilan d'impact sur l'activité", "Le registre de conformité"]),
]
