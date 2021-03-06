from pages.base_page import Page
from pages.port_of_call import PortOfCall
from pages.top_navigation import TopNavigation
from pages.shore_excursions import ShoreExcursions


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.page = Page(self.driver)

        self.port_of_call_page = PortOfCall(self.driver)
        self.top_navigation = TopNavigation(self.driver)
        self.shore_excursions = ShoreExcursions(self.driver)