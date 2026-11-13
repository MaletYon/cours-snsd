import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h import *

SPEC = [
    T("Jour 13 / 15 · Séance de 2 heures", "Risques, sécurité, continuité, conformité", "« Un plan de continuité qui n'a pas été essayé n'existe pas. »", "Partie V · Chapitre C14"),
    R("Jour 12 · Piloter l'exécution", ["Une **cellule de portefeuille** mesure sans conduire", "Indice de délai **0,60**, indice de coût **0,89** à la première revue", "Un bénéfice a un **propriétaire** dans le métier", "Révision **annuelle**, avant le budget"]),
    A([("15 min", "**Deux sortes de risques**"), ("20 min", "**Le registre des risques** du schéma directeur"), ("15 min", "**La sécurité**"),
       ("25 min", "**La continuité** : le bilan d'impact"), ("15 min", "**La conformité** et les projets"), ("30 min", "**Exercice** en séance · synthèse")]),
    C("C14", "Chapitre 14", "PARTIE V · MISE EN ŒUVRE", "Risques, sécurité, continuité, conformité", "« Quatre jours. »"),
    O(["Distinguer les risques **du** schéma directeur de ceux qu'il **traite**", "Écrire un risque en **trois parties** et le coter", "Dire ce que le schéma directeur apporte à la **sécurité**",
       "Conduire un **bilan d'impact** sur l'activité", "Tirer un **registre de conformité** de la carte d'applicabilité", "Citer quatre **parades** à l'échec des projets"]),
    D("Deux sortes de risques", "ISO 31000 : l'effet de l'incertitude sur les objectifs", [("Les risques du schéma directeur", "Ce qui peut empêcher de l'exécuter. Ils se gèrent dans le **pilotage**."),
        ("Les risques qu'il traite", "Ceux qui pèsent sur le système d'information. Ils commandent une partie du **portefeuille**.")]),
    TB("Le registre des risques", "Tableau 14.1 du livre · seuil d'attention à 12", ["N°", "Risque", "P", "I", "C", "Traitement"], [0.8, 5.0, 0.7, 0.7, 0.8, 3.4], [
        ["R1", "Subvention non inscrite en loi de finances", "4", "4", "16", "Scénario de repli"], ["R2", "Reprise des onze fichiers défaillante", "4", "4", "16", "Fiabilisation avant reprise"],
        ["R3", "Départ des deux agents de la liquidation", "3", "5", "15", "Documentation, binômes"], ["R4", "Marché du secours infructueux", "3", "4", "12", "Consultation préalable"],
        ["R5", "Postes non autorisés", "3", "4", "12", "Saisine de la tutelle"], ["R6", "Refus du fichier unique par les antennes", "3", "3", "9", "Antennes pilotes"]], 14,
        note="Un risque s'écrit : une cause, un événement, une conséquence. Quatre traitements : éviter, réduire, transférer, accepter."),
    K("Ce que le schéma directeur donne à la sécurité", "ISO/IEC 27001 · loi n° 2010/012", [("O", "Une organisation", "Un responsable de la sécurité rattaché au directeur général."), ("B", "Un budget", "Une ligne propre : 6 % de la dépense informatique annuelle dès 2026."),
        ("R", "Une règle de projet", "Chaque fiche comporte une analyse de risque de sécurité et son coût."), ("C", "Un calendrier", "Audit obligatoire, tests d'intrusion, revues d'habilitations sur cinq ans.")], 2),
    D("Deux mesures de continuité", "ISO 22301 · le bilan d'impact sur l'activité", [("Durée maximale d'interruption admissible", "Délai au-delà duquel l'arrêt cause un dommage inacceptable. Elle fixe le **temps pour redémarrer**."),
        ("Perte de données maximale admissible", "Ancienneté maximale des données retrouvées. Elle fixe la **fréquence des sauvegardes** ou de la réplication.")]),
    TB("Le bilan d'impact de l'ANPP", "Tableau 14.2 du livre", ["Activité", "Interruption admissible", "Perte admissible", "Constat de mars 2024"], [3.4, 2.6, 2.4, 3.2], [
        ["Paiement des prestations", "4 heures", "1 heure", "4 jours, 11 jours de données"], ["Encaissement (e-RECETTES)", "8 heures", "1 heure", "Aucun secours"],
        ["Liquidation des droits", "2 jours", "1 jour", "4 jours"], ["Comptabilité", "5 jours", "1 jour", "4 jours"]],
        note="Quatre heures d'interruption admissible imposent un second site et une réplication. Voilà pourquoi le secours coûte 620 millions."),
    TB("Le registre de conformité", "Tableau 14.3 du livre (extrait)", ["Exigence", "Source", "État en 2025", "Projet"], [3.6, 2.8, 2.8, 2.4], [
        ["Audit de sécurité", "Loi n° 2010/012", "Non réalisé depuis 2020", "Obligatoire n° 2"], ["Formalités des traitements", "Loi n° 2024/017", "Non engagées", "Obligatoire n° 3"],
        ["Engagements et paiements", "Loi n° 2018/012", "Conforme", "Plan de financement"], ["Approbation par le conseil", "Loi n° 2017/010", "Conforme", "Délibération"]],
        note="La carte d'applicabilité devient un registre. La conformité se construit dans les projets, dès la conception."),
    K("Quatre parades à l'échec des projets", "Elles relèvent du schéma directeur", [("T", "La taille", "Aucun lot ne dépasse deux ans ni 800 millions."), ("J", "Le jalon d'arrêt", "Un point où le comité décide de poursuivre ou non."),
        ("C", "La coexistence", "L'ancien système reste en service jusqu'à la recette du nouveau."), ("R", "Le regard extérieur", "Une revue indépendante annuelle des trois projets les plus lourds.")], 2),
    SC("Quatre jours", "ANPP · mars 2024", ["Un onduleur de la salle des serveurs cède un mardi à 14 heures. La base des paiements est corrompue.", "La dernière sauvegarde utilisable date de **onze jours**. Les paiements partent avec **quatre jours** de retard.",
        "Le schéma directeur de 2019 prévoyait un plan de secours : le projet n° 17. Il n'avait jamais démarré, faute de budget."], "Personne n'avait écrit ce que coûterait son absence."),
    METIERS3(("Responsable de la sécurité", "Tenir la politique, programmer les audits, viser les fiches de projet."), ("Responsable de la continuité", "Conduire le bilan d'impact avec les métiers. Organiser l'exercice annuel."),
             ("Directeur de métier", "Dire combien de temps il peut tenir sans son système. Signer sa réponse.")),
    EX("Le bilan d'impact", "25 minutes, en binôme", "Pour l'activité « paiement des prestations » : quatre heures d'interruption, une heure de perte.",
       ["Pourquoi la sauvegarde quotidienne est-elle exclue ?", "Quelles solutions restent ?", "Quelle pièce prouve que le plan fonctionne ?"],
       "Corrigé. Une sauvegarde quotidienne peut faire perdre vingt-quatre heures. Restent la réplication et un second site prêt. La pièce : le compte rendu signé du dernier exercice."),
    SY(["Deux sortes de risques : ceux **du** schéma directeur, ceux qu'il **traite**", "Un risque : **cause, événement, conséquence**, et un propriétaire", "La sécurité reçoit une organisation, un budget, une règle, un calendrier",
        "Le **bilan d'impact** fixe l'interruption et la perte admissibles", "La carte d'applicabilité devient un **registre de conformité**"]),
    M(["Chapitre C14 en entier", "Exercices 14.1 (coter) et 14.3 (accepter)"]),
    F("Jour 14 · Données, intelligence artificielle, plateformes, sobriété", ["Gouverner une donnée", "Cinq conditions pour un cas d'usage", "Échanges, hébergement, durée de vie"]),
]
