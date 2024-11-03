# -*- coding: utf-8 -*-

from pyfbsdk import (FBVector3d, FBModelTransformationType, FBSystem,
                     FBCharacter, FBFindModelByLabelName, FBMessageBox)

def SetBoneMapping() -> dict:
    mapping_bone = {
        "HipsLink"              :  "pelvis",
        "LeftUpLegLink"         :  "thigh_l",
        "LeftLegLink"           :  "calf_l",
        "LeftFootLink"          :  "foot_l",
        "RightUpLegLink"        :  "thigh_r",
        "RightLegLink"          :  "calf_r",
        "RightFootLink"         :  "foot_r",
        "SpineLink"             :  "stomach",
        "LeftArmLink"           :  "arm_l",
        "LeftForeArmLink"       :  "forearm_l",
        "LeftHandLink"          :  "hand_l",
        "RightArmLink"          :  "arm_r",
        "RightForeArmLink"      :  "forearm_r",
        "RightHandLink"         :  "hand_r",
        "HeadLink"              :  "head",
        "LeftToeBaseLink"       :  "toe_l",
        "RightToeBaseLink"      :  "toe_r",
        "LeftShoulderLink"      :  "clavicle_l",
        "RightShoulderLink"     :  "clavicle_r",
        "NeckLink"              :  "neck",
        "Spine1Link"            :  "chest",
        "LeftHandThumb1Link"    :  "f_thumb1_l",
        "LeftHandThumb2Link"    :  "f_thumb2_l",
        "LeftHandThumb3Link"    :  "f_thumb3_l",
        "LeftHandThumb4Link"    :  "f_thumb4_l",
        "LeftHandIndex1Link"    :  "f_index1_l",
        "LeftHandIndex2Link"    :  "f_index2_l",
        "LeftHandIndex3Link"    :  "f_index3_l",
        "LeftHandIndex4Link"    :  "f_index4_l",
        "LeftHandMiddle1Link"   :  "f_middle1_l",
        "LeftHandMiddle2Link"   :  "f_middle2_l",
        "LeftHandMiddle3Link"   :  "f_middle3_l",
        "LeftHandMiddle4Link"   :  "f_middle4_l",
        "LeftHandRing1Link"     :  "f_ring1_l",
        "LeftHandRing2Link"     :  "f_ring2_l",
        "LeftHandRing3Link"     :  "f_ring3_l",
        "LeftHandRing4Link"     :  "f_ring4_l",
        "LeftHandPinky1Link"    :  "f_pinky1_l",
        "LeftHandPinky2Link"    :  "f_pinky2_l",
        "LeftHandPinky3Link"    :  "f_pinky3_l",
        "LeftHandPinky4Link"    :  "f_pinky4_l",
        "RightHandThumb1Link"   :  "f_thumb1_r",
        "RightHandThumb2Link"   :  "f_thumb2_r",
        "RightHandThumb3Link"   :  "f_thumb3_r",
        "RightHandThumb4Link"   :  "f_thumb4_r",
        "RightHandIndex1Link"   :  "f_index1_r",
        "RightHandIndex2Link"   :  "f_index2_r",
        "RightHandIndex3Link"   :  "f_index3_r",
        "RightHandIndex4Link"   :  "f_index4_r",
        "RightHandMiddle1Link"  :  "f_middle1_r",
        "RightHandMiddle2Link"  :  "f_middle2_r",
        "RightHandMiddle3Link"  :  "f_middle3_r",
        "RightHandMiddle4Link"  :  "f_middle4_r",
        "RightHandRing1Link"    :  "f_ring1_r",
        "RightHandRing2Link"    :  "f_ring2_r",
        "RightHandRing3Link"    :  "f_ring3_r",
        "RightHandRing4Link"    :  "f_ring4_r",
        "RightHandPinky1Link"   :  "f_pinky1_r",
        "RightHandPinky2Link"   :  "f_pinky2_r",
        "RightHandPinky3Link"   :  "f_pinky3_r",
        "RightHandPinky4Link"   :  "f_pinky4_r",
    }

    return mapping_bone


def prepare_characterize()->bool:
    mapping_rot = {
        "pelvis"        :  FBVector3d(173.485, 0.000793457, -180) ,
        "thigh_l"       :  FBVector3d(174.975, 6.38468, 9.04656) ,
        "calf_l"        :  FBVector3d(-170.099, 6.2806, 7.69015) ,
        "foot_l"        :  FBVector3d(91.6881, 5.13961, 0.334436) ,
        "thigh_r"       :  FBVector3d(-5.02311, -6.38564, -9.04661) ,
        "calf_r"        :  FBVector3d(9.89845, -6.28166, -7.69023) ,
        "foot_r"        :  FBVector3d(-88.3139, -5.14049, -0.334) ,
        "stomach"       :  FBVector3d(179.604, 0.000424839, -180) ,
        "arm_l"         :  FBVector3d(1.17854e-07, -1.62088e-07, -90) ,
        "forearm_l"     :  FBVector3d(-6.77605e-07, 6.20136e-08, -90) ,
        "hand_l"        :  FBVector3d(180, 2.84619e-06, 90) ,
        "arm_r"         :  FBVector3d(180, -4.37936e-07, 90) ,
        "forearm_r"     :  FBVector3d(-180, -3.94648e-07, 90) ,
        "hand_r"        :  FBVector3d(-3.05457e-07, 1.29021e-06, -90) ,
        "head"          :  FBVector3d(176.157, 0.00121908, -179.92) ,
        "toe_l"         :  FBVector3d(-0.0437221, 3.96034, -0.13881) ,
        "toe_r"         :  FBVector3d(179.956, -3.96126, 0.139368) ,
        "clavicle_l"    :  FBVector3d(-178.933, -9.17926, 80.8431) ,
        "clavicle_r"    :  FBVector3d(1.06813, 9.18143, -80.8408) ,
        "neck"          :  FBVector3d(170.893, 0.0212864, 179.997) ,
        "chest"         :  FBVector3d(179.215, 0.000139334, 180) ,
        "f_thumb1_l"    :  FBVector3d(98.2744, -18.9115, 141.641) ,
        "f_thumb2_l"    :  FBVector3d(92.9358, -36.8122, 153.904) ,
        "f_thumb3_l"    :  FBVector3d(92.1074, -58.9782, 158.061) ,
        "f_thumb4_l"    :  FBVector3d(147.622, -11.5729, 79.9015) ,
        "f_index1_l"    :  FBVector3d(168.137, 2.46648, 75.186) ,
        "f_index2_l"    :  FBVector3d(165.66, -4.22729, 65.6964) ,
        "f_index3_l"    :  FBVector3d(168.056, -5.63113, 59.5739) ,
        "f_index4_l"    :  FBVector3d(108.838, 77.1532, -15.5148) ,
        "f_middle1_l"   :  FBVector3d(175.412, -0.767079, 77.2378) ,
        "f_middle2_l"   :  FBVector3d(173.98, -0.961445, 53.7078) ,
        "f_middle3_l"   :  FBVector3d(174.765, -1.31633, 37.9085) ,
        "f_middle4_l"   :  FBVector3d(133.314, 86.003, -6.69783) ,
        "f_ring1_l"     :  FBVector3d(-178.913, 0.632627, 77.6571) ,
        "f_ring2_l"     :  FBVector3d(178.638, 2.66132, 55.0433) ,
        "f_ring3_l"     :  FBVector3d(177.956, 3.96136, 39.1202) ,
        "f_ring4_l"     :  FBVector3d(21.3811, 85.4974, -110.969) ,
        "f_pinky1_l"    :  FBVector3d(-170.531, 9.49253, 77.4943) ,
        "f_pinky2_l"    :  FBVector3d(-174.719, 12.0952, 66.8044) ,
        "f_pinky3_l"    :  FBVector3d(-175.837, 14.1933, 57.074) ,
        "f_pinky4_l"    :  FBVector3d(-8.82583, 77.5242, -133.753) ,
        "f_thumb1_r"    :  FBVector3d(-81.1898, 19.182, -140.922) ,
        "f_thumb2_r"    :  FBVector3d(-86.7108, 35.7595, -153.183) ,
        "f_thumb3_r"    :  FBVector3d(-87.0929, 59.3904, -156.83) ,
        "f_thumb4_r"    :  FBVector3d(-31.8795, 11.2591, -79.2579) ,
        "f_index1_r"    :  FBVector3d(-11.8643, -2.46481, -75.1871) ,
        "f_index2_r"    :  FBVector3d(-14.3404, 4.23011, -65.6925) ,
        "f_index3_r"    :  FBVector3d(-11.9453, 5.63244, -59.5776) ,
        "f_index4_r"    :  FBVector3d(-71.1575, -77.1516, 15.5072) ,
        "f_middle1_r"   :  FBVector3d(-4.68503, 1.12443, -77.2084) ,
        "f_middle2_r"   :  FBVector3d(-5.96622, 1.2924, -54.0529) ,
        "f_middle3_r"   :  FBVector3d(-5.07829, 1.66592, -37.7409) ,
        "f_middle4_r"   :  FBVector3d(-41.7436, -85.849, 1.93102) ,
        "f_ring1_r"     :  FBVector3d(1.19385, -1.01445, -77.7243) ,
        "f_ring2_r"     :  FBVector3d(-1.44337, -3.04822, -54.6943) ,
        "f_ring3_r"     :  FBVector3d(-2.18716, -4.33168, -39.3125) ,
        "f_ring4_r"     :  FBVector3d(-159.337, -85.105, 111.482) ,
        "f_pinky1_r"    :  FBVector3d(9.47169, -9.48952, -77.4977) ,
        "f_pinky2_r"    :  FBVector3d(5.28592, -12.0922, -66.8157) ,
        "f_pinky3_r"    :  FBVector3d(4.16931, -14.191, -57.0917) ,
        "f_pinky4_r"    :  FBVector3d(171.144, -77.5253, 133.767) ,
    }

    for bone_name in mapping_rot.keys():
        bone_model = FBFindModelByLabelName(bone_name)
        if bone_model:
            bone_model.SetVector(mapping_rot[bone_name], FBModelTransformationType.kModelRotation)
        else:
            FBMessageBox("Warning", bone_name + " was not found in the scene.", "OK")
            return False
    
    # settle bone rotation in the UI
    FBSystem().Scene.Evaluate()

    return True


if __name__ in ('__main__', 'builtins'):
    check = prepare_characterize()
    if check:
        bonemap = SetBoneMapping()
        chara = FBCharacter("Casky")
        
        # mapping
        for propname in bonemap.keys():
            prop = chara.PropertyList.Find(propname)
            if prop != None:
                prop.append(FBFindModelByLabelName(bonemap[propname]))
                
        # characterize
        chara.SetCharacterizeOn(True)

        if chara.GetCharacterizeError() == "":
            FBMessageBox("Message", "Characterize Casky completed.", "OK")
        else:
            FBMessageBox("Caution", chara.GetCharacterizeError(), "OK")
        

# Cleanup
del(FBVector3d, FBModelTransformationType, FBSystem, 
    FBCharacter, FBFindModelByLabelName, FBMessageBox)
del(SetBoneMapping, prepare_characterize, check, bonemap, chara, propname, prop)