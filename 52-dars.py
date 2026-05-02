class Davlatlar:
    def __init__(self, nomi, poytaxti, aholisi):
        self.nomi = nomi
        self.poytaxti = poytaxti
        self.aholisi = aholisi
        self.joylashuvi = "Yevropa"
        self.tili = "Ingliz tili"
        self.maydoni = 1000000
    def get_nomi(self):
        return f"{self.nomi.title()} davlati"
    def get_poytaxti(self):
        return f"{self.nomi.title()}ning poytaxti {self.poytaxti.title()} shahridir."
    def get_aholisi(self):
        return f"{self.nomi.title()}ning aholisi {self.aholisi} million kishidir."
    def get_joylashuvi(self):
        return f"{self.nomi.title()} davlati {self.joylashuvi.title()}da joylashgan."
    def get_tili(self):
        return f"{self.nomi.title()} davlati {self.tili.title()} tilini ishlatadi."
    def get_maydoni(self):
        return f"{self.nomi.title()} davlati {self.maydoni} kv. km maydon qo'lga kiritadi."
     
Uzb = Davlatlar       ("uzbekiston", "toshkent", 448978, "Osiya", "Ingliz tili", 1000000)
rus = Davlatlar       ("rossiya", "moskva", 144478, "Yevropa", "Rus tili", 17098242)
print(Uzb.get_nomi())
print(Uzb.get_poytaxti())
class shaxs:
    def __init__(self, ism, yosh, tyili):
        self.ism = name
        self.yosh = age
        self.tyili = year

    def get_ism(self):
        return f"Shaxsning ismi {self.ism.title()}."
    def get_yosh(self):
        return f"{self.ism.title()}ning yoshi {self.yosh} yoshda."
    def get_tili(self):
        return f"{self.ism.title()}ning tili {self.tili.title()}."
    def get_tyili(self):
        return f"{self.ism.title()} {self.tyili} yilda tug'ilgan."
class Talaba(shaxs):
    def __init__(self, ism, yosh, tyili, id):
        super().__init__(ism, yosh, tyili)
        self.bosqich = bosqich
t=Talaba("Ali", 20, 2004, 12345)
print(t.get_ism())
