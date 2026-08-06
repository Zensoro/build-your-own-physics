"""Generate real-simulation preview images for the static site.

Each challenge (except 10-relativity, which is math-only) is rendered by
running its solution's `__main__` with `plt.show` redirected to `savefig`.
For 08-fluid we run a lighter simulation; for 10-relativity we draw a
Minkowski spacetime diagram using the solution's own `lorentz()` transform.
"""
import os
import sys
import runpy
import importlib.util
import matplotlib

matplotlib.use("Agg")
# Use a CJK-capable font when available so challenge previews render cleanly.
matplotlib.rcParams["font.sans-serif"] = [
    "PingFang SC",
    "Heiti SC",
    "STHeiti",
    "SimHei",
    "Arial Unicode MS",
    "DejaVu Sans",
]
matplotlib.rcParams["axes.unicode_minus"] = False
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site", "previews")
os.makedirs(OUT, exist_ok=True)


def save_show(path):
    def _show(*_a, **_k):
        fig = plt.gcf()
        fig.savefig(path, dpi=90, bbox_inches="tight")
        plt.close("all")
    return _show


def run_main(challenge_dir, save_path):
    sol = os.path.join(challenge_dir, "solutions")
    py = [f for f in os.listdir(sol) if f.endswith(".py")][0]
    target = os.path.join(sol, py)
    plt.show = save_show(save_path)
    runpy.run_path(target, run_name="__main__")


def load_module(path):
    spec = importlib.util.spec_from_file_location("mod", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def preview_fluid(save_path):
    mod = load_module(os.path.join(ROOT, "challenges/08-fluid/solutions/fluid.py"))
    rho, ux, uy = mod.simulate_lid_driven(nx=64, ny=64, n_steps=4000)
    wx = np_gradient(uy, axis=1)
    wy = np_gradient(ux, axis=0)
    vort = wx - wy
    plt.figure(figsize=(6, 5))
    plt.imshow(vort, cmap="RdBu_r", origin="lower")
    plt.colorbar(label="vorticity")
    plt.quiver(ux[::4, ::4], uy[::4, ::4], scale=30)
    plt.title("Lid-driven cavity: main vortex + corner vortices")
    plt.tight_layout()
    plt.savefig(save_path, dpi=90, bbox_inches="tight")
    plt.close("all")


def np_gradient(a, axis):
    import numpy as np
    return np.gradient(a, axis=axis)


def preview_relativity(save_path):
    mod = load_module(os.path.join(ROOT, "challenges/10-relativity/solutions/relativity.py"))
    v = 0.6
    g = mod.gamma(v)
    fig, ax = plt.subplots(figsize=(6.5, 6))
    # S frame grid
    for i in range(-5, 6):
        ax.plot([-5, 5], [i, i], color="#cccccc", lw=0.6)
        ax.plot([i, i], [-5, 5], color="#cccccc", lw=0.6)
    # light cone
    ax.plot([-5, 5], [-5, 5], "k--", lw=1, alpha=0.5)
    ax.plot([-5, 5], [5, -5], "k--", lw=1, alpha=0.5)
    # S' axes: x' axis (ct = v x) and ct' axis (x = v ct)
    ax.plot([-5, 5], [v * -5, v * 5], "C3", lw=2, label=f"S' x'-axis")
    ax.plot([v * -5, v * 5], [-5, 5], "C2", lw=2, label=f"S' ct'-axis")
    # a moving particle worldline in S
    ax.plot([-5, 5], [0.3 * -5, 0.3 * 5], "C0", lw=1.5, label="particle (v=0.3c in S)")
    ax.axhline(0, color="black", lw=1)
    ax.axvline(0, color="black", lw=1)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect("equal")
    ax.set_xlabel("x (c=1)")
    ax.set_ylabel("ct (c=1)")
    ax.set_title(f"Minkowski diagram  (v=0.6c,  γ={g:.3f})")
    ax.legend(loc="upper left", fontsize=8)
    plt.tight_layout()
    plt.savefig(save_path, dpi=90, bbox_inches="tight")
    plt.close("all")


def main():
    targets = [
        ("01-projectile", "preview_01.png"),
        ("02-pendulum", "preview_02.png"),
        ("03-orbit", "preview_03.png"),
        ("04-nbody", "preview_04.png"),
        ("05-wave-machine", "preview_05.png"),
        ("06-heat-engine", "preview_06.png"),
        ("07-double-pendulum", "preview_07.png"),
        ("09-electromagnetism", "preview_09.png"),
        ("11-quantum", "preview_11.png"),
        ("12-solar-system", "preview_12.png"),
    ]
    for name, out in targets:
        path = os.path.join(OUT, out)
        d = os.path.join(ROOT, "challenges", name)
        print(f"[gen] {name} -> {out}", flush=True)
        run_main(d, path)

    print("[gen] 08-fluid (lightweight) -> preview_08.png", flush=True)
    preview_fluid(os.path.join(OUT, "preview_08.png"))
    print("[gen] 10-relativity (Minkowski) -> preview_10.png", flush=True)
    preview_relativity(os.path.join(OUT, "preview_10.png"))
    print("DONE")


if __name__ == "__main__":
    main()
