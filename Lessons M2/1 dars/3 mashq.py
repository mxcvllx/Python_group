""""""
"""
3. Computer klass va obyekt yarating, ma'lumotlarini chop eting.
"""
class Computer:

    def __init__(self, name, color, device, memory_ssd, memory_hdd, ram):
        print(name, color, device, memory_ssd, memory_hdd, ram)
        self.name = name
        self.color = color
        self.device = device
        self.ssd = memory_ssd
        self.hdd = memory_hdd
        self.ram = ram


print("1-project")
name = "Mac"
color = "White"
device = "M1"
hdd = "None"
ssd = "1tb"
ram = "16 gb"

computer_object1 = Computer(name, color, device, hdd, ssd, ram)
print(f" Name:{name},  "
      f" Color:{color}, "
      f" device:{device}, "
      f" hdd:{hdd},"
      f" ssd:{ssd}, "
      f" ram:{ram} ")


print("2-project")
name = "Aser"
color = "Black"
device = "Core i7"
hdd = "1tb"
ssd = "500gb"
ram = "8 gb"

computer_object2 = Computer(name, color, device, hdd, ssd, ram)

print(f"Name:{name}, "
      f" Color:{color}, "
      f" device:{device}, "
      f" hdd:{hdd}, "
      f" ssd:{ssd}, "
      f" ram:{ram} ")