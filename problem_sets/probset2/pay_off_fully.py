def pay_off_fully(balance, annualInterestRate):
    """
    Calculates the minimum monthly payment required in order to pay off the balance of a credit card
    within one year

    :param balance: Outstanding balance on credit card
    :type balance: float
    :param annualInterestRate: annual interest rate as a decimal
    :type annualInterestRate: float
    :param monthlyPaymentRate: minimum monthly payment rate as a decimal
    :type monthlyPaymentRate: float
    :return: monthly payment required to pay off balance within one year, as a multiple of $10
    :rtype: int
    >>> pay_off_fully(3329, 0.2)
    310
    """

    #variable assignment
    currentBalance = balance
    monthlyInterestRate = annualInterestRate/12

