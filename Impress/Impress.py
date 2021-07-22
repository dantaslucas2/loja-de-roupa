from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm
from reportlab.platypus import Flowable, Table, SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import subprocess

class Documento(object):
    """docstring for Documento."""

    def __init__(self, produtos, compra=None):
        self.altura =  8.5*inch
        self.largura = 11*inch

        self.pdf = canvas.Canvas("homu.pdf",bottomup=0)
        self.pdf.setPageSize((self.largura, self.altura))

        self.fonte = "Helvetica"
        self.pdf.setFont(self.fonte, 11)
        self.linha_corte()
        self.linha_documento(30, compra, produtos)

        self.pdf.showPage()
        self.pdf.save()


        subprocess.Popen(['homu.pdf'], shell=True)

    def linha_corte(self):
        """ Cria linha que separa a folha A4"""
        self.pdf.setDash(6,3)
        self.pdf.line(self.largura/2, 0, self.largura/2, self.altura)
        self.pdf.setDash(1)

    def linha_documento(self, parametro, compra, produtos):
        #tabela
        self.celula_largura = (self.largura-parametro - self.largura/2+parametro)/10
        self.celula_altura = (self.altura-parametro - self.altura/2+parametro)/5

        #emitidor
        self.pdf.line(self.largura/2+parametro, parametro, self.largura/2+parametro, self.altura-parametro) #linha esquerda
        self.pdf.line(self.largura-parametro, parametro, self.largura-parametro, self.altura-parametro) #linha direita
        self.pdf.line(self.largura/2+parametro, parametro, self.largura-parametro, parametro)
        self.pdf.line(self.largura/2+parametro, self.altura-parametro, self.largura-parametro, self.altura-parametro)
        self.pdf.setFont(self.fonte, 18)
        self.pdf.drawCentredString(self.largura/4*3, parametro+25, "Patricia Máximo Modas Plus Size")
        self.pdf.setFont(self.fonte+"-Bold", 15)
        self.pdf.drawCentredString(self.largura/4*3, parametro+50, "Termo de recebimento de mercadoria")
        self.pdf.setFont(self.fonte, 14)
        self.pdf.drawString(self.largura/2+parametro+15, parametro+90, "Cliente: ")
        cliente = compra[4]
        self.pdf.drawString(self.largura/2+parametro+70, parametro+90, cliente)
        self.pdf.drawString(self.largura/2+parametro+15, parametro+105, "Bairro: ")
        bairro = compra[5]
        self.pdf.drawString(self.largura/2+parametro+60, parametro+105, bairro)
        self.pdf.drawString(self.largura/2+parametro+15, parametro+120, "Data: ")
        data = compra[2]
        self.pdf.drawString(self.largura/2+parametro+60, parametro+120, data)
        self.pdf.drawString(self.largura/4*3, parametro+90, "Pagamento: ")
        pagamento = compra[6]
        self.pdf.drawString(self.largura/4*3+78, parametro+90, pagamento)

        self.pdf.drawString(self.largura/4*3, parametro+105, "Endereço: ")
        endereco = compra[0]
        self.pdf.drawString(self.largura/4*3, parametro+120, endereco)


        self.pdf.setFont(self.fonte, 11)
        self.pdf.line(self.largura/2+parametro+15, self.altura-parametro-30, self.largura-parametro-15, self.altura-parametro-30)
        self.pdf.setFont("Helvetica", 10)
        self.pdf.drawCentredString(self.largura/4*3, self.altura-parametro-20, "(Assinatura)")
        self.pdf.drawCentredString(self.largura/4*3, self.altura-parametro-10, "Rio de Janeiro - 2020")

        #tabela
        self.pdf.setFont(self.fonte, 10)
        print("self.celula_largura: ", self.celula_largura)
        laargura = (self.celula_largura)*3/2
        print("laargura: ", laargura)

        teste = [['','','',''],['','','',''],['','','',''],['','','',''],['','','',''],['','','',''],['','','',''],['','','',''],['','','','']]
        tablee = Table(teste, colWidths=laargura)
        tablee.setStyle([("ALIGN", (0,0), (-1,-1), "CENTER"),
                ("BACKGROUND", (0,0), (-1,-1), colors.lavenderblush),
                ('TEXTCOLOR',(0,-1),(-1,-1),colors.white),
                ("FONTSIZE", (0,0), (-1,-1), 8),
                ('GRID', (0,0),(-1,-1),1,colors.black)])
        tablee.wrapOn(self.pdf, self.largura, self.altura)

        tablee.drawOn(self.pdf, self.largura/2 + 80, 180)

        dado = [["Item", "Tamanho", "Estampa","Valor"]]


        for i in produtos:
            dado.insert(0,i)
        print(dado)

        table = Table(dado, colWidths=laargura)
        table.setStyle([("ALIGN", (0,-1), (-1,-1), "CENTER"),
                ("INNERGRID", (0,0), (2,2), 0.5, colors.black),
                ("BACKGROUND", (0,0), (-1,-1), colors.lavenderblush),
                ("BACKGROUND", (0,-1), (-1,-1), colors.gray),
                ('TEXTCOLOR',(0,-1),(-1,-1),colors.white),
                ("FONTSIZE", (0,0), (-1,-1), 8),
                ('GRID', (0,0),(-1,-1),1,colors.black),
                ('BOX', (0,0), (-1,-1), 0.25, colors.black)])

        table.wrapOn(self.pdf, self.largura, self.altura)

        table.drawOn(self.pdf, self.largura/2 + 80, 180)

        #recebedor
        self.pdf.line(0+parametro, parametro, self.largura/2-parametro, parametro) #linha superior
        self.pdf.line(0+parametro, self.altura-parametro, self.largura/2-parametro, self.altura-parametro) #linha inferior
        self.pdf.line(parametro, parametro, parametro, self.altura-parametro) #linha esquerda
        self.pdf.line(self.largura/2-parametro, parametro, self.largura/2-parametro, self.altura-parametro) #linha esquerda
        self.pdf.setFont(self.fonte, 17)
        self.pdf.drawCentredString(self.largura/4, parametro+25, "Patricia Máximo Modas Plus Size")

        self.pdf.setFont(self.fonte+"-Bold", 15)
        self.pdf.drawCentredString(self.largura/4, parametro+50, "Termo de recebimento de mercadoria")
        self.pdf.setFont(self.fonte, 14)
        self.pdf.drawString(parametro+15, parametro+90, "Cliente: ")
        cliente = compra[1]
        self.pdf.drawString(parametro+70, parametro+90, cliente)
        self.pdf.drawString(parametro+15, parametro+105, "Bairro: ")
        bairro = compra[0]
        self.pdf.drawString(parametro+60, parametro+105, bairro)
        self.pdf.drawString(parametro+15, parametro+120, "Data: ")
        self.pdf.drawString(parametro+60, parametro+120, "**/**/**")
        self.pdf.setFont(self.fonte, 11)
        self.pdf.line(parametro+15, self.altura-parametro-30, self.largura/2-parametro-15, self.altura-parametro-30)
        self.pdf.setFont("Helvetica", 10)
        self.pdf.drawCentredString(self.largura/4, self.altura-parametro-20, "(Assinatura)")
        self.pdf.drawCentredString(self.largura/4, self.altura-parametro-10, "Rio de Janeiro - 2020")


if __name__ == '__main__':
    lista = [["Macacã", "XG", "Onça","100.0"], ["Vestido Longo", "GG", "Preto","90.0"],["Vestido curto", "M", "Branco","70"]]
    compra = ["Rua dos Romeros", "200.0", "18-05-2020","10","Ana Maria","Olaria","Dinheiro"]
    #comprac = [endereco, valor, data, frete, cliente, bairro, metodo_pg]
    #iten = [tipo, tamanho, estampa, valor]
    Documento(lista,compra)
