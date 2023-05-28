import speech_recognition as s_r


def AudioInput():
    # print(s_r._version_)  # just to print the version not required
    r = s_r.Recognizer()
    # my device index is 1, you have to put your device index
    my_mic = s_r.Microphone(device_index=1)
    with my_mic as source:
        print("Say now!!!!")
        r.adjust_for_ambient_noise(source)  # reduce noise
        audio = r.listen(source)  # take voice input from the microphone
    return r.recognize_google(audio)  # to print voice into text
