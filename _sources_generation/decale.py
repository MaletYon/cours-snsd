# -*- coding: utf-8 -*-
"""Recale la chronologie fictive du cours SNSD deux ans plus tôt : la mission ANPP se déroule du
14 janvier au 26 juin 2025, la première revue a lieu le 30 juin 2026. Toutes les illustrations sont
antérieures à décembre 2026. Les dates réelles (textes, normes, documents nationaux) ne bougent pas.
Usage : python decale.py fichier [fichier...]   (réécrit en place, affiche les années restantes à relire)"""
import io, re, sys
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet"]
LONG = {"janvier": 31, "février": 28, "mars": 31, "avril": 30, "mai": 31, "juin": 30, "juillet": 31}
SEP = r"(?:~| |\\u00a0)"
def plus2(j, m):
    j += 2
    if j > LONG[m]:
        j -= LONG[m]; m = MOIS[MOIS.index(m) + 1]
    return j, m
def decale(s, garder_2027_2031=False):
    P = {}
    def prot(rx):
        nonlocal s
        def f(m):
            k = "\x00%d\x00" % len(P); P[k] = m.group(0); return k
        s = re.sub(rx, f, s)
    # ---- dates et années réelles, à ne pas toucher
    for rx in [r"Mars 2026, pour 2026-2030", r"22(?: |~)mars(?: |~)2019", r"janvier(?: |~)2019", r"mondial de 2024", r"données de 2022", r"africain de 2024", r"date de 2024", r"20\d\d/\d+", r"R-20\d\d/\d+", r"\\cite\{[^}]*\}", r"2026-2027", r"(?:13 |13~)?novembre(?: |~)2026", r"décembre(?: |~)2026", r"octobre(?: |~)2026",
               r"Cameroun [Nn]umérique 2020", r"Cameroun [Nn]umérique 2030", r"[Nn]umérique(?: au Cameroun)?(?: |~)2026-2030", r"[Ss]anté numérique(?: |~)20\d\d-20\d\d",
               r"(?:[Pp]lan|pour|projet de plan|Projet de Plan|Projet de plan)(?: |~)2026-2030", r"2026(?: |~)?[-~–](?: |~)?2030(?=\}|, [éÉ]dition)", r"2020-2030", r"2010-2019", r"2020-2024", r"2016(?: |~)?[–-](?: |~)?2020",
               r"2035", r"d'ici(?: |~)2030", r"en 2030(?= et sur)", r"horizon(?: |~)2030", r"[éÉ]dition(?: |~)2025", r":20\d\d", r"COBIT(?: |~)2019", r"année(?: |~)2025", r"Août 2025",
               r"\d+(?:er|\\textsuperscript\{er\})?(?: |~)(?:et(?: |~)\d+(?: |~))?(?:janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)(?: |~)(?:19\d\d|200\d|201\d|2022|2023|2024)",
               r"15(?: |~)février(?: |~)2025", r"[fF]évrier(?: |~)2025", r"[jJ]uillet(?: |~)202[45]", r"7 et 8(?: |~)juillet(?: |~)2025", r"4(?: |~)mars(?: |~)2026", r"Mars 2026, pour", r"mars(?: |~)2026(?=\. Il compte huit)",
               r"[fF]évrier(?: |~)202[24]", r"[mM]ai(?: |~)2016", r"22(?: |~)septembre(?: |~)2024", r"[Rr]apport annuel(?: |~)2024", r"depuis 2023", r"(?:loi|lois|règlement|lettre circulaire|texte|stratégie nationale d'intelligence artificielle|Stratégie d'intelligence artificielle|intelligence artificielle)(?: camerounaise)? de 20\d\d",
               r"de 2024 sur", r"date de(?: |~)2022", r"édition, 2022", r"de(?: |~)2021, qui traite", r"ISO(?: |~)37000 de(?: |~)2021", r"en 2024(?= portait)", r"superviseur(?: |~)en(?: |~)2024", r"panne de 2026 et l'Opération", r"panne de(?: |~)2026(?= et)",
               r"stratégie nationale 2025", r"Stratégie continentale 2024", r"données 2022", r"Pacte africain 2024", r"mondial 2024", r"OCDE 2014", r"de 2025 cite", r"Juillet 2025", r"2020, pour", r"2020-2030", r"hal-\d+", r"© MaletYon 2026", r"MaletYon 2026",
               r"(?:Porter|Barney|Teece|Wernerfelt|Christensen|Rochet et Tirole|Coase|Williamson|Kaplan et Norton|Nolan|Rockart|McFarlan|Luftman|Venkatraman|Solow|Brynjolfsson|Carr|Ward et Daniel|Weill et Ross|Bharadwaj|Westerman|Rogers|Davis|Mintzberg(?: et Waters)?|Henderson et Venkatraman|Robertson)[ ,]+(?:19|20)\d\d(?:[, ]+(?:19|20)\d\d)*",
               r"en(?: |~)(?:19\d\d|200\d|201[0-6])", r"de(?: |~)2012", r"2009", r"version 1\.0 -- novembre 2026"]:
        prot(rx)
    if garder_2027_2031:
        prot(r"20(?:27|28|29|30|31)")
    # ---- dates de la mission : jour + 2, année 2027 -> 2025 ; dates sans année : jour + 2
    def dm(m):
        j = int(m.group("j")); mo = m.group("m"); an = m.group("a") or ""
        j, mo = plus2(j, mo)
        js = "1\\textsuperscript{er}" if (j == 1 and "textsuperscript" in m.group(0)) else ("1er" if j == 1 else str(j))
        return js + m.group("s") + mo + (m.group("s2") + "\x01" if an else "")
    s = re.sub(r"(?<![\d,])(?P<j>\d{1,2})(?:er|\\textsuperscript\{er\})?(?P<s>" + SEP + r")(?P<m>janvier|février|mars|avril|mai|juin|juillet)(?:(?P<s2>" + SEP + r")(?P<a>2027))?(?!" + SEP + r"?20\d\d)(?!" + SEP + r"\d)", dm, s)
    # ---- années de la fiction
    s = s.replace("2026-2030", "\x02").replace("2021-2025", "\x03").replace("2021 à 2025", "\x04")
    s = re.sub(r"(?P<p>(?:\b(?:en|de|pour|depuis|fin|début|et|entre|Entre|En|De|Depuis|Pour|Fin|Dès|dès|courant|vers|jusqu'en|qu'en|d'ici|Plan|Registre|présence|exercice|budget|année|[dD]écembre|[sS]eptembre|[oO]ctobre|[nN]ovembre|[aA]oût|[mM]ars|[jJ]anvier|[fF]évrier|[aA]vril|[mM]ai|[jJ]uin|[jJ]uillet|directeur)|[(«\"'/])(?:~| )?)(?P<a>20(?:19|2[0-6]))(?!\d|/|-20)",
               lambda m: m.group("p") + str(int(m.group("a")) - 2), s)
    s = re.sub(r"20(27|28|29|30|31)", lambda m: str(2000 + int(m.group(1)) - 2), s)
    s = s.replace("\x02", "2024-2028").replace("\x03", "2019-2023").replace("\x04", "2019 à 2023")
    s = s.replace("\x01", "2025")
    s = s.replace("vendredi 30~juin~2026", "mardi 30~juin~2026").replace("vendredi 30 juin 2026", "mardi 30 juin 2026")
    for k in sorted(P, key=len, reverse=True):
        s = s.replace(k, P[k])
    return s
if __name__ == "__main__":
    for f in sys.argv[1:]:
        t = io.open(f, encoding="utf-8").read()
        u = decale(t, garder_2027_2031=("LAB-05" in f))
        io.open(f, "w", encoding="utf-8").write(u)
        for i, l in enumerate(u.split("\n"), 1):
            if re.search(r"20(?:1[7-9]|2\d|30)", re.sub(r"20\d\d/\d+|\\cite\{[^}]*\}", "", l)):
                print("%s:%d: %s" % (f.split("/")[-1], i, l.strip()[:170]))
