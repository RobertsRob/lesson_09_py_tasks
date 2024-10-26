# 1.task
# Постройте график гиперболы y = 24 / x для значений x от 0 до 10, исключая ноль. Отобразите данные красными ромбами с пунктирной линией, задайте заголовок "Гипербола", подпишите оси и включите сетку синего цвета с толстыми штрихпунктирными линиями.
# task_1_01.png
a = 24
x_massive = np.linspace(0, 10, 100)
x_massive = x_massive[x_massive != 0]
y_massive = a / x_massive

plt.plot(x_massive, y_massive, marker='d', linestyle='--', color='red', label='Данные')
plt.title("Гипербола")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.grid(True, linestyle='-.', color='blue', linewidth=1.5)
plt.show()


# 2.task
# Отобразите температуру спутника на орбите используя эти данные:
# Ось X — Время (в минутах), представляющее период орбиты
x = np.linspace(0, 60, 13)
# Ось Y — Температура спутника (в градусах Цельсия)
y = np.array([-120, -100, -60, 20, 80, 120, 130, 120, 80, 20, -60, -100, -120])
# task_1_01.png

x = np.linspace(0, 60, 13)
y = np.array([-120, -100, -60, 20, 80, 120, 130, 120, 80, 20, -60, -100, -120])

plt.plot(x, y, marker="s", linestyle="-", color="blue", label="temperature")

plt.title("Температура спутника на орбите")
plt.xlabel("Время (минуты)")
plt.ylabel("Температура (°C)")
plt.grid(True, linestyle="--", color="grey", linewidth=0.9)
plt.show()


# 3.task


years = [2000, 2005, 2010, 2015, 2020, 2023]
debt = [5.67, 7.93, 13.56, 18.15, 26.95, 33.04]

plt.plot(years, debt, marker='o', linestyle='-', color='purple', label="Внешний долг США")
plt.title("Рост внешнего долга США по годам")
plt.xlabel("Год")
plt.ylabel("Внешний долг (триллионы USD)")
plt.grid(True, linestyle='--', color='gray', linewidth=0.5)
plt.legend()

plt.show()


# 4.task

# 5.task
