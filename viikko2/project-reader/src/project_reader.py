from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
#        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        kirjasto = toml.loads(content, _dict=dict)

        name = kirjasto['tool']['poetry']['name']
        description = kirjasto['tool']['poetry']['description']
        dependencies = kirjasto['tool']['poetry']['dependencies'].keys()
        devel_dependencies = kirjasto['tool']['poetry']['dev-dependencies']

        return Project(name, description, dependencies, devel_dependencies)