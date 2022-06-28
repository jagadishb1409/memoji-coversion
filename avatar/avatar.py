import python_avatars as pa
import os
from django.conf import settings

def facialhairtype(fht_id):
    fhtype=pa.FacialHairType.NONE

    if fht_id == 1:
        fhtype = pa.FacialHairType.NONE
    elif fht_id == 2:
        fhtype = pa.FacialHairType.MOUSTACHE_MAGNUM

    elif fht_id == 3:
        fhtype = pa.FacialHairType.MOUSTACHE_FANCY
    elif fht_id == 4:
        fhtype = pa.FacialHairType.BEARD_LIGHT
    elif fht_id == 5:
        fhtype = pa.FacialHairType.BEARD_MEDIUM
    elif fht_id == 6:
        fhtype = pa.FacialHairType.BEARD_MAGESTIC
    return fhtype


def clothingtype(ct_id):
    ctype = pa.ClothingType.BLAZER_SHIRT
    sg = pa.ClothingGraphic.NONE 
    if ct_id == 1 or ct_id == 15:
        ctype = pa.ClothingType.BLAZER_SHIRT
        sg = pa.ClothingGraphic.NONE
    elif ct_id == 2 or ct_id == 16:
        ctype = pa.ClothingType.BLAZER_SWEATER
        sg = pa.ClothingGraphic.NONE
    elif ct_id == 3 or ct_id == 17:
        ctype = pa.ClothingType.COLLAR_SWEATER
        sg = pa.ClothingGraphic.NONE
    elif ct_id == 4 or ct_id == 18:
        ctype = pa.ClothingType.HOODIE
        sg = pa.ClothingGraphic.NONE
    elif ct_id == 5 or ct_id == 19:
        ctype = pa.ClothingType.OVERALL
        sg = pa.ClothingGraphic.NONE
    elif ct_id == 6 or ct_id == 20:
        ctype = pa.ClothingType.SHIRT_CREW_NECK
        sg = pa.ClothingGraphic.NONE
    elif ct_id == 7:
        ctype = pa.ClothingType.SHIRT_SCOOP_NECK
        sg = pa.ClothingGraphic.NONE
    elif ct_id == 8 or ct_id == 22:
        ctype = pa.ClothingType.GRAPHIC_SHIRT
        sg = pa.ClothingGraphic.BAT
    elif ct_id == 9 or ct_id == 23:
        ctype = pa.ClothingType.GRAPHIC_SHIRT
        sg = pa.ClothingGraphic.BEAR
    elif ct_id == 10 or ct_id == 24:
        ctype = pa.ClothingType.GRAPHIC_SHIRT
        sg = pa.ClothingGraphic.DEER
    elif ct_id == 11 or ct_id == 25:
        ctype = pa.ClothingType.GRAPHIC_SHIRT
        sg = pa.ClothingGraphic.DIAMOND
    elif ct_id == 12 or ct_id == 26:
        ctype = pa.ClothingType.GRAPHIC_SHIRT
        sg = pa.ClothingGraphic.HOLA
    elif ct_id == 13 or ct_id == 27:
        ctype = pa.ClothingType.GRAPHIC_SHIRT
        sg = pa.ClothingGraphic.PIZZA
    elif ct_id == 14 or ct_id == 28:
        ctype = pa.ClothingType.GRAPHIC_SHIRT
        sg = pa.ClothingGraphic.SKULL_OUTLINE
    elif ct_id == 21:
        ctype = pa.ClothingType.SHIRT_V_NECK
        sg = pa.ClothingGraphic.NONE
    return ctype, sg


def clothingcolor(cc_id):
    ccolor = pa.ClothingColor.BLACK

    if cc_id == 1:
        ccolor = pa.ClothingColor.BLACK
    elif cc_id == 2:
        ccolor = pa.ClothingColor.BLUE_01
    elif cc_id == 3:
        ccolor = pa.ClothingColor.BLUE_02
    elif cc_id == 4:
        ccolor = pa.ClothingColor.BLUE_03
    elif cc_id == 5:
        ccolor = pa.ClothingColor.GRAY_02
    elif cc_id == 6:
        ccolor = pa.ClothingColor.HEATHER
    elif cc_id == 7:
        ccolor = pa.ClothingColor.PASTEL_GREEN
    elif cc_id == 8:
        ccolor = pa.ClothingColor.PASTEL_ORANGE
    elif cc_id == 9:
        ccolor = pa.ClothingColor.PASTEL_YELLOW
    elif cc_id == 10:
        ccolor = pa.ClothingColor.PINK
    elif cc_id == 11:
        ccolor = pa.ClothingColor.RED
    return ccolor


def accessorytype(a_id):
    acc = pa.AccessoryType.NONE
    if a_id == 1 or a_id == 5:
        acc = pa.AccessoryType.NONE
    elif a_id == 2 or a_id == 6:
        acc = pa.AccessoryType.ROUND
    elif a_id == 3 or a_id == 7:
        acc = pa.AccessoryType.PRESCRIPTION_1
    elif a_id == 4 or a_id == 8:
        acc = pa.AccessoryType.PRESCRIPTION_2
    return acc


def haircolor(h_id):
    hcolor = pa.HairColor.AUBURN
    if h_id == 1:
        hcolor = pa.HairColor.AUBURN
    elif h_id == 2:
        hcolor = pa.HairColor.BLACK
    elif h_id == 3:
        hcolor = pa.HairColor.BLONDE
    elif h_id == 4:
        hcolor = pa.HairColor.BLONDE_GOLDEN
    elif h_id == 5:
        hcolor = pa.HairColor.BROWN
    elif h_id == 6:
        hcolor = pa.HairColor.BROWN_DARK
    elif h_id == 7:
        hcolor = pa.HairColor.PASTEL_PINK
    elif h_id == 8:
        hcolor = pa.HairColor.PLATINUM
    elif h_id == 9:
        hcolor = pa.HairColor.RED
    return hcolor


def hairtype(ht_id):
    htype = pa.HairType.NONE
    if ht_id == 1:
        htype = pa.HairType.NONE
    elif ht_id == 2:
        htype = pa.HairType.CAESAR
    elif ht_id == 3:
        htype = pa.HairType.CAESAR_SIDE_PART
    elif ht_id == 4:
        htype = pa.HairType.FRIZZLE
    elif ht_id == 5:
        htype = pa.HairType.SHAGGY
    elif ht_id == 6:
        htype = pa.HairType.SHORT_CURLY
    elif ht_id == 7:
        htype = pa.HairType.SHORT_DREADS_1
    elif ht_id == 8:
        htype = pa.HairType.SHORT_DREADS_2
    elif ht_id == 9:
        htype = pa.HairType.SHORT_FLAT
    elif ht_id == 10:
        htype = pa.HairType.SHORT_ROUND
    elif ht_id == 11:
        htype = pa.HairType.SHORT_WAVED
    elif ht_id == 12:
        htype = pa.HairType.SIDES
    elif ht_id == 13:
        htype = pa.HairType.BUN
    elif ht_id == 14:
        htype = pa.HairType.BIG_HAIR
    elif ht_id == 15:
        htype = pa.HairType.BOB
    elif ht_id == 16:
        htype = pa.HairType.CURLY
    elif ht_id == 17:
        htype = pa.HairType.DREADS
    elif ht_id == 18:
        htype = pa.HairType.FRIDA
    elif ht_id == 19:
        htype = pa.HairType.FRO
    elif ht_id == 20:
        htype = pa.HairType.FRO_BAND
    elif ht_id == 21:
        htype = pa.HairType.LONG_NOT_TOO_LONG
    elif ht_id == 22:
        htype = pa.HairType.MIA_WALLACE
    elif ht_id == 23:
        htype = pa.HairType.STRAIGHT_1
    elif ht_id == 24:
        htype = pa.HairType.STRAIGHT_STRAND
    return htype


def skincolor(sc_id):
    scolor = pa.SkinColor.PALE
    if sc_id == 1:
        scolor = pa.SkinColor.PALE
    elif sc_id == 2:
        scolor = pa.SkinColor.LIGHT
    elif sc_id == 3:
        scolor = pa.SkinColor.BROWN
    elif sc_id == 4:
        scolor = pa.SkinColor.TANNED
    elif sc_id == 5:
        scolor = pa.SkinColor.DARK_BROWN
    elif sc_id == 6:
        scolor = pa.SkinColor.BLACK
    return scolor





def update(fht_id, ct_id, cc_id, a_id, hc_id, ht_id, sc_id, ep):
    fht_id=int(fht_id)
    ct_id=int(ct_id)
    cc_id=int(cc_id)
    a_id=int(a_id)
    hc_id=int(hc_id)
    ht_id=int(ht_id)
    sc_id=int(sc_id)

    fhtype = facialhairtype(fht_id)
    ctype, sg = clothingtype(ct_id)
    ccolor = clothingcolor(cc_id)
    acc = accessorytype(a_id)
    hcolor = haircolor(hc_id)
    htype = hairtype(ht_id)
    scolor = skincolor(sc_id)
    emotion_prediction = ep
    my_avatar = pa.Avatar(
        style=pa.AvatarStyle.TRANSPARENT,
        background_color=pa.BackgroundColor.DEFAULT,
        eyebrows=pa.EyebrowType.DEFAULT_NATURAL,
        top=htype,
        # top=str.NONE,
        eyes=pa.EyeType.DEFAULT,
        nose=pa.NoseType.DEFAULT,
        mouth=pa.MouthType.DEFAULT,
        facial_hair=fhtype,
        skin_color=scolor,
        hair_color=hcolor,
        accessory=acc,
        clothing=ctype,
        clothing_color=ccolor,
        shirt_graphic=sg
    )

    if emotion_prediction == "Angry":
        my_avatar.eyebrows = pa.EyebrowType.ANGRY_NATURAL
        my_avatar.eyes = pa.EyeType.SQUINT
        my_avatar.mouth = pa.MouthType.SCREAM_OPEN
        


    elif emotion_prediction == "Disgust":
        my_avatar.eyebrows = pa.EyebrowType.FLAT_NATURAL
        my_avatar.eyes = pa.EyeType.SQUINT
        my_avatar.mouth = pa.MouthType.EATING

    elif emotion_prediction == "Fear":
        my_avatar.eyebrows = pa.EyebrowType.SAD_CONCERNED_NATURAL
        my_avatar.eyes = pa.EyeType.DEFAULT
        my_avatar.mouth = pa.MouthType.SAD

    elif emotion_prediction == "Happy":
        my_avatar.eyebrows = pa.EyebrowType.RAISED_EXCITED_NATURAL
        my_avatar.eyes = pa.EyeType.HAPPY
        my_avatar.mouth = pa.MouthType.SMILE

    elif emotion_prediction == "Sad":
        my_avatar.eyebrows = pa.EyebrowType.SAD_CONCERNED_NATURAL
        my_avatar.eyes = pa.EyeType.CRY
        my_avatar.mouth = pa.MouthType.SAD

    elif emotion_prediction == "Surprise":
        my_avatar.eyebrows = pa.EyebrowType.RAISED_EXCITED_NATURAL
        my_avatar.eyes = pa.EyeType.SURPRISED
        my_avatar.mouth = pa.MouthType.SCREAM_OPEN

    elif emotion_prediction == "Neutral":
        my_avatar.eyebrows = pa.EyebrowType.DEFAULT_NATURAL
        my_avatar.eyes = pa.EyeType.DEFAULT
        my_avatar.mouth = pa.MouthType.SERIOUS

    my_avatar.render(os.path.join(settings.BASE_DIR, 'static/output/emoji1.svg'))
    my_avatar.render(os.path.join(settings.BASE_DIR, 'static/output/emoji2.svg'))