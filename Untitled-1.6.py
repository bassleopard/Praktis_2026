def merge_orders(web_orders: list, app_orders: list) -> list:
    merged = []

    i = 0
    j = 0

    while i < len(web_orders) and j < len(app_orders):

        if web_orders[i]["created_at"] <= app_orders[j]["created_at"]:
            merged.append(web_orders[i])
            i += 1
        else:
            merged.append(app_orders[j])
            j += 1

    while i < len(web_orders):
        merged.append(web_orders[i])
        i += 1

    while j < len(app_orders):
        merged.append(app_orders[j])
        j += 1

    return merged


# Приклад використання
web_orders = [
    {"id": 1, "created_at": 1},
    {"id": 3, "created_at": 5},
    {"id": 5, "created_at": 9}
]

app_orders = [
    {"id": 2, "created_at": 2},
    {"id": 4, "created_at": 6},
    {"id": 6, "created_at": 10}
]

result = merge_orders(web_orders, app_orders)

print(result)