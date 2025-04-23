import qrcode
import cv2

# QR Code Encoder
def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save("qr_code.png")
    print("QR Code generated and saved as qr_code.png")

# QR Code Decoder
def decode_qr_code(file_path):
    img = cv2.imread(file_path)
    detector = cv2.QRCodeDetector()
    value, pts, qr_code = detector(img)
    
    if value:
        print("Decoded QR Code Data:", value)
    else:
        print("No QR Code detected")

# User Input for QR Code Encoding or Decoding
choice = input("Do you want to Encode (E) or Decode (D) a QR Code? ").lower()

if choice == 'e':
    data = input("Enter the data to encode into a QR code: ")
    generate_qr_code(data)
elif choice == 'd':
    file_path = input("Enter the path of the QR code image to decode: ")
    decode_qr_code(file_path)
else:
    print("Invalid choice!")
