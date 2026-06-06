import tkinter as tk
from tkinter import messagebox

# Song class, foydalanuvchi kiritgan so'zga asoslangan qo'shiq yaratish
class Song:
    def __init__(self, keyword):
        self.keyword = keyword
        
    def generate_song(self):
        # Har bir so'z uchun o'ziga xos qo'shiq yaratish
        song_lyrics = f"Bu qo'shiq '{self.keyword}' haqida!\n"
        song_lyrics += f"{self.keyword} bilan birga dunyo g'aroyib,\n"
        song_lyrics += f"Bu dunyo senga, {self.keyword} bilan yorug'\n"
        song_lyrics += f"Har bir qadamda seni eslayman,\n"
        song_lyrics += f"{self.keyword} bilan sevaman, hayotim o'zgaradi.\n"
        return song_lyrics

# Tkinter interfeysi
class SongGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Qo'shiq Generator")
        self.root.geometry("500x400")
        
        # Kirish maydoni
        self.label = tk.Label(self.root, text="Bir so'z kiriting:", font=("Helvetica", 14))
        self.label.pack(pady=10)
        
        # So'z kiritish maydoni
        self.entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.entry.pack(pady=10)
        
        # Qo'shiqni generatsiya qilish tugmasi
        self.generate_button = tk.Button(self.root, text="Qo'shiqni Yaratish", font=("Helvetica", 14), command=self.generate_song)
        self.generate_button.pack(pady=20)
        
        # Natija uchun matn oynasi
        self.result_text = tk.Text(self.root, height=8, width=50, font=("Helvetica", 12), wrap=tk.WORD)
        self.result_text.pack(pady=10)
        
    def generate_song(self):
        # Foydalanuvchidan kiritilgan so'zni olish
        keyword = self.entry.get().strip()
        
        # Agar so'z kiritilmagan bo'lsa, xabar ko'rsatish
        if not keyword:
            messagebox.showerror("Xatolik", "Iltimos, so'zni kiriting!")
            return
        
        # Song ob'ektini yaratish va qo'shiqni olish
        song = Song(keyword)
        song_lyrics = song.generate_song()
        
        # Qo'shiqni matn oynasiga chiqarish
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, song_lyrics)

# Asosiy dastur
if __name__ == "__main__":
    root = tk.Tk()
    app = SongGeneratorApp(root)
    root.mainloop()