import customtkinter as ctk
import random
import string

from func import Encoder, Decrypt


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")



TITLE_FONT = ("Segoe UI", 26, "bold")
TEXT_FONT = ("Segoe UI", 16)
BUTTON_FONT = ("Segoe UI", 15, "bold")



LANG = {

    "Русский": {
        "title": "CRYPTO-BLOCK",
        "text": "Текст",
        "key": "Ключ",
        "depth": "Сила преобразования",
        "encrypt": "Зашифровать",
        "decrypt": "Расшифровать",
        "generate": "Создать ключ",
        "strength": "Надёжность ключа:",
        "error": "❌ Неверные данные",
        "copy": "📋 Копировать",
        "depth_error": "❌ Максимальная глубина кодирования не может превышать 900."

    },

    "English": {
        "title": "CRYPTO-BLOCK",
        "text": "Text",
        "key": "Key",
        "depth": "Transformation strength",
        "encrypt": "Encrypt",
        "decrypt": "Decrypt",
        "generate": "Generate key",
        "strength": "Strength:",
        "error": "❌ Invalid data",
        "copy": "📋 Copy",
        "depth_error": "❌ The maximum encoding depth cannot exceed 900."
    },

    "中文": {
        "title": "CRYPTO-BLOCK",
        "text": "文本",
        "key": "密钥",
        "depth": "转换强度",
        "encrypt": "加密",
        "decrypt": "解密",
        "generate": "生成密钥",
        "strength": "强度:",
        "error": "❌ 数据错误",
        "copy": "📋 复制",
        "depth_error": "❌ 最大编码深度不能超过900."
    },

    "Español": {
        "title": "CRYPTO-BLOCK",
        "text": "Texto",
        "key": "Clave",
        "depth": "Fuerza de transformación",
        "encrypt": "Cifrar",
        "decrypt": "Descifrar",
        "generate": "Crear clave",
        "strength": "Fuerza:",
        "error": "❌ Datos incorrectos",
        "copy": "📋 Copiar",
        "depth_error": "❌ La profundidad máxima de codificación no puede superar 900."
    }
}




class CryptoApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.lang = "Русский"
        self.strength_value = 0
        self.last_output = ""

        self.geometry("700x780")
        self.minsize(700, 780)
        self.title("CRYPTO-BLOCK")
        self.resizable(False, False)



        # HEADER

        header = ctk.CTkFrame(
            self,
            corner_radius=30
        )

        header.pack(
            padx=25,
            pady=15,
            fill="x"
        )



        self.title_label = ctk.CTkLabel(
            header,
            text="",
            font=TITLE_FONT
        )

        self.title_label.pack(
            side="left",
            padx=20
        )


        self.language = ctk.CTkOptionMenu(
            header,
            values=list(LANG.keys()),
            width=150,
            command=self.change_language
        )

        self.language.pack(
            side="right",
            padx=10
        )


        self.theme = ctk.CTkSwitch(
            header,
            text="☀️ / 🌙",
            command=self.change_theme
        )

        self.theme.pack(
            side="right",
            padx=10
        )




        # MAIN CARD

        card = ctk.CTkFrame(
            self,
            corner_radius=35
        )

        card.pack(
            padx=25,
            pady=5
        )



        self.text_label = ctk.CTkLabel(
            card,
            text="",
            font=TEXT_FONT
        )

        self.text_label.pack(
            pady=10
        )

        self.text_box = ctk.CTkTextbox(
            card,
            width=520,
            height=120,
            corner_radius=25,
            font=TEXT_FONT
        )


        self.text_box.pack(
            pady=10
        )


        self.key_label = ctk.CTkLabel(
            card,
            text="",
            font=TEXT_FONT
        )

        self.key_label.pack(
            pady=(0, 5)
        )



        self.key = ctk.CTkEntry(
            card,
            width=520,
            height=45,
            corner_radius=25,
            font=TEXT_FONT
        )

        self.key.pack(
            pady=8
        )

        self.strength_label = ctk.CTkLabel(
            card,
            text="",
            font=TEXT_FONT
        )

        self.strength_label.pack(
            pady=(0, 5)
        )

        self.strength = ctk.CTkProgressBar(
            card,
            width=520,
            height=8,
            corner_radius=10
        )

        self.strength.pack()

        self.strength.set(0)

        self.key.bind(
            "<KeyRelease>",
            self.check_strength
        )



        self.generate_btn = ctk.CTkButton(
            card,
            width=220,
            height=35,
            corner_radius=20,
            font=BUTTON_FONT,
            command=self.generate_key
        )

        self.generate_btn.pack(
            pady=5
        )

        self.depth_label = ctk.CTkLabel(
            card,
            text="",
            font=TEXT_FONT
        )

        self.depth_label.pack(
            pady=5
        )



        self.depth = ctk.CTkEntry(
            card,
            width=520,
            height=45,
            corner_radius=25,
            font=TEXT_FONT
        )

        self.depth.pack()




        buttons = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        buttons.pack(
            pady=10
        )



        self.encrypt_btn = ctk.CTkButton(
            buttons,
            width=220,
            height=45,
            corner_radius=30,
            font=BUTTON_FONT,
            command=self.encrypt
        )

        self.encrypt_btn.grid(
            row=0,
            column=0,
            padx=15
        )



        self.decrypt_btn = ctk.CTkButton(
            buttons,
            width=220,
            height=45,
            corner_radius=30,
            font=BUTTON_FONT,
            command=self.decrypt
        )

        self.decrypt_btn.grid(
            row=0,
            column=1,
            padx=15
        )


        # OUTPUT

        self.result = ctk.CTkTextbox(
            card,
            width=520,
            height=130,
            corner_radius=25,
            font=TEXT_FONT
        )

        self.result.pack(
            pady=(5, 10)
        )

        self.copy_btn = ctk.CTkButton(
            card,
            text="",
            width=220,
            height=35,
            corner_radius=20,
            font=BUTTON_FONT,
            command=self.copy_result
        )

        self.copy_btn.pack(
            pady=(0, 5)
        )

        self.result.configure(
            state="disabled"
        )

        self.update_language()




    def update_language(self):

        lang = LANG[self.lang]

        self.title_label.configure(
            text="🔐 "+lang["title"]
        )

        self.text_label.configure(
            text=lang["text"]
        )

        self.key_label.configure(
            text=lang["key"]
        )

        self.depth_label.configure(
            text=lang["depth"]
        )

        self.encrypt_btn.configure(
            text="🔒 "+lang["encrypt"]
        )

        self.decrypt_btn.configure(
            text="🔓 "+lang["decrypt"]
        )

        self.generate_btn.configure(
            text="🎲 "+lang["generate"]
        )

        self.copy_btn.configure(
            text=lang["copy"]
        )

        self.check_strength()

        if self.last_output == "DEPTH_ERROR":
            self.output(
                LANG[self.lang]["depth_error"]
            )




    def change_language(self,value):

        self.lang=value
        self.update_language()




    def change_theme(self):

        if self.theme.get():
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")

    def check_strength(self, event=None):

        key = self.key.get()

        if not key:
            self.strength.set(0)

            self.strength_label.configure(
                text=""
            )

            # полностью очищаем визуальный остаток
            self.strength.configure(
                progress_color=(
                    "#1f1f1f",
                    "#1f1f1f"
                )
            )

            return

        score = 0

        if len(key) >= 4:
            score += 0.25

        if len(key) >= 10:
            score += 0.25

        if any(c.isdigit() for c in key):
            score += 0.2

        if any(c.isupper() for c in key):
            score += 0.15

        if any(not c.isalnum() for c in key):
            score += 0.15

        self.strength.set(score)

        if score < 0.4:
            icon = ""
            color = "#ff3b30"

        elif score < 0.75:
            icon = ""
            color = "#ffcc00"

        else:
            icon = ""
            color = "#34c759"

        self.strength.configure(
            progress_color=color
        )

        self.strength_label.configure(
            text=LANG[self.lang]["strength"] + " " + icon
        )


    def generate_key(self):

        key="".join(
            random.choice(
                string.ascii_letters+
                string.digits+
                "!@#$%"
            )
            for _ in range(16)
        )


        self.key.delete(0,"end")
        self.key.insert(0,key)

        self.check_strength()

    def get_data(self):

        text = self.text_box.get(
            "1.0",
            "end-1c"
        )

        key = self.key.get()

        depth = self.depth.get()

        if not key or not depth.isdigit():
            return None

        depth = int(depth)

        if depth > 900:
            return "DEPTH_ERROR"

        if depth < 1:
            return None

        return text, key, depth

    def output(self, text):

        self.last_output = text

        self.result.configure(
            state="normal"
        )

        self.result.delete(
            "1.0",
            "end"
        )

        self.result.insert(
            "end",
            text
        )

        self.result.configure(
            state="disabled"
        )



    def copy_result(self):

        text = self.result.get(
            "1.0",
            "end"
        ).strip()

        if text:
            self.clipboard_clear()
            self.clipboard_append(text)

    def encrypt(self):

        data = self.get_data()

        if data == "DEPTH_ERROR":
            self.output(
                LANG[self.lang]["depth_error"]
            )
            return

        if not data:
            self.output(
                LANG[self.lang]["error"]
            )
            return

        text, key, depth = data

        self.output(
            Encoder(text, key, depth)
        )

    def decrypt(self):

        data = self.get_data()

        if data == "DEPTH_ERROR":
            self.last_output = "DEPTH_ERROR"

            self.output(
                LANG[self.lang]["depth_error"]
            )
            return

        if not data:
            self.output(
                LANG[self.lang]["error"]
            )
            return

        text, key, depth = data

        try:
            self.output(
                Decrypt(text, key, depth)
            )

        except:
            self.output(
                LANG[self.lang]["error"]
            )




app=CryptoApp()
app.mainloop()