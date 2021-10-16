print("----Status Kelulusan Ujian Mahasiswa----")
nama= (input("Nama : "))
mtk= float(input("Nilai Matematika : "))
bhsindo= float(input("Nilai Bhs. Indonesia : "))
ipa= float(input("Nilai IPA : "))
if (mtk>70) and (bhsindo>60) and (ipa>60):
    print("Status Kelulusan : ", nama,"Dinyatakan LULUS")
else:
    print("Status Kelulusan : ", nama,"Dinyatakan TIDAK LULUS")