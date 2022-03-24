from seleniumwire.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

from lib.constants import env

class Driver:
  def __init__(self):
    self.driver         = None
    self.options        = None
    self.service        = None
    self.wire_options   = None

  def initialize(self):
    if self.options is None:
      self.set_options()
    
    if self.service is None:
      self.set_service()

    if self.wire_options is None:
      self.set_wire_options()

    self.driver = Chrome(
      options=self.options,
      seleniumwire_options=self.wire_options,
      service=self.service
    )

  def set_options(self, options=None):
    if options is None:
      options = Options()

      options.add_argument("user-agent={}".format(env.USER_AGENT))
      options.add_argument("--allow-running-insecure-content")
      options.add_argument("--disable-extensions")
      options.add_argument("--disable-gpu")
      options.add_argument("--disable-dev-shm-usage")
      options.add_argument("--headless")
      options.add_argument("--ignore-certificate-errors")
      options.add_argument("--no-sandbox")
      options.add_argument("--proxy-bypass-list=*")
      options.add_argument("--proxy-server='direct://'")
      options.add_argument("--window-size=1920,1080")

    self.options = options

  def set_service(self, service=None):
    if service is None:
      service = Service(env.EXEC_PATH)

    self.service = service

  def set_wire_options(self, options=None):
    if options is None:
      options = {
        "proxy": {
          "http": "",
          "https": "",
          "no_proxy": "http://localhost,http://127.0.0.1"
        }
      }

    self.wire_options = {}