"""Build the SwapnaLoka profile as DOCX and PDF from one content source.

Usage:  python tools/build_profile.py
Output: docs/SwapnaLoka_Profile_Swapnil_Sapre.docx / .pdf
Needs:  python-docx, reportlab
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PHOTO = ROOT / "assets" / "img" / "swapnil.jpg"
OUT = ROOT / "docs"
NAME = "SwapnaLoka_Profile_Swapnil_Sapre"

NAVY, GOLD, SAFFRON, INK, SOFT = "10204A", "B8862F", "D9732B", "16213A", "4A5571"

TITLE = "Swapnil Sapre"
TAGLINE = "Builder · Innovator · Entrepreneur"
ROLES = ("Semiconductor, Embedded-Systems & Deep-Tech AI Veteran · Advisor · Consultant · "
         "Coach · Program Leader · Hindi Poet · Ghazal Singer · Percussionist · "
         "Distinguished Alumnus, IIM Bangalore")
CONTACT = [
    ("Location", "Bengaluru, India"),
    ("LinkedIn", "linkedin.com/in/swapnils29"),
    ("Email", "sapreswapnil@yahoo.co.in"),
    ("YouTube", "Damruki: Bansuri Beats playlist"),
    ("Books", "amazon.in: author Swapnil Sapre"),
]
STATS = [("24+", "years in semiconductors & embedded systems"),
         ("6+", "years leading AI-processor silicon"),
         ("Spec to HVM", "end-to-end product ownership"),
         ("5", "books: technology, music, poetry")]

ABOUT = [
    "Swapnil Sapre is a semiconductor and systems leader with over 24 years across ASIC/SoC design, "
    "chip architecture, AI processors, embedded systems, product engineering and high-volume "
    "manufacturing. He has held engineering and product roles at Ambient Scientific, Western Digital, "
    "AMD, Freescale/NXP, Mindtree and Wipro, which gives him an end-to-end view from system architecture "
    "and silicon to software, productization and commercial deployment.",
    "Today he leads engineering for ultra-low-power edge-AI silicon and advises deep-tech startups and "
    "emerging technology organizations on turning ideas into viable, scalable, market-ready products. "
    "He builds ventures where technology meets culture, music and well-being, and he mentors engineers "
    "and founders.",
    "He is a Distinguished Alumnus of IIM Bangalore. He is also a trained Tabla and Mridangam player, a singer "
    "of ghazals, bhajans and abhangs, the composer of the bhajan album \"Raam Gunjan\", the founder of the "
    "Damruki school of rhythm, and a Hindi poet who writes as \"Noor\" / \"Sopaan Noor\". He studies Dharma "
    "and Jyotish (Indian astrology) and is a fan of Kho Kho and Kabaddi.",
]
QUOTE = "Building technology with purpose, businesses with responsibility, teams with trust, and people with empathy."

VENTURES = [
    ("Chiluka (chiluka.online)", "A dharmic companion for the family: tradition, faithfully told. Includes guidance services and an installable app."),
    ("SwaraKul (swarakul.online)", "A lineage-centred platform connecting students with gurus of Indian classical music. \"Every swara counts.\""),
    ("Damruki: School of Rhythm & Seven Swaras (founder)", "Hindustani and Carnatic music and percussion (Tabla, Mridangam) for learners of every background; formerly Rhythm Seven. Personal learning paths, workshops and concert tours, and music for well-being rooted in Nada Yoga."),
    ("Suphala Care (suphalacare.com)", "Holistic nutrition and wellness practice of Dr Suguna Sapre (PhD, renal nutrition): personal food plans for weight, women's health, children, seniors and chronic conditions. Co-builder of its digital platform, booking, programmes and the SuViva network of complementary practitioners."),
    ("Industry showcases", "Proof-of-concept products for MWC 2018/2019 and COMPUTEX 2019, including a 1 TB SD card and the first SD-form-factor NVMe card."),
]

SERVICES = [
    ("Deep-tech & semiconductor advisory", "FPGA prototyping with PPA trade-offs; chip development, tape-out readiness and production operations; edge-AI platform strategy; extreme-environment microelectronics."),
    ("Strategy for startups & services firms", "Deep-tech go-to-market and customer acquisition; L&D strategy; program management; art, music and wellness ventures."),
    ("Coaching & mentoring", "Engineers moving into architecture, product and leadership roles; founders turning a technical idea into a product; part-time faculty."),
    ("Speaking", "PPA as a product decision · Spec to silicon to volume · Bring-up and verification that catch real bugs · Open hardware and India's deep-tech ecosystem · Skilling semiconductor engineers."),
]

EXPERTISE = [
    "ASIC / SoC / VLSI: spec to GDS", "Pre- & post-silicon verification and validation",
    "Tape-out to production: wafer sort, OSAT, packaging", "High-volume manufacturing and cost optimization",
    "Embedded bring-up and SDK releases", "FPGA prototyping on Intel and Xilinx",
    "RISC-V and ARM platforms", "Power, performance and thermal optimization",
    "Test, evaluation and customer boards", "Characterization, qualification and reliability",
    "Storage: SSD, SD/microSD, NVMe, UFS, USB", "Product line and program management",
]

CAREER = [
    ("2026 – now", "Consultant & Advisor", "Independent", "Part-time engagements in FPGA prototyping, deep-tech GTM, AI vision chips, cryogenic ICs, AR/VR learning, and teaching."),
    ("2020 – now", "AVP – Engineering", "Ambient Scientific", "Silicon-to-system lifecycle for ultra-low-power AI processors: spec to GDS2, verification and validation, bring-up, boards, SDK and production."),
    ("2012 – 2020", "System Architect, Technologist & Product Line Manager", "Western Digital", "Flash-storage products (SD, microSD, SSD, NVMe) from SoC architecture to certified shipping product; ran the SD/microSD line."),
    ("2011 – 2012", "Senior Design Engineer", "AMD", "Fusion SoC verification; led the global graphics OVC; DDR3 PHY DFx."),
    ("2007 – 2011", "Module Lead", "Mindtree", "DMA controller architecture, a configurable SoC verification platform, DO-254 IP; clients included Intel and Nokia."),
    ("2006 – 2007", "Design Engineer", "Freescale (NXP)", "ARM platform SoC verification; \"BRAVO\" award for the ARM validation suite."),
    ("2004 – 2006", "Project Engineer", "Wipro", "IEEE 1394, SATA and DO-254 aircraft-engine control IP."),
    ("2002 – 2004", "Lecturer & Embedded Developer", "PCCE Goa · Infocorp", "Taught VLSI and embedded systems; built embedded products."),
]

BOOKS = [
    ("Nuts and Bolts of Open Hardware", "Technology, 2012 (ISBN 9781300339861)"),
    ("Python — a Kid's and Hardware Engineer's Perspective", "Technology, 2012 (ISBN 9781300339403)"),
    ("Understanding Indian Music through Rhythms", "Music course book, 2016 (ISBN 9781365588259)"),
    ("Noorana", "Hindi poetry, as \"Noor\""),
    ("Chuski", "Hindi poetry"),
]
ARTICLES = [
    "Mungi Udali Akashi: When the Small Transcends the Infinite (LinkedIn, Nov 2026)",
    "How to Select the Right AI Model for Your Edge Hardware (LinkedIn, Nov 2026)",
    "SDK-First Thinking: Building Developer-Friendly AI Platforms (LinkedIn, Nov 2026)",
    "Regular LinkedIn posts on SoC verification craft: bus bridges, regressions, testbench libraries, CSR maps",
]
PAPERS = [
    "SNUG 2007: Constrained Driven Random based Methodology for Verification of Generic Designs",
    "IPESC '09, Grenoble: configurable System-on-Chip methodology",
    "ICWET '11: Design and Implementation of Universal DMA Controller",
    "FOSS.IN '09: VLSI Ecosystem and Open-Source Movement, an open-hardware perspective",
    "Peer reviewer for the IEEE National Symposium on VLSI Design & Technology (2007, 2009, 2012) and DAC 2010",
]

MUSIC = [
    "Began Tabla at six in Bhopal under Shri Sanjay Mishra. Completed a 10-year course at Indira Kala Sangeet "
    "Vishwavidyalaya, Khairagarh, trained for five years with Shri Suresh Samant in Pune, and has studied for "
    "15 years with Dr. Aneesh Pradhan (Mumbai).",
    "Trained in Mridangam under the late Vidwan Dr. Nandyala Ramamurthy (Nadabrahma Thyagaraja Ashram, Bengaluru), "
    "bridging the Hindustani and Carnatic rhythm traditions. Has accompanied instrumental and vocal artists and "
    "Kathak, Bharatanatyam and contemporary dance.",
    "Composed and recorded \"Raam Gunjan\" (11 bhajans). Organizes Kavi Sammelans, and teaches through Damruki, where "
    "he plays Tabla and Mridangam with flautist Samarth on the \"Bansuri Beats\" YouTube series.",
]

POETRY = [
    "Writes Hindi poetry as \"Noor\" (light) and \"Sopaan Noor\" (steps of light): ghazals, nazms, geet and "
    "bhajans about love, longing, devotion, family, Dharma and everyday joy. Collections: \"Noorana\" and \"Chuski\".",
    "Honoured as a \"Literary Colonel\" for promoting Hindi literature. Organizes Kavi Sammelans and poetry "
    "ensembles, and often sets his own verse to tune and taal.",
]
REPERTOIRE = ("Ghazal & Nazm · Khayal, Dhrupad, Prabandh · Carnatic kritis (Thyagaraja, Purandaradasa) · "
              "Bhajan, Kirtan, Abhang (Hindi, Marathi, Kannada) · Qawwali & Sufi · Folk & film")
INTERESTS = [
    ("Dharma & the saints", "scriptures and poet-saints, from Sant Muktabai to Purandaradasa"),
    ("Jyotish", "Vedic astrology: grahas, nakshatras, panchang"),
    ("Desi sports", "Kho Kho and Kabaddi"),
    ("Solo travel", "mountains, villages, riverbeds, temples and folk rhythms"),
    ("Nada Yoga & wellness", "sound as meditation; holistic education"),
    ("Tinkering", "FPGA boards, RISC-V cores, Python, teaching kids to build"),
]
HONOURS = [
    "Distinguished Alumnus, IIM Bangalore",
    "\"Literary Colonel\" for promoting Hindi literature",
    "\"BRAVO\" award, Freescale, for the ARM validation suite",
]

EDUCATION = [
    ("M.S., VLSI CAD", "Manipal University"),
    ("PGSEM, Enterprise Management", "IIM Bangalore · Distinguished Alumnus"),
    ("DLP, Embedded Systems", "IIT Bombay (Powai)"),
    ("PG Diploma, VLSI", "Bitmapper Integration Technologies"),
    ("B.E., Electronics & Telecommunication", "BIT Durg"),
]

FOOTER = "SwapnaLoka · the pen site of Swapnil Sapre"


# ---------------------------------------------------------------- DOCX
def build_docx(path):
    from docx import Document
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Pt, RGBColor, Cm

    rgb = lambda h: RGBColor.from_string(h)
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    for side in ("left_margin", "right_margin"):
        setattr(sec, side, Cm(1.8))
    sec.top_margin, sec.bottom_margin = Cm(1.5), Cm(1.5)

    st = doc.styles["Normal"]
    st.font.name, st.font.size = "Calibri", Pt(10.5)
    st.font.color.rgb = rgb(INK)
    st.paragraph_format.space_after = Pt(4)

    def shade(cell, hexcolor):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), hexcolor)
        tcPr.append(shd)

    def no_borders(table):
        tbl = table._tbl
        tblPr = tbl.tblPr
        b = OxmlElement("w:tblBorders")
        for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
            e = OxmlElement(f"w:{edge}"); e.set(qn("w:val"), "nil"); b.append(e)
        tblPr.append(b)

    def run(p, text, size=None, bold=False, italic=False, color=None, font=None):
        r = p.add_run(text)
        r.bold, r.italic = bold, italic
        if size: r.font.size = Pt(size)
        if color: r.font.color.rgb = rgb(color)
        if font: r.font.name = font
        return r

    def heading(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12); p.paragraph_format.space_after = Pt(4)
        run(p, text.upper(), 11, True, color=NAVY)
        pPr = p._p.get_or_add_pPr()
        bdr = OxmlElement("w:pBdr"); bot = OxmlElement("w:bottom")
        bot.set(qn("w:val"), "single"); bot.set(qn("w:sz"), "8"); bot.set(qn("w:color"), GOLD); bot.set(qn("w:space"), "2")
        bdr.append(bot); pPr.append(bdr)

    def bullet(label, text=None):
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(2)
        if text:
            run(p, label + ": ", bold=True); run(p, text, color=SOFT)
        else:
            run(p, label, color=SOFT)

    # header band
    t = doc.add_table(rows=1, cols=2); no_borders(t); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c0, c1 = t.rows[0].cells
    c0.width, c1.width = Cm(4.2), Cm(13.2)
    for c in (c0, c1): shade(c, NAVY)
    c0.paragraphs[0].add_run().add_picture(str(PHOTO), width=Cm(3.6))
    c0.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = c1.paragraphs[0]; run(p, "SWAPNALOKA · PROFILE", 8.5, True, color="E9CF98")
    p = c1.add_paragraph(); run(p, TITLE, 26, True, color="FFFFFF", font="Georgia")
    p = c1.add_paragraph(); run(p, TAGLINE, 13, True, color="E9CF98", font="Georgia")
    p = c1.add_paragraph(); run(p, ROLES, 9.5, color="D6D9E4")
    p = c1.add_paragraph(); run(p, "  ·  ".join(v for _, v in CONTACT[:3]), 9, color="FFFFFF")

    # stats
    doc.add_paragraph()
    s = doc.add_table(rows=1, cols=4); no_borders(s)
    for cell, (big, small) in zip(s.rows[0].cells, STATS):
        shade(cell, "F3EDE1")
        p = cell.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run(p, big, 16, True, color=NAVY, font="Georgia")
        p = cell.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run(p, small, 8.5, color=SOFT)

    heading("About")
    for para in ABOUT:
        p = doc.add_paragraph(); run(p, para, color=SOFT)
    p = doc.add_paragraph(); run(p, "“" + QUOTE + "”", 11, italic=True, color=GOLD, font="Georgia")

    heading("Builder · Innovator · Entrepreneur")
    for a, b in VENTURES: bullet(a, b)

    heading("Advisory · Consulting · Coaching")
    for a, b in SERVICES: bullet(a, b)

    heading("Core expertise")
    et = doc.add_table(rows=(len(EXPERTISE) + 2) // 3, cols=3); no_borders(et)
    for i, item in enumerate(EXPERTISE):
        cell = et.rows[i // 3].cells[i % 3]
        run(cell.paragraphs[0], "▪ ", color=GOLD); run(cell.paragraphs[0], item, 9.5)

    heading("Career at a glance")
    ct = doc.add_table(rows=0, cols=2); no_borders(ct)
    for when, role, org, desc in CAREER:
        r = ct.add_row().cells
        r[0].width, r[1].width = Cm(2.8), Cm(14.6)
        run(r[0].paragraphs[0], when, 9.5, True, color=SAFFRON)
        p = r[1].paragraphs[0]; run(p, role, bold=True); run(p, "  ·  " + org, color=GOLD)
        p = r[1].add_paragraph(); run(p, desc, 9.5, color=SOFT)

    heading("Books & publications")
    for title, kind in BOOKS: bullet(title, kind)
    for pp in PAPERS: bullet(pp)

    for a in ARTICLES: bullet(a)

    heading("Hindi poetry · Noor")
    for para in POETRY:
        p = doc.add_paragraph(); run(p, para, color=SOFT)

    heading("Music & arts")
    for para in MUSIC:
        p = doc.add_paragraph(); run(p, para, color=SOFT)
    p = doc.add_paragraph(); run(p, "Repertoire: ", bold=True); run(p, REPERTOIRE, color=SOFT)

    heading("Honours")
    for h in HONOURS: bullet(h)

    heading("Beyond work")
    for a, b in INTERESTS: bullet(a, b)

    heading("Education")
    for deg, inst in EDUCATION: bullet(deg, inst)

    heading("Connect")
    for k, v in CONTACT: bullet(k, v)

    footer = sec.footer.paragraphs[0]; footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run(footer, FOOTER, 8, color="7A8296")
    doc.save(path)


# ---------------------------------------------------------------- PDF
def build_pdf(path):
    from reportlab.lib.colors import HexColor, white
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer,
                                    Table, TableStyle, Image, KeepTogether)
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    # Windows fonts with good Unicode coverage (·, →, —, “ ”)
    fonts = Path("C:/Windows/Fonts")
    try:
        pdfmetrics.registerFont(TTFont("Body", str(fonts / "calibri.ttf")))
        pdfmetrics.registerFont(TTFont("Body-B", str(fonts / "calibrib.ttf")))
        pdfmetrics.registerFont(TTFont("Body-I", str(fonts / "calibrii.ttf")))
        pdfmetrics.registerFont(TTFont("Serif", str(fonts / "georgia.ttf")))
        pdfmetrics.registerFont(TTFont("Serif-B", str(fonts / "georgiab.ttf")))
        pdfmetrics.registerFont(TTFont("Serif-I", str(fonts / "georgiai.ttf")))
        from reportlab.pdfbase.pdfmetrics import registerFontFamily
        registerFontFamily("Body", normal="Body", bold="Body-B", italic="Body-I", boldItalic="Body-B")
        B, BB, BI, S, SB, SI = "Body", "Body-B", "Body-I", "Serif", "Serif-B", "Serif-I"
    except Exception:
        B, BB, BI, S, SB, SI = "Helvetica", "Helvetica-Bold", "Helvetica-Oblique", "Times-Roman", "Times-Bold", "Times-Italic"

    C = lambda h: HexColor("#" + h)
    W, H = A4
    M = 16 * mm

    body = ParagraphStyle("b", fontName=B, fontSize=9.6, leading=13.4, textColor=C(SOFT), spaceAfter=4)
    h2 = ParagraphStyle("h", fontName=BB, fontSize=10.5, leading=13, textColor=C(NAVY), spaceBefore=10, spaceAfter=5)
    bl = ParagraphStyle("bl", parent=body, leftIndent=10, bulletIndent=0, spaceAfter=2.5)
    quote = ParagraphStyle("q", fontName=SI, fontSize=10.5, leading=14, textColor=C(GOLD), spaceBefore=2, spaceAfter=4)
    small = ParagraphStyle("s", parent=body, fontSize=8.6, leading=11, spaceAfter=0)

    def section(title, width=None):
        t = Table([[Paragraph(title.upper(), h2)]], colWidths=[width or (W - 2 * M)])
        t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 1, C(GOLD)),
                               ("LEFTPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                               ("TOPPADDING", (0, 0), (-1, -1), 4)]))
        return [t, Spacer(1, 4)]

    def b(label, text=None):
        if text:
            return Paragraph(f"<font name='{BB}' color='#{INK}'>{label}:</font> {text}", bl, bulletText="•")
        return Paragraph(label, bl, bulletText="•")

    header_h = 62 * mm

    def first_page(c, d):
        c.saveState()
        c.setFillColor(C(NAVY)); c.rect(0, H - header_h, W, header_h, fill=1, stroke=0)
        c.setFillColor(C(GOLD)); c.rect(0, H - header_h - 1.2 * mm, W, 1.2 * mm, fill=1, stroke=0)
        # photo in gold ring
        r = 21 * mm; cx, cy = M + r, H - header_h / 2
        c.setFillColor(C(GOLD)); c.circle(cx, cy, r + 1.3 * mm, fill=1, stroke=0)
        p = c.beginPath(); p.circle(cx, cy, r); c.clipPath(p, stroke=0, fill=0)
        c.drawImage(str(PHOTO), cx - r, cy - r, 2 * r, 2 * r, mask="auto")
        c.restoreState(); c.saveState()
        x = M + 2 * r + 9 * mm
        c.setFillColor(C("E9CF98")); c.setFont(BB, 8); c.drawString(x, H - 17 * mm, "SWAPNALOKA  ·  PROFILE")
        c.setFillColor(white); c.setFont(SB, 26); c.drawString(x, H - 28 * mm, TITLE)
        c.setFillColor(C("E9CF98")); c.setFont(SB, 13); c.drawString(x, H - 36 * mm, TAGLINE)
        ps = ParagraphStyle("r", fontName=B, fontSize=9, leading=12, textColor=C("D6D9E4"))
        para = Paragraph(ROLES, ps); _, ph = para.wrap(W - x - M, 30 * mm); para.drawOn(c, x, H - 40 * mm - ph)
        c.setFillColor(white); c.setFont(B, 8.6)
        c.drawString(x, H - 54 * mm, "  ·  ".join(v for _, v in CONTACT[:3]))
        c.restoreState(); footer(c, d)

    def footer(c, d):
        c.saveState(); c.setFont(B, 7.8); c.setFillColor(C("7A8296"))
        c.drawString(M, 9 * mm, FOOTER); c.drawRightString(W - M, 9 * mm, f"Page {d.page}")
        c.restoreState()

    doc = BaseDocTemplate(str(path), pagesize=A4, leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=16 * mm,
                          title="SwapnaLoka — Profile of Swapnil Sapre", author="Swapnil Sapre")
    f1 = Frame(M, 16 * mm, W - 2 * M, H - header_h - 6 * mm - 16 * mm, id="f1")
    f2 = Frame(M, 16 * mm, W - 2 * M, H - M - 16 * mm, id="f2")
    doc.addPageTemplates([PageTemplate("first", [f1], onPage=first_page, autoNextPageTemplate="rest"),
                          PageTemplate("rest", [f2], onPage=footer)])

    story = []
    # stats strip
    cw = (W - 2 * M) / 4
    sb = ParagraphStyle("sb", fontName=SB, fontSize=15, leading=18, textColor=C(NAVY), alignment=1)
    ss = ParagraphStyle("ss", parent=small, alignment=1)
    st = Table([[[Paragraph(x, sb), Paragraph(y, ss)] for x, y in STATS]], colWidths=[cw] * 4)
    st.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), C("F3EDE1")),
                            ("LINEAFTER", (0, 0), (-2, -1), 0.6, C("E4DCCB")),
                            ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7)]))
    story += [st, Spacer(1, 4)]

    story += section("About")
    story += [Paragraph(x, body) for x in ABOUT]
    story.append(Paragraph("“" + QUOTE + "”", quote))

    story += section("Builder · Innovator · Entrepreneur")
    story += [b(x, y) for x, y in VENTURES]

    story += section("Advisory · Consulting · Coaching")
    story += [b(x, y) for x, y in SERVICES]

    rows = [EXPERTISE[i:i + 3] for i in range(0, len(EXPERTISE), 3)]
    et = Table([[Paragraph(f"<font color='#{GOLD}'>▪</font> {c}", small) for c in r] for r in rows],
               colWidths=[(W - 2 * M) / 3] * 3)
    et.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                            ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story.append(KeepTogether(section("Core expertise") + [et]))

    story += section("Career at a glance")
    when_s = ParagraphStyle("w", fontName=BB, fontSize=8.8, leading=12, textColor=C(SAFFRON))
    role_s = ParagraphStyle("r", fontName=BB, fontSize=9.8, leading=12.5, textColor=C(INK))
    rows = [[Paragraph(w, when_s), [Paragraph(f"{r} <font name='{B}' color='#{GOLD}'>· {o}</font>", role_s),
                                    Paragraph(d, small)]] for w, r, o, d in CAREER]
    ct = Table(rows, colWidths=[26 * mm, W - 2 * M - 26 * mm])
    ct.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                            ("LINEBELOW", (0, 0), (-1, -2), 0.4, C("E4DCCB"))]))
    story.append(ct)

    story += section("Books & publications")
    story += [b(f"<i>{t}</i>", k) for t, k in BOOKS]
    story += [b(x) for x in PAPERS]

    story += [b(x) for x in ARTICLES]

    story += section("Hindi poetry · Noor")
    story += [Paragraph(x, body) for x in POETRY]

    story += section("Music & arts")
    story += [Paragraph(x, body) for x in MUSIC]
    story.append(Paragraph(f"<font name='{BB}' color='#{INK}'>Repertoire:</font> {REPERTOIRE}", body))

    story += section("Honours")
    story += [b(x) for x in HONOURS]

    story += section("Beyond work")
    story += [b(x, y) for x, y in INTERESTS]

    half = (W - 2 * M) / 2 - 4 * mm
    left = section("Education", half) + [b(d, i) for d, i in EDUCATION]
    right = section("Connect", half) + [b(k, v) for k, v in CONTACT]
    two = Table([[left, right]], colWidths=[half + 8 * mm, half])
    two.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                             ("RIGHTPADDING", (0, 0), (0, -1), 8 * mm)]))
    story.append(two)
    logo = ROOT / "assets" / "img" / "swapnaloka_logo.png"
    cta = ParagraphStyle("cta", fontName=SI, fontSize=11.5, leading=16, textColor=C(NAVY), alignment=1)
    story.append(KeepTogether([Spacer(1, 6 * mm), Image(str(logo), 28 * mm, 28 * mm), Spacer(1, 2 * mm),
              Paragraph("Open for advisory, consulting, coaching, mentoring and speaking engagements, "
                        "and always happy to make music and poetry together.", cta)]))

    doc.build(story)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    build_docx(OUT / f"{NAME}.docx")
    build_pdf(OUT / f"{NAME}.pdf")
    print("built", OUT / f"{NAME}.docx", "and .pdf")
