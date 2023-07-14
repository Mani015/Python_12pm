# def shopping_bill(promo=False):
#     items_prices = [10, 5, 20, 2, 8]
#     pct_off = 0
#
#     def half_off():
#         nonlocal pct_off
#         pct_off = .50
#
#     if promo:
#         half_off()
#
#     total = sum(items_prices) - (sum(items_prices) * pct_off)
#     print(total)
#
#
# shopping_bill(True)
# 22.5



def shopping_bill(promo=False):
    items_prices = [10, 5, 20, 2, 8]
    pct_off = 0

    def half_off():
        nonlocal pct_off
        pct_off = .50

    if promo:
        half_off()

    total = sum(items_prices) - (sum(items_prices) * pct_off)
    print(total)

shopping_bill()
# 45

