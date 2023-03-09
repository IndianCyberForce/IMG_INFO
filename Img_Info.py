from PIL import Image
from PIL.ExifTags import TAGS
import sys
from colorama import Fore
from time import sleep
import sys,os,time
def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
banner="""
'####:'##::::'##::'######::::::'####:'##::: ##:'########::'#######::
. ##:: ###::'###:'##... ##:::::. ##:: ###:: ##: ##.....::'##.... ##:
: ##:: ####'####: ##:::..::::::: ##:: ####: ##: ##::::::: ##:::: ##:
: ##:: ## ### ##: ##::'####::::: ##:: ## ## ##: ######::: ##:::: ##:
: ##:: ##. #: ##: ##::: ##:::::: ##:: ##. ####: ##...:::: ##:::: ##:
: ##:: ##:.:: ##: ##::: ##:::::: ##:: ##:. ###: ##::::::: ##:::: ##:
'####: ##:::: ##:. ######::::::'####: ##::. ##: ##:::::::. #######::
....::..:::::..:::......:::::::....::..::::..::..:::::::::.......:::
"""


def Starting():
    clr()
    print(Fore.CYAN+banner)
    print(Fore.BLUE+"\nAuthor:Mr.Grey_Hacker\n")
    print(Fore.LIGHTYELLOW_EX+"Indian "+Fore.WHITE+"Cyber "+Fore.GREEN+"Force\n")
    imagename = input(Fore.WHITE+"Enter Img File Path: ")

    image = Image.open(imagename)

    info_dict = {
        "Filename": image.filename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode,
        "Image is Animated": getattr(image, "is_animated", False),
        "Frames in Image": getattr(image, "n_frames", 1)
    }

    for label,value in info_dict.items():
        print(f"{label:25}: {value}")
        

    exifdata = image.getexif()


    for tag_id in exifdata:
        
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:25}: {data}")
    End()
def End():
    Ending=input(str(Fore.GREEN+"Do You Want More Pic Information(Y/n):"))        
    if Ending == 'y' or Ending == 'Y' or Ending == 'Yes' or Ending == 'yes':
        print(Fore.RED+"I Am Again Starting....")
        time.sleep(1)
        clr()
        Starting()
    elif Ending == 'n' or Ending == 'N' or Ending == 'no' or Ending == 'No':
        print(Fore.RED+"Exiting.....")
        time.sleep(1)
        exit()
    else:
        print(Fore.RED+"Wrong Value Input, Try Again....!!!")
        time.sleep(1)
        End()
Starting()
