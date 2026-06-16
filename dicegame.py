import random

playing = True
while True:
    choice = input('Lempar dadu? (y/n): ')
    if choice == 'y' or choice == 'Y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
    elif choice == 'n' or choice == 'N':
        print('Dadu tidak dilempar.')
    else:
        print('Pilihan tidak valid. Harap masukkan "y" atau "n".')