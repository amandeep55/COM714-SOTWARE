from typing import List
from invoice import Invoice
from receipt import Receipt

class Household:

    def __init__(self, custodian:str, invoices:List[Invoice], receipts:List[Receipt]):
        self.__custodian = custodian
        self.__invoices = invoices
        self.__receipts = receipts

    def remove_invoice(self, position)-> None:
        self.__invoices.pop(position)

    def add_invoice(self, new_invoice: Invoice)-> None:
        self.__invoices.append(new_invoice)

    def get_invoices(self) ->List[Invoice]:
        return self.__invoices

    def get_receipts(self)->List[Receipt]:
        return self.__receipts

    def add_receipt(self, new_receipt:Receipt)->None:
        self.__receipts.append((new_receipt))

    def get_object_in_invoiceList(self, position)-> Invoice:
        return self.__invoices[position]

    def get_object_in_receiptsList(self, position)->Receipt:
        return self.__receipts[position]

    def get_custodian(self) ->str:
        return self.__custodian

    def set_custodian(self, new_custodian)->None:
        self.__custodian = new_custodian

    def get_specific_invoice(self, position:int)->None:
        print("Payment date: " + self.__invoices[position].get_payment_date())
        print("Total value: " + str(self.__invoices[position].get_total_value()))
        print("Amount paid: " + str(self.__invoices[position].get_amount_paid()))
        print("Amount remaining: " + str(self.__invoices[position].get_amount_remaining()))

    def create_invoice(self, payment_date:str, total_value:int, amount_paid:int)->Invoice:
        invoice = Invoice(payment_date, total_value, amount_paid)
        self.__invoices.append(invoice)
        return invoice

    def create_invoice_new(self)->Invoice:
        print("*** Creating Invoice ***")
        payment_date = input("What is the payment date?: ")
        total_value = int(input("What is the total value of the invoice?: "))
        amount_paid = int(input("How much is being paid straight away?: "))
        new_invoice = Invoice(payment_date, total_value, amount_paid)
        print("*** Invoice Created! ***")
        return new_invoice

    def create_receipt_new(self)-> Receipt:
        userContinue = input("Would you like to create a receipt? Enter 'y' or 'n': ")
        if userContinue =='y':
            print("*** Creating Receipt ***")
            payment_date = input("What is the payment date?: ")
            payment_amount = int(input("What is the payment amount?: "))
            new_receipt = Receipt(payment_date, payment_amount)
            print("*** Receipt Created! ***")
            return new_receipt
        else:
            return

    def add_receipt_and_invoice_new(self, receipt:Receipt, invoice:Invoice)->None:
        self.__invoices.append(invoice)
        self.__receipts.append(receipt)

    def create_receipt(self, payment_date:str, payment_amount:int):
        receipt = Receipt(payment_date, payment_amount)
        self.__receipts.append(receipt)
        return receipt

    def take_payment_generate_receipt(self, payment_date:str,amount_paid:int, invoice_position:int)->None:
        self.__invoices[invoice_position].add_amount_paid(amount_paid)
        self.__invoices[invoice_position].set_amount_remaining()
        receipt = Receipt(payment_date, amount_paid)
        self.__receipts.append(receipt)
        print("Receipt for " + "£" +str(amount_paid) + " for " + self.get_custodian() + " has been generated")

    def print_invoices(self)->None:
        for x in self.__invoices:
            print("***Printing invoices***")
            print("Payment date: " + x.get_payment_date())
            print("Total value: " +"£" + str(x.get_total_value()))
            print("Amount paid: " +"£" + str(x.get_amount_paid()))
            print("Amount remaining: " +"£" + str(x.get_amount_remaining()))

    def print_receipts(self)->None:
        for x in self.__receipts:
            print("***Printing receipts***")
            print("Payment date: " + x.get_payment_date())
            print("Payment amount: £" + str(x.get_payment_amount()))

    def get_invoices_value(self)->int:
        total_value = 0
        for x in self.__invoices:
            print(x.get_full_details())
            total_value = total_value + x.get_total_value()
        return total_value
















