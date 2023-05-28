from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Get default audio device using PyCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# Get current volume 
def VolumeInc():
    currentVolumeDb = volume.GetMasterVolumeLevel()
    if currentVolumeDb+6.0>0.0:
        print("Volume Can't be Increased")
        return
    else:
        volume.SetMasterVolumeLevel(currentVolumeDb + 6.0, None)
def Mute():
    print("I am in mute now!!")
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    currentVolumeDb = volume.GetMasterVolumeLevel()
    print("Current Volume",currentVolumeDb)
    currentVolumeDb=-65.25
    print("Updated volume",currentVolumeDb)
    volume.SetMasterVolumeLevel(currentVolumeDb,None)
def VolumeDec():
    currentVolumeDb = volume.GetMasterVolumeLevel()
    if currentVolumeDb-6.0<-65.25:
        print("Volume Cannot be Decreased")
        return
    else:
        volume.SetMasterVolumeLevel(currentVolumeDb - 6.0,None)
# flag = True
# while flag:
#     x=input("Enter + or - or 0 or 1 or * to Increase ,Decrease, Mute, UnMute and Exit the volume respectively\n")
#     if x=="*":
#         flag=False
#     elif x=="0":
#         currentVolumeDb = volume.GetMasterVolumeLevel()
#         currentVolumeDb=-65.25
#         volume.SetMasterVolumeLevel(currentVolumeDb,None)
#     elif x=="1":
#         currentVolumeDb = volume.GetMasterVolumeLevel()
#         currentVolumeDb = 0.0
#         volume.SetMasterVolumeLevel(currentVolumeDb,None)
#     else:
#         invoker(x)

# # x=input("Enter Increase or Decrease to Increase and Decrease the volume respectively\n")
# # if x=="Increase":
# #     IncreaseVolume()
# # else:
# #     DecreaseVolume()

# # NOTE: -6.0 dB = half volume !