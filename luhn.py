def checksum_is_valid(card_number):
    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    result = ( (sum % 10) == 0 )
    if result == True: 
        print card_number + ' is legit'
        return True

def check_cards(first_four, last_four):
    num_of_valid_cards = 0
    middle_digits = open('middle_digit_list', 'r')
    for i in middle_digits:
	full_card = combine(first_four, i, last_four)
        result = checksum_is_valid(full_card)
        if result == True:
            num_of_valid_cards += 1
    print num_of_valid_cards + ' valid card numbers'

def combine(first_four, middle_eight, last_four):
    middle = middle_eight.rstrip('\n')
    return (first_four+middle+last_four)



checksum_is_valid('real number')

#test numbers
check_cards('6011', '3001')
#check_cards('4147', '6642')

