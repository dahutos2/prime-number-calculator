#!/bin/bash
set -e

# iOSプロジェクト名はプロジェクトルート名と合わせて
APP_NAME="primecalc"
PROJECT_DIR="${APP_NAME}-ios"
DICTIONARY="./" 
PYTHON_LIB="$HOME/.kivy-ios/build/python3/build/lib/libpython3.a"

echo "🔍 Python3 iOSビルドの確認"
if [ ! -f "$PYTHON_LIB" ]; then
    echo "📥 Python3 を iOS 向けにビルドします..."
    toolchain build python3
else
    echo "✅ Python3 は既にビルド済みです"
fi

echo "🔧 Kivy コアライブラリのビルド"
toolchain build kivy

echo "📦 iOS アプリプロジェクト作成 or 再利用"
if [ ! -d "$PROJECT_DIR" ]; then
    toolchain create "$APP_NAME" "$DICTIONARY"
else
    echo "✅ 既存の $PROJECT_DIR を再利用します"
fi

echo "📁 フォントを同期 (assets/fonts → $PROJECT_DIR/assets/fonts/)"
rm -rf "$PROJECT_DIR/assets/fonts"
mkdir -p "$PROJECT_DIR/assets/fonts"
cp assets/fonts/ipaexg.ttf "$PROJECT_DIR/assets/fonts/"

echo "✅ 完了: $PROJECT_DIR に iOS ビルド環境が整いました"
