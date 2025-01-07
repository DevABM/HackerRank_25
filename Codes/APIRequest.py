import requests

def get_total_products(category, min_price, max_price):
    base_url = "https://jsonmock.hackerrank.com/api/inventory"
    total_count = 0
    page = 1

    while True:
        # Construct the API URL with the current page and category
        url = f"{base_url}?Category={category}&Page={page}"
        
        # Perform the GET request
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"API request failed with status code {response.status_code}")
        
        # Parse the JSON response
        data = response.json()
        products = data.get("data", [])
        total_pages = data.get("total_pages", 0)
        
        # Filter products by price range and count them
        for product in products:
            if min_price <= product["price"] <= max_price:
                total_count += 1
        
        # Break if we've processed all pages
        if page >= total_pages:
            break
        
        page += 1
    
    return total_count

# Example usage
category = "Accessories"
min_price = 10.0
max_price = 50.0
result = get_total_products(category, min_price, max_price)
print(f"Total products: {result}")
