import os, runpy, io
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(D,"generar.py")).read()
ns={"__file__":__file__}; exec(src.split("W,H=A4")[0].replace("import os, io","import os, io"),ns)
OBRAS=ns["OBRAS"]
from collections import Counter
print(Counter(o[5] for o in OBRAS))
A=[(i,o) for i,o in enumerate(OBRAS,1) if o[5]=="Andrés Schwalb"]
print([i for i,_ in A])
W,H=A4; c=canvas.Canvas(os.path.join(D,"Obras_Andres_Schwalb.pdf"),pagesize=A4)
c.setTitle("Obras de Andrés Schwalb")
def head():
    c.setFont("Helvetica-Bold",18); c.drawCentredString(W/2,H-55,"PINTURAS PILAR SOUSA")
    c.setFont("Helvetica",12); c.drawCentredString(W/2,H-75,f"Obras de propiedad de Andrés Schwalb — Total: {len(A)} obras")
    c.line(40,H-88,W-40,H-88)
head(); y=H-100; R=95
for i,(f,t,tec,a,m,p,n) in A:
    if y-R<40: c.showPage(); head(); y=H-100
    im=Image.open(os.path.join(D,f)).convert("RGB"); im.thumbnail((300,300))
    b=io.BytesIO(); im.save(b,"JPEG",quality=70); b.seek(0)
    iw,ih=im.size; s=min(110/iw,(R-10)/ih)
    c.drawImage(ImageReader(b),45,y-5-ih*s,iw*s,ih*s)
    x=170; c.setFont("Helvetica-Bold",13); c.drawString(x,y-20,f"Obra N.º {i}")
    c.setFont("Helvetica",10)
    for k,l in enumerate([f"{t} · {tec}",f"Año: {a}   ·   Medidas: {m}"]+([f"Nota: {n}"] if n else [])):
        c.drawString(x,y-38-k*14,l)
    y-=R; c.setStrokeGray(0.8); c.line(40,y+2,W-40,y+2); c.setStrokeGray(0)
c.save()
