import math
import matplotlib.pyplot as plt
 
# ===== 1. Variant ma'lumotlarini kiriting =====
m  = 1.8     # suv massasi, kg
P  = 750    # isitgich quvvati, W
k  = 11     # issiqlik yo'qotish koeffitsiyenti, W/°C
T0 = 16     # boshlang'ich (atrof-muhit) harorati, °C
c  = 4190    # suvning solishtirma issiqlik sig'imi, J/(kg·°C)
 
# ===== 2. Dinamik parametrlarni hisoblash =====
tau   = m * c / k        # vaqt doimiysi, s
K     = 1 / k            # kuchaytirish koeffitsiyenti, °C/W
T_ust = T0 + K * P       # barqaror harorat, °C
 
print(f"Vaqt doimiysi     tau   = {tau:.1f} s = {tau/60:.2f} min")
print(f"Kuchaytirish koef. K     = {K:.4f} °C/W")
print(f"Barqaror harorat  T_ust = {T_ust:.2f} °C")
print(f"95% ga yetish vaqti     = {3*tau/60:.1f} min")
 
# ===== 3. T(t) jadvali =====
def T(t):
    return T0 + K * P * (1 - math.exp(-t / tau))
 
print("\n  t, min     T, °C")
for i in range(0, 11):
    t = i * tau / 2
    print(f"{t/60:8.1f}  {T(t):8.2f}")
 
# ===== 4. Grafik =====
vaqt = [i * 5 * tau / 200 for i in range(201)]
harorat = [T(t) for t in vaqt]
plt.plot([t/60 for t in vaqt], harorat, linewidth=2, label="T(t)")
plt.axhline(T_ust, linestyle="--", color="gray", label="T_ust")
plt.axvline(tau/60, linestyle=":", color="red", label="t = tau")
plt.plot(tau/60, T(tau), "ro")
plt.xlabel("Vaqt, min")
plt.ylabel("Harorat, °C")
plt.title("Suv isitgichning o'tish xarakteristikasi")
plt.grid(True)
plt.legend()
# plt.show()
plt.savefig("result.png", dpi=300, bbox_inches="tight")
plt.close()
