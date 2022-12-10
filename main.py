from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, rows in df.iterrows():
    pdf.add_page()
    # Set up the Header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=rows["Topic"], align='L', ln=1, border=0)
    for y in range(20, 298, 10):
        pdf.line(x1=10, y1=y, x2=200, y2=y)

    # Set up the Footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=rows["Topic"], align="R")

    for i in range(rows["Pages"]-1):
        pdf.add_page()
        # Set up the Footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=rows["Topic"], align="R")
        for y in range(20, 298, 10):
            pdf.line(x1=10, y1=y, x2=200, y2=y)

pdf.output("Output.pdf")
