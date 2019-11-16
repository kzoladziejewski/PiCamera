import base64

class ConverterToBase64():

    def __init__(self):
        pass

    def convert_image_to_base_64(self, name):
        with open(name, 'rb') as image_file:
            encoded = base64.b64encode(image_file.read())
            return encoded