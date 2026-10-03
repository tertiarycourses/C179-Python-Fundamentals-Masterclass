import copy, re

OLD_TITLE, NEW_TITLE = "Python Fundamental Course for Beginners", "Python Fundamentals Masterclass"

def set_text(par, text):
    """Rewrite a paragraph through runs[0] so its formatting survives."""
    if not par.runs:
        par.add_run(text)
        return
    par.runs[0].text = text
    for r in par.runs[1:]:
        r.text = ""

def delete(par):
    par._p.getparent().remove(par._p)

def set_cell(cell, text):
    set_text(cell.paragraphs[0], text)
    for extra in cell.paragraphs[1:]:
        delete(extra)

def retitle_all(doc):
    def fix(par):
        if OLD_TITLE in par.text:
            set_text(par, par.text.replace(OLD_TITLE, NEW_TITLE))
    for par in doc.paragraphs:
        fix(par)
    for t in doc.tables:
        for c in t._cells:
            for par in c.paragraphs:
                fix(par)

def para_by_text(doc, start):
    hits = [p for p in doc.paragraphs if p.text.startswith(start)]
    assert len(hits) == 1, (start, len(hits))
    return hits[0]

def delete_range(doc, first_start, stop_start):
    """Delete paragraphs from the one starting with first_start up to (not incl.) stop_start."""
    pars = doc.paragraphs
    i = next(k for k, p in enumerate(pars) if p.text.startswith(first_start))
    j = next(k for k, p in enumerate(pars) if k > i and p.text.startswith(stop_start))
    for p in pars[i:j]:
        delete(p)
    return j - i

def rebuild_rows(table, spec):
    """spec = [(template_row_index, [cell texts])]; replaces every body row (row 0 = header kept)."""
    tpl = [copy.deepcopy(r._tr) for r in table.rows]
    tbl = table._tbl
    for r in list(table.rows)[1:]:
        tbl.remove(r._tr)
    for ti, texts in spec:
        tbl.append(copy.deepcopy(tpl[ti]))
        row = table.rows[-1]
        cells = []
        for c in row.cells:
            if not cells or cells[-1]._tc is not c._tc:
                cells.append(c)
        assert len(cells) == len(texts), (len(cells), texts)
        for c, t in zip(cells, texts):
            set_cell(c, t)

KA = re.compile(r"\s*\((?:[KA][^()]*·\s*)+(LO\d)\)")   # "(K1–K4 · A1, A2 · LO1)" -> "(LO1)"

# Source deck slides dropped by convert_deck (0-based); slide refs in the docs are 1-based.
DROPPED = [2, 9, 10, 11, 13, 14, 15, 16, 138, 139, 140]

def new_slide(n):
    i = n - 1
    assert i not in DROPPED, n
    return n - sum(1 for d in DROPPED if d < i)

def remap_slides(s):
    s = re.sub(r"\[Slides (\d+)–(\d+)\]", lambda m: f"[Slides {new_slide(int(m[1]))}–{new_slide(int(m[2]))}]", s)
    return re.sub(r"\[Slide (\d+)\]", lambda m: f"[Slide {new_slide(int(m[1]))}]", s)
