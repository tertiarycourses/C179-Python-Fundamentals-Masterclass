"""Copy labs/ + the LG Markdown mirror from source-wsq/ and strip the WSQ layer."""
import re, shutil, pathlib
OLD, NEW = "Python Fundamental Course for Beginners", "Python Fundamentals Masterclass"
src = pathlib.Path("source-wsq")
if pathlib.Path("labs").exists():
    shutil.rmtree("labs")
shutil.copytree(src / "labs", "labs")

def scrub(t):
    t = re.sub(r"  ·  TSC mapping: [^—\n]*— (.)", lambda m: "  ·  Focus: " + m[1], t)       # lab headers
    t = re.sub(r"\.  TSC mapping: [^\n]*\.", ".", t)                                           # LG topic intros
    t = re.sub(r"^TSC mapping: [^—\n]*— ", "Focus: ", t, flags=re.M)                           # LG activity lines
    return t.replace(OLD, NEW)

for f in pathlib.Path("labs").rglob("*.md"):
    f.write_text(scrub(f.read_text()))

lg = (src / f"LG-{OLD}.md").read_text()
lg = lg.replace("**WSQ Course Code:** TGS-2019503161", "**Course Code:** C179").replace("Version v20 · 9 August 2026", "Version 1.0 · 4 October 2026")
lg = lg.replace("This Learner Guide accompanies the WSQ course Python Fundamental Course for Beginners (TGS-2019503161)",
                "This Learner Guide accompanies the course Python Fundamentals Masterclass (C179)")
lg = re.sub(r"The course is mapped to the ICT Skills Framework TSC[^\n]*",
            "Each activity opens with a one-line focus statement describing the skill it practises. The guide, the slides "
            "and the lesson plan are generated from one content source, so they always stay aligned.", lg)
lg = re.sub(r"- Try the recommended follow-on courses to advance:[^\n]*",
            "- Try the recommended follow-on courses to advance: Python Data Analysis Masterclass; AI Vibe Coding with "
            "Python; SQL Masterclass.", lg)
pathlib.Path(f"LG-{NEW}.md").write_text(scrub(lg))
print("ok")
