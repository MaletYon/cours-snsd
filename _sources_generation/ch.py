# -*- coding: utf-8 -*-
"""Gabarit des chapitres du livre SNSD : produit le fichier .tex d'un chapitre à partir d'un contenu compact."""
import io, math, os
R = '/home/claude/cours-snsd/'
BAR = '% ' + '=' * 76

def fr(x, d=2):
    return ('%.*f' % (d, x)).replace('.', '{,}')

def tab(spec, heads, rows, cap=None, num=None):
    o = ['\\begin{tableaucours}{%s}{%%' % spec]
    o.append(' &\n'.join('    \\tableauHeader{%s}' % h for h in heads))
    o.append('}')
    for r in rows:
        o.append(' & '.join(r) + ' \\\\')
    o.append('\\end{tableaucours}')
    if cap:
        o.append('\\vspace{-0.8em}')
        o.append('\\begin{center}{\\small\\itshape Tableau~%s. %s}\\end{center}' % (num, cap))
    return '\n'.join(o)

def box(env, body, title=None):
    return '\\begin{%s}%s\n%s\n\\end{%s}' % (env, '{%s}' % title if title else '', body.strip(), env)

def items(l, env='itemize'):
    return '\\begin{%s}\n' % env + '\n'.join('    \\item ' + x for x in l) + '\n\\end{%s}' % env

COTE = {'O': '\\OUI{}', 'N': '\\NON{}', 'K': '\\NEK{}'}
MOTS = ['Aucun', 'Un', 'Deux', 'Trois', 'Quatre', 'Cinq', 'Six', 'Sept', 'Huit', 'Neuf', 'Dix', 'Onze', 'Douze']
NB = ['zéro', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf', 'dix', 'onze', 'douze']

def mesures(rows):
    n = len(rows); o = sum(1 for r in rows if r[1] == 'O'); k = sum(1 for r in rows if r[1] == 'K'); no = n - o - k
    h = -sum((c / n) * math.log2(c / n) for c in (o, no, k) if c)
    return n, o, no, k, o / n, k / n, h

def lecture(titre, rows, texte, head='Exigence'):
    n, o, no, k, mu, u, h = mesures(rows)
    t = tab('L{7.6cm}cL{3.4cm}', [head, 'Cote', 'Preuve'], [[a, COTE[c], p] for a, c, p in rows])
    dec = '%s \\OUI{}, %s \\NON{}, %s \\NEK{} sur %s.' % (MOTS[o], NB[no], NB[k], NB[n])
    d3 = lambda x: fr(x, 3) if abs(x * 100 - round(x * 100)) > 1e-9 else fr(x, 2)
    return box('boxlecture', t + '\n\n\\medskip\n\\textbf{Décompte.} ' + dec + '\n\\hfill\\lecture{%s}{%s}{%s}\n\n\\medskip\n\\textbf{Lecture.} %s' % (d3(mu) if mu else '0', d3(u) if u else '0', fr(h, 2), texte.strip()), titre)

def chapitre(fichier, num, titre, label, mark, epi, epi_src, niveau, prereq, objectifs, ouv_titre, ouverture, corps,
             metiers, resume, points, exos, lectures, transition, sources=''):
    o = [BAR, '% Fichier  : ' + fichier, '% Titre    : ' + titre, '% Auteur   : MINKA MI NGUIDJOÏ Thierry Emmanuel',
         '% Version  : 1.0 -- novembre 2026', '% Corrigés : corriges/Corr_' + ('P00' if num == 0 else 'C%02d' % num) + '.tex', BAR]
    if sources:
        o += ['% Sources : ' + l for l in sources.strip().split('\n')] + [BAR]
    o += ['', '\\chapter{%s}' % titre, '\\label{%s}' % label, '\\chaptermark{%s}' % mark, '',
          '\\epigraph{%%\n    %s%%\n}{%s}' % (epi, epi_src), '', '\\niveauChapitre{%s}{%%\n    %s\n}' % (niveau, prereq), '',
          box('boxobjectifs', items(objectifs)), '', '\\bigskip', '', BAR,
          '\\section*{Avant de commencer : %s}' % ouv_titre, BAR, '', ouverture.strip(), '', corps.strip(), '']
    for m, t in metiers:
        o += [box('boxmetier', t, m), '']
    o += [box('boxresume', items(resume)), '',
          box('boxinfo', '\\textbf{Points de contrôle.} Vous avez compris ce chapitre si vous savez~:\n' + items([p + ('~;' if i < len(points) - 1 else '.') for i, p in enumerate(points)])), '']
    niv = {1: '\\niveaubase', 2: '\\niveaumoyen', 3: '\\niveauexpert'}
    for i, (t, n, e) in enumerate(exos, 1):
        o += ['\\begin{boxexo}[title={\\ding{45}\\quad Exercice~%s.%d. %s %s}]\n%s\n\\end{boxexo}' % ('P' if num == 0 else num, i, t, niv[n], e.strip()), '']
    o += ['\\bigskip', '', box('boxinfo', '\\textbf{Pour aller plus loin.}\n' + items(lectures)), '',
          box('boxinfo', '\\textbf{Transition.} ' + transition.strip()), '']
    import re
    s = re.sub(r',(\s+)et(\s)', r'\1et\2', '\n'.join(o))
    assert ', et ' not in s.replace('\n', ' '), [x for x in s.replace('\n', ' ').split('.') if ', et ' in x][:3]
    assert '’' not in s and '—' not in s
    os.makedirs(os.path.dirname(R + fichier), exist_ok=True)
    io.open(R + fichier, 'w', encoding='utf-8').write(s)
    print(fichier, len(s.split('\n')), 'lignes')

def sec(titre, label):
    return '\n'.join([BAR, '\\section{%s}' % titre, '\\label{%s}' % label, BAR, ''])
