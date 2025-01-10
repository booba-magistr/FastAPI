class RBProduct:
    def __init__(self, product_id:int | None = None, 
                 product_name:str | None = None,
                 category_id:int | None = None):
        self.id = product_id
        self.name = product_name
        self.category_id = category_id

    def to_dict(self):  # Для формирования SELECT запросов
        data = {'id': self.id, 'name': self.name, 'category_id': self.category_id}
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data