import fitz  # PyMuPDF
import sys

def extract_first_page(pdf_path, output_image):
    try:
        doc = fitz.open(pdf_path)
        page = doc.load_page(0)  # first page
        pix = page.get_pixmap()
        pix.save(output_image)
        print(f"First page saved as {output_image}")
        doc.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_first_page("../Documents/ima/ima x 教师群体.pdf", "cover.png")
