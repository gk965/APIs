from importlib.machinery import SourceFileLoader
request = SourceFileLoader("requests", "users\garim\appdata\local\programs\python\python37\lib\site-packages")
response = request.get("https://randomuser.me/api/")
response.text