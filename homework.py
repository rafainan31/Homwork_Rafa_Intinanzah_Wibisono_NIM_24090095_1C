title=' Penyaluran Bansos Stunting'
print(title.upper())

Biodata = {f'nama orang tua' : 'imam arif',
           'nama anak' : 'tito',
           'umur anak' : 3,
           'pekerjaan orang tua' : 'pekerja swasta',
           'pendapatan' : 2100000,}
Biodata = {f'nama oranga tua' : 'gunawan' ,
             'nama anak' : 'joseph',
             'umur anak' : 2,
             'pekerjaan orang tua' : 'petani',
             'pendapatan' : 1000000,}
Biodata = {f'nama orang tua' : 'avis',
             'nama anak' : 'siti astuti',
             'umur anak' : 2,
             'pekerjaan orang tua' : 'pns',
             'pendapatan' : 3500000,}
Biodata = {f'nama orang tua' : 'sambo',
             'nama anak' : 'putri candrawati',
             'umur anak' : 3,
             'pekerjaan orang tua' : 'polisi',
             'pendapatan' : 5500000,}

nama  = str(input('masukan nama orang tua :'))
nama = str(input('masukan nama anak :'))
umur = int(input('masukan umur :'))
pekerjaan_orang_tua = str(input('masukan pekerjaan orang tua :'))
pendapatan = int(input('masukan pendapatan :'))
layak_mendapatkan = True
tidak_layak_mendapatkan = False
pekerjaan_yang_tidak_layak_mendapatkan_bansos_stunting = {'pns','polisi'}

if (pekerjaan_orang_tua not in pekerjaan_yang_tidak_layak_mendapatkan_bansos_stunting) and layak_mendapatkan or tidak_layak_mendapatkan and (pendapatan <= 1000000):
    hasil = ('mendapatkan bansos stunting')
else:
    hasil = ('tidak mendapatkan bansos stunting')

print('nama : ', nama)
print('nama :', nama)
print('umur : ', umur) 
print('pekerjaan :', pekerjaan_orang_tua)
print('pendapatan :', pendapatan)
print('klasifikasi :', hasil)

