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

# 5.task

# 6.task

# 7.task
