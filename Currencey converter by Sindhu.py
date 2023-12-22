import requests

def get_exchange_rate(base_currency, target_currency):
    # Replace with a reliable API endpoint for currency exchange rates
    api_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    
    try:
        response = requests.get(api_url)
        data = response.json()
        
        exchange_rate = data['rates'][target_currency]
        return exchange_rate
    except Exception as e:
        print(f"Error fetching exchange rates: {e}")
        return None

def convert_currency(amount, exchange_rate):
    converted_amount = amount * exchange_rate
    return converted_amount

if __name__ == "__main__":
    base_currency = input("Enter the base currency code (e.g., USD): ").upper()
    target_currency = input("Enter the target currency code (e.g., EUR): ").upper()

    amount = float(input("Enter the amount to convert: "))

    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate is not None:
        converted_amount = convert_currency(amount, exchange_rate)
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
