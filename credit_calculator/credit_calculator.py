import argparse
import math


class CreditCalculator:
    """Credit Calculator"""

    def __init__(self, type, principal, periods, interest, payment):
        self.type = type
        self.principal = principal
        self.periods = periods
        self.interest = interest
        self.payment = payment
        self.i = self.interest / (12 * 100)

    def check_input(self):
        """Check input"""

        value_list = [self.principal, self.periods, self.interest, self.payment]
        unknown_value_list = []
        for i in value_list:
            if i == None:
                unknown_value_list.append(i)
            if len(unknown_value_list) > 1:
                print("Incorrect parameters")
                exit()
        self.operation_type()

    def operation_type(self):
        """Operation type"""

        match self.type:
            case "diff":
                self.diff()
            case "annuity":
                self.annuity()

    def annuity(self):
        """Annuity"""

        if self.payment is None:
            x = (1 + self.i) ** self.periods
            self.payment = math.ceil(self.principal * (self.i * x) / (x - 1))
            overpayment = self.periods * self.payment - self.principal
            print(f"Your annuity payment: {self.payment}\nOverpayment: {overpayment}")
        elif self.periods is None:
            x = self.payment / (self.payment - self.i * self.principal)
            self.periods = math.ceil(math.log(x, 1 + self.i))
            years = self.periods // 12
            months = self.periods % 12
            overpayment = self.periods * self.payment - self.principal
            if years == 0:
                print(f"It will take {months} months to repay this loan!")
            elif months == 0:
                print(f"It will take {years} years to repay this loan!")
            else:
                print(f"It will take {years} years and {months} months to repay this loan!")
            print(f"Overpayment: {overpayment}")
        elif self.principal is None:
            x = (1 + self.i) ** self.periods
            self.principal = math.floor(self.payment * (x - 1) / (self.i * x))
            overpayment = self.periods * self.payment - self.principal
            print(f"Your loan principal: {self.principal}\nOverpayment: {overpayment}")

    def diff(self):
        """Diff"""

        """Differentiated payment calculation"""
        total_payment = 0

        for month in range(1, self.periods + 1):
            payment = self.principal / self.periods + self.interest / 1200 * (
                    self.principal - (self.principal * (month - 1)) / self.periods)
            total_payment += payment
            print(f"Month {month}: payment is {round(payment)}")

        overpayment = total_payment - self.principal
        print(f"Overpayment = {round(overpayment)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Credit calculator")

    parser.add_argument("-t", "--type", type=str, choices=["annuity", "diff"])
    parser.add_argument("-prin", "--principal", type=float)
    parser.add_argument("-per", "--periods", type=int)
    parser.add_argument("-i", "--interest", type=float)
    parser.add_argument("-pay", "--payment", type=float)

    args = parser.parse_args()

    start = CreditCalculator(args.type, args.principal, args.periods, args.interest, args.payment)
    start.check_input()
