# ----- Mini Projet ------
# | Nom :  Belkasmi      |
# | Prenom : Abdeldjalil |
# ------------------------
from PIL import Image
from colorama import Fore,Style

COLOR_INDEX = {
    'red' : 0,
    'green': 1,
    'blue' : 2
}
COLORS = {
    'red' : (255,0,0), 
    'blue' : (0,0,255),
    'green' : (0,255,0),
    'white' : (255,255,255),
    'black': (0,0,0) 
}

def convertir_image(img,name,old_color_name,new_color_name):
    new_img = Image.new('RGB',img.size,'white')
    w , h = img.size
    # Verify That Color is RGB
    if old_color_name  not in COLOR_INDEX or new_color_name not in COLOR_INDEX:
        print(Fore.RED,"Invalid Color",Style.RESET_ALL)

    idx = COLOR_INDEX[old_color_name]
    newColor = COLORS[new_color_name]
    
    for i in range(h):
        for j in range(w):
            r,g,b = img.getpixel((j,i))
            pixel = (r,g,b)
            others = pixel[:idx] + pixel[idx:]
            if pixel[idx] >= others[0] + 25 and pixel[idx] >= others[1] + 25:
                new_img.putpixel((j,i),newColor)
            else:
                new_img.putpixel((j,i), pixel)
    
    new_img.save(f"{name}_{old_color_name}_to_{new_color_name}.png","PNG")

def image_mirroir(img,name):
    img_mirroir = Image.new('RGB',img.size,'white')
    w , h = img.size
    for i in range(h):
        for j in range(w):
            r,g,b = img.getpixel((j,i))
            img_mirroir.putpixel((w-1-j,i),(r,g,b))
    img_mirroir.save(f"{name}_mirroir.png","PNG")
def delta_energie(pixel1,pixel2):
    r1,g1,b1 = pixel1
    r2,g2,b2 = pixel2
    return (r1-r2)**2+(g1-g2)**2+(b1 -b2)**2
def detect_object(img,name):
    edges = Image.new('RGB', img.size, 'white')
    w,h = img.size
    T = [-1,0,1]

    for x in range(w):
        for y in range(h):
            voisinage = []   
            pixel = img.getpixel((x,y))

            for dx in T:
                for dy in T:
                    if dx == 0 and dy == 0:
                        continue

                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < w and 0 <= ny < h:
                        p2 = img.getpixel((nx,ny))
                        d = delta_energie(pixel,p2)
                        voisinage.append(d)

            if any(d > 200 for d in voisinage):
                edges.putpixel((x,y),(0,0,0))

    edges.save(f"{name}_objects.png","PNG")
def brouiller_image(img, name):
    img_br = Image.new('RGB', img.size, 'white')
    w, h = img.size
    T = [i for i in range(5)]

    for x in range(w):
        for y in range(h):
            moy_r = moy_g = moy_b = 0 # Moyenne (RGB)
            count = 0 # N.Pixels Parcourus

            for dx in T:
                for dy in T:
                    if dx == 0 and dy == 0: # Skip (x,y)
                        continue
                    # Pixels Voisins
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < w and 0 <= ny < h:
                        r,g,b = img.getpixel((nx,ny))
                        moy_r += r
                        moy_g += g
                        moy_b += b
                        count += 1
            if count: 
                img_br.putpixel((x,y),(moy_r//count , moy_g//count, moy_b//count) )# Integer Division        
    img_br.save(f"{name}_brouille.png",'PNG')





# --- Main ---
if __name__ == "__main__":
    # Création Image
    img = Image.open('segmenttrees.jpg').convert('RGB')
    # Convertir 
    convertir_image(img,'segmenttrees','blue','green') # Blue To Green
    # Mirroir
    image_mirroir(img,'segmenttrees') 
    # Detecter Objet
    detect_object(img,'segmenttrees')
    # Brouiller
    brouiller_image(img,'segmenttrees')
    

    print(Fore.GREEN," Succés : Images Genérées ",Style.RESET_ALL)