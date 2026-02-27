import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
import time
import math

# --------------------------------------------------------------------------------------hesaplama icin gereken diger fonkslar
def generate_points(n):
    """Rastgele nokta kumesi olusturur."""
    return np.random.randint(0, 100, size=(n, 2))

def get_cross_product(p1, p2, p3):
    """ Saat yonu tersi (+) veya saat yonu (-)."""
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

# -------------------------------------------------------------------------------------------algoritmalar

def brute_force_hull(points):
    """Kaba Kuvvet - Teorik Karmasiklik: O(n^3). """
    n = len(points)
    hull_edges = []
    start_time = time.perf_counter()
    # Her (p, q) nokta cifti kontrol edilir: O(n^2)
    for i in range(n):
        for j in range(n):
            if i == j: continue
            p1, p2 = points[i], points[j]
            all_on_one_side = True
            # Kumedeki diger noktalar kontrol: O(n)
            for k in range(n):
                if k == i or k == j: continue
                if get_cross_product(p1, p2, points[k]) < 0:
                    all_on_one_side = False
                    break
            if all_on_one_side:
                hull_edges.append((p1, p2))
    return hull_edges, time.perf_counter() - start_time





def graham_scan_hull(points):
    """Graham Scan Algoritmasi - Teorik Karmasiklik: O(n log n). """
    n = len(points)
    if n < 3: return points, 0
    start_time = time.perf_counter()
    # 1. en alt noktayi bulma: O(n)
    pivot = min(points, key=lambda p: (p[1], p[0]))
    # 2. aciya gore siralama: O(n log n) 
    sorted_pts = sorted(points.tolist(), key=lambda p: math.atan2(p[1]-pivot[1], p[0]-pivot[0]))
    # 3.Stack ile tarama: O(n)
    hull = [sorted_pts[0], sorted_pts[1]]
    for i in range(2, len(sorted_pts)):
        while len(hull) > 1 and get_cross_product(hull[-2], hull[-1], sorted_pts[i]) <= 0:
            hull.pop() 
        hull.append(sorted_pts[i])
    return np.array(hull), time.perf_counter() - start_time

# ----------------------------------------------------------------------------------------------arayuzun yonetimi






fig, ax = plt.subplots(figsize=(10, 8))
plt.subplots_adjust(bottom=0.35)
n_current = 100
current_points = generate_points(n_current)

def draw_base():
    ax.clear()
    ax.scatter(current_points[:, 0], current_points[:, 1], color='gray', s=20, alpha=0.6)
    ax.set_title(f"Convex Hull Analizi (N={n_current})")
    ax.set_xlim(-5, 105)
    ax.set_ylim(-5, 105)



def update_n(text):
    global n_current, current_points
    try:
        val = int(text)
        if val > 2:
            n_current = val
            current_points = generate_points(n_current)
            draw_base()
            plt.draw()
    except ValueError: pass



def run_brute(event):
    draw_base()
    #--------------------------------------------------------------------------------  her N degeri icin deneme
    edges, duration = brute_force_hull(current_points)
    for p1, p2 in edges:
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'r-', linewidth=1)
    ax.set_title(f"Kaba Kuvvet (O(n^3)) - Sure: {duration:.6f} sn")
    plt.draw()



def run_graham(event):
    draw_base()
    hull, duration = graham_scan_hull(current_points)
    if len(hull) > 0:
        hull_plot = np.vstack([hull, hull[0]])
        ax.plot(hull_plot[:, 0], hull_plot[:, 1], 'g-', linewidth=2)
    ax.set_title(f"Graham Scan (O(n log n)) - Sure: {duration:.6f} sn")
    plt.draw()




def run_perf_test(event):
    # -----------------------------------------------------------------------------performans testi girilenn N degerine kadar olcum yapar 
    n_values = [int(x) for x in np.linspace(10, n_current, 5)] 
    bf_times, gs_times = [], []

    
    print(f"Performans testi baslatildi (Maksimum N={n_current})...")
    for n in n_values:
        pts = generate_points(n)
        _, t_bf = brute_force_hull(pts)
        bf_times.append(t_bf)
        _, t_gs = graham_scan_hull(pts)
        gs_times.append(t_gs)

        print(f"N={n} icin sureler olculudu..")



    plt.figure("Performans Karsilastirma Grafigi")
    plt.plot(n_values, bf_times, 'b-o', label='Kaba Kuvvet ')
    plt.plot(n_values, gs_times, 'g-s', label='Graham Scan ')
    plt.xlabel('N (Nokta Sayisi)')
    plt.ylabel('Sure (Saniye)')
    plt.title(f'N={n_current} Degerine Kadar Calisma Sureleri')
    plt.legend()
    plt.grid(True)
    plt.show()





#----------------------------------------------------------------------------------- arayuz
draw_base()
ax_box = plt.axes([0.15, 0.22, 0.1, 0.05])
text_box = TextBox(ax_box, 'N Degeri: ', initial="100")
text_box.on_submit(update_n)


ax_brute = plt.axes([0.1, 0.08, 0.25, 0.08])
ax_graham = plt.axes([0.37, 0.08, 0.25, 0.08])
ax_perf = plt.axes([0.65, 0.08, 0.25, 0.08])


btn_brute = Button(ax_brute, 'Kaba Kuvveti Bul', color='mistyrose')
btn_graham = Button(ax_graham, 'Graham Scani Bul', color='honeydew')
btn_perf = Button(ax_perf, 'Performans Testi Yap', color='aliceblue')



btn_brute.on_clicked(run_brute)
btn_graham.on_clicked(run_graham)
btn_perf.on_clicked(run_perf_test)

plt.show()



