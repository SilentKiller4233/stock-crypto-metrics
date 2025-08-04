import yfinance as yf
import requests

# ------------------ STOCK FUNCTIONS ------------------

def get_stock_info(ticker: str) -> dict:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        balance_sheet = stock.balance_sheet

        # Try primary values from .info
        equity = info.get("totalStockholderEquity")
        assets = info.get("totalAssets")
        liabilities = info.get("totalLiab")

        # Fallback for equity
        if not equity:
            possible_equity_keys = [
                "Total Stockholder Equity",
                "Common Stock Equity",
                "Total Equity Gross Minority Interest"
            ]
            for key in possible_equity_keys:
                if key in balance_sheet.index:
                    equity = balance_sheet.loc[key].sort_index(ascending=False).iloc[0]
                    break

        # Fallback for assets
        if not assets and "Total Assets" in balance_sheet.index:
            assets = balance_sheet.loc["Total Assets"].sort_index(ascending=False).iloc[0]

        # Fallback for liabilities
        if not liabilities:
            possible_liability_keys = [
                "Total Liab",
                "Total Liabilities Net Minority Interest",
                "Total Current Liabilities"
            ]
            for key in possible_liability_keys:
                if key in balance_sheet.index:
                    liabilities = balance_sheet.loc[key].sort_index(ascending=False).iloc[0]
                    print(f"DEBUG — Using fallback liabilities from '{key}': {liabilities}")
                    break

        return {
            "name": info.get("shortName"),
            "price": info.get("currentPrice"),
            "market_cap": info.get("marketCap"),
            "eps": info.get("trailingEps"),
            "pe_ratio": None,
            "dividend_yield": info.get("dividendYield"),
            "book_value": info.get("bookValue"),
            "net_income": info.get("netIncomeToCommon"),
            "shareholder_equity": equity,
            "total_liabilities": liabilities,
            "total_assets": assets,
            "ps_ratio": info.get("priceToSalesTrailing12Months")
        }

    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return {}

# ------------------ CRYPTO FUNCTIONS ------------------

def get_crypto_info(coin_id: str) -> dict:
    try:
        url = f"https://api.coingecko.com/api/v3/coins/{coin_id.lower()}"
        response = requests.get(url)
        data = response.json()
        market_data = data["market_data"]

        return {
            "name": data["name"],
            "symbol": data["symbol"],
            "price": market_data["current_price"]["usd"],
            "market_cap": market_data["market_cap"]["usd"],
            "volume": market_data["total_volume"]["usd"],
            "circulating_supply": market_data["circulating_supply"],
            "max_supply": market_data.get("max_supply"),
            "price_change_24h": market_data.get("price_change_percentage_24h")
        }
    except Exception as e:
        print(f"Error fetching crypto data: {e}")
        return {}

# ------------------ RATIO FUNCTIONS ------------------

def safe_divide(n, d):
    try:
        return n / d if n is not None and d not in [0, None] else None
    except:
        return None

def calculate_pe(price, eps):
    return safe_divide(price, eps)

def calculate_pb(price, book_value):
    return safe_divide(price, book_value)

def calculate_roe(net_income, equity):
    return safe_divide(net_income, equity)

def calculate_debt_to_equity(total_liab, equity):
    return safe_divide(total_liab, equity)

def calculate_roa(net_income, total_assets):
    return safe_divide(net_income, total_assets)

def calculate_token_value_per_supply(market_cap, supply):
    return safe_divide(market_cap, supply)

def calculate_token_inflation(circulating_supply, max_supply):
    return safe_divide(circulating_supply, max_supply)

def calculate_liquidity(volume, market_cap):
    return safe_divide(volume, market_cap)

# ------------------ UTILITY ------------------

def format_currency(value):
    return f"${value:,.2f}" if isinstance(value, (int, float)) else "N/A"
