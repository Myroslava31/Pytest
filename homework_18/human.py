import json
import xml.etree.ElementTree as ET

class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        return json.dumps(self.__dict__)

    def convert_to_xml(self):
        human_element = ET.Element("human")
        name_element = ET.SubElement(human_element, "name")
        name_element.text = self.name
        age_element = ET.SubElement(human_element, "age")
        age_element.text = str(self.age)
        gender_element = ET.SubElement(human_element, "gender")
        gender_element.text = self.gender
        birth_year_element = ET.SubElement(human_element, "birth_year")
        birth_year_element.text = str(self.birth_year)
        return ET.tostring(human_element, encoding="unicode")

if __name__ == '__main__':
    human = Human('Vasyl', 32, 'male', 1991)
    print(human.convert_to_json())
    print(human.convert_to_xml())
