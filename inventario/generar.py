from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os
D=os.path.dirname(os.path.abspath(__file__))
# (foto, titulo, tecnica, año, medidas, propietario, nota)
OBRAS=[
 ("01.jpg","Sin título","Técnica mixta sobre cartulina","Sin fecha","32,5 cm x 49,5 cm","Andrés Schwalb",""),
 ("02.jpg","Sin título","Técnica mixta sobre tela","2021","110 cm x 110 cm","Álvaro Sousa","Andrés Schwalb no recuerda"),
 ("03.jpg","Sin título","Acrílico sobre tela","2019","122 cm x 92 cm","Andrés Schwalb",""),
 ("04.jpg","Sin título","Acrílico sobre tela","Sin fecha","100 cm x 150 cm","Andrés Schwalb",""),
 ("05.jpg","Sin título","Óleo sobre tela","2018","80 cm x 120 cm","Álvaro Sousa",""),
 ("06.jpg","Sin título","Óleo sobre tela","2018","60 cm x 50 cm","Álvaro Sousa",""),
 ("07.jpg","Sin título","Técnica mixta sobre tela","2019","140 cm x 34 cm / 140 cm x 22 cm / 140 cm x 43 cm","Andrés Schwalb","Tríptico"),
 ("08.jpg","Sin título","Acrílico sobre tela","2018","59 cm x 79 cm","Andrés Schwalb",""),
 ("09.jpg","Sin título","Dibujo, técnica mixta sobre tela","2018","87 cm x 81 cm","Desconocido (vendido)","Según Andrés Schwalb fue vendido; no sabe a quién"),
 ("10.jpg","Sin título","Técnica mixta sobre tela","2020","60 cm x 120 cm","Andrés Schwalb",""),
 ("11.jpg","Sin título","Óleo sobre tela","2023","64 cm x 79 cm","Álvaro Sousa",""),
 ("12.jpg","Sin título","Óleo sobre tela","2006","64 cm x 79 cm","Andrés Schwalb","Andrés Schwalb lo dona"),
 ("13.jpg","Sin título","Técnica mixta sobre MDF","2017","61 cm x 74 cm","Andrés Schwalb",""),
 ("14.jpg","Sin título","Técnica mixta sobre tela","2020","50 cm x 70 cm","Andrés Schwalb",""),
 ("15.jpg","Sin título","Acrílico sobre tela","Sin fecha","50 cm x 40 cm","Álvaro Sousa",""),
 ("16.jpg","Sin título","Acrílico sobre tela","Sin fecha","120 cm x 90 cm","Andrés Schwalb",""),
 ("17.jpg","Sin título","Acrílico sobre tela","Sin fecha","78 cm x 36 cm","Desconocido","Andrés Schwalb no sabe quién es el propietario"),
 ("18.jpg","Sin título","Acrílico sobre tela","Sin fecha","120 cm x 45 cm","Andrés Schwalb",""),
 ("19.jpg","Sin título","Acrílico sobre tela","Sin fecha","51 cm x 40 cm","Andrés Schwalb",""),
 ("20.jpg","Sin título","Acrílico sobre tela","Sin fecha","100 cm x 70 cm","Andrés Schwalb","Díptico"),
 ("21.jpg","Sin título","Acrílico sobre tela","Sin fecha","70 cm x 70 cm / 70 cm x 70 cm / 70 cm x 70 cm","Andrés Schwalb","Tríptico"),
 ("22.jpg","Sin título","Óleo sobre tela","Sin fecha","90 cm x 90 cm","Álvaro Sousa",""),
 ("23.jpg","Sin título","Desconocida","Sin fecha","Desconocidas","Álvaro Sousa",""),
]
W,H=A4; c=canvas.Canvas(os.path.join(D,"Cuadros_Pilar_Sousa_Galeria.pdf"),pagesize=A4)
c.setTitle("Cuadros Pilar Sousa Galería")
for i,(f,t,tec,a,m,p,n) in enumerate(OBRAS,1):
    c.setFont("Helvetica-Bold",20); c.drawCentredString(W/2,H-60,"Cuadros Pilar Sousa Galería")
    c.setFont("Helvetica",10); c.drawCentredString(W/2,H-78,"Inventario documentado de obras")
    c.line(50,H-90,W-50,H-90)
    img=ImageReader(os.path.join(D,f)); iw,ih=img.getSize()
    s=min((W-100)/iw,(H-360)/ih); w,h=iw*s,ih*s
    c.drawImage(img,(W-w)/2,H-110-h,w,h)
    y=H-150-h
    c.setFont("Helvetica-Bold",16); c.drawString(50,y,f"Obra N.º {i}")
    for k,v in [x for x in (("Título",t),("Técnica",tec),("Año",a),("Medidas",m),("Propietario",p),("Nota",n)) if x[1]]:
        y-=26; c.setFont("Helvetica-Bold",12); c.drawString(50,y,k+":")
        c.setFont("Helvetica",12); c.drawString(140,y,v)
    c.setFont("Helvetica",9); c.drawCentredString(W/2,30,f"Página {i} de {len(OBRAS)}")
    c.showPage()
c.save()
