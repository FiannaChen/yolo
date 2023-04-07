import base64
import json
import math
import os
import detect
import time
from io import BytesIO
from PIL import Image
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

# create a restful api for the image detection
@csrf_protect
@csrf_exempt
def detectImage(request):
    # create a response map for the result

    # get the methond of the get request,the parameter is the base64 code of the image
    if request.method == 'POST':
        # judge the body is empty
        try:
            received_json_data = json.loads(request.body)
        except Exception as e:
            return HttpResponse('the request body is empty')
        
        # judge the image is empty
        try:
            received_json_data['image'] == None
        except Exception as e:
            return HttpResponse('can not get the param image')
        # get the image
        image = received_json_data['image']
        # detect the str image contains data:image/jpeg;base64,
        try:
            image.find('data:image/jpeg;base64,') != -1
            image = image.replace('data:image/jpeg;base64,', '')
            image = f"{image}{'=' * ((4 - len(image) % 4) % 4)}"
            image = base64.b64decode(image)
        except Exception as e:
            return HttpResponse(e)
        # if the format convert to base64 is not success,return the error
        # modify the image name to uuid
        uuid = time.time()
        image_name = str(uuid) + '.jpg'
        # save the image
        with open(image_name, 'wb') as f:
            f.write(image)

        result = detect.run(image_name)
        if result != None:
            if result['status'] == True:

                # get the host path
                host_path = os.path.abspath(os.path.dirname(__file__))
                host_path = host_path.split('CV')[0]
                image_path = host_path + 'CV/' + result['dataDir'] + '/' + image_name
                # read the image
                with open(image_path, 'rb') as f:
                    image = f.read()
                # encode the image
                image = base64.b64encode(image)
                # delete the image
                os.remove(image_path)
                # get the front path of the imagepath
                image_path = image_path.split(image_name)[0]
                # delete directory
                os.removedirs(image_path)

                print(image_path)
                # delete the original image
                os.remove(image_name)
                # return the result
                return HttpResponse(image)

            else:
                return HttpResponse(result['false'])
