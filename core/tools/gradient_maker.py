from PIL import Image, ImageDraw
from io import BytesIO

def create_gradient(colors, width, height):

    gradient = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(gradient)
    num_colors = len(colors)
    color_width = width / (num_colors - 1)
    for i in range(num_colors - 1):
        color_start = i * color_width
        color_end = (i + 1) * color_width
        start_color = tuple(int(colors[i][j:j+2], 16) for j in (1, 3, 5))
        end_color = tuple(int(colors[i+1][j:j+2], 16) for j in (1, 3, 5))
        for x in range(int(color_start), int(color_end)):
            ratio = (x - color_start) / (color_end - color_start)
            color = (
                int(start_color[0] * (1 - ratio) + end_color[0] * ratio),
                int(start_color[1] * (1 - ratio) + end_color[1] * ratio),
                int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
            )
            draw.line((x, 0, x, height), fill=color)

    _bytes = BytesIO()
    gradient.save(_bytes, "png")
    _bytes.seek(0)

    return _bytes