def diamond(tinggi, state):
    letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # Atas
    for i in range(1, tinggi + 1):
        baris = ''

        # Section Space
        for j in range(tinggi - i):
            baris += ' '

        angka = 1
        # Section Line Numbers
        for k in range(1, i + 1): #123
            baris += letter_list[angka-1] #123
            angka += 1 #234
            
        angka -= 2 #karna di awal sudah nambah 1 dan di akhir ditambah 1 lagi, supaya turun 2 angka sesuai urutan perlu dikurangin 2
        
        # Section Total Reverse Numbers Line
        for l in range(i - 1, 0, -1):
            # print(i-1)
            baris += letter_list[l-1]
            angka -= 1
        
        # Menampilkan baris
        print(baris)
        
    # Bawah
    if state == "even":
        for i in range(tinggi, 0, -1):
            baris = ''

            # Section Space
            for j in range(tinggi - i):
                baris += ' '

            angka = 1
            # Section Line Numbers
            for k in range(1, i + 1): #123
                baris += letter_list[angka-1] #123
                angka += 1 #234
                
            angka -= 2 #karna di awal sudah nambah 1 dan di akhir ditambah 1 lagi, supaya turun 2 angka sesuai urutan perlu dikurangin 2
            
            # Section Total Reverse Numbers Line
            for l in range(i - 1, 0, -1):
                # print(i-1)
                baris += letter_list[l-1]
                angka -= 1
            
            # Menampilkan baris
            print(baris)
    else:
        for i in range(tinggi-1, 0, -1):
            baris = ''

            # Section Space
            for j in range(tinggi - i):
                baris += ' '

            angka = 1
            # Section Line Numbers
            for k in range(1, i + 1): #123
                baris += letter_list[angka-1] #123
                angka += 1 #234
                
            angka -= 2 #karna di awal sudah nambah 1 dan di akhir ditambah 1 lagi, supaya turun 2 angka sesuai urutan perlu dikurangin 2
            
            # Section Total Reverse Numbers Line
            for l in range(i - 1, 0, -1):
                # print(i-1)
                baris += letter_list[l-1]
                angka -= 1
            
            # Menampilkan baris
            print(baris)

def sanitize_input():
    max = 9
    tinggi = input("Masukkan Tinggi Yang diinginkan ("+ str(max) + ") : ")
    if not tinggi.isdigit():
        print('Please Only Input Numbers!!!')
        return sanitize_input()
    state = "even" if int(tinggi) % 2 == 0 else "odd"
    tinggi = int((int(tinggi) + 1) / 2)
    if tinggi > max:
        print(f'Max Height is ' + str(max) + ' for better view.')
        return sanitize_input()
    return diamond(tinggi, state)

sanitize_input()