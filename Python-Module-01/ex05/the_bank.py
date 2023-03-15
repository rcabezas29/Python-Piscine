import random

class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount
        
class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def add(self, new_account: Account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        if type(new_account) != Account or new_account in self.accounts:
            return False
        else:
            self.accounts.append(new_account)
            return True
        
    def transfer(self, origin, dest, amount):
        """ Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        for account in self.accounts:
            if account.__dict__['name'] == origin or account.__dict__['name'] == dest:
                for atr in account.__dict__:
                    if (atr.startswith('b')):
                        return False
                if not hasattr(account, 'zip') or not hasattr(account, 'addr'):
                    return False
                if 'name' not in account.__dict__ or 'id' not in account.__dict__ or 'value' not in account.__dict__:
                    return False
                if type(account.__dict__['name']) != str:
                    return False
                if type(account.__dict__['id']) != int:
                    return False
            if account.__dict__['name'] == origin:
                if account.__dict__['value'] < amount:
                    return False
        
        for account in self.accounts:
            if account.__dict__['name'] == origin:
                account.__dict__['value'] -= amount
            elif account.__dict__['name'] == dest:
                account.__dict__['value'] += amount
        
    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        for account in self.accounts:
            if hasattr(account, "name") and type(name) == str and account.name == name:
                for atr in account.__dict__:
                    if (atr.startswith('b')):
                        atr = atr[1:]
                        return True
                if not hasattr(account, 'zip'):
                    account.zip = f'{random.randint(100, 999)}-{random.randint(100, 999)}'
                    return True
                if not hasattr(account, 'addr'):
                    account.addr = 'Madrid'
                    return True
        return False
