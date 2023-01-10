from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
  
class Generate:
    def __init__(self, img, title, price):
        self.img = img
        self.title = title
        self.price = price

    def textfy(self):
        #Abre a img
        imagem = Image.open(self.img)

        #abre sobreposição
        draw = ImageDraw.Draw(imagem)

        #definir fonte
        fonteB = ImageFont.truetype('assets/AmsiProAKSNarrow-Regular.ttf', 40)
        fonteS = ImageFont.truetype('assets/AmsiProAKSNarrow-Regular.ttf', 24)

        #escrever texto
        draw.text((50, 52), self.title, font=fonteB)
        draw.text((50, 101), self.price, font=fonteS)

        # salvar img
        imagem.save('/tmp/newImage.jpg', 'JPEG')

        return 'sucess'
