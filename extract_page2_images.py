import fitz  # PyMuPDF
import os

def extract_images_from_page(pdf_path, page_index):
    doc = fitz.open(pdf_path)
    page = doc[page_index]
    image_list = page.get_images(full=True)
    
    print(f"Found {len(image_list)} images on page {page_index + 1}")
    
    for i, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        filename = f"page_{page_index+1}_img_{i+1}.{image_ext}"
        with open(filename, "wb") as f:
            f.write(image_bytes)
        print(f"Saved {filename}")
    
    doc.close()

if __name__ == "__main__":
    # Page 2 is index 1
    extract_images_from_page("../Documents/ima/ima x 教师群体.pdf", 1)
