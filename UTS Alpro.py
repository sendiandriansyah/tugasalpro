def inputan(komentar):
    masukkan = int(input(komentar + '= '))
    return masukkan

def hargakwh(komentar2):
    masukkanharga = int(input(komentar2 + "= "))
    return masukkanharga

def getkwh(watt, waktu):
    kwh = watt*waktu/1000
    return kwh

def gettotalkwh(lampu, kipas, televisi):
    totalkwh = lampu+kipas+televisi
    return totalkwh

def biaya(kwh, harga):
    perhari = kwh*harga
    return perhari

def main():
    wattlampu = inputan("Watt Lampu")
    wattkipas = inputan("Watt Kipas")
    watttelevisi = inputan("Watt Televisi")
    waktulampu = inputan("Waktu Lampu")
    waktukipas = inputan("Waktu Kipas")
    waktutelevisi = inputan("Waktu Televisi")

    harga = hargakwh("harga")

    kwhlampu = getkwh(wattlampu, waktulampu)
    kwhkipas = getkwh(wattkipas, waktukipas)
    kwhtelevisi = getkwh(watttelevisi, waktutelevisi)
    totalkwh = gettotalkwh(kwhlampu, kwhkipas, kwhtelevisi)

    biayaperhari = biaya(totalkwh, harga)
    biayaperbulan = biaya(biayaperhari, 30)

    print("kWh Lampu:", kwhlampu)
    print("kWh Kipas:", kwhkipas)
    print("kWh Televisi:", kwhtelevisi)
    print("Total kWh:", totalkwh)
    print("Biaya Per Hari: Rp", biayaperhari)
    print("Biaya Per Bulan: Rp", biayaperbulan)
main()