Ta = int(input("Kindly enter the air temprature"))
V = int(input("Kindly enter the wind speed"))

WCI = 13.12 + 0.6215Ta  - 11.37V ** 0.16 + 0.3965TaV ** 0.16

Print("The wind chill index is:" + str (WCI))