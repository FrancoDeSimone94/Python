from pathlib import Path
from docx import Document
import os

# Ruta segura del archivo
template_path = Path(__file__).resolve().parent / "plantilla.docx"

# Verificar si el archivo existe
if not template_path.is_file():
    print(f"❌ Archivo no encontrado en: {template_path}")
else:
    print(f"✅ Archivo encontrado en: {template_path}")

    # Intentar abrir con python-docx
    try:
        doc = Document(str(template_path))
        print("✅ La plantilla se abrió correctamente. Es un .docx válido.")
        # Mostrar las primeras líneas de texto
        full_text = [p.text for p in doc.paragraphs if p.text.strip() != ""]
        print("Primeros párrafos del documento:", full_text[:5])
    except Exception as e:
        print("❌ Error al abrir la plantilla:", e)
