import os
from kivy.resources import resource_add_path, resource_find
from kivy.core.text import LabelBase, DEFAULT_FONT

# iOSでは __file__ を使った path 解決が正しく動作しないため、
# 相対パスで指定して resource_find に依存する方式に変更
resource_add_path(os.path.join(os.path.dirname(__file__), "assets", "fonts"))

# ipaexg.ttf のパスを取得（リソースとして正しく見つかることを確認）
ipa_font_path = resource_find("ipaexg.ttf")
if not ipa_font_path:
    raise FileNotFoundError("ipaexg.ttf がリソースパスに見つかりません")

LabelBase.register(
    name=DEFAULT_FONT,
    fn_regular=ipa_font_path,
    fn_bold=ipa_font_path,
    fn_italic=ipa_font_path,
    fn_bolditalic=ipa_font_path,
)
