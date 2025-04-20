import os
from pygments import highlight
from pygments.lexers import guess_lexer_for_filename
from pygments.formatters import HtmlFormatter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import tempfile
import imgkit

# Cấu hình đường dẫn
code_dir = "backend"
output_pdf = "all_code.pdf"
imgkit_config = imgkit.config()  # cấu hình wkhtmltoimage nếu cần

# Tạo PDF
c = canvas.Canvas(output_pdf, pagesize=A4)
width, height = A4
margin = 50

def add_image_to_pdf(image_path):
    c.drawImage(ImageReader(image_path), margin, margin, width - 2 * margin, height - 2 * margin, preserveAspectRatio=True, anchor='n')
    c.showPage()

for root, _, files in os.walk(code_dir):
    for file in files:
        filepath = os.path.join(root, file)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                code = f.read()
                lexer = guess_lexer_for_filename(filepath, code)
                formatter = HtmlFormatter(full=True, style='monokai')
                highlighted_code = highlight(code, lexer, formatter)

                with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as html_file:
                    html_file.write(highlighted_code.encode('utf-8'))
                    html_path = html_file.name

                with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as img_file:
                    img_path = img_file.name
                    imgkit.from_file(html_path, img_path, config=imgkit_config)
                    add_image_to_pdf(img_path)

        except Exception as e:
            print(f"Lỗi với {filepath}: {e}")

# Lưu file PDF cuối cùng
c.save()
print(f"✅ Đã tạo file PDF: {output_pdf}")
