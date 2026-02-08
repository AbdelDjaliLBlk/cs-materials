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

# --- Main ---
if __name__ == "__main__":
    # Création Image
    img = Image.open('segmenttrees.jpg').convert('RGB')
    # Convertir 
    convertir_image(img,'segmenttrees','blue','green') # Blue To Green
    # Mirroir
    image_mirroir(img,'segmenttrees') 


    print(Fore.GREEN,"Image Genérée",Style.RESET_ALL)