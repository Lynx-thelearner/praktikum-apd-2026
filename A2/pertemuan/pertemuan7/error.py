for i in range(3):
    try:
        angka = int(input('Masukkan Angka : '))
    except ValueError:
        print('input yang anda masukkan bukan Integer (angka)')
    else :
        print(f'Angka yang kamu input : {angka}')