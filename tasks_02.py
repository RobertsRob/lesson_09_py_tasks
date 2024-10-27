# 1.task
# Постройте график, который показывает изменения численности населения Латвии за последние 10 лет. 
years = np.array([2012, 2014, 2016, 2018, 2020, 2022])
population = np.array([1990400, 1973900, 1945200, 1920500, 1889000, 1856000])

years = np.array([2012, 2014, 2016, 2018, 2020, 2022])
population = np.array([1990400, 1973900, 1945200, 1920500, 1889000, 1856000])

plt.figure(figsize=(10, 6), facecolor="thistle")
plt.plot(years, population, marker="o", linestyle="-", color="blue", label="Население")
plt.title("Изменение численности населения Латвии", fontsize=16, fontweight="bold", color="darkviolet")
plt.xlabel("Годы", fontsize=12)
plt.ylabel("Численность населения", fontsize=12)
plt.grid(True, linestyle="--", color="gray", linewidth=0.8)
plt.legend(loc="best", fontsize=10)
plt.tight_layout()
plt.show()


# 2.task
# Создайте график, который иллюстрирует зависимость валового внутреннего продукта (ВВП) Латвии от уровня безработицы за последние 5 лет. 
years = np.array([2018, 2019, 2020, 2021, 2022])
gdp = np.array([34.5, 36.3, 32.0, 35.1, 37.8])  # В миллиардах евро
unemployment_rate = np.array([7.1, 6.5, 8.2, 7.5, 6.8])  # В процентах


years = np.array([2018, 2019, 2020, 2021, 2022])
gdp = np.array([34.5, 36.3, 32.0, 35.1, 37.8])
unemployment_rate = np.array([7.1, 6.5, 8.2, 7.5, 6.8])

fig, ax1 = plt.subplots(figsize=(10, 6), facecolor='lightcyan')
ax2 = ax1.twinx()

ax1.plot(years, gdp, marker='o', linestyle='-', color='green', label='ВВП (млрд евро)')
ax2.plot(years, unemployment_rate, marker='s', linestyle='--', color='orange', label='Уровень безработицы (%)')

ax1.set_title("ВВП и уровень безработицы в Латвии", fontsize=16, fontweight='bold', color='navy')
ax1.set_xlabel("Годы", fontsize=12)
ax1.set_ylabel("ВВП (млрд евро)", fontsize=12, color='green')
ax2.set_ylabel("Уровень безработицы (%)", fontsize=12, color='orange')

ax1.grid(True, linestyle='--', color='gray', linewidth=0.8)
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.show()

# 3.task
# Исследуйте зависимость первой космической скорости от массы космического тела. Постройте график, который показывает, как изменяется первая космическая скорость при разных значениях массы (например, планет).
mass = np.array([0.5, 1, 1.5, 2, 2.5])  # Масса в земных массах
velocity = np.sqrt(9.81 * (mass * 5.972e24) / (6371e3))  # Первая космическая скорость в м/с

mass = np.array([0.5, 1, 1.5, 2, 2.5])
velocity = np.sqrt(9.81 * (mass * 5.972e24) / (6371e3))

plt.figure(figsize=(10, 6), facecolor='lavender')
plt.plot(mass, velocity, marker='^', linestyle='-', color='purple', label='Первая космическая скорость')
plt.title("Зависимость первой космической скорости от массы", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Масса (в земных массах)", fontsize=12)
plt.ylabel("Первая космическая скорость (м/с)", fontsize=12)
plt.grid(True, linestyle=':', color='grey', linewidth=0.7)
plt.legend(loc='best', fontsize=10)
plt.tight_layout()
plt.show()


# 4.task
# Постройте график изменения температуры на поверхности планеты в зависимости от времени. Настройте фон графика и добавьте легенду для различных типов температур (дневная, ночная).
time = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])  # Время в часах
day_temp = np.array([15, 18, 20, 25, 30, 32, 30, 25, 20, 15, 10, 8, 5])  # Дневная температура
night_temp = np.array([5, 7, 9, 10, 12, 15, 16, 15, 13, 10, 8, 6, 4])  # Ночная температура

time = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])
day_temp = np.array([15, 18, 20, 25, 30, 32, 30, 25, 20, 15, 10, 8, 5])
night_temp = np.array([5, 7, 9, 10, 12, 15, 16, 15, 13, 10, 8, 6, 4])

plt.figure(figsize=(10, 6), facecolor='lightyellow')
plt.plot(time, day_temp, marker='o', linestyle='-', color='orange', label='Дневная температура')
plt.plot(time, night_temp, marker='s', linestyle='--', color='blue', label='Ночная температура')
plt.title("Изменение температуры в течение суток", fontsize=16, fontweight='bold', color='darkred')
plt.xlabel("Время (часы)", fontsize=12)
plt.ylabel("Температура (°C)", fontsize=12)
plt.grid(True, linestyle='-.', color='grey', linewidth=0.9)
plt.legend(loc='best', fontsize=10)
plt.tight_layout()
plt.show()


# 5.task

# 6.task
