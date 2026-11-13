import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h import *

SPEC = [
    T("Jour 11 / 15 · Séance de 2 heures", "Chiffrer, financer, acheter, doter", "« Un plan sans ressources est un vœu. » Principe du cours", "Partie IV · Chapitre C12"),
    R("Jour 10 · Portefeuille et trajectoire", ["**22 projets** retenus pour 4 180 millions", "Cinq **obligatoires**, onze différés, sept rejetés", "Trois lots pour la refonte, **six projets** au plus à la fois", "Un pic de dépense en **2027**"]),
    A([("20 min", "**Le coût complet** et l'estimation"), ("20 min", "**La valeur actuelle nette** et ses limites"), ("20 min", "**Engager, payer, financer**"),
       ("15 min", "**Faire, acheter, louer**"), ("15 min", "**Doter** : les compétences"), ("30 min", "**Exercice** en séance · synthèse")]),
    C("C12", "Chapitre 12", "PARTIE IV · MÉTHODE", "Chiffrer, financer, acheter, doter", "« Qui paiera ensuite ? »"),
    O(["Calculer le **coût complet** d'un projet", "Donner une estimation avec sa **fourchette** et sa provision", "Calculer une **valeur actuelle nette**",
       "Présenter un projet en **engagements et paiements**", "Établir un plan de financement avec un **scénario de repli**", "Choisir entre **faire, acheter et louer**"]),
    TB("Les cinq postes du coût complet", "Tableau 12.1 du livre", ["Poste", "Contenu"], [3.0, 8.4], [
        ["Investissement", "Logiciels, matériels, intégration, reprise des données, formation"], ["Charges internes", "Temps des agents affectés au projet"],
        ["Fonctionnement", "Maintenance, licences, hébergement, liaisons, énergie"], ["Renouvellement", "Remplacement des matériels, montées de version"], ["Sortie", "Reprise des données et retrait en fin de vie"]],
        note="Référentiel des bénéficiaires : 340 millions d'investissement, puis 48 millions par an dès 2027. Coût complet sur la période : 484 millions."),
    P("Estimer", "Chapitre 12, section 12.2", ["Trois méthodes : l'**analogie**, le **détail**, le **prix de marché**", "En phase de schéma directeur, une fourchette de **plus ou moins 30 %** est honnête",
        "L'incertitude se couvre par une **provision pour aléas**", "L'ANPP prévoyait 20 millions de marge. Le cabinet propose **8 %** des projets non obligatoires"]),
    D("La valeur actuelle nette", "Un franc reçu dans cinq ans vaut moins qu'un franc reçu aujourd'hui", [("Le calcul", "Guichet unique : 180 millions, gain net de 55 millions par an pendant cinq ans. À 8 %, les gains valent 219,6 millions. **VAN = 39,6 millions**."),
        ("La limite", "La plupart des bénéfices d'une administration ne sont pas des recettes. Ward et Daniel les classent : financiers, quantifiables, mesurables, **observables**.")]),
    TB("Engager et payer", "Tableau 12.2 du livre · lot 2, liquidation, en millions", ["", "2026", "2027", "2028", "Total"], [4.8, 1.6, 1.6, 1.6, 1.8], [
        ["Autorisations d'engagement", "780", "", "", "780"], ["Crédits de paiement", "150", "420", "210", "780"]],
        note="L'engagement est pris en totalité, sans quoi le marché ne peut pas être signé. Les paiements suivent les livraisons."),
    TB("Le plan de financement", "Tableau 12.3 du livre", ["Ressource", "Montant (millions)", "Condition"], [4.6, 2.4, 4.4], [
        ["Ressources propres de l'Agence", "2 300", "Délibération annuelle du conseil"], ["Subvention d'investissement de l'État", "1 200", "Inscription en loi de finances"],
        ["Partenaire technique et financier", "680", "Convention à signer"], ["Total", "4 180", ""]],
        note="Une ressource est acquise, demandée ou espérée. Le scénario de repli ramène le portefeuille à 2 300 millions."),
    S4("Le fonctionnement de 2029", "Ce que le conseil doit savoir le jour où il approuve", [("+310", "millions de charges annuelles des nouveaux systèmes"), ("−85", "millions libérés par le retrait de neuf applications"), ("+225", "millions de fonctionnement annuel en plus"), ("2", "chiffres approuvés : l'enveloppe et le fonctionnement à terme")]),
    TB("Faire, acheter, louer", "Tableau 12.4 du livre · Coase 1937, Williamson 1975", ["Voie", "Convient quand", "Point de vigilance"], [1.8, 5.0, 4.6], [
        ["Faire", "Le besoin est propre à l'organisation et au cœur du métier", "Dépendance à quelques agents"], ["Acheter", "Un produit du marché couvre le besoin commun", "Coût des adaptations, dépendance à l'éditeur"],
        ["Louer", "Le besoin varie ou l'investissement est impossible", "Lieu des données, réversibilité, charge récurrente"]]),
    TB("Le plan de dotation", "Tableau 12.5 du livre · la division passe de 19 à 27 agents", ["Compétence", "Postes", "Voie"], [4.6, 1.6, 5.2], [
        ["Responsable de la sécurité", "1", "Recrutement en 2025"], ["Chefs de projet", "2", "Un recrutement, une mobilité interne"], ["Architecte", "1", "Recrutement en 2026"],
        ["Données", "3", "Deux recrutements, une reconversion"], ["Acheteur informatique", "1", "Mobilité depuis les marchés"]]),
    SC("Vingt-deux voitures", "Mission ANPP · 27 mai 2025", ["M. ABDOULAYE additionne les investissements : 4 180 millions. Neuf fiches n'ont pas de coût annuel.",
        "« Vous me demandez d'approuver l'achat de vingt-deux voitures sans me dire ce qu'elles consomment. »", "Le cabinet reprend les neuf fiches. En 2029, l'Agence paiera **225 millions de plus** chaque année."],
        "Avec la provision de 242 millions, le total atteint 4 422 millions. Le comité retire deux projets."),
    METIERS3(("Directeur financier", "Qualifier chaque ressource. Refuser un plan dont tout le financement est espéré."), ("Acheteur", "Traduire le portefeuille en marchés. Écrire les clauses de réversibilité."),
             ("Consultant", "Donner des fourchettes. Écrire le scénario de repli sans attendre qu'on le demande.")),
    EX("Valeur actuelle nette", "25 minutes, en binôme", "Un projet coûte 120 millions et procure 40 millions de gain net par an pendant quatre ans.", ["Calculez la valeur actuelle nette au taux de 8 %", "Refaites le calcul au taux de 15 %", "Que concluez-vous ?"],
       "Corrigé. À 8 % : 132,5 moins 120, soit 12,5 millions. À 15 % : 114,2 moins 120, soit moins 5,8 millions. Le taux se fixe avant de calculer."),
    SY(["Le **coût complet** ajoute le fonctionnement, le renouvellement et la sortie", "Une estimation se donne avec une **fourchette** et une provision", "Un projet public se présente en **engagements et paiements**",
        "Une ressource est **acquise, demandée ou espérée**", "Le conseil approuve **l'enveloppe et le fonctionnement** à terme"]),
    M(["Chapitre C12 en entier", "Exercices 12.3 (la provision) et 12.4 (le repli)"]),
    F("Jour 12 · Piloter l'exécution", ["La cellule de portefeuille", "La valeur acquise", "Bénéfices, imprévus, révision annuelle"]),
]
