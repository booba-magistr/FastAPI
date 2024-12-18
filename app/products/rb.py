class RBProduct:
    def __init__(self, product_id:int | None = None, 
                 product_name:str | None = None):
        self.id = product_id
        self.name = product_name

    def to_dict(self):
        data = {'id': self.id, 'name': self.name}
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data