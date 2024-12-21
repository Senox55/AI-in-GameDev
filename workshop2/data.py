import gspread

gc = gspread.service_account(filename='white-watch-442306-a6-7c7198ce884e.json')
sh = gc.open("UnityWorkshop2")

coins = 150
zombies_counter = 0
coins_price = 20  # Цена за 12 патрон
bullets_per_zombie = 2  # Среднее кол-во пуль, чтобы убить одного зомби
bullets_per_purchase = 12  # количество пуль за одну покупку

for wave in range(1, 10):
    zombies_in_wave = wave * 10  # В каждой волне на 10 зомби больше, чем в предыдущей
    zombies_counter += zombies_in_wave
    coins_earned = zombies_in_wave * wave  # Каждый зомби приносит монеты, равные номеру волны

    coins += coins_earned

    if zombies_counter >= 75:  # Когда убито достаточно зомби для покупки пуль
        bullets_needed = zombies_counter * bullets_per_zombie
        purchases = bullets_needed // bullets_per_purchase

        # Рассчитываем, сколько пуль нужно
        total_cost = purchases * coins_price

        if coins >= total_cost:
            coins -= total_cost


    sh.sheet1.update(('A' + str(wave)), [[wave]])
    sh.sheet1.update(('B' + str(wave)), [[coins]])

    print(f"После волны {wave}: Монеты = {coins}, Убито зомби = {zombies_counter}")

