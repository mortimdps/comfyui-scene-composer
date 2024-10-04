from src.components import Component
from src.utils import stringify_tags


class Body(Component):

    def __init__(self, data):
        super().__init__(data)

    def get_body_type(self):
        return self.data.random_data["body"]["body_type"]
    
    def get_chest(self):
        return self.data.random_data["body"]["chest"]
    
    def get_skin_color(self):
        suffix = "skin"
        color = stringify_tags(self.data.random_data["body"]["skin_color"])
        if color == "":
            return [""]
        return [f"{color} {suffix}"]

    def get_freckles(self):
        return self.data.random_data["body"]["freckles"]

    def get_tanlines(self):
        return self.data.random_data["body"]["tanlines"]
    
    def get_tattoo(self):
        tattoo_type = self.data.random_data["body"]["tattoo_type"]
        if tattoo_type == [""]:
            return tattoo_type
        tattoo_location = self.data.random_data["body"]["tattoo_location"]
        return tattoo_type + tattoo_location

    def get_skin(self):
        return self.get_skin_color() + self.get_freckles() + self.get_tanlines() + self.get_tattoo()

    def build_prompt(self):
        self.prompt = self.get_body_type() + self.get_skin() + self.get_chest()
