import numpy as np
import os

# Initialize directories
env_MEDIA_DIR = os.getenv("MEDIA_DIR")
if env_MEDIA_DIR:
    MEDIA_DIR = env_MEDIA_DIR
elif os.path.isfile("media_dir.txt"):
    with open("media_dir.txt", 'rU') as media_file:
        MEDIA_DIR = media_file.readline().strip()
else:
    MEDIA_DIR = os.path.join(
        os.path.expanduser('~'),
        "/"
    )
if not os.path.isdir(MEDIA_DIR):
    MEDIA_DIR = "./media"
    print(
        f"Media will be stored in {MEDIA_DIR + os.sep}. You can change "
        "this behavior by writing a different directory to media_dir.txt."
    )

VIDEO_DIR = os.path.join("videos")
RASTER_IMAGE_DIR = os.path.join("media","raster_images")
SVG_IMAGE_DIR = os.path.join("media","svg_images")
SOUND_DIR = os.path.join("media","sounds")
###
THIS_DIR = os.path.dirname(os.path.realpath(__file__))
FILE_DIR = os.path.join(os.getenv("FILE_DIR", default="."), "files")
TEX_DIR = os.path.join(FILE_DIR, "Tex")
TEXT_DIR = os.path.join(FILE_DIR, "Text")
# These two may be depricated now.
MOBJECT_DIR = os.path.join(FILE_DIR, "mobjects")
IMAGE_MOBJECT_DIR = os.path.join(MOBJECT_DIR, "image")

for folder in [FILE_DIR, RASTER_IMAGE_DIR, SVG_IMAGE_DIR, VIDEO_DIR,
               TEX_DIR, MOBJECT_DIR, IMAGE_MOBJECT_DIR,SOUND_DIR,TEXT_DIR]:
    if not os.path.exists(folder):
        os.makedirs(folder)

TEX_USE_CTEX = False
TEX_TEXT_TO_REPLACE = "YourTextHere"
#-----------TEX OPTIONS-------------------
#-----------Normal
TEMPLATE_TEX_FILE = os.path.join(
    THIS_DIR,"tex_files", "tex_template.tex" if not TEX_USE_CTEX
    else "ctex_template.tex"
)
with open(TEMPLATE_TEX_FILE, "r") as infile:
    TEMPLATE_TEXT_FILE_BODY = infile.read()
    TEMPLATE_TEX_FILE_BODY = TEMPLATE_TEXT_FILE_BODY.replace(
        TEX_TEXT_TO_REPLACE,
        "\\begin{align*}\n" + TEX_TEXT_TO_REPLACE + "\n\\end{align*}",
    )
#-----------Tikz
TEMPLATE_TEX_FILE_TIKZ = os.path.join(
    THIS_DIR,"tex_files", "tex_template_tikz.tex")
with open(TEMPLATE_TEX_FILE_TIKZ, "r") as infile:
    TEMPLATE_TEXT_FILE_BODY_TIKZ = infile.read()
    TEMPLATE_TEX_FILE_BODY_TIKZ = TEMPLATE_TEXT_FILE_BODY_TIKZ.replace(
        TEX_TEXT_TO_REPLACE,
        "\\begin{tikzpicture}\n" + TEX_TEXT_TO_REPLACE + "\n\\end{tikzpicture}",
    )
#-----------Listings
TEMPLATE_TEX_FILE_LISTINGS = os.path.join(
    THIS_DIR,"tex_files", "tex_template_listings.tex")
with open(TEMPLATE_TEX_FILE_LISTINGS, "r") as infile:
    TEMPLATE_TEXT_FILE_BODY_LISTINGS = infile.read()
    TEMPLATE_TEX_FILE_BODY_LISTINGS = TEMPLATE_TEXT_FILE_BODY_LISTINGS.replace(
        TEX_TEXT_TO_REPLACE,
        "\\begin{lstlisting}\n" + TEX_TEXT_TO_REPLACE + "\n\\end{lstlisting}",
    )
#-----------Music
TEMPLATE_TEX_FILE_MUSIC = os.path.join(
    THIS_DIR,"tex_files", "tex_template_music.tex")
with open(TEMPLATE_TEX_FILE_MUSIC, "r") as infile:
    TEMPLATE_TEXT_FILE_BODY_MUSIC = infile.read()
    TEMPLATE_TEX_FILE_BODY_MUSIC = TEMPLATE_TEXT_FILE_BODY_MUSIC.replace(
        TEX_TEXT_TO_REPLACE,
        "\\begin{music}\n" + TEX_TEXT_TO_REPLACE + "\n\\end{music}",
    )
#-----------Braces
TEMPLATE_TEX_FILE_BRACES = os.path.join(
    THIS_DIR,"tex_files", "tex_template_braces.tex")
with open(TEMPLATE_TEX_FILE_BRACES, "r") as infile:
    TEMPLATE_TEXT_FILE_BODY_BRACES = infile.read()
    TEMPLATE_TEX_FILE_BODY_BRACES = TEMPLATE_TEXT_FILE_BODY_BRACES.replace(
        TEX_TEXT_TO_REPLACE,
        "\\begin{align*}\n" + TEX_TEXT_TO_REPLACE + "\n\\end{align*}",
    )
#-----------Fonts
TEMPLATE_TEX_FILE_FONTS = os.path.join(
    THIS_DIR,"tex_files", "tex_template_fonts.tex")
with open(TEMPLATE_TEX_FILE_FONTS, "r") as infile:
    TEMPLATE_TEXT_FILE_BODY_FONTS = infile.read()
    TEMPLATE_TEX_FILE_BODY_FONTS = TEMPLATE_TEXT_FILE_BODY_FONTS.replace(
        TEX_TEXT_TO_REPLACE,
        "\\begin{align*}\n" + TEX_TEXT_TO_REPLACE + "\n\\end{align*}",
    )
#-----------FULL
TEMPLATE_TEX_FILE_FULL = os.path.join(
    THIS_DIR,"tex_files", "tex_template_full.tex")
with open(TEMPLATE_TEX_FILE_FULL, "r") as infile:
    TEMPLATE_TEXT_FILE_BODY_FULL = infile.read()
    TEMPLATE_TEX_FILE_BODY_FULL = TEMPLATE_TEXT_FILE_BODY_FULL.replace(
        TEX_TEXT_TO_REPLACE,
        "\\begin{align*}\n" + TEX_TEXT_TO_REPLACE + "\n\\end{align*}",
    )
#----------Custom
def get_template_tex(mode,begin="\\begin{align*}\n",end="\n\\end{align*}"):
    ttf=os.path.join(THIS_DIR,"tex_files", "tex_template_%s.tex"%mode)
    with open(ttf, "r") as infile:
        ttextfb = infile.read()
        ttexfb = ttextfb.replace(
            TEX_TEXT_TO_REPLACE,
            begin + TEX_TEXT_TO_REPLACE + end,
        )
        return ttextfb,ttexfb


HELP_MESSAGE = """
   Usage:
   python extract_scene.py <module> [<scene name>]
   -p preview in low quality
   -s show and save picture of last frame
   -w write result to file [this is default if nothing else is stated]
   -o <file_name> write to a different file_name
   -l use low quality
   -m use medium quality
   -a run and save every scene in the script, or all args for the given scene
   -q don't print progress
   -f when writing to a movie file, export the frames in png sequence
   -t use transperency when exporting images
   -n specify the number of the animation to start from
   -r specify a resolution
   -c specify a background color
"""
SCENE_NOT_FOUND_MESSAGE = """
   {} is not in the script
"""
CHOOSE_NUMBER_MESSAGE = """
Choose number corresponding to desired scene/arguments.
(Use comma separated list for multiple entries)
Choice(s): """
INVALID_NUMBER_MESSAGE = "Fine then, if you don't want to give a valid number I'll just quit"

NO_SCENE_MESSAGE = """
   There are no scenes inside that module
"""

NOT_SETTING_FONT_MSG='''
Warning:
You haven't set font.
If you are not using English, this may cause text rendering problem.
You set font like:
text = Text('your text', font='your font')
or:
class MyText(Text):
    CONFIG = {
        'font': 'My Font'
    }
'''
START_X_FONT = 30
START_Y_FONT = 20
NORMAL_FONT = 'NORMAL'
ITALIC_FONT = 'ITALIC'
OBLIQUE_FONT = 'OBLIQUE'
BOLD_FONT = 'BOLD'

# There might be other configuration than pixel shape later...
PRODUCTION_QUALITY_CAMERA_CONFIG = {
    "pixel_height": 1080,
    "pixel_width": 1920,
    "frame_rate": 60,
}

HIGH_QUALITY_CAMERA_CONFIG = {
    "pixel_height": 1080,
    "pixel_width": 1920,
    "frame_rate": 30,
}

MEDIUM_QUALITY_CAMERA_CONFIG = {
    "pixel_height": 720,
    "pixel_width": 1280,
    "frame_rate": 30,
}

LOW_QUALITY_CAMERA_CONFIG = {
    "pixel_height": 480,
    "pixel_width": 854,
    "frame_rate": 15,
}

CUSTOM_QUALITY_CAMERA_CONFIG = {
    "pixel_height": 720,
    "pixel_width": 1280,
    "frame_rate": 10,
}

DEFAULT_PIXEL_HEIGHT = PRODUCTION_QUALITY_CAMERA_CONFIG["pixel_height"]
DEFAULT_PIXEL_WIDTH = PRODUCTION_QUALITY_CAMERA_CONFIG["pixel_width"]
DEFAULT_FRAME_RATE = 30

DEFAULT_POINT_DENSITY_2D = 25
DEFAULT_POINT_DENSITY_1D = 250

DEFAULT_STROKE_WIDTH = 4

FRAME_HEIGHT = 8.0
FRAME_WIDTH = FRAME_HEIGHT * DEFAULT_PIXEL_WIDTH / DEFAULT_PIXEL_HEIGHT
FRAME_Y_RADIUS = FRAME_HEIGHT / 2
FRAME_X_RADIUS = FRAME_WIDTH / 2

SMALL_BUFF = 0.1
MED_SMALL_BUFF = 0.25
MED_LARGE_BUFF = 0.5
LARGE_BUFF = 1

DEFAULT_MOBJECT_TO_EDGE_BUFFER = MED_LARGE_BUFF
DEFAULT_MOBJECT_TO_MOBJECT_BUFFER = MED_SMALL_BUFF


# All in seconds
DEFAULT_POINTWISE_FUNCTION_RUN_TIME = 3.0
DEFAULT_WAIT_TIME = 1.0


ORIGIN = np.array((0., 0., 0.))
UP = np.array((0., 1., 0.))
DOWN = np.array((0., -1., 0.))
RIGHT = np.array((1., 0., 0.))
LEFT = np.array((-1., 0., 0.))
IN = np.array((0., 0., -1.))
OUT = np.array((0., 0., 1.))
X_AXIS = np.array((1., 0., 0.))
Y_AXIS = np.array((0., 1., 0.))
Z_AXIS = np.array((0., 0., 1.))

# Useful abbreviations for diagonals
UL = UP + LEFT
UR = UP + RIGHT
DL = DOWN + LEFT
DR = DOWN + RIGHT

TOP = FRAME_Y_RADIUS * UP
BOTTOM = FRAME_Y_RADIUS * DOWN
LEFT_SIDE = FRAME_X_RADIUS * LEFT
RIGHT_SIDE = FRAME_X_RADIUS * RIGHT

PI = np.pi
TAU = 2 * PI
DEGREES = TAU / 360

FFMPEG_BIN = "ffmpeg"

# Colors
COLOR_MAP = {
    "DARK_BLUE": "#236B8E",
    "DARK_BROWN": "#8B4513",
    "LIGHT_BROWN": "#CD853F",
    "BLUE_E": "#1C758A",
    "BLUE_D": "#29ABCA",
    "BLUE_C": "#58C4DD",
    "BLUE_B": "#9CDCEB",
    "BLUE_A": "#C7E9F1",
    "TEAL_E": "#49A88F",
    "TEAL_D": "#55C1A7",
    "TEAL_C": "#5CD0B3",
    "TEAL_B": "#76DDC0",
    "TEAL_A": "#ACEAD7",
    "GREEN_E": "#699C52",
    "GREEN_D": "#77B05D",
    "GREEN_C": "#83C167",
    "GREEN_B": "#A6CF8C",
    "GREEN_A": "#C9E2AE",
    "YELLOW_E": "#E8C11C",
    "YELLOW_D": "#F4D345",
    "YELLOW_C": "#FFFF00",
    "YELLOW_B": "#FFEA94",
    "YELLOW_A": "#FFF1B6",
    "GOLD_E": "#C78D46",
    "GOLD_D": "#E1A158",
    "GOLD_C": "#F0AC5F",
    "GOLD_B": "#F9B775",
    "GOLD_A": "#F7C797",
    "RED_E": "#CF5044",
    "RED_D": "#E65A4C",
    "RED_C": "#FC6255",
    "RED_B": "#FF8080",
    "RED_A": "#F7A1A3",
    "MAROON_E": "#94424F",
    "MAROON_D": "#A24D61",
    "MAROON_C": "#C55F73",
    "MAROON_B": "#EC92AB",
    "MAROON_A": "#ECABC1",
    "PURPLE_E": "#644172",
    "PURPLE_D": "#715582",
    "PURPLE_C": "#9A72AC",
    "PURPLE_B": "#B189C6",
    "PURPLE_A": "#CAA3E8",
    "WHITE": "#FFFFFF",
    "BLACK": "#000000",
    "LIGHT_GRAY": "#BBBBBB",
    "LIGHT_GREY": "#BBBBBB",
    "GRAY": "#888888",
    "GREY": "#888888",
    "DARK_GREY": "#444444",
    "DARK_GRAY": "#444444",
    "DARKER_GREY": "#222222",
    "DARKER_GRAY": "#222222",
    "GREY_BROWN": "#736357",
    "PINK": "#D147BD",
    "GREEN_SCREEN": "#00FF00",
    "ORANGE": "#FF862F",
    #TB-colors
    "TT_FONDO_0": "#303038",
    "TT_FONDO_1": "#4f4a51",
    "TT_FONDO_2": "#23262b",
    "TT_FONDO_VERDE": "#3f7d5c",
    "TT_FONDO_AZUL": "#474a66",
    "TT_FONDO_NARANJA": "#e6613a",
    "TT_FONDO_ROSA": "#942357",
    "TT_VERDE_1": "#118559",
    "TT_VERDE_2": "#00e300",
    "TT_TEXTO": "#d7d7d7",
    "TT_AZULROYAL_1": "#266bb3",
    "TT_AZULROYAL_2": "#426391",
    "TT_PURPURAROYAL": "#8561b5",
    "TT_AZUL_T": "#68a8e1",
    "TT_NARANJA_T": "#e37000",
    "TT_ROSA_T": "#ca9797",
    "TT_AMARILLO_T": "#fff000",
    "TT_SIMBOLO": "#fffab3",
    "TT_PURPURA_D": "#973097",
    #M
    "M_FONDO_0": "#303030",
    "M_FONDO_1": "#232323",
    "M_FONDO_2":"#3f3f3f",
    "M_TEXTO_VERDE": "#94942b",
    "M_FONDO_GRIS": "#cacaca",
    "M_FONDO_VERDE": "#caca94",
    #N
    "N_AZUL_CLARO":"#389ebd",
    "N_VERDE_CLARO":"#7f7f00",
    "N_FONDO_OSCURO":"#232323",
    "N_FONDO_MEDIO":"#303030",
    "N_CYAN_1":"#4282a1",
    "N_CYAN_2":"#476e82",
    "N_ROJO_1":"#bd3019",
    "N_ROJO_2":"#8c2311",
    "N_FONDO_MORADO":"#ab97b5",
    "N_MORADO_OSCURO":"#7f7fff",
    "N_FONDO_NARANJA":"#c58f7f",
    "N_FONDO_VERDE_PASTEL":"#cce1d4",
    #ST
    "ROSA_ST":"#F8206B",
    "VERDE_ST":"#A1E303",
    "AMARILLO_ST":"#E6DC6B",
    "FONDO_ST":"#272822",
    "AZUL_ST":"#64DAF8",
    "NARANJA_ST":"#FF9514",
}
PALETTE = list(COLOR_MAP.values())
locals().update(COLOR_MAP)
for name in [s for s in list(COLOR_MAP.keys()) if s.endswith("_C")]:
    locals()[name.replace("_C", "")] = locals()[name]

# Streaming related configuration
LIVE_STREAM_NAME = "LiveStream"
TWITCH_STREAM_KEY = "YOUR_STREAM_KEY"
STREAMING_PROTOCOL = "tcp"
STREAMING_IP = "127.0.0.1"
STREAMING_PORT = "2000"
STREAMING_CLIENT = "ffplay"
STREAMING_URL = f"{STREAMING_PROTOCOL}://{STREAMING_IP}:{STREAMING_PORT}?listen"
STREAMING_CONSOLE_BANNER = """
Manim is now running in streaming mode. Stream animations by passing
them to manim.play(), e.g.
>>> c = Circle()
>>> manim.play(ShowCreation(c))
"""

def set_custom_quality(height,fps):
    video_parameters=[
        ("pixel_height",height),
        ("pixel_width",int(height*16/9)),
        ("frame_rate",fps)
    ]
    for v_property,v_value in video_parameters:
        CUSTOM_QUALITY_CAMERA_CONFIG[v_property]=v_value

def return_tex_file(tex_template):
    return os.path.join(
        THIS_DIR,"tex_files", tex_template if not TEX_USE_CTEX
        else "ctex_template.tex"
        )

def return_tex_template(width,template_file="tex_template.tex"):
    tex_template = return_tex_file(template_file)
    with open(tex_template, "r") as infile:
        PRE_JUSTIFY_TEXT = infile.read()
        JUSTIFY_TEXT = PRE_JUSTIFY_TEXT.replace(
        TEX_TEXT_TO_REPLACE,
        "\\begin{tabular}{p{%s cm}}"%width + TEX_TEXT_TO_REPLACE + "\\end{tabular}")
        return JUSTIFY_TEXT