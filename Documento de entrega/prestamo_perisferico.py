#Se importan librerias
from docxtpl import DocxTemplate
from datetime import datetime
import pandas as pd
import os



#carga la fecha del dia
fecha_hoy = datetime.today().strftime("%d %b, %Y")

#Cargar la data de inventario
df = pd.read_csv('transacciones.csv', delimiter = ";")

#setea fecha en la plantilla
my_context = { 'fecha_hoy' : fecha_hoy}
template_path = r"C:\Users\fsimone\Downloads\Libros\Python\plantilla_nuevo.docx"
print("Archivo existe:", os.path.isfile(template_path))
#busca info de las celdas para la plantilla
for index, fila in df.iterrows():
    if fila.notnull().any(): 

        doc = DocxTemplate(template_path)

    context = {
            'numero_ticket': fila['ticket_nro'] if pd.notnull(fila['ticket_nro']) else " ",
            'concepto_entrega': fila['concepto_entrega'] if pd.notnull(fila['concepto_entrega']) else " ",
            'nombre_usuario': fila['nombre_usuario'] if pd.notnull(fila['nombre_usuario']) else " ",
            'departamento': fila['dpto'] if pd.notnull(fila['dpto']) else " ",
            'material': fila['tipo_material'] if pd.notnull(fila['tipo_material']) else " ",
            'nro_etiqueta': fila['nro_etiqueta'] if pd.notnull(fila['nro_etiqueta']) else " ",
            'serial_nro': fila['serial_nro'] if pd.notnull(fila['serial_nro']) else " ",
            'responsable_it': fila['resp_it'] if pd.notnull(fila['resp_it']) else " ",
                }
    context.update(my_context)
    
    doc.render(context)
    doc.save(f"{fila['numero_ticket']}_doc_{fila['nombre_usuario']}.docx")



numbers = {
  "first": 1,
  "second": 2,
  "third": 3,
  "fourth": 4,
}