import sys

donor_db = [("William Gates, III", [100.0, 120.10]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 343.87, 411.32]),
            ("Mark Zuckerberg", [1660.23, 4320.87, 10432.0]),
            ("Harry Potter", [3000.33, 12345.25])
            ]


def menu():
    prompt = "\n".join(("Welcome to the Mailroom!",
                        "What would you like to do?",
                        '1. Send a Thank You',
                         '2. Create a Report',
                         '3. quit'))
    
    print(prompt)
    
    while True:
        try:
            option = input('Please put in 1, 2, or 3 to pick an action: ')
            if option.strip() == '1':
                return 1
            if option.strip() == '2':
                return 2
            if option.strip() == '3':
                return 3
            else:
                raise ValueError
        except ValueError:
            print('Invalid option.')    


def send_thank_you():
    donor_name = get_donor_name()
    if donor_name.strip() == '':
        return
    else:
        new_donation_amount = new_donation()
        if new_donation_amount == '':
            return
        else:
            donor_list = get_donor_list()
            if donor_name not in donor_list:
                donor_db.append((donor_name, []))
            donor_list = get_donor_list()
            idx = donor_list.index(donor_name)
            donations_list = donor_db[idx][1]

            donations_list.append(new_donation_amount)

            print(f'\nDear {donor_name}, \n\nIt is our greatest honor to thank you for your generous donation of ${"{:.2f}".format(new_donation_amount)}! We are grateful to call you one of our donors. \n\nWith warmest regards, \nThe Mailroom Team\n\n')


def new_donation():
    while True:
        try:
            donation = input('Donation Amount (Press enter to return to main menu): ')
            if donation == '':
                return ''
            donation = float(donation)
            return round(donation, 2)
        except ValueError:
            print('Invalid amount. Please try again')


def get_donor_name():
    while True:
        prompt = 'Donor Full Name (put `list` to see all donors or enter to return to main menu): '
        donor_name = input(prompt)
        if donor_name.strip() == 'list':
            print('-------------------------')
            print('{:^25}'.format('Donor List'))
            print('-------------------------')
            listy = get_donor_list()
            for i in listy:
                print(i)
            print('')
        elif donor_name.strip() == '':
            return ''
        else:
            return donor_name


def get_donor_list():
    donors = [donor[0] for donor in donor_db]
    return donors


def create_report():
    print('\nDonor Name                | Total Given | Num Gifts | Average Gift')
    print('-------------------------------------------------------------------')
    db = sorted(donor_db, key=sort_key, reverse=True)

    for donor, amount_list in db:
        sum_total = get_total_sum(amount_list)
        len_list = get_total_donations(amount_list)
        average_don = get_average_donations(sum_total, len_list)
        print('{:<25}'.format(donor), '| $', '{:>9.2f}'.format(sum_total), '|', str(len_list).center(9), '| $', '{:>10}'.format(str(average_don)))

    print('')

def sort_key(donor):
    return sum(donor[1])


def get_total_sum(listy):
    return sum(listy)


def get_total_donations(listy):
    return len(listy)


def get_average_donations(sum_total, len_list):
    return round(sum_total/len_list, 2)


def exit_program():
    print('Bye!')
    sys.exit()


def main():
    while True:
        option = menu()
        if option == 1:
            send_thank_you()
        elif option == 2:
            create_report()
        else:
            exit_program()


main()
