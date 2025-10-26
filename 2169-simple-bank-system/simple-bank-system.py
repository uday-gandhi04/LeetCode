class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.balance=[0]
        self.balance.extend(balance)
        self.n=len(balance)

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if account1<1 or account1>self.n or account2<1 or account2>self.n:
            return False
        if self.balance[account1]<money:
            return False
        
        self.balance[account1]-=money
        self.balance[account2]+=money

        return True     

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account<1 or account>self.n:
            return False
        
        self.balance[account]+=money
        return True

        

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account<1 or account>self.n or self.balance[account]<money:
            return False
        
        self.balance[account]-=money
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)