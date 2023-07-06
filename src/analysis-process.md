<script
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
  type="text/javascript">
</script>

# Schema of General Process

## Process in Abaqus
<p align="center">
  <img src="../img/process-schema/process-abaqus.png" width="1200">
<p>

## Process in Abaqus vs Process in HyperWorks
<p align="center">
  <img src="../img/process-schema/process-abaqus-vs-hyperworks.png" width="1200">
<p>

---
# Step by Step

## Import the model from Onshape to HyperWorks
1. In **Onshape**, Right click on the tab for the specific assembly, then click **Export...**
2. Select **PARASOLID**
3. Click **Export**
4. Go to HyperWorks. **File** > **Import...** > **Geometry Model**
5. Select the model from Onshape and click **Open**
6. Select the desired unit system like **MMKS**
7. Click **Import**

<p align="center">
  <img src="../img/import-model/export-parasolid.png" width="800">
  <img src="../img/import-model/import-x_t.png" width="800">
  <img src="../img/import-model/select-unit-system.png" width="800">
<p>

---

## The Basic of Creating Boundary Conditions
1. Right click on the Model Browser > Create > Load Collector
2. Naming **SPC** for this Load Collector conventionally
3. Click Model Ribbon > Rigids. To create RBE2 for the nodes with the same BC
4. Click Analyze Ribbon > Constraints. To assign the BC (SPC) to the independent node of the RBE2.

<p align="center">
  <img src="../img/create-bc/create-loadcollector.png" width="800">
  <img src="../img/create-bc/naming-loadcollector.png" width="800">
  <img src="../img/create-bc/create-rbe2.png" width="800">
  <img src="../img/create-bc/assign-spc.png" width="800">
  <img src="../img/create-bc/create-bc-completed.png" width="800">
<p>

---

## The Basic of Creating Loads
1. Right click on the Model Browser > Create > Load Collector
2. Naming **Load** for this Load Collector conventionally
3. Click Analyze Ribbon > Loads (Pressures). To create pressure on the specific entities with specific magnitude.


<p align="center">
  <img src="../img/create-load/create-loadcollector.png" width="800">
  <img src="../img/create-load/naming-loadcollector.png" width="800">
  <img src="../img/create-load/create-pressure.png" width="800">
  <img src="../img/create-load/create-load-completed.png" width="800">
<p>

---

## The Basic of Setting an Analysis
1. Right click on the Model Browser > Create > Load Step, then a **subcase** would be created.
2. Naming the subcae and assign its **analysis type**, **BCs** and **loads**.
3. Right click on the Model Browser > Create > Cards > Output, then a **GLOBAL_OUTPUT_REQUEST** card would be created.
4. Activate the **STRAIN** item. Normally, stress and displacement are default output.


<p align="center">
  <img src="../img/set-analysis/create-loadstep.png" width="800">
  <img src="../img/set-analysis/set-loadstep.png" width="800">
  <img src="../img/set-analysis/create-output.png" width="800">
  <img src="../img/set-analysis/assign-strain-output.png" width="800">
<p>

---

## Running an Analysis
1. Click Analyze Ribbon > Analyze (Run)
2. Give a name for ***.fem**
3. Click Export
4. **Compute Console** will pop up. Click **...**
5. Set the options **-nt** (cpus), **-core** (control of used memory)
6. Click Apply Selected
7. Click Run

<p align="center">
  <img src="../img/run-analysis/export-fem.png" width="800">
  <img src="../img/run-analysis/compute-console.png" width="400">
<p>

Reference: 
  - <https://2022.help.altair.com/2022/hwsolvers/os/topics/solvers/os/run_options_os_r.htm>

---

# Modal Analysis

## Algorithms
In OptiStruct, normal modes analysis can be performed using one of two algorithms.

| Algorithm | Card name | Pros | Cons |
|-----------|-----------|------|------|
| Lanczos | EIGRL | accurate | slow for large problems (millions of DOF, hundreds of modes) |
| AMSES | EIGRA | much shorter run times | calculations are not exact (modal frequencies are still accurate to a few digits) |

Reference: <https://help.altair.com/hwsolvers/os/topics/solvers/os/analysis_normal_modes_r.htm#analysis_normal_modes_r>

---

## Setting Procedures
1. Create a **Load Step Input** and name it **Modal** conventionally. **EIGRL** or **EIGRA** should be choosed depending on the situation. The required parameters are shown as the following tables.
2. Create a **Load Step** and select **Normal modes** as the analysis type. Name it **Normal Modes** conventionally. Select the existed SPC (Load Collector) and METHOD (Load Step Input).
3. Create card **PARAM** and activate the output **EFFMASS** so that the effctive mass corresponding to each modes would be output at the `*.out` file.

<p align="center">
  <img src="../img/modal-analysis/procedures.png" width="800">
  <img src="../img/modal-analysis/modal-parameters.png" width="500">
  <img src="../img/modal-analysis/effective-mass-output.png" width="500">
<p>

---

# Frequency Response Analysis (FRA)

## Methods
Two types of frequency response analysis:
1. Direct frequency response analysis
2. Modal frequency response analysis, with different solvers:
   - Regular factorization (default)
   - FASTFR (default)
   - FFRS

---

## Requirements for Frequency Range
- Accurate data from modal frequency response requires calculating modes at frequencies higher than the required excitation frequency. 
- Recommended modal frequency range >= 1.5 to 2 times the excitation frequency range. 
- For example, to get accurate modal frequency response predictions to 300 Hz, you should calculate the modes to >= 450Hz.

---

## Frequency Response Function (FRF)
The term **FRF** is frequently mentioned in the Altair tutorial slides without any accompanying explanation. To address this lack of information, I have discovered a reference that provide the explanation about it.

> The FRF of a system is often referred to as its "transfer function" but this term should strictly be reserved for the response of the system expressed in Laplace notation. 

<p align="center">
  <img src="../img/frf/frf-explanation.png" width="300">
<p>

---

## Mind Map of FRF Analysis

<p align="center">
  <img src="../img/frf/mind-map.png" width="1000">
<p>

---

## SPCD
- The `SPCD` card defines an enforced displacement, velocity or acceleration.
- To create Loads/SPCD, click Analyze ribbon > Constraints

---

## DAREA
- The `DAREA` card represents a force excitation loading.
- To create Loads/DAREA, click Analyze ribbon > Constraints

---

## RLOAD
- RLOAD1
  - $P(f) = A[C(f) + iD(f)]e^{i(\theta-2\pi f\tau)}$
  - A: EXCITEID
  - C: TC
  - D: TD
  - $\tau$: DELAY
- RLOAD2
  - $P(f) = A \times B(f) e^{i(\varphi(f) + \theta - 2\pi f\tau)}$
  - A: EXCITEID
  - B: TB
  - $\varphi(f)$: TP
  - $\theta$: DPHASE
  - $\tau$: DELAY

---

## TABLED
$$
y = \left\{
  \begin{aligned}
    y_T (x) && \text{, for TABLED1} \\ 
    y_T (x - X_1) && \text{, for TABLED2} \\
    y_T (\frac{x - X_1}{X_2}) && \text{, for TABLED3} \\
    \sum_{i=0}^{N}{A_i(\frac{x - X_1}{X_2})^i} && \text{, for TABLED4}
  \end{aligned}
\right. 
$$

where $X_1$, $X_2$ and $A_i$ are input parameters and

$$
y_T(x) = \left\{
  \begin{aligned}
    \frac{(x_j - x)}{(x_j - x_i)}y_i + \frac{(x - x_i)}{(x_j - x_i)}y_j && \text{, for linear-x and linear-y} \\
    \frac{\ln(x_j/x)}{\ln(x_j/x_i)}y_i + \frac{\ln(x/x_i)}{\ln(x_j/x_i)}y_j && \text{, for log-x and linear-y} \\
    \exp\left[\frac{(x_j - x)}{(x_j - x_i)}\ln y_i + \frac{(x - x_i)}{(x_j - x_i)}\ln y_j\right] && \text{, for linear-x and log-y} \\
    \exp\left[\frac{\ln(x_j/x)}{\ln(x_j/x_i)}\ln y_i + \frac{\ln(x/x_i)}{\ln(x_j/x_i)}\ln y_j\right] && \text{, for log-x and log-y} \\
    y_i + (y_j - y_i) \frac{\left(x - x_i\right)^3}{\left(x_j - x_i\right)^3}\left(10 - 15 \frac{\left(x - x_i\right)}{\left(x_j - x_i\right)} + \frac{\left(x - x_i\right)^2}{\left(x_j - x_i\right)^2} \right) && \text{, for linear-x and smooth-y}
  \end{aligned}
\right. 
$$

---

## FREQi

<p align="center">
  <img src="../img/frf/freq1.png" width="500">
  <img src="../img/frf/freq2.png" width="500">
  <img src="../img/frf/freq3.png" width="500">
  <img src="../img/frf/freq4.png" width="500">
  <img src="../img/frf/freq5.png" width="500">
<p>

---
