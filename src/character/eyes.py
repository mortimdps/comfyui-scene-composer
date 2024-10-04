from src.components import Component
from src.utils import stringify_tags


class Eyes(Component):
    def __init__(self, data):
        super().__init__(data)
    
    def get_eyes_covered(self):
        return self.data.random_data["eyes"]["eyes-covered"]
    
    def get_eye_color(self):
        suffix = "eyes"
        type = self.data.random_data["eyes"]["eyes-uncovered"]["type"]
        if "unicolor" in type:
            color = stringify_tags(self.data.random_data["eyes"]["unicolor-eyes"]["color"])
            return [
                f"{color} {suffix}"
            ]
        if "multicolor" in type:
            color_one = stringify_tags(self.data.random_data["eyes"]["multicolor-eyes"]["color-one"])
            color_two = stringify_tags(self.data.random_data["eyes"]["multicolor-eyes"]["color-two"])
            return [
                "heterochromia",
                f"{color_one} {suffix}",
                f"{color_two} {suffix}"
            ]
        return [""]
    
    def get_glowing_eyes(self):
        return self.data.random_data["eyes"]["eyes-uncovered"]["glowing"]
    
    def get_glasses(self):
        suffix = "glasses"
        if [""] == self.data.random_data["eyes"]["eyes-uncovered"]["glasses"]:
            return [""]
        type = stringify_tags(self.data.random_data["eyes"]["glasses"]["type"])
        round_eyewear = stringify_tags(self.data.random_data["eyes"]["glasses"]["round-eyewear"])
        colored_type = self.data.random_data["eyes"]["glasses"]["colored"]["type"]
        if "tinted" in colored_type:
            color = stringify_tags(self.data.random_data["eyes"]["glasses"]["colored"]["colors"])
            return [
                f"{type}{suffix}",
                f"{round_eyewear}",
                f"{color}-tinted eyewear"
            ]
        if "opaque" in colored_type:
            return [
                f"{type}{suffix}",
                f"{round_eyewear}",
                f"opaque {suffix}"
            ]
        return [
            f"{type}{suffix}",
            f"{round_eyewear}",
        ]
        

    def get_eyes_uncovered(self):
        return self.get_eye_color() + self.get_glowing_eyes() + self.get_glasses()

    def get_eyes(self):
        type = self.data.random_data["eyes"]["type"]
        if "eyes-covered" in type:
            return self.get_eyes_covered()
        if "eyes-uncovered" in type:
            return self.get_eyes_uncovered()
        return [""]

    def build_prompt(self):
        self.prompt = self.get_eyes()
