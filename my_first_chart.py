import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic" #윈도우는 Malgun Gothic
temperature = [27, 20, 19, 20, 23]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(temperature)
for i, p in enumerate(temperature):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points",
xytext=(0, 8), ha="center")
ax.set_title("2026 10 12 ~ 10 16 춘천 최고기온")
fig.savefig("my_first_chart.png")