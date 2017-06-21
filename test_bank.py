import unittest 
from bank import BankAccount, SavingsAccount, CurrentAccount

class TestSaving(unittest.TestCase):
    """ Tests SavingsAccount Class  """

    #create global variables
    def setUp(self):
        self.savings_account = SavingsAccount()
    
    #test the account is a child of the bank account class
    def test_create_savings_account(self):
        self.assertTrue(self.savings_account, BankAccount)
    
    #test add person
    def test_add_person(self):
        self.assertEqual(self.savings_account.add_person("Adams Kariuki"), "Person Successfully Added")
    
    #test add invalid person
    def test add_invalid_person(self):
        error = "Invalid Account Name"
        self.assertEqual(self.savings_account.add_person(""), error)
        self.assertEqual(self.savings_account.add_person("A@@ "), error)
        self.assertEqual(self.savings_account.add_person(68768), error)

    #test successful deposit    
    def test_savings_deposit(self):
        self.savings_account.deposit(5000)
        self.assertEqual(self.savings_account.balance, 5000)
    
    #test invalid deposit amounts
    def test_saving_deposit_invalid(self):
        deposit_error_message = "Invalid Deposit amount"
        self.assertEqual(self.savings_account.deposit(-100), deposit_error_message)
        self.assertEqual(self.savings_account.deposit('ak122'), deposit_error_message)
        self.assertEqual(self.savings_account.deposit(0), deposit_error_message)
        self.assertEqual(self.savings_account.balance, 0)
    
    #test successful withdraw
    def test_savings_withdraw(self):
        self.savings_account.deposit(5000)
        self.savings_account.withdraw(3000)
        self.assertEqual(self.savings_account.balance, 2000)
    
    #test invalid withdraw amounts
    def test_savings_withdraw_invalid(self):
        withdraw_error_message = "Invalid Withdraw Amount"
        self.assertEqual(self.savings_account.withdraw('lk2000'), withdraw_error_message)
        self.assertEqual(self.savings_account.withdraw(0), withdraw_error_message)
        self.assertEqual(self.savings_account.withdraw(-100), withdraw_error_message)
        self.assertEqual(self.savings_account.balance, 0)
    
    #test account overdrafts
    def test_savings_overdraft(self):
        self.savings_account.withdraw(9000) 
        self.assertGreaterEqual(self.savings_account.balance, -3000, msg='Overdraft Exceeded. Overdraft Limit is 3000 KES') 


class TestCurrent(unittest.TestCase):
    """ Tests CurrentAccount Class  """

    #create global variables
    def setUp(self):
        self.current_account = CurrentAccount()

    #test the account is a child of the bank account class
    def test_create_current_account(self):
        self.assertTrue(self.current_account, BankAccount)
    
    #test add person
    def test_add_person(self):
        self.assertEqual(self.current_account.add_person("Akash Barga"), "Person Successfully Added")

    #test add invalid person
    def test add_invalid_person(self):
        error = "Invalid Account Name"
        self.assertEqual(self.current_account.add_person(""), error)
        self.assertEqual(self.current_account.add_person("A@@ 423423"), error)
        self.assertEqual(self.current_account.add_person(68768), error)
        
    #test successful deposit 
    def test_current_deposit(self):
        self.current_account.deposit(5000)
        self.assertEqual(self.current_account.balance, 6000)
    
    #test invalid deposit amounts
    def test_current_deposit_invalid(self):
        deposit_error_message = "Invalid Deposit amount"
        self.assertEqual(self.current_account.deposit(-100), deposit_error_message)
        self.assertEqual(self.current_account.deposit('ak122'), deposit_error_message)
        self.assertEqual(self.current_account.deposit(0), deposit_error_message)
        self.assertEqual(self.current_account.balance, 1000)
        
    #test successful withdraw
    def test_current_withdraw(self):
        self.current_account.deposit(5000)
        self.current_account.withdraw(3000)
        self.assertEqual(self.current_account.balance, 3000)
    
    #test invalid withdraw amounts
    def test_current_withdraw_invalid(self):
        withdraw_error_message = "Invalid Withdraw Amount"
        self.assertEqual(self.current_account.withdraw('lk2000'), withdraw_error_message)
        self.assertEqual(self.current_account.withdraw(0), withdraw_error_message)
        self.assertEqual(self.current_account.withdraw(-100), withdraw_error_message)
        self.assertEqual(self.current_account.balance, 1000)
    
    #test account overdrafts
    def test_current_overdraft(self):
        self.current_account.withdraw(7000)
        self.assertGreaterEqual(self.current_account.balance, 1000, msg="Overdrafts are not allowed")