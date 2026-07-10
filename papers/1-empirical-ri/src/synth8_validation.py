"""synth8_validation.py — planted-ground-truth validation (pilot-design.md §6).

Runs the SAME estimator/analysis code path the MNIST experiment uses, on the
Synth-8 planted domain (D = {0,1}^3, 8 classes) from ri_pilot.synth8, and checks
every estimator against its exact closed form BEFORE trusting the MNIST numbers.
This is where H5 (transport) and H6 (half-gap vs known injected noise) live —
the MNIST run has no ground-truth transport pair to exhibit them on.

Plants (design §6):
  * deterministic parity pair (v1=b0, v2=b1), q = parity b0^b1:
        transport -> C_fine = 0, CI_coarse = 1 bit           [H5]
  * pure-coupling pair (v3,v4 keyed to b2, Prop 22.4(2)), q = b2:
        C_fine = CI_coarse = 3/2 - (3/4)log2(3) ~ 0.3113 bits
  * two BSC(0.15) looks at b0 (v5,v6):
        accumulation gain > 0                                 [H2]
        blind decay matches mixture; enriched TV linear       [H3]
        targeted hard zero at eps* = d/(2+d)                  [H4]
  * half-gap: deterministic view ~ 1/2 (exact jump); BSC-noised view < 1/2
        (graded), and nu_delta -> 1/2 as injected noise -> 0  [H6]
"""
import os, sys, json
import numpy as np
from math import log2

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "shared"))
from ri_pilot import (synth8, estimate_channel, ledger_table, deficiency,
                      blind_mix, targeted_attack, q_info, q_tv, refusal)

N = 60000
COUPLING_CLOSED = 1.5 - 0.75 * log2(3)   # ~0.3113


def parity_q():
    return [((z & 1) ^ ((z >> 1) & 1)) for z in range(8)]


def bit_q(i):
    return [(z >> i) & 1 for z in range(8)]


def main():
    os.makedirs("results", exist_ok=True)
    Z, V = synth8(N)
    prior = np.array([np.mean(Z == z) for z in range(8)])
    nc = np.bincount(Z, minlength=8)
    out = {"n": N, "closed_forms": dict(coupling=COUPLING_CLOSED)}

    # ---- H5: transport (deterministic parity pair) ----
    qpar = parity_q()
    Pv1 = estimate_channel(V["v1"], Z, 2, 8)
    Pv2 = estimate_channel(V["v2"], Z, 2, 8)
    Pj12 = estimate_channel(V["v1"] * 2 + V["v2"], Z, 4, 8)
    lt = ledger_table(Pv1, Pv2, Pj12, prior, qpar)
    out["transport"] = dict(C_fine=lt["C_fine"], CI_coarse=lt["CI_coarse"],
                            I_joint=lt["I_joint"],
                            H5_pass=bool(lt["C_fine"] < 0.02 and lt["CI_coarse"] > 0.95))
    print(f"[H5 transport] C_fine={lt['C_fine']:.4f} (plant 0)  "
          f"CI_coarse={lt['CI_coarse']:.4f} (plant 1.0)  I_joint={lt['I_joint']:.4f}")

    # ---- pure coupling quantum ----
    qb2 = bit_q(2)
    Pv3 = estimate_channel(V["v3"], Z, 2, 8)
    Pv4 = estimate_channel(V["v4"], Z, 2, 8)
    Pj34 = estimate_channel(V["v3"] * 2 + V["v4"], Z, 4, 8)
    lt2 = ledger_table(Pv3, Pv4, Pj34, prior, qb2)
    out["coupling"] = dict(C_fine=lt2["C_fine"], CI_coarse=lt2["CI_coarse"],
                           closed=COUPLING_CLOSED,
                           gap=abs(lt2["CI_coarse"] - COUPLING_CLOSED))
    print(f"[coupling]     C_fine={lt2['C_fine']:.4f}  CI_coarse={lt2['CI_coarse']:.4f}  "
          f"closed={COUPLING_CLOSED:.4f}  gap={abs(lt2['CI_coarse']-COUPLING_CLOSED):.4f}")

    # ---- H2: accumulation (two BSC(0.15) looks at b0), q = b0 ----
    qb0 = bit_q(0)
    Pv5 = estimate_channel(V["v5"], Z, 2, 8)
    Pv6 = estimate_channel(V["v6"], Z, 2, 8)
    I5 = q_info(Pv5, prior, qb0); I6 = q_info(Pv6, prior, qb0)
    Pj56 = estimate_channel(V["v5"] * 2 + V["v6"], Z, 4, 8)
    Ij56 = q_info(Pj56, prior, qb0)
    gain = Ij56 - max(I5, I6)
    out["accumulation"] = dict(I_v5=float(I5), I_v6=float(I6), I_joint=float(Ij56),
                               gain=float(gain), H2_pass=bool(gain > 0))
    print(f"[H2 accumul.]  I_v5={I5:.4f} I_v6={I6:.4f} I_joint={Ij56:.4f} gain={gain:+.4f}")

    # ---- H3: blind law + linear enriched TV (single BSC look v5) ----
    P_clean = Pv5
    d0 = q_tv(P_clean, prior, qb0)
    blind = []
    for eps in [0, .15, .3, .45, .6, .75, .9]:
        c = V["v5"].copy()
        flip = np.random.default_rng(int(eps * 100) + 1).random(N) < eps
        c[flip] = np.random.default_rng(int(eps * 100) + 2).integers(0, 2, flip.sum())
        Pm = estimate_channel(c, Z, 2, 8)
        I_meas = q_info(Pm, prior, qb0); tv_meas = q_tv(Pm, prior, qb0)
        I_pred = q_info(blind_mix(P_clean, eps), prior, qb0)
        tv_pred = (1 - eps) * d0
        blind.append(dict(eps=eps, I_meas=float(I_meas), I_pred=float(I_pred),
                          tv_meas=float(tv_meas), tv_pred=float(tv_pred)))
    maxIgap = max(abs(b["I_meas"] - b["I_pred"]) for b in blind)
    maxTVgap = max(abs(b["tv_meas"] - b["tv_pred"]) for b in blind)
    out["blind"] = dict(d0=float(d0), curve=blind, max_I_gap=float(maxIgap),
                        max_TV_gap=float(maxTVgap),
                        H3_pass=bool(maxIgap < 0.02 and maxTVgap < 0.02))
    print(f"[H3 blind]     d0={d0:.4f}  max|I gap|={maxIgap:.4f}  max|TV gap|={maxTVgap:.4f}")

    # ---- H4: targeted hard zero at eps* = d/(2+d), d = L1 = 2*TV ----
    d_L1 = 2 * d0
    eps_star = d_L1 / (2 + d_L1)
    targ = []
    for eps in [max(0, eps_star - .1), eps_star, min(.99, eps_star + .1)]:
        Pt = targeted_attack(P_clean, prior, qb0, eps)
        targ.append(dict(eps=float(eps), I=float(q_info(Pt, prior, qb0)),
                         tv=float(q_tv(Pt, prior, qb0))))
    I_at_star = [t for t in targ if abs(t["eps"] - eps_star) < 1e-9][0]["I"]
    out["targeted"] = dict(d_L1=float(d_L1), eps_star=float(eps_star), curve=targ,
                           I_at_eps_star=float(I_at_star),
                           H4_pass=bool(abs(I_at_star) < 1e-3))
    print(f"[H4 targeted]  eps*={eps_star:.4f}  I(eps*)={I_at_star:.5f} (plant 0)")

    # ---- H6: half-gap classifier vs known injected noise ----
    # deterministic pair -> exact interval, nu_delta ~ 1/2 (jump, Prop 69.2)
    nu_det = deficiency(Pv1, Pv2)
    # sweep BSC crossover injected into a deterministic view of b0; nu_delta of the
    # (noisy -> deterministic) Blackwell interval should be < 1/2 (graded) and
    # decrease toward 0 as the view sharpens (noise -> 0 makes it sufficient).
    Pdet_b0 = estimate_channel(V["v1"], Z, 2, 8)  # v1 = b0 deterministically
    sweep = []
    for cross in [0.05, 0.15, 0.30, 0.45]:
        rng = np.random.default_rng(int(cross * 1000))
        noisy = np.where(rng.random(N) < cross, 1 - V["v1"], V["v1"])
        Pn = estimate_channel(noisy, Z, 2, 8)
        nu = deficiency(Pn, Pdet_b0)   # how far the noisy view is from the sufficient one
        sweep.append(dict(crossover=cross, nu_delta=float(nu),
                          graded=bool(nu < 0.5 - 0.02)))
    out["half_gap"] = dict(nu_deterministic_pair=float(nu_det),
                           deterministic_at_boundary=bool(nu_det > 0.49),
                           injected_noise_sweep=sweep,
                           H6_pass=bool(nu_det > 0.49 and all(s["graded"] for s in sweep)))
    print(f"[H6 half-gap]  deterministic pair nu_delta={nu_det:.4f} (>=1/2 jump)")
    for s in sweep:
        print(f"                 BSC({s['crossover']:.2f}) nu_delta={s['nu_delta']:.4f} "
              f"graded={s['graded']}")

    # ---- refusal rule exercised ----
    out["refusal_demo"] = dict(
        pass_k16=bool(refusal(nc, 16)),
        refuse_k4096=bool(not refusal(nc, 4096)),
        n_min=int(nc.min()))
    print(f"[refusal]      k^2=16 -> {refusal(nc,16)} ; k=4096 -> {refusal(nc,4096)} "
          f"(n_min={nc.min()})")

    verdicts = {f"H{i}": out[k][f"H{i}_pass"] for i, k in
                [(2, "accumulation"), (3, "blind"), (4, "targeted"),
                 (5, "transport"), (6, "half_gap")]}
    # H1 (admissibility Delta>0) is exercised on MNIST E1; note it here.
    verdicts["H1"] = "see MNIST E1 (no planted admissibility gap in Synth-8)"
    out["verdicts"] = verdicts
    print("\nVERDICTS:", verdicts)

    with open("results/synth8_validation.json", "w") as f:
        json.dump(out, f, indent=2)
    print("wrote results/synth8_validation.json")


if __name__ == "__main__":
    main()
