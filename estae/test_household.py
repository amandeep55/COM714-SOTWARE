import unittest
from invoice import Invoice
from receipt import Receipt
from household import Household

class TestHousehold(unittest.TestCase):

    def test_remove_invoice(self):
        test_invoice = Invoice("1st December 2021", 1000, 0)
        test_receipt = Receipt("1st May 2021", 500)
        Tester = Household("Alex", [test_invoice], [test_receipt])
        Tester.remove_invoice(0)
        self.assertEqual(len(Tester.get_invoices()), 0, "Should be 0")

    def test_add_invoice(self):
        test_invoice = Invoice("1st December 2021", 1000, 0)
        test_receipt = Receipt("1st May 2021", 500)
        Tester = Household("Alex", [test_invoice], [test_receipt])
        test_invoice2 = Invoice("1st Jan 2021", 900, 50)
        Tester.add_invoice(test_invoice2)
        self.assertEqual(len(Tester.get_invoices()), 2, "Should be 2")

    def test_add_receipt(self):
        test_invoice = Invoice("1st December 2021", 1000, 0)
        test_receipt = Receipt("1st May 2021", 500)
        Tester = Household("Alex", [test_invoice], [test_receipt])
        test_receipt2 = Receipt("1st December 2020", 400)
        Tester.add_receipt(test_receipt2)
        self.assertEqual(len(Tester.get_receipts()), 2, "Should be 2")

    def test_get_object_in_invoiceList(self):
        test_invoice = Invoice("1st December 2021", 1000, 0)
        test_receipt = Receipt("1st May 2021", 500)
        Tester = Household("Alex", [test_invoice], [test_receipt])
        self.assertEqual(Tester.get_object_in_invoiceList(0), test_invoice, "Incorrect object returned")

    def test_get_object_in_receiptsList(self):
        test_invoice = Invoice("1st December 2021", 1000, 0)
        test_receipt = Receipt("1st May 2021", 500)
        Tester = Household("Alex", [test_invoice], [test_receipt])
        self.assertEqual(Tester.get_object_in_receiptsList(0), test_receipt, "Incorrect object returned")

    def test_create_invoice(self):
        test_invoice = Invoice("1st December 2021", 1000, 0)
        test_receipt = Receipt("1st May 2021", 500)
        Tester = Household("Alex", [test_invoice], [test_receipt])
        Tester.create_invoice("1st March", 2000, 0)
        self.assertEqual(len(Tester.get_invoices()), 2, "Should be 2")

    def test_crete_receipt(self):
        test_invoice = Invoice("1st December 2021", 1000, 0)
        test_receipt = Receipt("1st May 2021", 500)
        Tester = Household("Alex", [test_invoice], [test_receipt])
        Tester.create_receipt("1st May 2020", 500)
        self.assertEqual(len(Tester.get_receipts()), 2, "Should be 2")

    def test_get_invoices_value(self):
        test_invoice = Invoice("1st December 2021", 1000, 0)
        test_receipt = Receipt("1st May 2021", 500)
        Tester = Household("Alex", [test_invoice], [test_receipt])
        self.assertEqual(Tester.get_invoices_value(), 1000, "Incorrect value returned")



if __name__ == '__main__':
    unittest.main()

