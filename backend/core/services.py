import csv
import json


class SerializerFactory:
    def __init__(self,):
        self._creators = {}

    def get_serialize(self, format):
        creator = self._creators.get(format)
        if not creator:
            raise ValueError("")
        return creator()

    def register_formart(self, format, creator):
        self._creators[formart] = creator


class BaseParser:
    def __init__(self):
        pass

    def parse():
        pass


class JsonParserSerlize(BaseParser):
    pass


class CsvParser(BaseParser):
    pass


factory = SerializerFactory()
