from src.generators.user_localization import UserLocalization


class User:

    def __init__(self):
        self.result = {}
        self.reset()

    def set_status(self, status="Active"):
        self.result['account_status'] = status
        return self

    def set_balance(self, balance=0):
        self.result['balance'] = balance
        return self

    def set_avatar(self, avatar="https://google.com/"):
        self.result['avatar'] = avatar
        return self

    def reset(self):
        self.set_status()
        self.set_balance()
        self.set_avatar()
        self.result["localization"] = {
                "en": UserLocalization('en_US').build(),
                "ru": UserLocalization('ru_RU').build()
            }
        return self

    def build(self):
        return self.result


# a = User().build()
# b = User().set_balance(20).set_status('asdf').build()
# print(a)
# print(b)
"""
{
    'account_status': 'Active', 
    'balance': 0, 
    'avatar': 'https://google.com/', 
    'localization': {
        'en': {'nickname': 'Sarah'}, 
        'ru': {'nickname': 'Алексей'}
    }
}
"""

