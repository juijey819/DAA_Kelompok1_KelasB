import random
import time
import pandas as pd

def greedy_edit_distance(a, b):
    i = j = dist = 0
    len_a, len_b = len(a), len(b)

    while i < len_a and j < len_b:
        if a[i] == b[j]:
            i += 1
            j += 1
        elif i + 1 < len_a and a[i + 1] == b[j]:
            i += 1
            dist += 1
        elif j + 1 < len_b and a[i] == b[j + 1]:
            j += 1
            dist += 1
        else:
            i += 1
            j += 1
            dist += 1

    return dist + (len_a - i) + (len_b - j)

def edit_distance_dp(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost
            )

    return dp[n][m], dp

df = pd.read_csv("Rill-Fake dataset.csv")
df["Rill"] = df["Rill"].fillna("").astype(str)
df["Fake"] = df["Fake"].fillna("").astype(str)
df["n"] = df["Rill"].str.len()

def run_benchmark():
    random.seed(42)

    sizes = [3, 6, 9, 12, 15]

    print(f"\n{'n':<5} | {'Metode':<10} | {'Waktu Rata-rata (ms)':<20} | {'Gap (%)':<10}")
    print("-" * 55)

    t_greedy_times = []
    t_dp_times = []
    gap_percentages = []

    for n in sizes:
        subset = df[(df["n"] >= n - 1.5) & (df["n"] <= n + 1.5)]

        n_sample = min(50, len(subset))
        if n_sample == 0:
            print(f"Warning: Tidak ada data untuk ukuran n={n}")
            continue

        sample_data = subset.sample(n_sample, random_state=42)
        test_data = list(zip(sample_data["Rill"], sample_data["Fake"]))

        for name, func in [("Greedy", greedy_edit_distance), ("DP", edit_distance_dp)]:
            times_list = []
            results = []

            for a, b in test_data:
                start = time.perf_counter()
                for _ in range(20):
                    res = func(str(a), str(b))
                end = time.perf_counter()

                times_list.append(((end - start) / 20) * 1000)

                if name == "DP":
                    results.append(res[0])
                else:
                    results.append(res)

            avg_time = sum(times_list) / len(times_list)

            if name == "Greedy":
                opt_res_raw = [edit_distance_dp(str(a), str(b)) for a, b in test_data]
                opt_res = [val[0] for val in opt_res_raw]

                total_opt = sum(opt_res)
                if total_opt == 0:
                    gap = 0
                else:
                    gap = sum(abs(results[i] - opt_res[i]) for i in range(len(results))) / total_opt * 100

                gap_percentages.append(gap)
                t_greedy_times.append(avg_time)
                print(f"{n:<5} | {name:<10} | {avg_time:<20.6f} | {gap:<10.2f}%")
            else:
                t_dp_times.append(avg_time)
                print(f"{n:<5} | {name:<10} | {avg_time:<20.6f} | {'0.00%':<10}")

        print("-" * 55)

    return sizes, t_greedy_times, t_dp_times, gap_percentages

if __name__ == "__main__":
    run_benchmark()

import pandas as pd

df = pd.read_csv("Rill-Fake dataset.csv")
df["Rill"] = df["Rill"].fillna("").astype(str)
df["Fake"] = df["Fake"].fillna("").astype(str)


df["greedy"] = df.apply(lambda row: greedy_edit_distance(row["Rill"], row["Fake"]), axis=1)
df["dp"] = df.apply(lambda row: edit_distance_dp(row["Rill"], row["Fake"])[0], axis=1)
df["selisih"] = df["greedy"] - df["dp"]

# Simpan hasil
df.to_csv("results.csv", index=False)

print("Selesai! Hasil disimpan ke results.csv")

mistakes = df[df["greedy"] != df["dp"]]
mistakes.to_json("greedy_mistakes.json", index=False)
print("Total kasus greedy salah:", len(mistakes))