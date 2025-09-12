def main():
    cost_per_item = 19.99
    quantity = 5
    # Part 1/3 of the code
    subtotal_cost = cost_per_item * quantity
    tax = subtotal_cost * 0.13
    total_cost = cost_per_item * 5.65

    # Part 2/3 of the code
    print(f'cost_per_item = ${cost_per_item:0.2f}')
    print(f'quantity = {quantity}')
    print(f'subtotal_cost = ${subtotal_cost:0.2f}')
    print(f'tax = ${tax:0.2f}')
    print(f'total_cost = ${total_cost:0.2f}')


    # Part 3/3 of the code
    initial_investment = 1000
    interest_rate = 0.035
    investment = initial_investment
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    print('After 5 years, your investment will be worth ' + str(investment) + ' dollars.')
    # expected output: After 5 years, your investment will be worth 1187.6863056468749 dollars.
if __name__ == "__main__":
    main() 