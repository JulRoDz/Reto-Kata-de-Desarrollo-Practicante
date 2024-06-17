def min_change(coins):
  for coin in coins:
    if not isinstance(coin, int) or coin <= 0:
      raise ValueError("La lista debe ser de valores positivos.")

  coins.sort()

  current_change = 0
  for coin in coins:
    if coin > current_change + 1:
      return current_change + 1
    current_change += coin
  return current_change + 1

try:
  coins_list = input("Ingrese una lista de monedas separadas por comas: ").split(',')
  coins_list = [int(coin.strip()) for coin in coins_list]


  result = min_change(coins_list.copy())
  print(result)
except ValueError as e:
  print("Error:", e)