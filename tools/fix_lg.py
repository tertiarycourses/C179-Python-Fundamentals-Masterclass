import re, shutil, docx
from docxutil import *

SRC = "source-wsq/courseware/LG-Python Fundamental Course for Beginners.docx"
OUT = "courseware/LG-Python Fundamentals Masterclass.docx"
shutil.copy(SRC, OUT)
d = docx.Document(OUT)

set_text(para_by_text(d, "This Learner Guide accompanies"),
         "This Learner Guide accompanies the course Python Fundamentals Masterclass (C179), conducted by Tertiary "
         "Infotech Academy Pte Ltd. It provides the detailed step-by-step instructions for all 21 hands-on activities, "
         "organised by the six course topics. The course slides stay visual and high-level; THIS guide is where every "
         "activity is worked through line by line, so use it during class and for practice afterwards.")
set_text(para_by_text(d, "The course is mapped to"),
         "Each activity opens with a one-line focus statement describing the skill it practises. The guide, the slides "
         "and the lesson plan are generated from one content source, so they always stay aligned.")
retitle_all(d)
set_text(para_by_text(d, "TGS Ref No:"), "Course Code: C179")
set_text(para_by_text(d, "Version 20"), "Version 1.0")

for p in d.paragraphs:
    t = p.text
    if ".  TSC mapping:" in t:                       # topic intro line
        set_text(p, t.split(".  TSC mapping:")[0] + ".")
    elif t.startswith("TSC mapping:"):               # activity focus line
        rest = t.split(" — ", 1)[1]
        set_text(p, "Focus: " + rest)

set_text(para_by_text(d, "Try the recommended follow-on courses"),
         "Try the recommended follow-on courses to advance: Python Data Analysis Masterclass; AI Vibe Coding with "
         "Python; SQL Masterclass.")

t0 = d.tables[0]
set_cell(t0.rows[1].cells[0], "1.0"); set_cell(t0.rows[1].cells[1], "4 October 2026")
set_cell(t0.rows[1].cells[2], "First release of the Python Fundamentals Masterclass Learner Guide — detailed "
         "step-by-step for all 21 hands-on activities across six topics.")
t0._tbl.remove(t0.rows[2]._tr)
d.save(OUT)
print("saved", OUT)
