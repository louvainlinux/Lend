import tempfile

from PIL import Image, ImageFont, ImageDraw
import cups
import qrcode


def generate_warning(text):
    """ Returns a PIL image containing a warning with text text"""
    img_logo = Image.open('label_generator/warning.png')

    img = Image.new('L', (559, 176), 'white')
    img.paste(img_logo, (20, 13, 200, 163))

    draw = ImageDraw.Draw(img)

    # Draw Louvain-li-Nux
    font = ImageFont.truetype("label_generator/nb_font.ttf", 50)
    draw.text((220, 69), text, font=font)

    return img


def generate_label(machine_id):
    """ Returns a PIL image containing the label with id machine_id """
    img_qr = qrcode.make('http://lend.louvainlinux.be/info-{}'.format(machine_id))
    img_qr = img_qr.resize((176, 176))

    img_logo = Image.open('label_generator/logo.png')

    img = Image.new('L', (559, 176), 'white')
    img.paste(img_logo, (20, 13, 137, 163))
    img.paste(img_qr, (383, 0, 559, 176))

    draw = ImageDraw.Draw(img)

    # Draw machine id
    font = ImageFont.truetype("label_generator/nb_font.ttf", 40)
    draw.text((200, 125), str(machine_id).zfill(6), font=font)

    # Draw Louvain-li-Nux
    font = ImageFont.truetype("label_generator/text.ttf", 38)
    draw.text((160, 0), "Louvain-li-Nux", font=font)

    # Draw Rue constantin meunier 12, LLN
    font = ImageFont.truetype("label_generator/text.ttf", 19)
    draw.text((160, 50), "Rue Constantin Meunier 12", font=font)
    draw.text((160, 75), "1348 Louvain-la-Neuve", font=font)
    return img


def print_label(label, printer, location):
    """ Print a label on the printer named ``printer``"""
    file_loc = tempfile.mkstemp('.png')[1]
    label.save(file_loc)
    con = cups.Connection()
    con.setPrinterDevice(printer, location)
    con.printFile(printer, file_loc, "Label", {})
