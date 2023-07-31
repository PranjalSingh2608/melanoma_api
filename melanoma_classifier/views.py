from django.shortcuts import render
import urllib
import numpy as np
# from PIL import Image
from .apps import VGGModelConfig
from .models import ImageClassify
from .forms import ImageForm
from keras.preprocessing.image import load_img,img_to_array
import matplotlib.pyplot as plt
import cv2




        # arr=np.asarray(bytearray(req.read()),dtype=np.uint8)
        # image=cv2.imdecode(arr,-1)
        # image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        # image=cv2.resize(image,(224,224))
        # # image=np.array(image)/255
        # image=np.expand_dims(image,axis=0)

        # melanoma_predict=melanoma_classify.predict(image)
        # probability=melanoma_predict[0]
        # if probability[0]>0.5:
        #     result=str('%.2f' % (probability[0]*100)+'% Malignant')
        # else:
        #     result=str('%.2f' % ((1-probability[0])*100)+'% Benign')

def classifier(img):
    melanoma_classify=VGGModelConfig.model
    arr=np.asarray(bytearray(img.read()),dtype=np.uint8)
    image=cv2.imdecode(arr,-1)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    image=cv2.resize(image,(224,224))
    image=np.expand_dims(image,axis=0)
    melanoma_predict=melanoma_classify.predict(image)
    probability=melanoma_predict[0]
    if probability[0]>0.5:
        result=str('%.2f' % (probability[0]*100)+'% Malignant')
    else:
        result=str('%.2f' % ((1-probability[0])*100)+'% Benign')
    return result

def mainView(request):
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            image_obj=form.instance
            image=image_obj.image
            prediction=classifier(image)
            context = {
                'form' : form,
                'image': image,
                'prediction':prediction,
            }
            return render(request ,'cover.html' , context=context)
    
    form = ImageForm()

    return render(request ,'cover.html' , {'form':form})            
