# takes a number
# returns a string based on factors of 3,5,7 or returns the num
def gen_rain_drops(num):
    rain = ""

    if num % 3 == 0:
        rain += "Pling"
    if num % 5 == 0:
        rain += "Plang"
    if num % 7 == 0:
        rain += "Plong"

    if rain == "":
        print(num)
    else:
        print(rain)


gen_rain_drops(28)
gen_rain_drops(30)
gen_rain_drops(34)
