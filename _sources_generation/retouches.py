# -*- coding: utf-8 -*-
# Retouches à la main après decale.py (sources de génération du livre et des corrigés).
import io
R = {
 'c01.py': [("calé sur la fin de la Stratégie nationale de développement en 2030 et sur\nle cadre budgétaire à moyen terme de l'Agence.",
             "calé sur le plan stratégique 2024-2028 de l'Agence et sur son cadre\nbudgétaire à moyen terme.")],
 'c04.py': [("Douala, mercredi 22~janvier~2025.", "Douala, mercredi 21~octobre~2026.")],
 'c06.py': [("Le plan Cameroun numérique 2026-2030 est noté comme attendu.", "Le plan national appelé à succéder à Cameroun numérique 2020 est noté comme attendu."),
            ('"O", "Plan 2026-2030")', '"O", "Plan 2024-2028")'),
            ("""Yaoundé, jeudi 6~février~2025. Le projet de note que le consultant junior soumet à Mme~EKANI commence ainsi~:
« Conformément au plan Cameroun numérique 2026-2030, l'ANPP engage sa transformation. » Mme~EKANI demande où
il a lu ce plan. Il en a entendu parler dans un séminaire.

Elle lui fait chercher le texte d'approbation.""",
             """Yaoundé, jeudi 15~octobre~2026. La cellule de portefeuille de l'ANPP prépare la révision annuelle du schéma
directeur. Le projet de préambule qu'un agent soumet à Mme~NGO BIYONG commence ainsi~: « Conformément au plan
Cameroun numérique 2026-2030, l'ANPP poursuit sa transformation. » Elle demande où il a lu ce plan. Il en a
entendu parler dans un séminaire.

Elle lui fait chercher le texte d'approbation."""),
            ("La phrase du consultant est donc fausse", "La phrase est donc fausse")],
 'c16.py': [("Nous sommes en 2032.", "Nous sommes en 2030.")],
 'ann.py': [("2025-2029 pour un plan 2026-2030", "2025-2029 pour un plan 2024-2028")],
 'corr_data1.py': [("puisque le plan 2026-2030 existe", "puisque le plan 2024-2028 existe")],
}
for f, L in R.items():
    s = io.open(f, encoding='utf-8').read()
    for a, b in L:
        assert s.count(a) == 1, (f, a[:50], s.count(a)); s = s.replace(a, b)
    io.open(f, 'w', encoding='utf-8').write(s)
print('retouches faites')
