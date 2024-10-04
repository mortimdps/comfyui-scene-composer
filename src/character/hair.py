from src.components import Component
from src.utils import stringify_tags

class Hair(Component):
    def __init__(self, data):
        super().__init__(data)

    def get_unicolor_hair(self):
        suffix = "hair"
        type = self.data.random_data["hair"]["hair_color_uniform"]
        if "hair-color-standard" in type:
            color = stringify_tags(self.data.random_data["hair"]["hair-color-standard"])
        else:
            color = stringify_tags(self.data.random_data["hair"]["hair-color-special"])
        return [
            f"{color} {suffix}"
        ]
    
    def get_multicolor_hair(self):
        suffix = "hair"
        type = stringify_tags(self.data.random_data["hair"]["hair-multicolor"])
        colored_tips = stringify_tags(self.data.random_data["hair"]["colored-tips"])
        color_one = stringify_tags(self.data.random_data["hair"]["hair-color-multicolor-colors"]["hair-one"])
        color_two = stringify_tags(self.data.random_data["hair"]["hair-color-multicolor-colors"]["hair-two"])
        return [
            f"{type} {suffix}",
            colored_tips,
            f"{color_one} {suffix}",
            f"{color_two} {suffix}"
        ]
    
    def get_hair_color(self):
        uni_or_multi = self.data.random_data["hair"]["unicolor_or_multicolor"]
        if "hair-unicolor" in uni_or_multi:
            return self.get_unicolor_hair()
        else:
            return self.get_multicolor_hair()

    def get_hair_length(self):
        suffix = "hair"
        length = stringify_tags(self.data.random_data["hair"]["length"])
        return [
            f"{length} {suffix}"
        ]

    def get_hair_style(self):
        suffix = "hair"
        style = stringify_tags(self.data.random_data["hair"]["style"])
        braid = stringify_tags(self.data.random_data["hair"]["braid"])
        if style == "":
            return [braid]
        return [
            f"{style} {suffix}",
            braid
        ]
        
    def get_hair_decoration(self):
        decoration = stringify_tags(self.data.random_data["hair"]["decoration"])
        decoration_color = stringify_tags(self.data.random_data["hair"]["decoration-color"])
        if "hair flower" == decoration:
            return [
                decoration,
                f"{decoration_color} flower"
            ]
        if "hair ribbon" == decoration:
            return [
                decoration,
                f"{decoration_color} ribbon"
            ]
        return [""]

    def build_prompt(self):
        self.prompt = self.get_hair_color() + self.get_hair_length() + self.get_hair_style() + self.get_hair_decoration()
