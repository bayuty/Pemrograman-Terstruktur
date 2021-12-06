try:
    file = open("e:\datalatno6hasil.txt","r")
    filehasil = open("e:\datalatno7.txt","w")

    isi = file.read()

    
    n = int(input("Masukkan angka pergeseran sebelumnya: "))
    
    hasil = ""
    for i in isi:
        char = ord(i)
        if char >= 65 and char <= 90:
            char_enc = char - n
            char_final = chr(char_enc)
            if char_enc < 65:
                char_enc = (char_enc + 90) - 64
                char_final = chr(char_enc)
            
            hasil += char_final
        
        elif char >= 97 and char <= 122:
            char_enc = char - n
            char_final = chr(char_enc)
            if char_enc < 97:
                char_enc = (char_enc + 122) - 96
                char_final = chr(char_enc)
            
            hasil += char_final
        else:
            hasil += chr(char)
                
    print(hasil)        
    filehasil.write(hasil)    
    filehasil.close()

except ValueError:
    print("Input tidak vaild")