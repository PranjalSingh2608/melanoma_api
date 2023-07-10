from django.shortcuts import render
import urllib
import numpy as np
# from PIL import Image
from drf_yasg.utils import swagger_auto_schema
from .apps import VGGModelConfig
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser
import cloudinary.uploader
import matplotlib.pyplot as plt
import cv2

@swagger_auto_schema(
    method='post',
)


class UploadView(APIView):
    parser_classes=(
        MultiPartParser,
        JSONParser,
    )
    @staticmethod
    def post(request):
        file=request.data.get('file')
        upload_data=cloudinary.uploader.upload(file)
        img=upload_data['url']
        
        melanoma_classify=VGGModelConfig.model

        req=urllib.request.urlopen(img)
        # img=Image.open(req)
        # img=img.resize((224,224))
        # img=np.array(img)/255
        # img=np.expand_dims(img,axis=0)
        # t=[]
        # t.append(np.array(img))
        # t_p=np.array(t)

        arr=np.asarray(bytearray(req.read()),dtype=np.uint8)
        image=cv2.imdecode(arr,-1)
        image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        image=cv2.resize(image,(224,224))
        # image=np.array(image)/255
        image=np.expand_dims(image,axis=0)

        melanoma_predict=melanoma_classify.predict(image)
        probability=melanoma_predict[0]
        if probability[0]>0.5:
            result=str('%.2f' % (probability[0]*100)+'% Malignant')
        else:
            result=str('%.2f' % ((1-probability[0])*100)+'% Benign')


        return Response(
            {
                "status":"success",
                "data":upload_data,
                "url":img,
                "melanoma_classification":result,
            },
            status=201
        )
