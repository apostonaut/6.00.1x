def minimum_payment(balance, annualInterestRate, monthlyPaymentRate):
    """

    :param balance: Outstanding balance on credit card
    :type balance: float
    :param annualInterestRate: annual interest rate as a decimal
    :type annualInterestRate: float
    :param monthlyPaymentRate: minimum monthly payment rate as a decimal
    :type monthlyPaymentRate: float
    :return: remaining balance after one year
    :rtype: float
    >>> minimum_payment(42, 0.2, 0.04)
    31.38
    """

    #variable assignment
    currentBalance = balance
    monthlyInterestRate = annualInterestRate/12


    month = 1
    while month <= 12:
        #charge monthly interest rate at beginning of month
        currentBalance = currentBalance + currentBalance*monthlyInterestRate

        #make minimum payment
        monthlyPayment = monthlyPaymentRate * currentBalance
        currentBalance -= monthlyPayment
        month += 1

    currentBalance = round(currentBalance, 2)
    print(currentBalance)


if __name__ == "__main__":
    import doctest
    doctest.testmod()


#
#     # Test Case 1:
#     balance = 42
#     annualInterestRate = 0.2
#     monthlyPaymentRate = 0.04
#
#     # Result Your Code Should Generate Below:
#     Remaining balance: 31.38
#
#     # To make sure you are doing calculation correctly, this is the
#     # remaining balance you should be getting at each month for this example
# Month; 1; Remaining; balance: 40.99;
# Month; 2; Remaining; balance: 40.01
# Month; 3; Remaining; balance: 39.05
# Month; 4; Remaining; balance: 38.11
# Month; 5; Remaining; balance: 37.2
# Month; 6; Remaining; balance: 36.3
# Month; 7; Remaining; balance: 35.43
# Month; 8; Remaining; balance: 34.58
# Month; 9; Remaining; balance: 33.75
# Month; 10; Remaining; balance: 32.94
# Month; 11; Remaining; balance: 32.15
# Month; 12; Remaining; balance: 31.38