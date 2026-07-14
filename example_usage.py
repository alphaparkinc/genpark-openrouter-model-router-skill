from client import OpenRouterModelRouterClient
client = OpenRouterModelRouterClient()
print(client.route("high", 0.10))