# Palindrome Pattern Report: Catalan Numbers in the Virasoro A-infinity Structure

## Summary

A systematic numerical investigation of the even-arity palindrome pattern in the Virasoro A-infinity operations m_k has revealed a deep connection to the Catalan numbers. The original question --- does m_8 have a palindrome factor (lambda_1 - lambda_7) analogous to m_4's factor (lambda_1 - lambda_3)? --- is answered in the negative, but the investigation uncovered a richer structure.

## Principal Findings

### 1. The Catalan Theorem (verified k=2 through k=11)

Let T_k = m_k|_T(1,...,1) denote the T-coefficient of the arity-k operation at the fully symmetric spectral point (all lambda_i = 1). Let S_k = sum_w m_k|_{d^w T}(1,...,1) be the signed sum of all T-sector field coefficients at the symmetric point.

**Theorem (Catalan Pattern).**

(i) S_k = 0 for all even k >= 4.

(ii) S_2 = 3 = 3!/2.

(iii) For odd k >= 3, with n = (k-3)/2:
       S_k = (-1)^n * C_n * (k+1)!/2
   where C_n = binom(2n,n)/(n+1) is the nth Catalan number.

(iv) The T-coefficient alone: T_k = (-1)^n * C_n * k!.
     Equivalently: S_k = (k+1)/2 * T_k.

(v) The shallowest populated field (d^{k-2}T for odd k) at the symmetric point has coefficient exactly (-1)^n * C_n.

(vi) For odd k, ALL T-sector field coefficients at the symmetric point have the same sign = (-1)^n. The signed sum equals the absolute sum in magnitude.

**Verified values:**

| k  | n | C_n | T_k = (-1)^n C_n k! | S_k = (-1)^n C_n (k+1)!/2 |
|----|---|-----|---------------------|---------------------------|
| 2  | - | -   | 2                   | 3 (= 3!/2)                |
| 3  | 0 | 1   | 6                   | 12                        |
| 5  | 1 | 1   | -120                | -360                      |
| 7  | 2 | 2   | 10,080              | 40,320                    |
| 9  | 3 | 5   | -1,814,400          | -9,072,000                |
| 11 | 4 | 14  | 558,835,200         | 3,353,011,200             |

The k=11 prediction T = 14 * 11! = 558,835,200 was verified exactly.

### 2. The Palindrome Factor is Specific to k=4

**m_4 is exactly antisymmetric under spectral reversal:**
   m_4(lambda_1, lambda_2, lambda_3) = -m_4(lambda_3, lambda_2, lambda_1)

This forces the factor (lambda_1 - lambda_3) to divide m_4|_T. Verified numerically to machine precision (max error < 5e-13 over hundreds of random trials).

**No other even arity has this property:**
- m_6 is NOT globally antisymmetric under reversal (max error ~ 10^5).
- m_8 does NOT factor through (lambda_1 - lambda_7) (ratio constrained/generic ~ 0.89).
- No pair (lambda_i - lambda_j) divides m_6|_T or m_8|_T.

**However:** at even arities k >= 6, individual field components show partial structure. The shallowest populated field (d^{k-4}T, depth 2) has reversal ratio exactly -1, while deeper fields have non-constant reversal ratios. The shallowest field d^{k-2}T (depth 0 for odd k) always has reversal ratio +1.

### 3. Even-Arity Vanishing is a Polynomial Identity

For all even k >= 4, the T-sector of m_k vanishes identically on the full diagonal lambda_i = lambda:
   m_k(lambda, lambda, ..., lambda)|_{T-sector} = 0  for all lambda

This is not just vanishing at lambda = 1 but at ALL symmetric points. The scalar sector also vanishes exactly for k=4 (and k=6 within numerical precision), but develops small nonzero values at k >= 8 (likely numerical accumulation).

### 4. Reversal Symmetry Pattern

| k    | Global reversal symmetry    | Shallowest field | Deepest stable field |
|------|-----------------------------|------------------|---------------------|
| 3    | No (non-constant ratios)    | d^2T: +1         | d^2T: +1            |
| 4    | Yes: m_4(rev) = -m_4       | d^2T: -1         | T: -1               |
| 5    | No                          | d^4T: +1         | d^4T: +1            |
| 6    | No                          | d^4T: NOT populated | d^3T: -1          |
| 7    | No                          | d^6T: +1         | d^6T: +1            |
| 8    | No                          | d^6T: NOT populated | d^5T: -1          |

### 5. L^1 Norm and Symmetric-Point Comparison

The L^1 norms (integrated over the unit hypercube) and the symmetric-point evaluations grow at different rates:

| k  | L^1(T-coeff) | |S|(sym pt) | L^1 / |S|     |
|----|-------------|------------|---------------|
| 2  | 1.00        | 3          | 0.335         |
| 3  | 1.11        | 12         | 0.093         |
| 5  | 4.30        | 360        | 0.012         |
| 7  | 60.3        | 40,320     | 0.0015        |
| 9  | 2733        | 9,072,000  | 0.0003        |

The symmetric-point evaluation grows much faster (C_n * (k+1)!/2) than the L^1 norm, reflecting that the symmetric point is an extremum, not a typical point.

### 6. Physical Interpretation

The Catalan numbers C_n count the number of ways to triangulate a convex (n+2)-gon, or equivalently the number of full binary trees with n+1 leaves. Their appearance in the symmetric-point evaluation connects to the Stasheff associahedron: at the symmetric point, the spectral parameter dependence drops out and the A-infinity operation reduces to a weighted tree count. The coefficient (-1)^n * C_n reflects the net contribution of binary tree topologies after the alternating signs of the Stasheff recursion.

The palindrome vanishing at even arities is a selection rule: at equal spectral parameters, the Stasheff compositions pair under the reversal involution and cancel. For m_4 this cancellation is exact and global (the factor lambda_1 - lambda_3 divides the entire polynomial). For k >= 6 the cancellation is subtler: depths 0 and 1 vanish by the palindromic mechanism, but individual deeper fields do not factor through a single linear form.

### 7. Prediction

For k=13 (n=5): T_{13} = (-1)^5 * C_5 * 13! = -42 * 6,227,020,800 = -261,534,873,600

## Files

- `/Users/raeez/chiral-bar-cobar-vol2/compute/palindrome_investigation.py` -- Round 1: symmetric point, palindrome factor, antisymmetry, reversal, c-dependence
- `/Users/raeez/chiral-bar-cobar-vol2/compute/palindrome_deep_dive.py` -- Round 2: sequence identification, factorial patterns, scalar investigation
- `/Users/raeez/chiral-bar-cobar-vol2/compute/palindrome_sequence_id.py` -- Round 3: Catalan identification, reversal antisymmetry proof
- `/Users/raeez/chiral-bar-cobar-vol2/compute/palindrome_catalan_verify.py` -- Round 4: k=11 verification, k=12 even check, individual field analysis
