# Practice with T-Tests: Customer Satisfaction Analysis Using DBA 710 Multiple Stores Dataset

## Introduction

This forum post presents the results of independent samples t-tests conducted using the "DBA 710 Multiple Stores.sav" dataset to examine customer satisfaction differences across various operational characteristics. The analysis follows rigorous statistical methodology to provide evidence-based insights for business decision-making.

## 2a. Statistical Analysis Conducted

Two independent samples t-tests were performed using the customer satisfaction scores (CUSTSCORE) as the dependent variable:

1. **Test 1**: Customer satisfaction differences between corporate-owned vs. franchise-owned facilities
2. **Test 2**: Customer satisfaction differences between urban vs. rural store settings

The analysis utilized Python with statistical libraries (scipy.stats) to replicate SPSS functionality, ensuring appropriate assumption testing including Levene's test for equal variances.

## 2b. Statistical Results

### Test 1: Customer Satisfaction by Ownership Type (Corporate vs. Franchise)

**Descriptive Statistics:**
- Corporate Stores: Mean = 25.56, SD = 4.20, n = 295
- Franchise Stores: Mean = 24.77, SD = 3.78, n = 574

**Assumption Testing:**
- Levene's Test for Equal Variances: F = 4.614, p = 0.032
- Equal variances **not** assumed (p < 0.05)

**Independent Samples T-Test Results:**
- t-statistic = 2.696
- degrees of freedom = 867
- p-value = 0.007
- Cohen's d (effect size) = 0.200

### Test 2: Customer Satisfaction by Store Setting (Urban vs. Rural)

**Descriptive Statistics:**
- Urban Stores: Mean = 27.19, SD = 2.90, n = 473
- Rural Stores: Mean = 22.47, SD = 3.46, n = 396

**Assumption Testing:**
- Levene's Test for Equal Variances: F = 0.994, p = 0.319
- Equal variances assumed (p > 0.05)

**Independent Samples T-Test Results:**
- t-statistic = 21.870
- degrees of freedom = 867
- p-value < 0.001
- Cohen's d (effect size) = 1.490

## 2c. Interpretation of Results

### Test 1: Ownership Type Analysis

The independent samples t-test revealed a **statistically significant difference** in customer satisfaction scores between corporate-owned and franchise-owned facilities, t(867) = 2.696, p = 0.007. Corporate-owned stores demonstrated higher customer satisfaction (M = 25.56, SD = 4.20) compared to franchise-owned stores (M = 24.77, SD = 3.78).

However, the effect size is small (Cohen's d = 0.200), suggesting that while the difference is statistically significant, the practical significance may be limited. This difference represents approximately a 3.2% higher satisfaction score for corporate stores.

**Business Implications:** Corporate ownership may provide better quality control mechanisms, standardized procedures, or resource allocation that contribute to slightly higher customer satisfaction. Organizations should investigate the operational differences that drive this advantage.

### Test 2: Store Setting Analysis

The analysis revealed a **highly statistically significant difference** in customer satisfaction between urban and rural store locations, t(867) = 21.870, p < 0.001. Urban stores showed substantially higher customer satisfaction (M = 27.19, SD = 2.90) compared to rural stores (M = 22.47, SD = 3.46).

The effect size is large (Cohen's d = 1.490), indicating both statistical and practical significance. Urban stores achieve approximately 21% higher customer satisfaction scores than rural locations.

**Business Implications:** This substantial difference suggests significant operational, demographic, or infrastructural factors that impact customer experience. Urban locations may benefit from better access to resources, higher customer expectations driving service excellence, or demographic differences in satisfaction reporting patterns.

## Statistical Methodology Notes

Both analyses followed appropriate statistical procedures:
- Independence assumption met (different stores)
- Normality assessed through large sample size (Central Limit Theorem applies)
- Homogeneity of variance tested using Levene's test
- Effect sizes calculated using Cohen's d for practical significance assessment
- Two-tailed tests used with α = 0.05 significance level

## Conclusions

The statistical analysis provides evidence-based insights for strategic decision-making:

1. **Ownership Structure**: Corporate stores achieve modestly higher customer satisfaction, warranting investigation into operational practices that could be standardized across franchise operations.

2. **Geographic Strategy**: The substantial urban-rural satisfaction gap represents a critical business challenge requiring targeted intervention strategies for rural locations or reevaluation of service delivery models.

These findings support data-driven decision-making processes and highlight areas for operational improvement and strategic focus.

---

## References

Field, A. (2018). *Discovering statistics using IBM SPSS Statistics* (5th ed.). SAGE Publications.

Hair, J. F., Black, W. C., Babin, B. J., & Anderson, R. E. (2019). *Multivariate data analysis* (8th ed.). Cengage Learning.

Pallant, J. (2020). *SPSS survival manual: A step by step guide to data analysis using IBM SPSS* (7th ed.). McGraw-Hill Education.

---

*Analysis conducted using Python statistical libraries (scipy.stats, pandas) following SPSS statistical methodology standards. Dataset: DBA 710 Multiple Stores.sav (N = 869).*
