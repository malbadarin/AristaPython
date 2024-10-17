import pprint
import pyeapi
node = pyeapi.connect(transport="https", host="192.168.8.15", username="cvpadmin", password="cvpadmin123", port=None)
version = node.execute(["show version"])
pprint(version)