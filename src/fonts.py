import pathlib
from kivy.resources import resource_add_path
from kivy.core.text import LabelBase, DEFAULT_FONT

# プロジェクトルートからの assets/fonts ディレクトリを絶対パスで取得
BASE_DIR = pathlib.Path(__file__).parent.parent
FONTS_DIR = BASE_DIR / "assets" / "fonts"
IPA_FONT = FONTS_DIR / "ipaexg.ttf"

# Kivy に「ここもリソースパスです」と教える
resource_add_path(str(FONTS_DIR))

# DEFAULT_FONT として参照される名前をすべて ipaexg.ttf に置き換え
LabelBase.register(
    name=DEFAULT_FONT,
    fn_regular=str(IPA_FONT),
    fn_bold=str(IPA_FONT),
    fn_italic=str(IPA_FONT),
    fn_bolditalic=str(IPA_FONT),
)
