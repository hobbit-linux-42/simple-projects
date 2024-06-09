try:
    from os import system
    from colorsys import rgb_to_hsv
    from colorama import init, Fore
except:
    print("""
Error.
try to install this python librarys:
colorama
colorsys
    """)

def color_popup():
    from tkinter.colorchooser import askcolor
    color = askcolor(color=None)
    if color[0]==None:
        exit(2)
    return rgb_to_hsv(color[0][0], color[0][1], color[0][2])

def play_hsv(hsv):
    init()
    play = lambda duration, frequency: system('play -n synth %s sin %s' % (duration, frequency))
    duration = hsv[2]/25 +1
    frequency = (hsv[0]*100)*5 +200
    volume = int(hsv[1]*100) +10
    B = Fore.BLUE
    G = Fore.GREEN
    R = Fore.RED
    Y = Fore.YELLOW
    W = Fore.WHITE
    print(f"""
    {Y}-----------------------------------
    {B}duration:   {int(duration)}      {Y}Brightness
    {G}frequency:  {int(frequency)}     {Y}Hue
    {R}volume:     {volume}%     {Y}Saturation   
    {Y}-----------------------------------
    {W}
    """)
    system(f"pactl -- set-sink-volume 0 {volume}%")
    try:
        play(duration, frequency)
    except:
        print("fail playing audio, to try install the sox package")
if __name__ == "__main__":
    play_hsv(color_popup())
