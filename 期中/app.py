# app.py

from translator import translate_text

def main():
    print("🔤 歡迎使用簡易翻譯器")
    while True:
        text = input("請輸入要翻譯的英文句子（輸入 q 離開）：\n> ")
        if text.lower() == "q":
            break
        translated = translate_text(text)
        print("👉 翻譯結果：", translated)
        print("")

if __name__ == "__main__":
    main()
