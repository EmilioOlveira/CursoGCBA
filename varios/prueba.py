
from PIL import Image, ImageDraw, ImageFont

# 1. Configuración de dimensiones y lienzo transparente (RGBA)
width, height = 1200, 650
image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Color Azul Corporativo (HEX #00338D -> RGB)
blue_color = (0, 51, 141, 255)

# 2. Cargar fuentes del sistema (Arial / Helvetica como opción limpia no tan cursiva)
# Si estás en Windows usa 'arial.ttf', en Mac/Linux podés usar 'DejaVuSans.ttf' o la ruta a tu fuente preferida.
try:
    font_main = ImageFont.truetype("arial.ttf", 220)
    font_sub = ImageFont.truetype("arial.ttf", 75)
except OSError:
    font_main = ImageFont.load_default()
    font_sub = ImageFont.load_default()

# 3. Textos
text_main = "O&Z"
text_sub = "Consultoría IT"

# 4. Cálculo de posiciones centradas
bbox_main = draw.textbbox((0, 0), text_main, font=font_main)
w_main = bbox_main[2] - bbox_main[0]
h_main = bbox_main[3] - bbox_main[1]

bbox_sub = draw.textbbox((0, 0), text_sub, font=font_sub)
w_sub = bbox_sub[2] - bbox_sub[0]

x_main = (width - w_main) / 2
y_main = 100

x_sub = (width - w_sub) / 2
y_sub = y_main + h_main + 60

# 5. Dibujar texto en el lienzo
draw.text((x_main, y_main), text_main, font=font_main, fill=blue_color)
draw.text((x_sub, y_sub), text_sub, font=font_sub, fill=blue_color)

# 6. Guardar archivo como PNG transparente
output_path = "logo_oz_consultoria_it.png"
image.save(output_path, "PNG")

print(f"¡Logo generado con éxito en '{output_path}' con transparencia real!")
