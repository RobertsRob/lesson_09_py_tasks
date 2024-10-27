# 1.task
# Постройте гистограмму роста ВВП по годам с 1980 по 2023 год.
gdp_growth = [3.0, 4.2, 4.4, 4.7, 4.3, 3.5, 3.0, 4.0, 3.8, 3.9, 2.7, 2.6, 3.1, 2.5, 1.6, 1.2, 1.5, 2.0, 3.2, 4.5, 5.0, 4.3, 3.9, 2.0]

gdp_growth = [3.0, 4.2, 4.4, 4.7, 4.3, 3.5, 3.0, 4.0, 3.8, 3.9, 2.7, 2.6, 3.1, 2.5, 1.6, 1.2, 1.5, 2.0, 3.2, 4.5, 5.0, 4.3, 3.9, 2.0]

plt.figure(figsize=(10, 5))
plt.hist(gdp_growth, bins=10, alpha=0.7, color='orange')
plt.title('GDP Growth Distribution (1980-2023)')
plt.xlabel('GDP Growth (%)')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('gdp_growth_histogram.png', dpi=300)
plt.show()


# 2.task
# Постройте круговую диаграмму для распределения ИТ-рынка на пять ключевых сегментов.
labels = ['Computer equipment', 'Telecomunications services', 'Software', 'Tech outcourcing and hardware maintence', 'Comunications equipment', 'Tech consulting and systems integration services']
sizes = [369, 602, 634, 503, 332, 573]

labels = ['Computer equipment', 'Telecomunications services', 'Software', 'Tech outcourcing and hardware maintence', 'Comunications equipment', 'Tech consulting and systems integration services']
sizes = [369, 602, 634, 503, 332, 573]

plt.figure(figsize=(10, 5))
plt.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=140)
plt.title('Market Share of Major IT Companies')
plt.axis('equal')
plt.tight_layout()
plt.show()


# 3.task
# Постройте график с областями, показывающий диапазон возможных значений силы в физике.
x = np.linspace(0, 10, 100)
force_min = 2 * x
force_max = 4 * x

x = np.linspace(0, 10, 100)
force_min = 2 * x
force_max = 4 * x

plt.figure(figsize=(10, 5))
plt.fill_between(x, force_min, force_max, color='lightblue', alpha=0.5)
plt.title('Force Range in Physics')
plt.xlabel('Distance (m)')
plt.ylabel('Force (N)')
plt.grid(True)
plt.tight_layout()
plt.savefig('force_range.png', dpi=300)
plt.show()


# 4.task
# Постройте столбчатую диаграмму, показывающую продажи различных категорий электроники.
categories = ['Смартфоны', 'Ноутбуки', 'Телевизоры', 'Планшеты', 'Наушники']
sales = [1500, 800, 600, 400, 300]

categories = ['Смартфоны', 'Ноутбуки', 'Телевизоры', 'Планшеты', 'Наушники']
sales = [1500, 800, 600, 400, 300]

fig, ax = plt.subplots()
bars = ax.bar(categories, sales, width=0.4, color=['lightcoral', 'sandybrown', 'khaki', 'lightblue', 'orchid'])

ax.set_xlabel('Категории электроники')
ax.set_ylabel('Продажи (ед.)')
ax.set_title('Продажи различных категорий электроники')
ax.grid()


plt.tight_layout()
plt.show()


# 5.task
# Создайте гистограмму, показывающую изменение выбросов CO2 в Латвии с 1980 по 2022 год.
years = np.arange(1980, 2022)
co2_emissions = [
    18819720, 18779330, 19152220, 19376600, 19607970,
    19804010, 20374980, 20969020, 21230070, 21219170,
    19703930, 17949900, 14259970, 11964820, 10430130,
    9179740, 9193740, 8755940, 8358850, 7809720,
    7179620, 7637810, 7629470, 7869870, 7923780,
    8029490, 8523030, 8893320, 8455920, 7714890,
    8863980, 8203950, 7997810, 7763040, 7538850,
    7627150, 7403590, 8076210, 7871050, 7252090,
    7238830, 6705370,
]

plt.figure(figsize=(12, 6))
plt.hist(co2_emissions, bins=10, alpha=0.7, color='orange', edgecolor='black')
plt.title('Гистограмма выбросов CO2 в Латвии (1980-2022)')
plt.xlabel('Выбросы CO2 (тонн)')
plt.ylabel('Частота')
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.show()


# 6.task
# Создайте график рассеяния, показывающий зависимость выбросов CO2 от численности населения в Латвии с 1980 по 2022 год.
co2_emissions = [
    18819720, 18779330, 19152220, 19376600, 19607970,
    19804010, 20374980, 20969020, 21230070, 21219170,
    19703930, 17949900, 14259970, 11964820, 10430130,
    9179740, 9193740, 8755940, 8358850, 7809720,
    7179620, 7637810, 7629470, 7869870, 7923780,
    8029490, 8523030, 8893320, 8455920, 7714890,
    8863980, 8203950, 7997810, 7763040, 7538850,
    7627150, 7403590, 8076210, 7871050, 7252090,
    7238830, 6705370,
]

population = [
    2511759, 2519970, 2532015, 2546971, 2562773,
    2579231, 2599778, 2625963, 2652247, 2664836,
    2660131, 2648940, 2614827, 2563820, 2521233,
    2485949, 2457905, 2433231, 2410209, 2390822,
    2368313, 2338301, 2311351, 2288984, 2264174,
    2239784, 2219032, 2200776, 2177711, 2142043,
    2097831, 2059941, 2034633, 2013010, 1994149,
    1977867, 1959863, 1942594, 1927588, 1914263,
    1885587, 1881063
]

plt.figure(figsize=(12, 6))
plt.scatter(population, co2_emissions, color='purple', marker='x')
plt.title('Зависимость выбросов CO2 от численности населения в Латвии (1980-2022)')
plt.xlabel('Численность населения')
plt.ylabel('Выбросы CO2 (тонн)')
plt.grid(True)
plt.tight_layout()
plt.show()
