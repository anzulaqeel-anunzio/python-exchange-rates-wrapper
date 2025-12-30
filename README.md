# Exchange Rates API Wrapper (Python)

A simple Python wrapper for fetching exchange rates.

## Features

-   **Latest Rates**: Get the latest exchange rates for a base currency.
-   **Currency Conversion**: Convert amounts between currencies.
-   **Supported Symbols**: Fetch list of supported currency symbols.

## Installation

1.  **Clone the repository**
2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Install Package**
    ```bash
    pip install .
    ```

## Usage

```python
import os
from exchange_rates import ExchangeRatesClient
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("EXCHANGE_RATES_API_KEY")

client = ExchangeRatesClient(api_key=api_key)

# Get latest rates for USD
result = client.get_latest_rates(base="USD")
print(f"1 USD = {result['rates']['EUR']} EUR")

# Convert currency
amount = client.convert(from_currency="USD", to_currency="GBP", amount=100)
print(f"100 USD = {amount} GBP")
```

## Configuration

Obtain an API Key from [exchangerate-api.com](https://www.exchangerate-api.com/) (or similar compatible service).

## Contact

Developed for Anunzio International by Anzul Aqeel.
Contact +971545822608 or +971585515742.

## License

MIT


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
