import shutil, docx
from docxutil import *

SRC = "source-wsq/courseware/LP-Python Fundamental Course for Beginners.docx"
OUT = "courseware/LP-Python Fundamentals Masterclass.docx"
shutil.copy(SRC, OUT)
d = docx.Document(OUT)
retitle_all(d)

set_text(para_by_text(d, "TGS Ref No:"), "Course Code: C179")
set_text(para_by_text(d, "Version 20"), "Version 1.0")
# TOC
delete(para_by_text(d, "Assessment\t"))
set_text(para_by_text(d, "Day 2 — Functions, Modules & Packages, Final Assessment\t"), "Day 2 — Functions, Modules & Packages\t5")
set_text(para_by_text(d, "Activity Reference (aligned to the Skills Framework TSC)\t"), "Activity Reference\t6")
# Assessment section (heading + 5 bullets)
assert delete_range(d, "Assessment", "Course Schedule") == 6
set_text(para_by_text(d, "Slide references"),
         "Slide references [Slide n] point into the course deck Python Fundamentals Masterclass-v1.0.pptx so the trainer can navigate directly.")
set_text(para_by_text(d, "Day 2 — Functions, Modules & Packages, Final Assessment"), "Day 2 — Functions, Modules & Packages")
for p in [p for p in d.paragraphs if p.text.startswith("Total training time:")]:
    set_text(p, "9:30am – 5:30pm · 450 minutes (7.5 instructional hours), with a 30-minute lunch.")
set_text(para_by_text(d, "Activity Reference (aligned"), "Activity Reference")

t0, t1, t2, t3, t4 = d.tables
# Version record: one release row
set_cell(t0.rows[1].cells[0], "1.0"); set_cell(t0.rows[1].cells[1], "4 October 2026")
set_cell(t0.rows[1].cells[2], "First release of the Python Fundamentals Masterclass courseware — 2-day schedule "
         "(9:30am–5:30pm) with 21 hands-on activities across six topics.")
t0._tbl.remove(t0.rows[2]._tr)
# Course information
set_cell(t1.rows[1].cells[0], "Course Code"); set_cell(t1.rows[1].cells[1], "C179")
set_cell(t1.rows[4].cells[1], "2 days · 7.5 instructional hours per day (15 hours)")
set_cell(t1.rows[5].cells[1], "9:30 am – 5:30 pm (30-minute lunch)")
t1._tbl.remove(t1.rows[2]._tr)          # Skills Framework TSC row

s2 = [remap_slides(r.cells[2].text) for r in t2.rows]
s3 = [remap_slides(r.cells[2].text) for r in t3.rows]
# Day 1: teaching already 450 min; the 90 min of breaks become one 30-min lunch.
rebuild_rows(t2, [
    (1, ["9:30–10:00", "30 min", "Welcome, trainer and learner introductions, ground rules, learning outcomes and course outline"]),
    (2, ["10:00–11:00", "60 min", s2[2]]),
    (4, ["11:00–12:45", "105 min", s2[4]]),
    (5, ["12:45–13:15", "30 min", "Lunch break"]),
    (6, ["13:15–14:45", "90 min", s2[6].replace("Digital attendance (PM). ", "")]),
    (8, ["14:45–15:30", "45 min", s2[8]]),
    (9, ["15:30–17:15", "105 min", s2[9]]),
    (10, ["17:15–17:30", "15 min", "Day 1 recap and Q&A"]),
])
# Day 2: the 165-min assessment block goes; topic rows 60/90/60/60 rescaled onto 420 min -> 95/135/95/95.
rebuild_rows(t3, [
    (1, ["9:30–9:45", "15 min", "Recap quiz on Day 1 topics"]),
    (2, ["9:45–11:20", "95 min", s3[2]]),
    (4, ["11:20–13:35", "135 min", s3[4]]),
    (5, ["13:35–14:05", "30 min", "Lunch break"]),
    (6, ["14:05–15:40", "95 min", s3[6].replace("Digital attendance (PM). ", "")]),
    (7, ["15:40–17:15", "95 min", s3[7].replace(". Course summary", "")]),
    (9, ["17:15–17:30", "15 min", "Course summary, course feedback and Q&A. End of class"]),
])
# Activity reference: TSC K/A column -> topic focus
focus = ["Overview · install · IDE · first script · comments",
         "Number · String · List · Tuple · Dictionary · Set",
         "Arithmetic · compound · comparison · membership · logical",
         "Conditional · loops · multiple sequences · comprehension",
         "Syntax · returns · arguments · lambda, map, filter",
         "Standard library · pip · pandas, matplotlib, yfinance"]
set_cell(t4.rows[0].cells[1], "Topic Focus")
for r, f in zip(t4.rows[1:], focus):
    set_cell(r.cells[1], f)
    set_cell(r.cells[2], remap_slides(r.cells[2].text))
d.save(OUT)
print("saved", OUT)
