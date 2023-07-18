import qrcode
from PIL import Image

def qr():
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                       box_size=10, border=4)
    qr.add_data("https://www.linkedin.com/in/nabeel-emamudeen-771b49210/")
    qr.make(fit=True)
    img = qr.make_image(fill_color="red", back_color="black")
    return img.save("qr.png")

def main():
    qr()

if __name__ == "qr":
    main()
