#Bank Account Simulator
def main():

    print('Welcome to My Bank')
    name = input("Please enter your name: ").lower()
    balance = float(input("Enter initial Balance: $"))

#main menu
    while True:
        print(f'Welcome {name}!')
        print('1. Check Balance')
        print('2. Deposit Money')
        print('3. Withdraw Money')
        print('4. Exit')

        choice = input('Please choose a number: ')
        if choice == '1':
            next_action = input('You chose 1. Back or Next? ').lower()
            if next_action == 'Back':
                print(f'Welcome {name}!')
                print('1. Check Balance')
                print('2. Deposit Money')
                print('3. Withdraw Money')
                print('4. Exit')
            elif next_action == 'next':
                next_action = True
            print(f'Your balance is: ${balance}')

        elif choice == '2':
            next_action = input('You chose 2. Back or Next? ').lower()
            if next_action == 'Back':
                print(f'Welcome {name}!')
                print('1. Check Balance')
                print('2. Deposit Money')
                print('3. Withdraw Money')
                print('4. Exit')
            elif next_action == 'next':
                next_action = True
                deposit = float(input(f'Please enter the amount you wish to deposit: $'))
                balance += deposit
            correct = input(f'You wish to deposit ${deposit}. Is this correct? (yes/ no) ').lower()
            if correct == 'yes':
                print(f'You have deposited ${deposit}. Your current balance is ${balance}.')
            elif correct == 'no':
                print('Transaction cancelled.')
            else:
                print('Invalid input. Please enter yes or no) ')

        elif choice  == '3':
            next_action = input('You chose 3. Back or Next? ').lower()
            if next_action == 'Back':
                print(f'Welcome {name}!')
                print('1. Check Balance')
                print('2. Deposit Money')
                print('3. Withdraw Money')
                print('4. Exit')
            elif next_action == 'next':
                next_action = True
            withdraw = float(input('Please enter amount you wish to withdraw: $'))
            balance -= withdraw
            correct = input(f'You wish to withdraw ${withdraw}. Is this correct? (yes/ no) ').lower()
            if correct == 'yes':
                print(f'You have withdrawn ${withdraw}. Your current balance is ${balance}.')
            elif correct == 'no':
                print('Transaction cancelled.')
            else:
                print('Invalid input. Please enter yes or no.')

        elif choice == '4':
            print('Thank you for using My Bank!')
            break
        else:
            print('Invalid input. Please enter a number.')
main()