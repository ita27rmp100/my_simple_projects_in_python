import gtts , os
f = input("the file : ")
with open(r"{}".format(f)) as file :
    name_of_file = os.path.split(r"{}".format(f))
    os.chdir(name_of_file[0])
    to_sound = gtts.gTTS(text=file.read())
    to_sound.save(name_of_file[1][0:name_of_file[1].index(".")]+"_1"+".mp3")
    print("ok")
    os.system(name_of_file[1][0:name_of_file[1].index(".")] + "_1" + ".mp3")
