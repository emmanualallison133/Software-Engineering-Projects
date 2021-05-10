class Invoice:

    def __init__(self):
        self.items = {}

    def addProduct(self, qnt, price, discount):
        self.items["qnt"] = qnt
        self.items["unit_price"] = price
        self.items["discount"] = discount
        return self.items

    def totalImpurePrice(self, products):
        total_impure_price = 0
        for k, v in products.items():
            total_impure_price += float(v['unit_price']) * int(v["qnt"])
        total_impure_price = round(total_impure_price, 2)
        return total_impure_price

    def totalDiscount(self, products):
        total_discount = 0
        for k, v in products.items():
            total_discount += int(v["qnt"])* float(v['unit_price']) * float(v["discount"]) / 100
        total_discount = round(total_discount,2)
        self.total_discount = total_discount
        return total_discount

    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products)
        return total_pure_price

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ["y", "n"]:
                return userInput
            print("y or n! Try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again.")
                continue
            else:
                return userInput

    #Calculates the total number of items in the invoice
    def totalNumOfItems(self, products):
        numOfItems = 0  #Holds the total number of items in the invoice

        #Loops through the items in the products
        for k, v in products.items():
            numOfItems += int(v["qnt"]) #Accumulates the quantity of each items in the "numOfItems" variable
        self.numOfItems = numOfItems
        return numOfItems   #Returns the numOfItems variable

    #Calculates the percentage saved on the total invoice when discounts are applied
    def percentSavedOnTotal(self, products):
        percentSaved = 0    #Holds the percent of money saved
        percentSaved = self.totalPurePrice(products) / self.totalImpurePrice(products) * 100    #Calculates the percentage of the pure price is to the impure price
        percentSaved = 100 - percentSaved   #Difference is the percent saved
        percentSaved = round(percentSaved, 2)   #Rounds the percentSaved to two decimal places
        return percentSaved     #Returns the "percentSaved" variable