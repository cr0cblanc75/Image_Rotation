from PIL import *
import math 

img = Image.open("joconde.jpg")
largeur, hauteur = img.size


def echange_pix(xa,ya):
    largeur, hauteur = img.size
    
    xb = ya
    yb = hauteur - 1 - xa
    return xb, yb


def rota_g():
    img2 = Image.new("RGB",(512, 512))
    img2 = Image.open("joconde_turn.jpg")

    for i in range(largeur):
        for j in range(hauteur):
            img2.putpixel((echange_pix(i,j)), img.getpixel((i,j)))

    img2.show()


def rota_cos(degree):
    img3 = Image.new("RGB",(600, 600))
    img3 = Image.open("joconde_turn_cos.jpg")
    
    midx = largeur//2
    midy = hauteur//2
    rads = math.radians(degree)

    for i in range(largeur):
        for j in range(hauteur):
            x = ((i-midx)*math.cos(rads)) + ((j-midy)*math.sin(rads))
            y = (-(i-midx)*math.sin(rads)) + ((j-midy)*math.cos(rads))
        
            x = round(x) + midx 
            y = round(y) + midy
            
            print(x, y)
            
            if (x >= 0 and y >= 0 and x < hauteur and  y < largeur):
                img3.putpixel((x,y), img.getpixel((i,j)))
    img3.show()
    

def echange_quadrant(image,xa,ya,xb,yb,n):
    



















