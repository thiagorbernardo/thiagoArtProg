
largura = 1920
altura = 1080
def setup():
    

    size(largura, altura)
    img = loadImage("back.jpg")
    #position(img)
    #blur(img)
    cascate(img)
    #colors(img)
    image(img, 0, 0)
    #sla(img)
    f = loadFont("#Thiago.vlw")
    textSize(1)
    textFont(f)
    fill(0,173,216,230)
    text("thiagoArtProg", 12, 60)
    
    save("saida/Back1.jpg")
    
    
def position(img):
    for i in range(len(img.pixels)):
        if(i+200 < len(img.pixels)):
            if(i%7 == 0):
                img.pixels[i] = img.pixels[i+200] 
                
                
def blur(img):
    for i in range(largura):
        for j in range(altura):
            indice = (j * largura) + i
            diff = -25 + floor(random(50))

            if (indice + diff < largura * altura):
                img.pixels[indice] = img.pixels[indice + diff]
                

def colors(img):
    for i in range(len(img.pixels)):
        vermelho = red(img.pixels[i])
        verde = green(img.pixels[i])
        azul = blue(img.pixels[i])
        
        if (vermelho > 50 and verde > 50 and azul > 50):
            vermelho = random(0,100)
            verde = random(0,100)
            azul = random(0,100)
            
        img.pixels[i] = color(vermelho, verde, azul)
        
def sla(img):
    
    
    for i in range(altura):
        largura_diff = -largura/2+random(largura)
        altura_diff = -altura/2+random(altura)
        
        r = floor(random(50))
        if(r> 48):
            image(img, largura_diff, i, largura, 1)
            
def cascate(img):
    #var = len(img.pixels)
    for i in range(len(img.pixels)):
        vermelho = red(img.pixels[i])
        verde = green(img.pixels[i])
        azul = blue(img.pixels[i])
        
        """if (i % 2 == 0):
            vermelho = random(0,vermelho)
            verde = random(0,verde)
            azul = random(0,azul)
            img.pixels[var] = color(vermelho, verde, azul)"""
        img.pixels[i] = color(vermelho, verde, azul)
        #var = var - 1
