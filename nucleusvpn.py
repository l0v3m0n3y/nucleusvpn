import requests
class Client():
	def __init__(self):
		self.api="https://api.nucleusvpn.com/api"
		self.api_2="https://napps-2.com/v1"
		self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
	def get_proxy_list(self):
		return requests.get(f"{self.api}/proxy",headers=self.headers).json()
	def get_my_ip(self):
		return requests.get(f"{self.api_2}/helpers/ips/insights",headers=self.headers).json()