# Stratégie numérique et schéma directeur SI (SNSD)

[← Tous les cours de MaletYon](https://github.com/maletyon) · [Livre (PDF)](SNSD_main.pdf) · [Présentations](Présentation/) · [Fiches par chapitre](fiches/) · [Corrigés](correction/README.md)

**UE MSN-2S4-MSI01** · Master Professionnel en Management des Systèmes d'Information · Semestre 4 · 3 crédits
Chaire UNESCO d'Afrique Centrale ACCES-TIC, sous la tutelle académique de l'École Nationale Supérieure Polytechnique de l'Université de Yaoundé I
Auteur : MINKA MI NGUIDJOÏ Thierry Emmanuel, enseignant-chercheur (LIMSI, ENSPY) · contact : maletyon@proton.me · année académique 2026-2027

> *Un schéma directeur se juge à son exécution.*

Beaucoup d'organisations possèdent un schéma directeur. Peu l'exécutent. Le cours apprend à en produire un qui tienne : partir de la stratégie de l'organisation, regarder l'existant, fixer une cible, choisir des projets, les ordonner, les financer, puis piloter et réviser. Il présente les théories dans leur texte d'origine (Porter, Barney, Mintzberg, Henderson et Venkatraman, Luftman, Weill et Ross), les normes et les cadres (ISO/IEC 38500, COBIT 2019, TOGAF, ISO 21504, ISO 31000), les doctrines internationales et africaines, puis le contexte camerounais : orientations nationales, finances publiques, marchés publics, textes de la CEMAC et de la COBAC. Chaque livrable est contrôlé par des exigences cotées OUI / NON / NEK et mesuré par μ, U et H, selon le programme de l'auditologie. Trois cas forment le fil rouge : l'ANPP (Yaoundé), établissement public dont le schéma directeur précédent n'a pas été exécuté, LiZbiZ (Douala), entreprise de logistique, et la BANQUE SANAGA (Douala). Les trois sont fictifs.

Le Plan de développement de l'économie numérique au Cameroun 2026-2030 est finalisé et déposé. Il est en cours de validation dans les services du Premier ministre à la date de ce cours. Le livre le présente dans ces termes au chapitre 6 et se rattache à la SND30, qui est en vigueur.

## Ce que contient ce dépôt

| Élément | Où | Description |
|---|---|---|
| Le livre du cours | [`SNSD_main.pdf`](SNSD_main.pdf) | Prologue, 16 chapitres, 4 annexes, compilé depuis [`SNSD_main.tex`](SNSD_main.tex) |
| Les présentations | [`Présentation/`](Présentation/) | 16 présentations PowerPoint : vision d'ensemble et 15 séances de 2 heures, avec notes du présentateur |
| Les fiches d'exercices | [`fiches/`](fiches/) | 17 fiches de 40 questions au format texte |
| Le livret de correction | [`correction/`](correction/) | Accès réservé : voir la page du dossier |
| Les sources LaTeX | `front/`, `partie0/` à `partie6/`, `annexes/`, `bibliographie/`, `figures/`, [`Style_SNSD.sty`](Style_SNSD.sty) | Sources du livre |
| Les sources de génération | `_sources_generation/` | Scripts Python qui produisent les chapitres et calculent les mesures des encadrés de lecture |

## Organisation du cours (30 heures, 15 séances de 2 heures)

Les 30 heures sont consacrées au cours magistral. Les travaux dirigés (fiches, exercices de fin de chapitre) et les travaux pratiques (dix laboratoires) se font à la maison, sur NDAP SUKULU.

| Partie | Chapitres | Fichiers |
|---|---|---|
| **Prologue** | 0. Le schéma directeur dort dans un tiroir | [`partie0/`](partie0/) |
| **I. Fondements** | 1. Stratégie, système d'information, numérique · 2. Les théories de la stratégie · 3. L'alignement et la valeur | [`partie1/`](partie1/) |
| **II. Le contexte international** | 4. Normes et référentiels · 5. Doctrines et stratégies numériques dans le monde et en Afrique | [`partie2/`](partie2/) |
| **III. Le contexte national** | 6. La stratégie numérique du Cameroun · 7. Le cadre juridique d'un schéma directeur | [`partie3/`](partie3/) |
| **IV. Méthode** | 8. Cadrer et gouverner la démarche · 9. Diagnostiquer l'existant · 10. Fixer la cible · 11. Portefeuille et trajectoire · 12. Chiffrer, financer, acheter, doter | [`partie4/`](partie4/) |
| **V. Mise en œuvre** | 13. Piloter l'exécution · 14. Risques, sécurité, continuité, conformité | [`partie5/`](partie5/) |
| **VI. Défis et recherche** | 15. Données, intelligence artificielle, plateformes, sobriété · 16. Auditer un schéma directeur, mesurer l'alignement | [`partie6/`](partie6/) |
| **Annexes** | A. Glossaire · B. Modèles · C. Textes et documents de référence · D. Les quarante-huit exigences de la mission ANPP | [`annexes/`](annexes/) |

| Séance | Contenu | Séance | Contenu |
|---|---|---|---|
| 1 | Prologue et chapitre 1 | 9 | Chapitre 10 |
| 2 | Chapitre 2 | 10 | Chapitre 11 |
| 3 | Chapitre 3 | 11 | Chapitre 12 |
| 4 | Chapitre 4 | 12 | Chapitre 13 |
| 5 | Chapitre 5 | 13 | Chapitre 14 |
| 6 | Chapitres 6 et 7 | 14 | Chapitre 15 |
| 7 | Chapitre 8 | 15 | Chapitre 16 |
| 8 | Chapitre 9 | | |

## NDAP SUKULU, la salle de classe compagnon

*Ndap sukulu* signifie « la salle de classe » en bassa, et *Malet Yon* « ton enseignant ». NDAP SUKULU est l'environnement d'évaluation du cours : une fiche de 20 questions tirées d'une banque de 100 par chapitre, et dix laboratoires pratiques, minutés et en nombre de tentatives limité. Le code de cours est **MSN-2S4-MSI01**. La présentation complète figure au début du livre.

| Utilisation | Où |
|---|---|
| En ligne | `https://maletyon.github.io/cours-snsd/ndap-sukulu/` |
| Sur un ordinateur, sans Internet | archive téléchargeable dans [`ndap-sukulu/`](ndap-sukulu/) |
| Sur un téléphone (fiches seulement) | `https://maletyon.github.io/cours-snsd/ndap-sukulu/telephone/` |
| Si votre réseau bloque `github.io` | adresse de secours `https://raw.githack.com/MaletYon/cours-snsd/main/ndap-sukulu/`, ou [archive à télécharger](https://github.com/MaletYon/cours-snsd/raw/main/ndap-sukulu/NDAP_SUKULU_SNSD_ordinateur.zip) pour travailler hors ligne |

La connexion se fait avec le matricule et le mot de passe remis par l'enseignant. Les copies sont remises à l'enseignant sous forme d'un fichier chiffré. Il les corrige et publie les résultats, que chacun consulte dans l'application. Le mode d'emploi complet est dans [`ndap-sukulu/README.md`](ndap-sukulu/README.md).

| Lab | Sujet | Chapitre | Mission |
|---|---|---|---|
| SNSD-LAB-01 | Cinq forces et chaîne de valeur | 2 | LiZbiZ |
| SNSD-LAB-02 | Mesurer la maturité de l'alignement | 3 | ANPP |
| SNSD-LAB-03 | Carte d'applicabilité des textes | 7 | Les trois |
| SNSD-LAB-04 | Inventaire applicatif et grille de McFarlan | 9 | ANPP |
| SNSD-LAB-05 | Comparer trois scénarios de cible | 10 | BANQUE SANAGA |
| SNSD-LAB-06 | Arbitrer un portefeuille sous contrainte | 11 | ANPP |
| SNSD-LAB-07 | Coût complet sur cinq ans | 12 | LiZbiZ |
| SNSD-LAB-08 | Tableau de bord d'exécution | 13 | ANPP |
| SNSD-LAB-09 | Registre des risques et continuité | 14 | BANQUE SANAGA |
| SNSD-LAB-10 | Audit intégrateur d'un schéma directeur | 16 | ANPP |

## Sources de recherche

Le cours s'appuie sur deux prépublications de l'auteur, déposées sur HAL : *Vers l'auditologie* (`hal-05701007`) et *Modelling Epistemic Uncertainty in IS Audit* (`hal-05701270`). Le chapitre 16 en applique la cotation à l'audit d'un schéma directeur et propose un indice d'alignement prouvé.

## Compiler le livre

Avec une distribution LaTeX : `pdflatex SNSD_main`, `biber SNSD_main`, `makeindex SNSD_main`, puis deux fois `pdflatex SNSD_main`.
Les présentations se régénèrent avec `python Présentation/_sources/run.py SNSD all` (Python 3 et python-pptx).

## Textes, normes et documents sous licence

Les lois, les décrets et les règlements sont cités par leur référence et leur date. Le livre ne cite un article que lorsqu'il a été lu. Les normes ISO et les autres documents sous licence cités dans le cours **ne sont pas distribués** dans ce dépôt. Le projet de plan 2026-2030 n'est pas publié : le livre en décrit la structure sans le reproduire.

## Licence

Contenu pédagogique : [CC BY-NC-SA 4.0](LICENSE.md). Code du générateur de présentations : MIT. Voir [`LICENSE.md`](LICENSE.md).
