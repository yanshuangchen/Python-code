import fitz
import os

def pdf2img(pdf_path, zoom_x, zoom_y):
    output_folder = r"C:\Users\86138\Desktop\picnic7"
    os.makedirs(output_folder, exist_ok=True)  # Create a folder to store the images
    
    for file_name in os.listdir(pdf_path):  # Iterate over files in the pdf_path folder
        if file_name.endswith(".pdf"):  # Process only PDF files
            pdf_file = os.path.join(pdf_path, file_name)  # Build the full path to the PDF file
            doc = fitz.open(pdf_file)  # Open the document
            
            for page in doc:  # Iterate over pages
                pix = page.get_pixmap(matrix=fitz.Matrix(zoom_x, zoom_y))  # Render the page as an image
                image_path = os.path.join(output_folder, f'page-{page.number+1}.png')  # Image save path
                pix.save(image_path, "png")  # Save the image as PNG format
            
            doc.close()  # Close the document

if __name__ == "__main__":
    pdf_directory = r"C:\Users\86138\Desktop\pic"
    zoom_x = 8
    zoom_y = 8
    pdf2img(pdf_directory, zoom_x, zoom_y)