class Solution:
    def lemonadeChange(self, bills):
        register = {
            5: 0,
            10: 0
        }
        for bill in bills:
            if bill == 5:
                register[5] += 1
            elif bill == 10:
                register[10] += 1
                if register[5] == 0:
                    return False
                register[5] -= 1
            else:
                if register[10] > 0:
                    register[10] -= 1
                    if register[5] > 0:
                        register[5] -= 1
                    else:
                        return False
                else:
                    if register[5] > 2:
                        register[5] -= 3
                    else:
                        return False
        return True