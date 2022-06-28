from django.shortcuts import render
from .models import Gender, SkinColor, ClothingColor, HairColor, HairType, FacialHairType, Accessory, ClothingType
from django.http import StreamingHttpResponse
from avatar.camera import VideoCamera
from avatar.camera import *
from avatar.avatar import update

# Create your views here.
def index(request):
    gender = Gender.objects.all()
    return render(request, 'index.html', {'gender': gender})



def character(request, genid): 
    skincolor = SkinColor.objects.all()
    clothingcolor = ClothingColor.objects.all()
    haircolor = HairColor.objects.all()
    hairtype = HairType.objects.all()
    facialhairtype = FacialHairType.objects.all()
    accessory = Accessory.objects.all()
    clothingtype = ClothingType.objects.all()
    gender = Gender.objects.get(pk=genid)

    context = {'skincolor': skincolor,'clothingcolor': clothingcolor,
    		   'haircolor': haircolor,'hairtype': hairtype,
    		   'facialhairtype': facialhairtype,'accessory': accessory,
               'clothingtype':clothingtype,'gender': gender}

    return render(request, 'character.html', context)

sc_id=0
cc_id=0
hc_id=0
ht_id=0
a_id=0
fht_id=0
ct_id=0
gend = 1

ep = "Neutral"

def epred(emotion):
    global ep
    ep = emotion

def res(request, genid):
    global sc_id,cc_id,hc_id,ht_id,a_id,fht_id,ct_id, ep, gend
    sc_id = request.GET.get('skincolor')
    cc_id = request.GET.get('clothingcolor')
    hc_id = request.GET.get('haircolor')
    ht_id = request.GET.get('hairtype')
    a_id = request.GET.get('accessory')
    fht_id = request.GET.get('facialhairtype')
    ct_id = request.GET.get('clothingtype')
    gender = Gender.objects.get(pk=genid)
    gend = gender.id
    if gend == 1:
        update(fht_id, ct_id, cc_id, a_id, hc_id, ht_id, sc_id, ep)
    if gend == 2:
        fht_id="1"
        update(fht_id, ct_id, cc_id, a_id, hc_id, ht_id, sc_id, ep)
    
    return render(request, 'result.html')

def gen(camera):
    while True:
        if gend == 1:
            global fht_id
            update(fht_id, ct_id, cc_id, a_id, hc_id, ht_id, sc_id, ep)
        if gend == 2:
            fht_id="1"
            update(fht_id, ct_id, cc_id, a_id, hc_id, ht_id, sc_id, ep)
    
        frame = camera.get_frame()
        update(fht_id, ct_id, cc_id, a_id, hc_id, ht_id, sc_id, ep)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):

     return StreamingHttpResponse(gen(VideoCamera()), content_type = 'multipart/x-mixed-replace; boundary=frame')       