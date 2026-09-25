from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os
D=os.path.dirname(os.path.abspath(__file__))
# (foto, titulo, tecnica, medidas, propietario)
OBRAS=[("01.jpg","Sin título","Técnica mixta sobre cartulina","32,5 cm x 49,5 cm","Por completar")]
W,H=A4; c=canvas.Canvas(os.path.join(D,"Cuadros_Pilar_Sousa_Galeria.pdf"),pagesize=A4)
c.setTitle("Cuadros Pilar Sousa Galería")
for i,(f,t,tec,m,p) in enumerate(OBRAS,1):
    c.setFont("Helvetica-Bold",20); c.drawCentredString(W/2,H-60,"Cuadros Pilar Sousa Galería")
    c.setFont("Helvetica",10); c.drawCentredString(W/2,H-78,"Inventario documentado de obras")
    c.line(50,H-90,W-50,H-90)
    img=ImageReader(os.path.join(D,f)); iw,ih=img.getSize()
    s=min((W-100)/iw,(H-360)/ih); w,h=iw*s,ih*s
    c.drawImage(img,(W-w)/2,H-110-h,w,h)
    y=H-150-h
    c.setFont("Helvetica-Bold",16); c.drawString(50,y,f"Obra N.º {i}")
    for k,v in (("Título",t),("Técnica",tec),("Medidas",m),("Propietario",p)):
        y-=26; c.setFont("Helvetica-Bold",12); c.drawString(50,y,k+":")
        c.setFont("Helvetica",12); c.drawString(140,y,v)
    c.setFont("Helvetica",9); c.drawCentredString(W/2,30,f"Página {i} de {len(OBRAS)}")
    c.showPage()
c.save()
