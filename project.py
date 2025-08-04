from helpers import *
from tabulate import tabulate

def main():
    print("\n🎯 Welcome to Finlytics CLI!")
    while True:
        print("\nMain Menu:")
        print("[1] Stock")
        print("[2] Crypto")
        print("[3] Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_stock_flow()
        elif choice == "2":
            show_crypto_flow()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid input.")

def show_stock_flow():
    ticker = input("Enter stock ticker (e.g., AAPL): ").strip().upper()
    data = get_stock_info(ticker)

    if not data or not data.get("price"):
        print("❌ Could not retrieve stock data.")
        return

    print("\n📈 Stock Information:")
    table = [
        ["Name", data["name"]],
        ["Price", format_currency(data["price"])],
        ["Market Cap", format_currency(data["market_cap"])],
        ["EPS", format_currency(data["eps"])],
        ["Dividend Yield", f"{data['dividend_yield']*100:.2f}%" if data['dividend_yield'] else "N/A"],
        ["Book Value", format_currency(data["book_value"])],
        ["Net Income", format_currency(data["net_income"])],
        ["Equity", format_currency(data["shareholder_equity"])],
    ]
    print(tabulate(table, tablefmt="fancy_grid"))

    after_data_menu("stock", data)

def show_crypto_flow():
    coin = input("Enter crypto name (e.g., bitcoin): ").strip().lower()
    data = get_crypto_info(coin)

    if not data or not data.get("price"):
        print("❌ Could not retrieve crypto data.")
        return

    print("\n💸 Crypto Information:")
    table = [
        ["Name", data["name"]],
        ["Symbol", data["symbol"].upper()],
        ["Price", format_currency(data["price"])],
        ["Market Cap", format_currency(data["market_cap"])],
        ["Volume", format_currency(data["volume"])],
        ["Circulating Supply", f"{data['circulating_supply']:,.0f}"],
        ["Max Supply", f"{data['max_supply']:,.0f}" if data['max_supply'] else "N/A"],
    ]
    print(tabulate(table, tablefmt="fancy_grid"))

    after_data_menu("crypto", data)

def after_data_menu(asset_type, info):
    while True:
        print("\n[1] Calculate Ratios\n[2] Search Another\n[3] Exit")
        next_step = input("Choose an option: ").strip()
        if next_step == "1":
            if asset_type == "stock":
                display_ratios_stock(info)
            else:
                display_ratios_crypto(info)
        elif next_step == "2":
            return
        elif next_step == "3":
            print("👋 Goodbye!")
            exit()
        else:
            print("❌ Invalid input.")

def display_ratios_stock(data):
    pe = calculate_pe(data["price"], data["eps"])
    pb = calculate_pb(data["price"], data["book_value"])
    roe = calculate_roe(data["net_income"], data["shareholder_equity"])
    de = calculate_debt_to_equity(data["total_liabilities"], data["shareholder_equity"])
    roa = calculate_roa(data["net_income"], data["total_assets"])
    ps = data.get("ps_ratio")

    print("\n📊 Financial Ratios (Stock):")
    table = [
        ["P/E Ratio", f"{pe:.2f}" if pe else "N/A"],
        ["P/B Ratio", f"{pb:.2f}" if pb else "N/A"],
        ["ROE", f"{roe*100:.2f}%" if roe else "N/A"],
        ["D/E Ratio", f"{de:.2f}" if de else "N/A"],
        ["ROA", f"{roa*100:.2f}%" if roa else "N/A"],
        ["P/S Ratio", f"{ps:.2f}" if ps else "N/A"],
    ]
    print(tabulate(table, tablefmt="fancy_grid"))


def display_ratios_crypto(data):
    token_value = calculate_token_value_per_supply(data["market_cap"], data["circulating_supply"])
    inflation = calculate_token_inflation(data["circulating_supply"], data["max_supply"])
    liquidity = calculate_liquidity(data["volume"], data["market_cap"])
    volatility_24h = data.get("price_change_24h")

    print("\n📊 Financial Ratios (Crypto):")
    table = [
        ["Market Cap / Circulating Supply", f"{token_value:.2f}" if token_value else "N/A"],
        ["Inflation (Current Supply / Max)", f"{inflation*100:.2f}%" if inflation else "N/A"],
        ["Liquidity Ratio", f"{liquidity:.4f}" if liquidity else "N/A"],
        ["24h Volatility", f"{volatility_24h:.2f}%" if volatility_24h else "N/A"],
    ]
    print(tabulate(table, tablefmt="fancy_grid"))


if __name__ == "__main__":
    main()
