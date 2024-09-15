from Crypto.Cipher import AES
from core.models import ErrorsModel
import base64,sys


## Decrypt Investor Documents

# start's here:
def decrypt_image(enc_image, key, tag,iv):
    try:
        key = key
        tag = tag
        iv = iv
        ct = enc_image
        # Decrypt the image data
        
        cipher = AES.new(key, AES.MODE_GCM, iv)

        image_data = cipher.decrypt_and_verify(ct, tag)
        
        # Encode the image data as a base64 string
        image_data_base64 = base64.b64encode(image_data).decode()
        
        return image_data_base64
        
    except Exception as e:
        ErrorsModel.objects.create(error_caught_function=f'decrypt_image - {sys.exc_info()[-1].tb_lineno}',error_message=e)
        pass
# end'here