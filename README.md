# stock-crypto-metrics

`stock-crypto-metrics` is a Python-based command-line application that allows users to analyze real-time financial data for both stocks and cryptocurrencies. It fetches live market data and calculates essential financial ratios such as P/E, P/B, ROE, ROA, D/E for stocks, and supply-based metrics for crypto. This project was developed as the final submission for Harvard's CS50P course.

---

## Features

- CLI-based interface with intuitive prompts
- Live data fetching via yfinance (stocks) and CoinGecko API (crypto)
- Analyze both traditional stocks and cryptocurrencies
- Displays key financial data:
  - Name, price, market cap, EPS, volume, etc.
- Calculates common financial ratios:
  - **Stocks**: P/E, P/B, ROE, ROA, D/E, P/S
  - **Crypto**: Market Cap per Token, Inflation Rate, Liquidity Ratio, 24h Volatility
- Clean, tabulated CLI output using `tabulate`
- Input validation and graceful handling of missing data
- Modular and scalable codebase (organized into `project.py` and `helpers.py`)

---

## Technologies Used

- Python 3
- `yfinance` (stock data)
- `requests` (API calls)
- `tabulate` (CLI table formatting)
- CoinGecko API (crypto data)

---

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/SilentKiller4233/stock-crypto-metrics.git
   cd stock-crypto-metrics
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # For Windows
   # or
   source .venv/bin/activate  # For macOS/Linux
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**

   ```bash
   python project.py
   ```

---

## Usage

- Upon running, choose from:
  - `[1] Stock` to enter a stock ticker (e.g., `AAPL`, `MSFT`)
  - `[2] Crypto` to enter a crypto name (e.g., `bitcoin`, `ethereum`)
  - `[3] Exit` to quit the program

- After entering a valid asset:
  - View raw data in a clean table
  - Choose to calculate financial ratios or search another asset
  - Navigate using menu options `[1]`, `[2]`, or `[3]`

- All ratios are calculated using live data.
- Missing or unavailable metrics are shown as `"N/A"`.

---

## Project Structure

```
stock-crypto-metrics/
├── project.py         # Main CLI application and user interface
├── helpers.py         # Functions for data fetching and financial calculations
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

### File Descriptions

#### project.py

The main entry point for the CLI. Handles:

- CLI flow and user prompts
- Routing between stock and crypto flows
- Tabular display of raw financial data
- User navigation and control flow
- Calls functions from `helpers.py`

---

#### helpers.py

Handles all external API communication and financial logic:

- `get_stock_info()` – Pulls stock info from yfinance and fallback balance sheet data
- `get_crypto_info()` – Pulls crypto info from CoinGecko
- Financial ratio calculators:
  - `calculate_pe`, `calculate_pb`, `calculate_roe`, `calculate_debt_to_equity`, `calculate_roa`
  - `calculate_token_inflation`, `calculate_liquidity`, etc.
- `format_currency()` – Consistent output formatting
- `safe_divide()` function for clean math

---

## Made for Final Project of CS50P