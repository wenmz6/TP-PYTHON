price = 85
discount = 20
reduction_amount = price * discount / 100
print(
    "Le prix de départ est de %d€, la réduction de %d%% et le prix final est de %d€ "
    % (price, discount, price - reduction_amount)
)
print(
    f"Le prix de départ est de {price}€, la réduction de {discount}% et le prix final est de {int(price-reduction_amount)}€"
)
