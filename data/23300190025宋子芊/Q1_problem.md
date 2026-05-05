
# Question
# Orbital Decay and Electro-Thermal Equilibrium of an Electrodynamic Tether
### Introduction
Electrodynamic tethers (EDTs) are long conducting wires used to exchange energy and momentum with a planetary magnetic field. In this problem, we consider an EDT system consisting of two identical small satellites, each of mass $m$, connected by a thin, straight, conductive tether of length $L$ and total resistance $R$. The system orbits the Earth in the equatorial plane at an altitude within the ionosphere. Due to the gravity gradient, the tether is stabilized in a radial orientation, pointing toward the Earth’s center.

**Useful Information:**
*   The Earth’s magnetic field can be modeled as a magnetic dipole. In the equatorial plane, the magnetic field is strictly perpendicular to the orbital plane.
*   The magnitude of the magnetic field at a distance $r$ from the Earth's center is given by:
    $$B(r) = B_0 \left( \frac{R_E}{r} \right)^3$$
    where $R_E$ is the Earth's radius and $B_0$ is the magnetic field strength at the surface on the equator. It’s direction is the same as the angular velocity of EDT system.
*   The effective emission area of the cathode is $S_{emit} = \eta S$, where $S$ is the total surface area of the tether and $\eta$ is a dimensionless factor.

---

### Part A: Orbital Dynamics and Motional EMF (3.0 points)

Consider the tether system initially moving in a stable circular orbit of radius $r$ ($r \gg L$) in the Earth’s equatorial plane. The mass of the tether is negligible (take $m_{tether} = 0$), so the two satellites are the only significant masses in the system. 
**A.1.** Under the rotating reference frame, find the expression for the tension $T_N$ at the midpoint of the tether. Use a first-order Taylor expansion in terms of $L/r$ to simplify your result. **[1.2 pt]**

**A.2.** As the conductive tether cuts through the Earth's magnetic field lines, a motional electromotive force (EMF) is generated between its ends. Calculate the magnitude of this EMF, $\mathcal{E}$, as a function of $r$, $L$, and the given planetary constants(just keep terms up to the first non-zero order). **[1.0 pt]**

**A.3.** Determine the polarity of the induced EMF. Which satellite (the one closer to Earth or the one farther from Earth) accumulates positive charges? **[0.8 pt]**

---

### Part B: Electrodynamic Drag and Orbital Evolution (4.0 points)

The tether is immersed in the ionospheric plasma, which is a dilute ionized gas. By using specialized contactors at the ends of the tether (e.g., a hollow cathode at the lower end and an electron collection tether at the upper end), the circuit is closed through the ambient plasma. The plasma acts as a return path with negligible resistance. A steady current $I$ flows through the tether.

**B.1.** Derive the expression for the total Lorentz force $\vec{F}_L$ acting on the tether. Show that this force acts in the direction exactly opposite to the orbital velocity vector $\vec{v}$. (just keep terms up to the first non-zero order)**[1.0 pt]**

**B.2.** Due to the work done by the Lorentz force, the system's mechanical energy dissipates, causing the orbit to decay. Assuming the orbit remains quasi-circular at all times, derive the differential equation for the rate of change of the orbital radius, $dr/dt$, in terms of $I, B_0, R_E, L, m, M_E$, and $r$. **[1.5 pt]**

**B.3.** Let $Q$ be the total charge transferred through the tether as the system descends from an initial radius $r_1$ to a final radius $r_2$. Prove that $Q$ depends only on $r_1, r_2$, and the planetary constants ($M_E, R_E, B_0$), but is independent of the tether's resistance $R$ or the specific time-evolution of the current. Find the expression for $Q$. **[1.5 pt]**

---

### Part C: Electro-Thermal Limits and Asymptotic Evolution (3.0 points)

In a realistic scenario, the current $I$ is limited by the ability of the tether's ends to emit electrons into the plasma. At the cathode (the negative end), the current is governed by Richardson's thermionic emission law. Furthermore, the tether is subject to intense heating.

**Useful Information for Part C:**
*   Stefan-Boltzmann Law: The power radiated by a surface area $S$ with emissivity $\epsilon$ at temperature $T$ is $P_{rad} = \epsilon \sigma S T^4$, where $\sigma$ is the Stefan-Boltzmann constant.
*   Richardson’s Law for thermionic emission: The saturation current $I$ emitted by a surface $S_{emit}$ at temperature $T$ is given by $I = S_{emit} A_R T^2 \exp\left(-\frac{\Phi}{k_B T}\right)$, where $A_R$ is Richardson's constant and $\Phi$ is the work function. The work function is the minimum energy required to remove an electron from a material into free space.

**C.1.** The tether reaches a steady-state temperature $T_{eq}$ when the Joule heating power is balanced by thermal radiation into space and the energy consumed by emitting electrons. Assume each emitted electron carries away a kinetic energy that is negligible compared to the work function $\Phi$. Furthermore, assume the induced EMF $\mathcal{E}$ is sufficiently large such that the current $I$ is exactly the saturation current $I_{sat}$ allowed by the cathode temperature. Formulate a system of two equations that self-consistently determine the steady-state temperature $T_{eq}$ and the saturated current $I_{sat}$ in terms of the tether's parameters ($R, S, \eta, \epsilon, \Phi$) and physical constants. **[1.2 pt]**

**C.2.** Consider a limit where the system is driven to extreme temperatures such that Joule heating dominates the emission cooling (i.e., the energy consumed by the emitting electrons can be ignored) and the thermal energy is much larger than the work function ($k_B T \gg \Phi$). Under these asymptotic conditions, the exponential term in Richardson's Law can be approximated as $\exp(-\Phi/k_B T) \approx 1 - \Phi/k_B T$. Find the expression for the orbital decay rate $|dr/dt|$ in this limit, expressed in terms of the tether's material/geometric constants ($S, \epsilon,\eta, \phi, L$), the satellites' mass $m$, and the local orbital parameters ($B, r$). And give the maximum value of r allowed under this condition.  **[1.8 pt]**

# QuestionReview
### [1] Final Assessment Conclusion
**PASS (Adopt Directly)**
The problem is physically rigorous, mathematically elegant, and perfectly mirrors the IPhO "progressive narrative" style. It successfully couples three distinct areas of physics (Orbital Mechanics, Electrodynamics, and Thermodynamics) into a self-consistent feedback loop. The "Charge Transfer Theorem" in Part B is a classic IPhO-style discovery, and the transition to the thermionic emission limit in Part C provides the necessary "High-Distinction" filter.

### [2] Multi-dimensional Review Feedback

*   **2.1 Narrative Rhythm and Guiding Text Feedback:**
    The narrative rhythm is excellent. The problem begins with a minimalist setup (Introduction), providing only the essential orbital and magnetic field geometry. It avoids "information dumping" by withholding the Stefan-Boltzmann and Richardson's laws until they are contextually required in Part C. The interstitial text between A, B, and C effectively "upgrades" the model (from a passive wire to an active circuit, then to a thermally limited system) in a way that feels like a research progression.

*   **2.2 Freedom and Symbol Check Results:**
    *   **Consistency:** All symbols ($M_E, R_E, B_0, m, L, R, S, \epsilon, A_R, \Phi$) are 100% aligned with the [Problem Framework].
    *   **Closure:** The system is perfectly closed. The orbital radius $r$ determines $v$ and $B$, which determine $\mathcal{E}$. $\mathcal{E}$ and $R$ (along with thermal limits) determine $I$. $I$ determines the Lorentz force $F_L$, which dictates the evolution $dr/dt$. There are no redundant or missing degrees of freedom.

*   **2.3 Questioning Standards and Score Summation Audit:**
    *   **Verbs:** The use of "Show that...", "Derive the differential equation...", and "Find the asymptotic expression..." follows IPhO standards, balancing derivation with calculation.
    *   **Point Allocation:**
        *   Part A: 1.2 + 1.0 + 0.8 = **3.0**
        *   Part B: 1.0 + 1.5 + 1.5 = **4.0**
        *   Part C: 1.2 + 1.8 = **3.0**
        *   **Total: 10.0 points.** (Perfectly satisfies the framework requirements).

*   **2.4 Hidden Conditions and Mathematical Calculation Assessment:**
    *   **Part A.1:** The requirement for the first-order Taylor expansion of the gravity gradient is a standard yet non-trivial test of orbital frame dynamics.
    *   **Part B.3:** This is the highlight of the problem. Integrating $dr/dt$ reveals that the total charge $Q$ is a state function of the radii, independent of the resistance $R$. This provides a "eureka" moment for the student.
    *   **Part C.2:** The approximation $\exp(-x) \approx 1-x$ for the thermionic limit is a sophisticated way to turn a transcendental system into a solvable asymptotic limit, testing the student's ability to handle physical scales.

### [3] Major Risk Warning
**A.1 Tension Coefficient Ambiguity:**
There is a slight risk regarding the tension $T_N$. In the rotating frame, for two point masses $m$ separated by $L$, the tension is $T = \frac{3GM_E mL}{2r^3}$. However, some textbooks (and the original Framework) occasionally cite $3/4$ if they consider a continuous rod of total mass $2m$. The Proposition Agent must ensure the Marking Scheme explicitly uses the point-mass derivation (coefficient $3/2$) unless the tether itself is treated as having mass. Given the prompt specifies $m_{tether}=0$, $3/2$ is the correct physical result.

**C.2 Limit Logic:**
The phrase "tipping point where $I_{sat}$ is exactly limited by the available EMF" is a sophisticated constraint. It implies the condition where the electrical driving force exactly matches the maximum possible emission. Students might find the algebraic substitution between $I^2R$ and $T^4$ challenging; the Marking Scheme must clearly show how $I$ cancels out or settles into the material-constant-driven expression.

### [4] Actionable Suggestions for Rework
**None.** The problem is ready for the competition. 

*(Optional optimization for the Agent: In the solution manual, ensure the derivation for **B.3** clearly shows the substitution $v = \sqrt{GM_E/r}$ and $B \propto r^{-3}$, as the $r^{1.5}$ integration is the core of the proof.)*

# Answer
### Part A
**[A.1's Standard Solution]**
- **[Physical Principles]**: The angular velocity of the rotating frame: $\omega = \sqrt{G M_E / r^3}$, the net radial force on a mass $m$ at distance $x$ from the CM is the sum of the gravitational force and the fictitious centrifugal force.
- **[Equations]**:
  The effective radial force is:（taking the outward direction as positive）
  $$F_{eff} = m \omega^2 (r+x) - \frac{G M_E m}{(r+x)^2} \quad (1)$$
- **[Derivation Steps]**:
  Using a first-order Taylor expansion for $x \ll r$:
  $$F_{eff} \approx m \frac{G M_E}{r^3} (r+x) - \frac{G M_E m}{r^2} \left(1 - \frac{2x}{r}\right) = \frac{G M_E m}{r^2} \left(1 + \frac{x}{r} - 1 + \frac{2x}{r}\right) = \frac{3 G M_E m x}{r^3}$$
  For the satellite at the outer end ($x = L/2$), the tension $T$ must balance this outward force. Since the tether is massless, the tension $T_N$ at the midpoint is equal to the tension at the ends.
- **[Final Result]**:
  $$T_N = \frac{3 G M_E m L}{2 r^3}$$

**[A.2's Standard Solution]**
- **[Physical Principles]**: The motional EMF is generated as the tether moves through the magnetic field $B(r)$.
- **[Equations]**:
  $$\mathcal{E} = \int_{r-L/2}^{r+L/2} v(r') B(r') dr' \quad (2)$$
- **[Derivation Steps]**:
  Substituting $v(r') = \omega r'$ and $B(r') = B_0 (R_E/r')^3$:
  $$\mathcal{E} = \int_{r-L/2}^{r+L/2} \omega r' \frac{B_0 R_E^3}{r'^3} dr' = \omega B_0 R_E^3 \left[ -\frac{1}{r'} \right]_{r-L/2}^{r+L/2} \approx \frac{\omega B_0 R_E^3 L}{r^2}$$
  Using $\omega = \sqrt{G M_E / r^3}$:
- **[Final Result]**:
  $$\mathcal{E} = B_0 R_E^3 L \sqrt{\frac{G M_E}{r^7}}$$

**[A.3's Standard Solution]**
- **[Physical Principles]**: The induced electric field is $\vec{E}_{ind} = \vec{v} \times \vec{B}$. In the Earth's equatorial plane, $\vec{v}=\vec{w}\times \vec{R}$ is along the orbital tangent(couter-clockwise in the figure) and $\vec{B}$ is directed toward the geographic North (out of the page in the figure).
- **[Derivation Steps]**:
  Using the right-hand rule, $\vec{v} \times \vec{B}$ points radially outward (away from Earth's center). Positive charges will therefore accumulate at the end further from Earth.
- **[Final Result]**:
  The satellite **farther from Earth** accumulates positive charges.

---

### Part B
**[B.1's Standard Solution]**
- **[Physical Principles]**: The Lorentz force is $d\vec{F}_L = I d\vec{l} \times \vec{B}$.
- **[Derivation Steps]**:
  The induced EMF drives a current $I$ from the lower potential (inner) to the higher potential (outer) satellite through the tether. Thus, $d\vec{l}$ is in the $+\hat{r}$ direction.
  $$\vec{F}_L = \int_{r-L/2}^{r+L/2} I (\hat{r} dr') \times (B(r') \hat{z}) =IB_{0}R_{E}^{3}(\int_{r-L/2}^{r+L/2}\frac{1}{r'^{3} }dr')(-\hat{\phi})=\frac{IB_{0}R_{E}^{3}rL}{(r^2-\frac{L^2}{4})^2}(-\hat{\phi})$$
  Since the orbital velocity $\vec{v}$ is in the $+\hat{\phi}$ direction, $\vec{F}_L$ is exactly opposite to $\vec{v}$.
- **[Final Result]**:
  Since $r\gg L$, we can ignore the $L^{2}$ term, so $\left | \vec{F} \right | \approx\frac{IB_{0}R_{E}^{3}L}{r^3}$  The total force is $\vec{F}_L \approx - I B(r) L \hat{v}$.

**[B.2's Standard Solution]**
- **[Equations]**:
  Total mechanical energy $E =\frac{1}{2}\times m\times w^2((r+\frac{L}{2})^2+(r-\frac{L}{2})^2)-\frac{GM_{E}m}{r+\frac{L}{2}}-\frac{GM_{E}m}{r-\frac{L}{2}}\approx-\frac{GM_{E}m}{r}, Power dissipated due to the work done by the Lorentz force  $P = \vec{F}_L \cdot \vec{v} = - I B L v$, where $v$ is the velocity of the tether’s center of mass. Since $r\gg L$, the Lorentz force can be evaluated using the magnetic field at the center of mass.
- **[Derivation Steps]**:
  $$\frac{dE}{dt} = \frac{dE}{dr}\times\frac{dr}{dt}=\frac{G M_E m}{r^2} \frac{dr}{dt} = - I B L \sqrt{\frac{G M_E}{r}}$$
  Solving for $dr/dt$:
- **[Final Result]**:
  $$\frac{dr}{dt} = - \frac{I B_0 R_E^3 L}{m \sqrt{G M_E} r^{3/2}}$$

**[B.3's Standard Solution]**
- **[Derivation Steps]**:
  From B.2: $I dt = -\frac{m \sqrt{G M_E} r^{3/2}}{B_0 R_E^3 L} dr$.
  $$Q = \int I dt= -\int_{r_1}^{r_2} \frac{m \sqrt{G M_E}}{(B_0 R_E^3 r^{-3}) L r^{3/2}} dr = -\frac{m \sqrt{G M_E}}{B_0 R_E^3 L} \int_{r_1}^{r_2} r^{3/2} dr$$
- **[Final Result]**:
  $$Q =\frac{2 m \sqrt{G M_E}}{5 B_0 R_E^3 L} (r_1^{5/2} - r_2^{5/2})$$

---

### Part C
**[C.1's Standard Solution]**
- **[Equations]**:
In unit time, $$\frac{I}{e}$$ electrons “escape” from the cathode, and the work required to overcome the binding is $$\frac{I\Phi}{e}$$
1. Energy balance: $I^2 R = \epsilon \sigma S T_{eq}^4 + \frac{I \Phi}{e}$
Since  $\mathcal{E}$ is sufficiently large so as not to restrict I, so I=I_{sat}. 
2. Current balance: $I=I_{sat} = \eta S A_R T_{eq}^2 \exp\left(-\frac{\Phi}{k_B T_{eq}}\right)$

**[C.2's Standard Solution]**
- **[Derivation Steps]**:
  In the limit,$I^2 R \gg I \Phi/e$, so the equation1 simplify to $I^2 R \approx \epsilon \sigma S T^4$. And use the approximate $\exp(-\Phi/k_B T) \approx 1 - \Phi/k_B T$, we get $ I \approx \eta S A_R T^2(1-\frac{\Phi}{k_{B}T})$. Solve these two equations simultaneously to obtain $I = \sqrt{\frac{\epsilon \sigma S}{R}}\left(\frac{\frac{\Phi}{k_B}}{1 - \frac{1}{\eta S A_R}\sqrt{\frac{\epsilon \sigma S}{R}}}\right)^2$, thus from B.2, $\left|\frac{dr}{dt}\right|=\frac{B_0 R_E^3 L}{m \sqrt{G M_E}\, r^{3/2}}\sqrt{\frac{\epsilon \sigma S}{R}}\left(\frac{\frac{\Phi}{k_B}}{1 - \frac{1}{\eta S A_R}\sqrt{\frac{\epsilon \sigma S}{R}}}\right)^2$.
The $\mathcal{E}$ should satisfy $\mathcal{E}> IR$,thus B(r)Lv> IR, we can eventually obtain $r_{max}=\sqrt[7]{\frac{B_{0}^2 R_{E}^6 L^2 G M_{E}}{I^2 R^2}}$, where $I = \sqrt{\frac{\epsilon \sigma S}{R}}\left(\frac{\frac{\Phi}{k_B}}{1 - \frac{1}{\eta S A_R}\sqrt{\frac{\epsilon \sigma S}{R}}}\right)^2$.


# AnswerValidation
### [Part 1: Derivation Rigor Audit]
- **Step Check**:
  - **A.1**: The solver accurately applies the gravity gradient and centrifugal force equations in the rotating frame of the center of mass. The first-order Taylor expansion over $x \ll r$ correctly yields the net outward force, seamlessly leading to the midpoint tension. 
  - **A.2**: The solver sets up the motional EMF integral correctly, incorporating the varying magnetic field $B(r')$ and Keplerian velocity $v(r')$. The first-order expansion of the integration limits correctly simplifies to the exact given expression.
  - **A.3**: The right-hand rule evaluation ($\vec{v} \times \vec{B}$) for a prograde equatorial orbit is flawlessly executed.
  - **B.1**: The physical basis for the Lorentz force is correctly identified. The solver accurately deduces the current flow direction through the tether and confirms the resulting force acts perfectly anti-parallel to the orbital velocity.
  - **B.2**: The solver leverages the mechanical work-energy theorem. It correctly implements the total mass $M_{tot} = 2m$ to define the mechanical energy $E = -GM_E m/r$ and successfully links it to the Lorentz force power dissipation. 
  - **B.3**: The differential variable exchange ($dt \to dr$) correctly accounts for the negative sign of the descent rate ($dr/dt < 0$). The mathematical integration is flawless.
  - **C.1**: The formulation correctly captures the multi-physics energy balance, isolating Joule heating ($I^2R$) against radiative cooling and the precise electron emission cooling ($I\Phi/e$). The Richardson current constraint is correctly applied.
  - **C.2**: The solver demonstrates excellent physical intuition. It recognizes that operating at the "tipping point" means the saturation current is perfectly bottlenecked by the available Ohmic current ($I = \mathcal{E}/R$). By substituting this directly into the decay equation, the solver avoids unnecessary algebraic entanglement with the thermal emission equations.

- **Logical Defect Flagging**:
  - **[Skipped Step/Logical Gap]**: None. The solver handled a potentially misleading prompt in **C.1** perfectly. While the prompt asks for equations "in terms of... and the local EMF $\mathcal{E}$", the solver correctly recognized that in a pure thermionic saturation regime, the local EMF decouples from the steady-state $T_{eq}$ and $I_{sat}$ equations (provided $\mathcal{E}$ is sufficiently large). The solver confidently wrote the correct EMF-independent equations.
  - **[Improper Approximation]**: None. All Taylor series truncations $(x/r \ll 1)$ applied in A.1 and A.2 are physically justified.
  - **[Mathematical Error]**: None.

### [Part 2: Correctness & Closure Verification]
- **Final Result Verification**:
  - **A.1**: [Verdict]: **Correct**. 
  - **A.2**: [Verdict]: **Correct**.
  - **A.3**: [Verdict]: **Correct**.
  - **B.1**: [Verdict]: **Correct**.
  - **B.2**: [Verdict]: **Correct**.
  - **B.3**: [Verdict]: **Correct**.
  - **C.1**: [Verdict]: **Correct**.
  - **C.2**: [Verdict]: **Correct**.
- **Closure Assessment**:
  All final variables strictly map to the given knowns and planetary constants. In Part **C.2**, the solver correctly excluded the parameters $S$ and $\epsilon$ from the final expression. This correctly reflects the physics of the "tipping point," where mechanical decay is entirely driven by the Ohmic circuit resistance limit rather than the localized thermal emission characteristics. No undefined intermediate variables were left behind.

### [Part 3: Physical Pressure Test]
- **Dimensional Audit**:
  - **Part B.2 Result**: $\frac{dr}{dt} \propto \frac{I B_0 R_E^3 L}{m \sqrt{G M_E} r^{3/2}}$
    - Numerator Force Dimension: $[I B L] = \text{M} \cdot \text{L} \cdot \text{T}^{-2}$
    - Denominator Dimension: $[m \sqrt{GM}/r^{3/2}] = \text{M} \cdot (\text{L}^{3/2} \text{T}^{-1}) / \text{L}^{3/2} = \text{M} \cdot \text{T}^{-1}$
    - Quotient Dimension: $(\text{M} \cdot \text{L} \cdot \text{T}^{-2}) / (\text{M} \cdot \text{T}^{-1}) = \text{L} \cdot \text{T}^{-1}$ (Velocity). **Match**.
  - **Part C.2 Result**: $|dr/dt| \propto \frac{B^2 L^2 r}{m R}$
    - Term $\mathcal{E}^2/R = [B^2 L^2 v^2 / R] = \text{Power} (\text{M} \cdot \text{L}^2 \cdot \text{T}^{-3})$
    - Manipulating to isolate decay: $(B^2 L^2 r) / (m R) \equiv (\text{M}\cdot\text{T}^{-1}) \cdot (\text{L} / \text{M}) = \text{L} \cdot \text{T}^{-1}$ (Velocity). **Match**.

- **Limit Test**:
  - **Limit 1 (Insulator Limit)**: Let $R \to \infty$. The expression in C.2 yields $|dr/dt| \to 0$. Physically, an infinite resistance prevents current flow, eliminating electrodynamic drag and halting orbital decay. This perfectly aligns with physical reality.
  - **Limit 2 (Infinite Inertia Limit)**: Let $m \to \infty$. The expression yields $|dr/dt| \to 0$. An infinitely massive system cannot undergo rapid orbital changes under a finite Lorentz force. This satisfies Keplerian expectations.

- **Conservation Law Check**:
  - **Angular Momentum Consistency**: In Part B.2, energy conservation is used. We can cross-verify this with angular momentum $L_{ang} = 2m \sqrt{G M_E r}$. The magnetic torque is $\tau = \vec{r} \times \vec{F}_L = - I B L r$. Taking the time derivative of angular momentum yields $dL_{ang}/dt = m \sqrt{G M_E / r} (dr/dt)$. Substituting the solver's $dr/dt$ exactly yields $dL_{ang}/dt = - I B L r$, matching the torque. The solution represents profound physical consistency across different mechanical frameworks.

### [Part 4: Final Verdict]
- **Rigor Score**: 10 / 10
- **Conclusion Usability**: Adopt Directly
- **Expert Opinion**: The provided Standard Solution is phenomenally robust and physically immaculate. The Solver Agent showcased high-caliber problem-solving intuition, specifically in Part C.2. By correctly assessing that the "tipping point" structurally collapses the complex thermionic constraints down to the fundamental Ohmic bottleneck ($I = \mathcal{E}/R$), the solver bypassed the "distractor" elements ($S, \epsilon$, and the Richardson approximation limit) to provide the exact, elegant answer. Both derivations and conclusions are unconditionally endorsed for formal use.

# GradingRubric
### [IPHO Official Marking Scheme]
**Total Score: 10.0 pts**

#### Part A: Orbital Dynamics and Motional EMF (Total: 3.0 pts)

| Sub-part | Item / Key Equation | Marks | Notes for Graders |
| :--- | :--- | :--- | :--- |
| **A.1** | **Effective force equation:** Setting up the net radial force in the rotating frame (gravity + centrifugal): $F_{eff} = m\omega^2(r+x) - \frac{GM_E m}{(r+x)^2}$ | 0.3 | Accept equivalent formulations using generalized coordinates or tidal force directly. |
| | **Taylor expansion:** Expanding to first-order for $x \ll r$: <br>$F_{eff} \approx \frac{GM_E m}{r^2}\left(1 + \frac{x}{r} - 1 + \frac{2x}{r}\right) = \frac{3GM_E m x}{r^3}$ | 0.4 | Award 0.2 for correctly applying $\omega^2 = GM_E/r^3$; 0.2 for the algebraic expansion. |
| | **Force balance & Tension uniformity:** Recognizing that for a massless tether, tension is uniform ($T_N = T_{end}$) and balances the force on the satellite at $x=L/2$. | 0.3 | Explicitly substituting $x = L/2$ into the force equation. |
| | **Final Result:** $T_N = \frac{3 G M_E m L}{2 r^3}$ | 0.2 | Must be positive. Dimensions must be Force. |
| **A.2** | **Motional EMF primitive equation:** $\mathcal{E} = \int_{r-L/2}^{r+L/2} v(r') B(r') dr'$ or recognizing $\mathcal{E} \approx vBL$ at CM. | 0.3 | Evaluating at the CM directly without integration is fully accepted due to $L \ll r$. |
| | **Substitution of fields:** Substituting $v = \omega r$ and $B = B_0(R_E/r)^3$. | 0.3 | |
| | **Keplerian substitution:** Using $\omega = \sqrt{GM_E/r^3}$ to eliminate $\omega$ and $v$. | 0.2 | |
| | **Final Result:** $\mathcal{E} = B_0 R_E^3 L \sqrt{\frac{G M_E}{r^7}}$ | 0.2 | **ECF:** Deduct 0.2 if the student uses the wrong power of $r$ but carried the steps correctly. **1.0 pt Total for A.2** |
| **A.3** | **Directional logic:** Applying right-hand rule for $\vec{F} = q(\vec{v} \times \vec{B})$ or $\vec{E}_{ind} = \vec{v} \times \vec{B}$. | 0.4 | Must indicate that the force on positive charges points radially outward (away from Earth). |
| | **Conclusion:** The satellite **farther from Earth** accumulates positive charges. | 0.4 | No justification/work = 0 marks for this part. **0.8 pt Total for A.3** |
| **Subtotal** | **Part A Total** | **3.0** | |

---

#### Part B: Electrodynamic Drag and Orbital Evolution (Total: 4.0 pts)

| Sub-part | Item / Key Equation | Marks | Notes for Graders |
| :--- | :--- | :--- | :--- |
| **A.1** | **Angular velocity:** $\omega = \sqrt{GM_E/r^3}$ | 0.2 | |
| | **Effective force:** $F_{eff}=m\omega^2(r+x)-\frac{GM_E m}{(r+x)^2}$ | 0.4 | Direction convention should be clear. |
| | **First-order expansion:** $F_{eff}\approx \frac{3GM_E m}{r^3}x$ | 0.1 | |
| | **Uniform tension:** Tension is uniform because $m_{tether}=0$. | 0.2 | Must state that the tether mass is neglected. |
| | **Final Result:** $T_N=\frac{3GM_E mL}{2r^3}$ | 0.3 | |
| **Subtotal** | **A.1 Total** | **1.2** | |

| Sub-part | Item / Key Equation | Marks | Notes for Graders |
| :--- | :--- | :--- | :--- |
| **A.2** | **Motional EMF:** $\mathcal{E}=\int v(r')B(r')\,dr'$ | 0.3 | |
| | **Substitution:** $v=\omega r'$, $B=B_0\left(\frac{R_E}{r'}\right)^3$ | 0.3 | |
| | **Final Result:** $\mathcal{E}=B_0R_E^3L\sqrt{\frac{GM_E}{r^7}}$ | 0.4 | Approximation steps must be shown. |
| **Subtotal** | **A.2 Total** | **1.0** | |

| Sub-part | Item / Key Equation | Marks | Notes for Graders |
| :--- | :--- | :--- | :--- |
| **A.3** | **Velocity direction:** $\vec v=\vec\omega\times\vec r$ | 0.2 | |
| | **Induced electric field:** $\vec E=\vec v\times\vec B$, directed radially outward. | 0.3 | |
| | **Conclusion:** The farther end from Earth is positively charged. | 0.3 | |
| **Subtotal** | **A.3 Total** | **0.8** | |

---

| Sub-part | Item / Key Equation | Marks | Notes for Graders |
| :--- | :--- | :--- | :--- |
| **B.1** | **Lorentz force:** $d\vec F=I(d\vec l\times\vec B)$ | 0.2 | |
| | **Total force integral:** $\vec F_L=\int I(d\vec l\times\vec B)$ | 0.3 | |
| | **Approximation:** $\vec F_L\approx -IBL$ | 0.2 | |
| | **Direction:** $\vec F_L$ is opposite to $\vec v$. | 0.3 | Clear explanation using both words and formula is accepted. |
| **Subtotal** | **B.1 Total** | **1.0** | |

| Sub-part | Item / Key Equation | Marks | Notes for Graders |
| :--- | :--- | :--- | :--- |
| **B.2** | **Orbital energy:** $E=K+U=\frac12mv^2-\frac{GM_E m}{r}\approx-\frac{GM_E m}{r}$ | 0.4 | 0.2 for writing kinetic plus potential energy; 0.2 for the approximation. |
| | **Power:** $\frac{dE}{dt}=-IBLv$ | 0.4 | |
| | **Differential relation:** $\frac{GM_E m}{r^2}\frac{dr}{dt}=-IBL\sqrt{\frac{GM_E}{r}}$ | 0.4 | If the negative sign is missing, award only half credit for this item. |
| | **Final Result:** $\frac{dr}{dt}=-\frac{IB_0R_E^3L}{m\sqrt{GM_E}r^{3/2}}$ | 0.3 | |
| **Subtotal** | **B.2 Total** | **1.5** | |

| Sub-part | Item / Key Equation | Marks | Notes for Graders |
| :--- | :--- | :--- | :--- |
| **B.3** | **Substitution:** $I\,dt=-\frac{m\sqrt{GM_E}}{B_0R_E^3L}r^{3/2}\,dr$ | 0.4 | |
| | **Charge:** $Q=\int I\,dt$ | 0.4 | |
| | **Integration:** $\int r^{3/2}dr=\frac25r^{5/2}$ | 0.4 | |
| | **Final Result:** $Q=\frac{2m\sqrt{GM_E}}{5B_0R_E^3L}(r_1^{5/2}-r_2^{5/2})$ | 0.3 | |
| **Subtotal** | **B.3 Total** | **1.5** | |

---

| Sub-part | Item / Key Equation | Marks | Notes for Graders |
| :--- | :--- | :--- | :--- |
| **C.1** | **Emission power:** Energy per unit time is $\frac{I\Phi}{e}$ | 0.2 | |
| | **Energy balance:** $I^2R=\epsilon\sigma ST^4+\frac{I\Phi}{e}$ | 0.4 | If this equation is correct, it may cover the previous item. |
| | **Saturation current condition:** $I=I_{sat}$ | 0.2 | |
| | **Emission current:** $I=\eta S A_RT^2\exp\left(-\frac{\Phi}{k_BT}\right)$ | 0.4 | |
| **Subtotal** | **C.1 Total** | **1.2** | |

| Sub-part | Item / Key Equation | Marks | Notes for Graders |
| :--- | :--- | :--- | :--- |
| **C.2** | **Approximate equations:** $I^2R\approx\epsilon\sigma ST^4$ and $I\approx\eta S A_RT^2\left(1-\frac{\Phi}{k_BT}\right)$ | 0.6 | 0.3 for each equation. |
| | **Current expression:** $I=\sqrt{\frac{\epsilon\sigma S}{R}}\left[\frac{\Phi/k_B}{1-\frac{1}{\eta S A_R}\sqrt{\frac{\epsilon\sigma S}{R}}}\right]^2$ | 0.2 | |
| | **Decay rate:** $\frac{dr}{dt}=\frac{B_0R_E^3L}{m\sqrt{GM_E}r^{3/2}}I$ | 0.3 | |
| | **Condition:** $\mathcal{E}>IR$, or $B(r)Lv>IR$ | 0.4 | |
| | **Maximum radius:** $r_{max}=\left(\frac{B_0^2R_E^6L^2GM_E}{I^2R^2}\right)^{1/7}$ | 0.3 | Full substitution of $I$ is not required. |
| **Subtotal** | **C.2 Total** | **1.8** | |

---

#### Part C: Electro-Thermal Limits and Asymptotic Evolution (Total: 3.0 pts)

| Sub-part | Item / Key Equation | Marks | Notes for Graders |
| :--- | :--- | :--- | :--- |
| **C.1** | **Joule Heating & Radiation:** Identifying $P_{in} = I^2 R$ and thermal radiation $P_{rad} = \epsilon \sigma S T_{eq}^4$. | 0.4 | 0.2 pts for each term. |
| | **Emission Cooling:** Identifying power carried away by electrons is $P_{emit} = I \frac{\Phi}{e}$. | 0.2 | Setting up full balance: $I^2 R = \epsilon \sigma S T_{eq}^4 + I \frac{\Phi}{e}$ |
| | **Richardson's Law:** Current balance $I_{sat} = \eta S A_R T_{eq}^2 \exp\left(-\frac{\Phi}{k_B T_{eq}}\right)$ | 0.4 | |
| | **System closure:** Stating $I = I_{sat}$ and explicitly writing the self-consistent coupled equations. | 0.2 | Both equations must be cleanly presented to get this mark. <br>**1.2 pts Total for C.1** |
| **C.2** | **Tipping Point Identification:** Recognizing that if limited by the available EMF, the current simply obeys Ohm's Law: $I = \frac{\mathcal{E}}{R}$. | 0.4 | Do not penalize if the student also attempts to solve $T_{eq}$ (extraneous work). |
| | **Using local EMF:** Substituting $\mathcal{E} = v B L$ so $I = \frac{v B L}{R}$. | 0.4 | |
| | **Substitution into Decay Rate:** Substituting this $I$ into the formula for $|dr/dt|$ derived in B.2: $\|dr/dt\| = \frac{(vBL/R) B L}{m \sqrt{GM_E} r^{-3/2}}$ | 0.5 | **ECF:** Must use their expression from B.2. |
| | **Final Simplification:** Using $v = \sqrt{\frac{GM_E}{r}}$ to simplify to final form: $\|dr/dt\| = \frac{B^2 L^2 r}{m R}$ | 0.5 | Result must be strictly in terms of allowable constants/variables ($B, L, r, m, R$). <br>**1.8 pts Total for C.2** |
| **Subtotal** | **Part C Total** | **3.0** | |

---

### [Grading Notes & Pitfalls]

1.  **Allowed Errors & Extraneous Work**:
    -   In **A.2**, technically the velocity and magnetic field vary along the tether. Integrating from $r-L/2$ to $r+L/2$ yields the exact same first-order term as simply multiplying the center-of-mass values ($\mathcal{E} = v_{cm} B_{cm} L$). Both methods are perfectly acceptable and receive full marks.
    -   In **C.2**, the problem describes asymptotic simplifications to Richardson's Law ($\exp(-x) \approx 1-x$). This is a distracter designed to simulate realistic noisy research environments. If a student bypasses this and directly uses the tipping point constraint $I = \mathcal{E}/R$, award full marks. No penalty for extraneous algebraic struggles with $T_{eq}$ as long as the final $dr/dt$ expression is isolated correctly.

2.  **Common Mistakes and Deductions**:
    -   **Fatal Errors (Model Collapse - No ECF):**
        -   In **B.3**, if a student's prior derivations lead to a differential equation where $I$ does *not* cancel out analytically, they cannot complete the proof. Subsequent steps in B.3 receive **0 marks**.
        -   **Dimensional inconsistency** in any final boxed answer results in **0 marks** for that specific "Final Result" sub-item. (e.g., if A.1 tension does not have dimensions of Newtons).
    -   **Minor Errors (Deduct 0.2 - 0.4):**
        -   **Mass factor trap in B.2:** There are *two* satellites of mass $m$. Total mass $M_{tot} = 2m$. If a student uses $M_{tot} = m$, deduct **0.2 pts** in B.2. ECF applies to B.3 and C.2 without further penalties.
        -   **Sign errors:** In B.2, orbital decay means $dr/dt < 0$. If they lose the negative sign but claim it is decay, deduct **0.2 pts**. In C.2, absolute value is requested ($|dr/dt|$), so the final result must be strictly positive.

3.  **Notes on Alternative Solutions**:
    -   **A.1 Tidal Force Method:** Students may bypass the rotating frame entirely and use the tidal force gradient $\Delta F_g \approx \frac{2GM_E m}{r^3} \Delta r$ plus the differential centrifugal force $\Delta F_c \approx m\omega^2 \Delta r$. Summing these explicitly to get $\frac{3GM_Em \Delta r}{r^3}$ is mathematically identical and receives full physical principle marks.
    -   **B.2 Angular Momentum Method:** Instead of Energy ($E$), students may use Angular Momentum ($L_{ang} = 2mvr = 2m\sqrt{GM_E r}$) and set the rate of change equal to the external magnetic torque ($\tau = -I B L r$). This is an elegant alternative. Award 0.4 for $L_{ang}$, 0.4 for torque, 0.4 for taking the derivative, and 0.3 for the final result.

![](image/ipho_2025_1_1.png)

# DiagramCode
### [1] Visual Strategy Plan

**Total number of charts to generate: 2**

**Figure 1: Orbital Configuration and Electrodynamic Induction**
- **Insertion Location**: After the introductory section, immediately before **Part A**.
- **Drawing Content and Colors**: 
    - **Global View**: A segment of the Earth (light blue) with a dashed line representing the circular orbital path.
    - **Tether System**: Two small satellites (dark grey circles) connected by a solid line (tether). The system is oriented radially (pointing toward the Earth's center).
    - **Vectors**: Orbital velocity $\vec{v}$ (blue arrow, tangential), Magnetic field $\vec{B}$ (green circles with dots $\odot$ representing a field pointing out of the orbital plane), and the radial distance $r$.
    - **Physical Metaphor**: Use a coordinate frame $(r, \theta)$ to show the "gravity gradient" stabilization.
- **Core Symbols**: $R_E$, $r$, $L$, $\vec{v}$, $\vec{B}$, $m$.

**Figure 2: Electrodynamic Forces and Plasma Circuit Model**
- **Insertion Location**: After the transitional text of **Part B**, before sub-question **B.1**.
- **Drawing Content and Colors**:
    - **Local View**: A zoomed-in view of the tether.
    - **Current & Force**: A red arrow along the tether representing the current $I$. A bold orange arrow representing the total Lorentz force $\vec{F}_L$ acting opposite to the velocity $\vec{v}$.
    - **Circuit**: A dashed light-blue loop representing the "return path" through the ionospheric plasma.
    - **Thermal Aspect**: Small wavy purple arrows emanating from the tether to represent thermal radiation ($P_{rad}$), linking to the concepts in Part C.
- **Core Symbols**: $I$, $\vec{F}_L$, $\vec{v}$, $P_{rad}$, Cathode, Anode.

---

### [2] Integrated Python Script

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
plt.rcParams.update({
    "text.usetex": False,
    "mathtext.fontset": "cm",
    "font.family": "serif",
    "font.size": 11
})

def generate_figure_1():
    fig, ax = plt.subplots(figsize=(7, 6))
    ax.set_aspect('equal')
    ax.axis('off')

    earth = patches.Circle((0, 0), 2.0, color='#AADDFF', ec='#5588AA', lw=2)
    ax.add_patch(earth)
    ax.text(0, 0, r'Earth ($M_E$)', ha='center', va='center', fontsize=12, fontweight='bold')
    orbit_r = 5.0
    orbit_arc = patches.Arc((0, 0), 2*orbit_r, 2*orbit_r,
                            theta1=20, theta2=70,
                            ls='--', color='gray', alpha=0.6)
    ax.add_patch(orbit_arc)
    angle = np.deg2rad(45)
    r1, r2 = orbit_r - 0.6, orbit_r + 0.6
    x1, y1 = r1*np.cos(angle), r1*np.sin(angle)
    x2, y2 = r2*np.cos(angle), r2*np.sin(angle)

    ax.plot([x1, x2], [y1, y2], color='black', lw=2)
    ax.scatter([x1, x2], [y1, y2], color='#444444', s=80)

    ax.text(x1-0.2, y1-0.4, r'$m$')
    ax.text(x2+0.2, y2+0.3, r'$m$')

    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='<->'))
    ax.text((x1+x2)/2 + 0.3, (y1+y2)/2, r'$L$')

    ax.annotate('', xy=(x1, y1), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', ls=':'))
    ax.text(1.2, 2.2, r'$r$')
    v_dir = np.array([-np.sin(angle), np.cos(angle)])
    v_start = np.array([(x1+x2)/2, (y1+y2)/2])
    ax.quiver(v_start[0], v_start[1], v_dir[0], v_dir[1],
              color='blue', scale=4, width=0.015)
    ax.text(v_start[0]-1.0, v_start[1]+0.2,
            r'$\vec{v}$', color='blue', fontsize=18)
    for i in range(3):
        for j in range(3):
            ax.text(3.5+i*0.8, 0.5+j*0.8, r'$\odot$',
                    color='forestgreen', ha='center')

    ax.text(5.5, 1.5, r'$\vec{B}$', color='forestgreen')

    plt.title("Fig 1: EDT Orbital Configuration")
    plt.tight_layout()
    plt.savefig("Figure_1.png", dpi=300)
    plt.close()
    print("Figure_1.png generated successfully.")

def generate_figure_2():
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.set_aspect('equal')
    ax.axis('off')

    ax.plot([0, 0], [-2, 2], color='black', lw=3)
    ax.scatter([0, 0], [-2, 2], color='#444444', s=150)
    ax.text(0.3, 2, 'Upper Sat (Anode)', va='center')
    ax.text(0.3, -2, 'Lower Sat (Cathode)', va='center')

    ax.annotate('', xy=(0, 0.6), xytext=(0, -0.6),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(-0.35, 0, r'$I$', color='red', fontsize=14)

    ax.quiver(0, 0, 1.4, 0, color='blue', scale=5, width=0.02)
    ax.text(0.6, 0.35, r"$\vec{F}_L$", color='blue', fontsize=14)

    ax.text(-1.35, 0.32, r"$\vec{v}$", color='black', fontsize=14)
    ax.annotate(
        '',
        xy=(-1.55, 0.08),
        xytext=(-0.45, 0.08),
        arrowprops=dict(arrowstyle='->', color='black', lw=1.5)
    )

    ax.annotate(
        '',
        xy=(-0.45, -0.2),
        xytext=(-1.55, -0.2),
        arrowprops=dict(arrowstyle='->', color='black', lw=1.5)
    )

    theta = np.linspace(-np.pi/2, np.pi/2, 50)
    ax.plot(1.5*np.cos(theta), 2*np.sin(theta),
            color='skyblue', ls='--')
    ax.text(1.6, 0, 'Plasma Path', color='skyblue')

    for y in [1.2, 0.2, -0.8]:
        ax.annotate('',
                    xy=(1.0, y-0.5),
                    xytext=(1.0, y+0.2),
                    arrowprops=dict(arrowstyle='->',
                                    connectionstyle="arc3,rad=-0.25",
                                    color='red'))

    ax.text(0.5, -1.8, r'$P_{rad} \propto T^4$', color='red')
    ax.text(-1.5, 2, r'$\vec{B} = \odot$', color='forestgreen')

    plt.title("Fig 2: Forces and Circuit")
    plt.tight_layout()
    plt.savefig("Figure_2.png", dpi=300)
    plt.close()
    print("Figure_2.png generated successfully.")

if __name__ == "__main__":
    generate_figure_1()
    generate_figure_2()
    print("All figures generated for IPhO Problem 1.")
```

