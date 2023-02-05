""""""


class Mexmonhona:
    def __init__(self, narxlar, tozalash_xizmati, nonushta, tushlik, kechlik):
        self.narxlar = narxlar
        self.tozalash_xizmati = tozalash_xizmati
        self.nonushta = nonushta
        self.tushlik = tushlik
        self.kechlik = kechlik

    def main_info(self):
        return f"1 haftalik narxlar:{self.narxlar}, nonushta:{self.nonushta}, " \
               f"tushlik:{self.tushlik}, kechki ovqat:{self.kechlik}"

    def return_info(self):
        main_info = self.main_info()
        return f"Mexmonxona info: {main_info}"


class Yashash:
    def __init__(self, bir_kun, bir_hafta, bir_oy, bir_yil):
        self.bir_kun = bir_kun
        self.bir_hafta = bir_hafta
        self.bir_oy = bir_oy
        self.bir_yil = bir_yil

    def main_info(self):
        return f"bir kun:{self.bir_kun}, bir hafta:{self.bir_hafta}" \
               f"bir oy:{self.bir_oy}, bir yil:{self.bir_yil}"

    def return_info(self):
        main_info = self.main_info()
        return f"Yashash info: {main_info}"


class AviaBilet:
    def __init__(self, premium_bilet, bizness_bilet, econom_bilet):
        self.premium_bilet = premium_bilet
        self.bizness_bilet = bizness_bilet
        self.econom_bilet = econom_bilet

    def main_info(self):
        return f"premium bilet:{self.premium_bilet}, " \
               f"bizness bilet:{self.bizness_bilet}" \
               f"econom bilet:{self.econom_bilet}"

    def bilet(self):
        familiy_price = 1500
        if self.premium_bilet == familiy_price:
            return self.premium_bilet
        elif self.bizness_bilet <= familiy_price:
            return self.bizness_bilet
        else:
            return self.econom_bilet

    def return_info(self):
        bilet = self.main_info()
        return f"Bilet price:{bilet}"


mexmonxona = Mexmonhona("premium class 1200$, bizness class 650$, standart class 350$",
                        "tozalash xizmati bepul",
                        " kritilgan",
                        " kiritilmagan",
                        " ovqat kiritilgan")

yashash = Yashash("premium 200$, bizness 100$, standart 50$",
                  "premium 1200$, bizness 650$, standart 350$",
                  "premium 4800$, bizness 2600$, standart 1400$",
                  "premium 57.600$, bizness 31.200$, standart 16.800$")

bilet = AviaBilet(1500, 3500, 800)


print(mexmonxona.return_info())
print(yashash.return_info())
print(Avia_Bilet.return_info(bilet))
