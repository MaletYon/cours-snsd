import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h import *

SPEC = [
    T("Jour 6 / 15 · Séance de 2 heures", "La stratégie numérique du Cameroun\nLe cadre juridique d'un schéma directeur", "« Un document attendu ne se cite pas comme un document en vigueur. »", "Partie III · Chapitres C06 et C07"),
    R("Jour 5 · Doctrines et stratégies numériques", ["**OCDE 2014**, **Pacte numérique mondial 2024** : des références, non des obligations", "**Infrastructure publique numérique** : identité, paiement, échange de données",
        "Les textes de l'Union africaine passent par le **droit national**", "RACINES : cinq étapes, trois instances"]),
    A([("20 min", "**Les documents d'orientation** du Cameroun"), ("15 min", "**Le plan 2026-2030** : état et contenu"), ("10 min", "**Les acteurs** et le rattachement stratégique"),
       ("35 min", "**Cinq familles de règles** : numérique, finances, organisation, achat, secteur"), ("10 min", "**La carte d'applicabilité**"), ("30 min", "**Exercice** en séance · synthèse")]),
    C("C06", "Chapitre 6", "PARTIE III · LE CONTEXTE NATIONAL", "La stratégie numérique du Cameroun", "« Conformément au plan Cameroun numérique 2026-2030, l'ANPP poursuit sa transformation. »"),
    O(["Situer la **Vision 2035**, la **SND30** et le plan Cameroun numérique 2020", "Dire l'**état exact** du plan 2026-2030", "Citer les **acteurs publics** du numérique",
       "**Rattacher** un schéma directeur en six points", "Dire ce que le **droit** impose au financement, à l'approbation et à l'achat", "Dresser une **carte d'applicabilité**"]),
    TB("Les documents d'orientation", "Tableau 6.1 du livre", ["Document", "Date", "État"], [5.6, 3.0, 2.8], [
        ["Cameroun Vision 2035", "2009", "En vigueur"], ["Plan stratégique Cameroun numérique 2020", "Mai 2016", "Échu"], ["Stratégie nationale de développement, SND30", "2020-2030", "En vigueur"],
        ["Stratégie nationale d'intelligence artificielle", "Juillet 2025", "Présentée"], ["Plan national de santé numérique", "2024-2028", "En vigueur, sectoriel"],
        ["Plan de développement de l'économie numérique", "2026-2030", "Déposé, en validation"]]),
    D("Le plan 2026-2030", "L'état exact à la date du cours", [("Son état", "Le Plan de développement de l'économie numérique au Cameroun 2026-2030 est **finalisé et déposé**. Il est en cours de validation dans les services du Premier ministre. Il n'est **pas en cours de mise en œuvre**."),
        ("La conduite", "Le schéma directeur le mentionne dans ces termes, se rattache à la **SND30** et prévoit de se réviser à l'approbation du plan.")]),
    TB("Ce que contient le projet de plan", "Tableau 6.3 du livre", ["Élément", "Contenu"], [2.8, 8.6], [
        ["Constat", "Le plan Cameroun numérique 2020 a connu un taux d'exécution très faible, pour cinq causes"], ["Cinq piliers", "Infrastructures, plateformes, services financiers numériques, entrepreneuriat, compétences"],
        ["Quatre axes", "Gouvernance, cadre juridique et institutionnel, exploitation, utilisation"], ["Mise en œuvre", "Un comité interministériel, puis une agence nationale de l'économie numérique"],
        ["Financement", "Fonds d'investissement, partenariats public-privé, alliances, subventions"]], 14),
    ST("Rattacher un schéma directeur", "Six points, une page en tête du document", [("1", "Le texte qui crée l'organisation et fixe ses missions."), ("2", "Le programme budgétaire."), ("3", "La stratégie du secteur, si elle existe."),
        ("4", "La SND30 et l'objectif concerné."), ("5", "Les documents attendus, avec leur état exact."), ("6", "Le tout en une page.")]),
    C("C07", "Chapitre 7", "PARTIE III · LE CONTEXTE NATIONAL", "Le cadre juridique d'un schéma directeur", "« Nous lancerons le projet en mars. »"),
    TB("Cinq familles de règles", "Tableau 7.1 du livre", ["Famille", "Textes principaux", "Question"], [2.2, 5.6, 3.6], [
        ["Numérique", "Lois n° 2010/012, 2010/013, 2010/021, 2024/017", "Que peut-on traiter, échanger ?"], ["Finances", "Lois n° 2018/011 et 2018/012", "Comment inscrire une dépense pluriannuelle ?"],
        ["Organisation", "Lois n° 2017/010 et 2017/011", "Qui approuve ?"], ["Achat", "Décrets n° 2018/366 et 2018/355", "Comment acquérir ?"], ["Secteur", "CEMAC, COBAC, OHADA", "Que demande le superviseur ?"]], 14),
    CP("Engager, payer, approuver", "Finances publiques et organes", "Loi n° 2018/012", ["Les **autorisations d'engagement** permettent de s'engager sur plusieurs années", "Les **crédits de paiement** limitent ce qui est payé dans l'année", "Un projet se rattache à un **programme** et à ses indicateurs"],
       "Lois n° 2017/010 et 2017/011", ["Le **conseil d'administration** approuve budgets et plans", "Le directeur général exécute", "Un document approuvé par la seule informatique n'engage pas les budgets"]),
    P("Ce que le code des marchés change", "Décret n° 2018/366 du 20 juin 2018", ["**Le délai** : plusieurs mois entre la décision et la notification", "**L'allotissement** : le fractionnement pour éviter une procédure est interdit",
        "**La programmation** : un projet absent de la programmation ne peut pas être lancé", "**Le besoin** se décrit par ses fonctions : le schéma directeur **ne nomme pas de produit**"]),
    TB("La carte d'applicabilité", "Tableau 7.3 du livre (extrait)", ["Texte", "ANPP", "LiZbiZ", "BANQUE SANAGA"], [5.0, 2.2, 2.0, 2.4], [
        ["Loi n° 2024/017, données personnelles", "Oui", "Oui", "Oui"], ["Loi n° 2018/012, régime financier", "Oui", "Non", "Non"], ["Décret n° 2018/366, marchés publics", "Oui", "Non", "Non"],
        ["Actes uniformes de l'OHADA", "Non", "Oui", "Oui"], ["Règlements de la COBAC", "Non", "Non", "Oui"], ["Règlements de paiement de la CEMAC", "Si mobile", "Non", "Oui"]]),
    SC("« Votre mars est un mars 2026 »", "Mission ANPP · 12 février 2025", ["Le directeur des prestations veut un tableau de bord des paiements « pour mars ».",
        "La dépense n'est pas inscrite au budget 2025. Le marché ne figure pas à la programmation.", "M. ABDOULAYE fait le compte : inscription, délibération, appel d'offres, commission, notification."],
        "Trois délais avant le démarrage : inscription budgétaire, programmation du marché, passation."),
    EX("Carte d'une université", "20 minutes, en binôme", "Dressez la carte d'applicabilité d'une université d'État qui veut un schéma directeur numérique.",
       ["Quels textes des cinq familles s'appliquent ?", "Pour trois d'entre eux, quelle exigence et quelle pièce ?", "Qui approuve le document ?"],
       "Corrigé indicatif. Lois 2010/012, 2024/017, 2018/012, code des marchés, texte organique. Pièces : tableau des engagements et paiements, plan d'achat, registre des traitements."),
    SY(["La **SND30** est en vigueur. Le plan 2026-2030 est **déposé, en validation**", "Aucun texte général n'impose un schéma directeur : l'obligation vient des textes organiques",
        "Engagements et paiements : **loi n° 2018/012**. Approbation : **le conseil**", "Le code des marchés impose des délais et interdit de **nommer un produit**", "La **carte d'applicabilité** se dresse texte par texte et se date"]),
    M(["Chapitres C06 et C07 en entier", "Exercices 6.2 (une page) et 7.2 (engagement et paiement)"]),
    F("Jour 7 · Cadrer et gouverner la démarche", ["Six questions, une note signée", "Qui préside le comité de pilotage", "Parties prenantes et responsabilités"]),
]
