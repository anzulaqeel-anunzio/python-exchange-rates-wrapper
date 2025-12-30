# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import requests

class ExchangeRatesClient:
    BASE_URL = "https://v6.exchangerate-api.com/v6"

    def __init__(self, api_key: str):
        """
        Initialize the Exchange Rates client.
        :param api_key: Your API Key.
        """
        if not api_key:
            raise ValueError("API Key is required.")
        self.api_key = api_key

    def _make_request(self, endpoint: str):
        url = f"{self.BASE_URL}/{self.api_key}/{endpoint}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_latest_rates(self, base: str = "USD"):
        """Get latest rates for a base currency."""
        return self._make_request(f"latest/{base}")

    def convert(self, from_currency: str, to_currency: str, amount: float):
        """Convert amount between currencies."""
        data = self._make_request(f"pair/{from_currency}/{to_currency}/{amount}")
        return data.get("conversion_result")

    def get_codes(self):
        """Get supported codes."""
        return self._make_request("codes")

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
