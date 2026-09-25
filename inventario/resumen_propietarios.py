import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
D=os.path.dirname(os.path.abspath(__file__))
ns={"__file__":os.path.join(D,"generar.py")}
exec(open(ns["__file__"]).read().split("W,H=A4")[0],ns)
O=list(enumerate(ns["OBRAS"],1))
st=getSampleStyleSheet(); c=ParagraphStyle("c",parent=st["Normal"],fontSize=11,leading=15)
def fila(nombre,filtro,extra=lambda i,o:""):
    L=[(i,o) for i,o in O if filtro(o[5])]
    return [nombre,str(len(L)),Paragraph(", ".join(f"{i}{extra(i,o)}" for i,o in L),c)]
data=[["Propietario","Cantidad","Obras N.º"],
 fila("Andrés Schwalb",lambda p:p=="Andrés Schwalb"),
 fila("Álvaro Sousa",lambda p:p=="Álvaro Sousa"),
 fila("Desconocido",lambda p:p.startswith("Desconocido"),lambda i,o:" (vendido)" if "vendido" in o[5] else "")]
data.append(["Total",str(len(O)),""])
t=Table(data,colWidths=[140,70,280])
t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#333333")),("TEXTCOLOR",(0,0),(-1,0),colors.white),
 ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("FONTNAME",(0,-1),(-1,-1),"Helvetica-Bold"),("FONTSIZE",(0,0),(-1,-1),11),
 ("ALIGN",(1,0),(1,-1),"CENTER"),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("GRID",(0,0),(-1,-1),0.5,colors.grey),
 ("ROWBACKGROUNDS",(0,1),(-1,-2),[colors.white,colors.HexColor("#f2f2f2")]),("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8)]))
h=ParagraphStyle("h",parent=st["Title"],fontSize=22); s=ParagraphStyle("s",parent=st["Normal"],fontSize=12,alignment=1)
doc=SimpleDocTemplate(os.path.join(D,"Resumen_por_propietario.pdf"),pagesize=A4,title="Resumen por propietario")
doc.build([Paragraph("PINTURAS PILAR SOUSA",h),Paragraph("Inventario septiembre 2026 — Resumen por propietario",s),Spacer(1,25),t])
