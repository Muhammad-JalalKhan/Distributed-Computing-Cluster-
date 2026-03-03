# 🖥️ Distributed Computing Cluster with Dask

A multi-machine distributed computing project using **Dask** to offload heavy ML and mathematical workloads across a network of computers (Ryzen master + i5 worker).

---

## 🧠 What This Project Does

This project sets up a **Dask distributed cluster** across two machines on a local network. Heavy tasks like hyperparameter tuning and stress computations are split and processed in parallel across both machines — significantly faster than running on a single PC.

---

## 🗂️ Project Structure

| File | Description |
|------|-------------|
| `start_master.bat` | Starts the Dask **scheduler + local worker** on the master (Ryzen) machine |
| `start_worker.bat` | Connects the **secondary machine** (i5) as a worker to the cluster |
| `cluster_compute.py` | Basic distributed task runner — sends 50 CPU-heavy math tasks to the cluster |
| `heavy_stress_test.py` | Full cluster stress test — runs 100 heavy tasks (prime search + matrix multiplication) |
| `distributed_ml_tuning.py` | Distributed **ML hyperparameter tuning** using Scikit-Learn + Dask (90 training sessions) |

---

## ⚙️ Setup & Usage

### Step 1 — Start the Cluster (Master Machine / Ryzen)
```bat
start_master.bat
```
This launches the Dask scheduler and registers the Ryzen as the first worker.

### Step 2 — Connect Worker Machine (i5)
```bat
start_worker.bat
```
Run this on the second machine to join it to the cluster.

### Step 3 — Monitor the Cluster
Open your browser and go to:
```
http://10.90.23.184:8787
```
This opens the **Dask Dashboard** where you can watch tasks being distributed in real-time.

### Step 4 — Run a Script
```bash
# Basic compute test
python cluster_compute.py

# Full stress test
python heavy_stress_test.py

# ML Hyperparameter Tuning
python distributed_ml_tuning.py
```

---

## 📦 Requirements

```bash
pip install dask distributed scikit-learn numpy joblib
```

---

## 🌐 Network Configuration

| Machine | Role | IP Address |
|---------|------|------------|
| Ryzen PC | Scheduler + Worker | `10.90.23.184` |
| Intel i5 PC | Worker | *(dynamic)* |

> ⚠️ Both machines must be on the **same local network** and able to reach port `8786`.

---

## 📊 What to Expect

- **`cluster_compute.py`** — 50 tasks distributed, results printed with timing
- **`heavy_stress_test.py`** — 100 tasks, high CPU + RAM usage on all workers for several minutes
- **`distributed_ml_tuning.py`** — 90 cross-validation sessions distributed across all cores in the cluster, outputs best ML parameters and accuracy score

---

## 💡 Key Concept

> Instead of one computer doing all the work, Dask **breaks tasks into chunks** and sends them to every available machine. The more workers you add, the faster it runs.
