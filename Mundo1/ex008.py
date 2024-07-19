import os

def clear_console():
    os.system('cls')

clear_console()

def meter_converter(meter):
    km = meter / 1000
    hm = meter / 100
    dam = meter / 10
    dm = meter * 10
    cm = meter * 100
    mm = meter * 1000
    
    return km, hm, dam, dm, cm, mm

meter = int(input('Digite uma distância em metros: '))
km, hm, dam, dm, cm, mm = meter_converter(meter)

print('{}'.format(km) + 'km')
print('{}'.format(hm) + 'hm')
print('{}'.format(dam) + 'dam')
print('{}'.format(dm) + 'dm')
print('{}'.format(cm) + 'cm')
print('{}'.format(mm) + 'mm')