
class ProxyDict():

    """wrapper for dictionary"""

    def __init__(self, user_data=None):
        if user_data is None:
            user_data = {}
        self.user_data = user_data
        self._user_data_len = len(user_data)
        self._user_data_items = user_data.items()
        self._user_data_values = user_data.values()

    def __repr__(self):
        return f"ProxyDict({self.user_data})"

    def __getitem__(self, key):
        return self.user_data[key]

    def __len__(self):
        return self._user_data_len

    def __iter__(self):
        for item in self.user_data.keys():
            yield item

    def __eq__(self, other):
        if self.user_data == other:
            return True
        return False

    def items(self):
        return self._user_data_items

    def values(self):
        return self._user_data_values

    def get(self, key, replace=None):
        try:
            return self.user_data[key]
        except:
            return replace

    def keys(self):
        return self.user_data.keys()



user_data = {'name': 'Trey Hunner', 'active': False}

p1 = ProxyDict(user_data)
p2 = ProxyDict(user_data.copy())

print(p2 == uata)

