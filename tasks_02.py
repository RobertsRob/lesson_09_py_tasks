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

# 3.task

# 4.task

# 5.task

# 6.task
