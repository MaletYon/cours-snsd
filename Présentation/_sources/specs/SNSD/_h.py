# Fonctions courtes pour écrire les specs SNSD : une fonction par type de diapositive.
# Elles produisent les dictionnaires attendus par slides.py. La charte est celle de tous les cours.
def T(tag, title, sub, right, size=None):
    d = {"k": "title", "tag": tag, "title": title, "sub": sub, "right": right}
    if size: d["size"] = size
    return d
def R(kicker, items): return {"k": "synthese", "title": "Rappel de la séance précédente", "kicker": kicker, "items": items}
def A(items, title=None, kicker=None):
    d = {"k": "agenda", "items": items}
    if title: d["title"] = title
    if kicker: d["kicker"] = kicker
    return d
def C(num, short, part, title, question): return {"k": "chapitre", "num": num, "short": short, "part": part, "title": title, "question": question}
def O(items): return {"k": "objectifs", "items": items}
def TB(title, kicker, head, widths, rows, size=None, note=None):
    d = {"k": "table", "title": title, "kicker": kicker, "head": head, "widths": widths, "rows": rows}
    if size: d["size"] = size
    if note: d["note"] = note
    return d
def D(title, kicker, items): return {"k": "definition", "title": title, "kicker": kicker, "items": items}
def CP(title, kicker, lh, li, rh, ri, bottom=None):
    d = {"k": "compare", "title": title, "kicker": kicker, "left": {"head": lh, "items": li}, "right": {"head": rh, "items": ri}}
    if bottom: d["bottom"] = bottom
    return d
def P(title, kicker, items, side=None):
    d = {"k": "points", "title": title, "kicker": kicker, "items": items}
    if side: d["side"] = {"head": side[0], "text": side[1]}
    return d
def SC(title, label, text, notes=None):
    d = {"k": "scenario", "title": title, "label": label, "text": text}
    if notes: d["notes"] = notes
    return d
def K(title, kicker, items, cols=3):
    return {"k": "cards", "title": title, "kicker": kicker, "cols": cols,
            "items": [{"head": h, "badge": b, "text": t} for b, h, t in items]}
def ST(title, kicker, items): return {"k": "steps", "title": title, "kicker": kicker, "items": items}
def S4(title, kicker, items, bottom=None):
    d = {"k": "stats", "title": title, "kicker": kicker, "items": items}
    if bottom: d["bottom"] = bottom
    return d
def Q(kicker, text, author, size=30): return {"k": "quote", "kicker": kicker, "text": text, "author": author, "size": size}
def EX(title, duree, text, questions, notes): return {"k": "exercice", "title": title, "duree": duree, "text": text, "questions": questions, "notes": notes}
def SY(items): return {"k": "synthese", "items": items}
def M(lecture): return {"k": "maison", "lecture": lecture}
def F(nxt, items, foot="Merci de votre attention · questions ?", label=None):
    d = {"k": "fin", "next": nxt, "items": items, "foot": foot}
    if label: d["label"] = label
    return d
METIERS3 = lambda a, b, c: K("Ce que la séance demande à chaque métier", "Fiches métier", [(x[0][0], x[0], x[1]) for x in (a, b, c)])
