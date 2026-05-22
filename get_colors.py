from PIL import Image

def get_colors(image_path):
    img = Image.open(image_path).convert('RGB')
    w, h = img.size
    
    # Top-left (usually white)
    tl = img.getpixel((10, 10))
    # Bottom-right (the green part)
    br = img.getpixel((w-10, h-10))
    # Bottom-left
    bl = img.getpixel((10, h-10))
    # Top-right
    tr = img.getpixel((w-10, 10))
    
    print(f"Top-Left: #{tl[0]:02x}{tl[1]:02x}{tl[2]:02x}")
    print(f"Bottom-Right: #{br[0]:02x}{br[1]:02x}{br[2]:02x}")
    print(f"Bottom-Left: #{bl[0]:02x}{bl[1]:02x}{bl[2]:02x}")
    print(f"Top-Right: #{tr[0]:02x}{tr[1]:02x}{tr[2]:02x}")

if __name__ == "__main__":
    get_colors("cover.png")
