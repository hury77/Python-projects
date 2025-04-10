from PIL import Image, ImageDraw

def create_icon(filename, shape, size=(64, 64), color="black"):
    image = Image.new("RGBA", size, (255, 255, 255, 0))  # Przezroczyste tło
    draw = ImageDraw.Draw(image)

    if shape == "triangle":  # Ikona Play
        draw.polygon([(16, 16), (48, 32), (16, 48)], fill=color)
    elif shape == "pause":  # Ikona Pause
        draw.rectangle([16, 16, 24, 48], fill=color)
        draw.rectangle([40, 16, 48, 48], fill=color)
    elif shape == "square":  # Ikona Stop
        draw.rectangle([16, 16, 48, 48], fill=color)
    elif shape == "folder":  # Ikona Open
        draw.rectangle([16, 24, 48, 48], fill=color)
        draw.rectangle([16, 16, 32, 24], fill=color)

    image.save(filename)

# Tworzenie ikon
create_icon("icons/play.png", "triangle")
create_icon("icons/pause.png", "pause")
create_icon("icons/stop.png", "square")
create_icon("icons/open.png", "folder")