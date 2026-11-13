import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h import *

SPEC = [
    T("Jour 15 / 15 · Séance de 2 heures", "Auditer un schéma directeur\nMesurer l'alignement", "« L'absence de preuve n'est pas la preuve de l'absence. » Règle du chapitre", "Partie VI · Chapitre C16"),
    R("Jour 14 · Données, intelligence artificielle, plateformes, sobriété", ["Une donnée de référence a un **propriétaire**", "Cinq conditions pour un cas d'usage : objectif, données, décision, preuve, exploitation",
        "Les **données viennent avant les modèles**", "Retirer avant d'ajouter"]),
    A([("15 min", "**Trois moments** d'audit"), ("20 min", "**L'objet, le critère, la preuve**"), ("25 min", "**Trois mesures** : µ, U, H"),
       ("15 min", "**Lire par domaine**, mesurer l'alignement"), ("15 min", "**Le rapport** et la clôture du cours"), ("30 min", "**Exercice** en séance · synthèse")]),
    C("C16", "Chapitre 16", "PARTIE VI · DÉFIS ET RECHERCHE", "Auditer un schéma directeur, mesurer l'alignement", "« Donnez-moi une note sur vingt. »"),
    O(["Distinguer les **trois moments** d'audit", "Écrire une **exigence** vérifiable par une pièce", "Coter OUI, NON ou NEK et **qualifier** un NEK",
       "Calculer et lire ensemble **µ, U et H**", "Calculer un **indice d'alignement prouvé**", "Structurer un **rapport** d'audit"]),
    TB("Trois moments, trois questions", "Tableau 16.1 du livre", ["Moment", "Question", "Pièces"], [2.8, 3.8, 4.8], [
        ["Avant l'approbation", "Le document est-il exécutable ?", "Document, note de cadrage, diagnostic, fiches, plan de financement"],
        ["Pendant l'exécution", "Est-il exécuté et piloté ?", "Procès-verbaux, tableau de bord, registres, marchés"], ["À l'échéance", "A-t-il produit ce qu'il promettait ?", "Mesures de départ et d'arrivée, comptes"]]),
    K("L'objet, le critère, la preuve", "Le programme de l'auditologie", [("O", "L'objet est délimité", "Un document daté, une période, un périmètre."), ("C", "Le critère préexiste", "Un texte, une norme, un engagement ou une règle de l'art reconnue."),
        ("P", "La preuve est une pièce", "Un document, un enregistrement, une observation consignée.")]),
    D("Trois cotes", "Sans pièce, la cote est NEK", [("OUI et NON", "La preuve montre que l'exigence est satisfaite, ou qu'elle ne l'est pas."),
        ("NEK", "L'auditeur ne peut pas conclure. **De preuve** quand la pièce manque. **De critère** quand l'exigence ne peut pas s'appliquer à cet objet.")]),
    TB("Le référentiel de l'ANPP", "Tableau 16.2 du livre · 48 exigences, huit domaines, cinq sources", ["Source", "Exemple d'exigence", "Exigences"], [3.4, 6.6, 1.6], [
        ["Textes", "Le document est approuvé par l'organe compétent", "9"], ["Normes de gouvernance", "L'organe de gouvernance surveille l'exécution", "8"],
        ["Engagements", "Chaque projet sert un objectif du plan stratégique", "7"], ["Règles de l'art", "Chaque projet affiche son coût annuel", "19"], ["Cohérence interne", "Le total des fiches égale le total du plan", "5"]]),
    D("Trois mesures", "Elles se lisent ensemble", [("µ et U", "**µ** = OUI / n : la part du prouvé. **U** = NEK / n : la part de ce que l'auditeur ignore."),
        ("H", "L'entropie de Shannon des trois cotes. Elle vaut 0 quand toutes les cotes sont identiques, 1,58 au plus quand elles sont à égalité.")]),
    S4("L'audit du 20 juin 2025", "Schéma directeur 2025-2029 de l'ANPP, avant approbation", [("37 / 7 / 4", "OUI, NON, NEK sur 48 exigences"), ("0,771", "µ : plus des trois quarts prouvés"), ("0,083", "U : le document est connu à 92 %"), ("0,99", "H, en bits")],
        "Les quatre NEK sont de preuve. Les sept NON se concentrent sur le chiffrage et sur les fiches."),
    TB("Lire par domaine", "Tableau 16.3 du livre", ["Domaine", "Exigences", "OUI", "NON", "NEK", "µ"], [4.4, 1.6, 1.1, 1.1, 1.1, 1.3], [
        ["Cadrage", "6", "5", "0", "1", "0,83"], ["Diagnostic", "6", "5", "1", "0", "0,83"], ["Cible", "6", "6", "0", "0", "1,00"], ["Portefeuille", "6", "5", "1", "0", "0,83"],
        ["Chiffrage et financement", "7", "3", "3", "1", "0,43"], ["Pilotage", "6", "5", "0", "1", "0,83"], ["Maîtrise des risques", "6", "4", "2", "0", "0,67"], ["Cadre juridique", "5", "4", "0", "1", "0,80"]], 14),
    CP("Mesurer l'alignement", "Deux mesures qui se complètent", "Luftman, 2000", ["Six critères, cinq niveaux", "Repose sur l'opinion de dirigeants interrogés", "Capte une **perception**"],
       "L'indice d'alignement prouvé", ["Huit exigences qui relient le système d'information à la stratégie", "Six OUI sur huit en juin 2025 : **0,75**", "Un OUI sur huit pour le document de 2019 : 0,125"],
       "L'indice ne dit pas que le système est aligné. Il dit que le dispositif qui doit produire l'alignement existe et qu'il est prouvé."),
    ST("Le rapport d'audit", "Dix pages, un ordre constant", [("1", "L'objet, le périmètre, la date, le référentiel."), ("2", "Les trois mesures, pour l'ensemble et par domaine."), ("3", "Les NON : fait, pièce, conséquence, recommandation."),
        ("4", "Les **NEK** : la pièce attendue et qui doit la produire."), ("5", "L'avis.")]),
    SC("« Une note sur vingt »", "ANPP · 20 juin 2025", ["M. TCHUENTE, président du conseil, reçoit l'auditeur interne six jours avant le conseil. Il veut savoir si le document est bon.",
        "L'auditeur pose trois nombres : 37 exigences prouvées, 7 non satisfaites, 4 non vérifiées.", "« Je peux vous dire ce qui est établi, ce qui manque et ce que j'ignore. Une note unique mélangerait les trois. »"],
        "L'auditeur avait siégé au groupe de travail finances : le rapport le signale en première page. On n'audite pas son propre travail."),
    EX("Trois mesures", "25 minutes, en binôme", "Un audit de 20 exigences donne 12 OUI, 5 NON et 3 NEK.", ["Calculez µ, U et H", "Rédigez l'avis en trois phrases", "Que changerait un U de 0,35 ?"],
       "Corrigé. µ = 0,60, U = 0,15, H = 1,35. Avec U = 0,35, l'avis est suspendu à la production des pièces."),
    K("Quatre pistes de recherche", "Pour un mémoire", [("1", "Le devenir des schémas directeurs", "Combien de documents adoptés sont exécutés à plus de moitié ? Aucune mesure publiée."), ("2", "Perception et preuve", "L'indice prouvé et la maturité de Luftman classent-ils de la même façon ?"),
        ("3", "Le paradoxe de la productivité", "La question de Solow reste ouverte pour les administrations d'Afrique centrale."), ("4", "L'informatique hors contrôle", "Quelle part de l'activité réelle repose sur des outils non recensés ?")], 2),
    SY(["Trois moments d'audit : **avant, pendant, à l'échéance**", "Un audit compare **un objet à un critère au moyen d'une preuve**", "**µ** mesure le prouvé, **U** l'ignoré, **H** la dispersion",
        "Les résultats se lisent **par domaine**", "Le rapport **publie les NEK**"]),
    M(["Chapitre C16 en entier et Annexe D", "Exercices 16.2 (réécrire) et 16.5 (l'audit à l'échéance)"]),
    F("Fin du cours · Épreuve de synthèse", ["Un schéma directeur se juge à son exécution", "Chaque livrable se contrôle sur pièces", "Ce que l'on ignore se dit"], "Merci pour ces quinze séances · questions ?", "CLÔTURE"),
]
