# Pearson Correlation Analysis of Retail Electronics Store Performance Variables

**Author:** Fabio Correa
**Course:** DBA 710 - Applied Business Research and Statistics
**Date:** July 29, 2025

## Abstract

This study examines relationships between building age, customer satisfaction, and return on investment across 869 retail electronics stores using Pearson correlation analysis. Results reveal a strong positive correlation between customer satisfaction and ROI (r = 0.637), explaining 40.6% of financial performance variance. Building age demonstrates opposing effects: positive correlation with customer satisfaction (r = 0.274) but negative correlation with ROI (r = -0.193). These findings support customer experience investments while highlighting facility management trade-offs. The analysis also demonstrates methodological limitations of correlation approaches for survey-based doctoral research, supporting the adoption of Structural Equation Modeling for complex organizational studies with non-normal Likert scale data.

## Introduction

Correlation analysis serves as a fundamental statistical technique for understanding relationships between continuous variables in business research (Field, 2018). In the retail electronics industry, understanding the interrelationships between operational metrics such as customer satisfaction, financial performance, and facility characteristics is crucial for strategic decision-making (Anderson & Sullivan, 1993; Fornell et al., 1996). Research has consistently demonstrated that customer satisfaction metrics serve as key predictors of financial performance across various retail contexts (Gupta & Zeithaml, 2006; Kumar et al., 2010).

This analysis investigates the correlations between three key performance indicators across 869 retail locations: building age (BLDGAGE), customer satisfaction scores (CUSTSCORE), and return on investment scores (ROISCORE). Understanding these relationships is particularly important in the retail electronics sector, where rapid technological changes and evolving consumer preferences create complex operational challenges (Grewal et al., 2017).

### Research Hypotheses

Based on service-profit chain theory and facility management literature, three specific hypotheses guide this analysis:

**H1:** Customer satisfaction scores will demonstrate a positive correlation with return on investment scores, supporting the service-profit chain model that links customer experience to financial performance (Heskett et al., 1994).

**H2:** Building age will demonstrate a negative correlation with customer satisfaction scores, as newer facilities typically provide enhanced customer experiences through modern amenities and layouts (Jones et al., 2010).

**H3:** Building age will demonstrate a negative correlation with return on investment scores, as newer facilities offer operational efficiencies that translate to better financial performance (Rondeau et al., 2012).

These hypotheses will be tested through Pearson correlation analysis to quantify relationship strength and direction, informing operational strategies and facility management decisions.

## Methodology

### Data Source and Variables

The analysis utilized data from 869 retail electronics stores with three continuous variables:

- **BLDGAGE**: Building age in years (continuous scale variable)
- **CUSTSCORE**: Customer satisfaction score ranging from 1-100 (continuous scale variable)
- **ROISCORE**: Return on investment score ranging from 1-100 (continuous scale variable)

### Statistical Analysis

Pearson product-moment correlation coefficients were calculated using SPSS-equivalent procedures in Python with the pyreadstat library for metadata preservation (Tabachnick & Fidell, 2019). The correlation matrix examined all pairwise relationships between the three variables. Pearson correlation is appropriate for continuous variables that meet assumptions of linearity, normality, and homoscedasticity (Hair et al., 2019). Correlation coefficients were interpreted using Cohen's (1988) guidelines:

- Small effect: r = 0.10 to 0.29
- Medium effect: r = 0.30 to 0.49
- Large effect: r = 0.50 to 1.0

Statistical significance was evaluated at α = 0.05, with effect sizes reported regardless of statistical significance to address the distinction between statistical and practical significance (Sullivan & Feinn, 2012).

## Results

### Pearson Correlation Matrix

The correlation analysis yielded the following results:

**Table 1: Pearson Correlation Matrix**

|           | BLDGAGE | CUSTSCORE | ROISCORE |
|-----------|---------|-----------|----------|
| BLDGAGE   | 1.000   | 0.274     | -0.193   |
| CUSTSCORE | 0.274   | 1.000     | 0.637    |
| ROISCORE  | -0.193  | 0.637     | 1.000    |

**Note:** All correlations significant at p < 0.001 level (N = 869)

### Key Findings

1. **Customer Satisfaction-ROI (r = 0.637)**: Strong positive correlation supports H1, confirming that stores with higher customer satisfaction achieve better financial performance, validating service-profit chain theory (Heskett et al., 1994; Rust & Zahorik, 1993).

2. **Building Age-Customer Satisfaction (r = 0.274)**: Weak positive correlation contradicts H2, suggesting established locations may benefit from familiarity or renovations rather than newer facilities driving satisfaction (Jones et al., 2010).

3. **Building Age-ROI (r = -0.193)**: Weak negative correlation supports H3, confirming that newer buildings achieve better financial performance through modern efficiency features (Rondeau et al., 2012).

## Statistical Interpretation

The customer satisfaction-ROI correlation (r = 0.637) supports service-profit chain theory, with customer satisfaction explaining 40.6% of ROI variance (Heskett et al., 1994; Szymanski & Henard, 2001). Building age creates a strategic tension: established locations benefit customer satisfaction while newer facilities optimize operational efficiency (Bitner, 1992; Nourse & Roulac, 1993). This pattern suggests facility management requires balanced approaches considering both customer experience and operational performance (Baron & Kenny, 1986).

## Application to Doctoral Research

While Pearson correlation provides valuable insights for continuous variables, doctoral research requires more robust approaches due to critical limitations:

**Likert Scale Issues:** 5-point Likert scales violate normality assumptions through ceiling/floor effects and ordinal properties, creating biased correlation estimates (Norman, 2010; Jamieson, 2004; Rhemtulla et al., 2012).

**Multicollinearity Concerns:** Organizational research involves intercorrelated constructs that compromise pairwise correlation interpretability and create unstable parameter estimates (Kline, 2016; Podsakoff et al., 2003).

### Structural Equation Modeling for Doctoral Research

My doctoral research will employ SEM to address correlation analysis limitations:

**Key SEM Advantages:**
- Handles non-normal 5-point Likert data through robust estimators (MLR, WLSMV) (Finney & DiStefano, 2013; Li, 2016)
- Models latent constructs while accounting for measurement error (Kline, 2016)
- Tests complex relationships including mediation and moderation effects (Byrne, 2016)
- Provides comprehensive model fit evaluation (CFI, TLI, RMSEA) (Hu & Bentler, 1999)

**Technical Solutions:**
- Polychoric correlations for categorical data (Flora & Curran, 2004)
- Robust standard errors for normality violations (Satorra & Bentler, 2001)
- Bootstrap confidence intervals for distribution-free inference (Nevitt & Hancock, 2001)

## Conclusion

This correlation analysis of 869 retail electronics stores reveals three key relationships with distinct practical and methodological implications.

H1 was strongly supported: customer satisfaction and ROI demonstrate a robust positive correlation (r = 0.637), providing clear evidence for customer experience investments. H2 was rejected: building age shows a positive rather than negative correlation with customer satisfaction (r = 0.274), suggesting established location benefits outweigh modernization advantages. H3 was supported: building age negatively correlates with ROI (r = -0.193), confirming newer facility operational advantages.

For doctoral research, these findings highlight correlation analysis limitations with Likert scale data, supporting the adoption of Structural Equation Modeling for complex organizational studies. The methodological progression from correlation to SEM represents best practice for handling non-normal survey data while enabling comprehensive model evaluation.

These results provide evidence-based guidance for retail facility management and demonstrate the value of correlation analysis as a foundation for advanced statistical approaches in business research.

## References

Anderson, E. W., & Sullivan, M. W. (1993). The antecedents and consequences of customer satisfaction for firms. *Marketing Science*, 12(2), 125-143. https://doi.org/10.1287/mksc.12.2.125

Baron, R. M., & Kenny, D. A. (1986). The moderator-mediator variable distinction in social psychological research: Conceptual, strategic, and statistical considerations. *Journal of Personality and Social Psychology*, 51(6), 1173-1182. https://doi.org/10.1037/0022-3514.51.6.1173

Bitner, M. J. (1992). Servicescapes: The impact of physical surroundings on customers and employees. *Journal of Marketing*, 56(2), 57-71. https://doi.org/10.1177/002224299205600205

Byrne, B. M. (2016). *Structural equation modeling with AMOS: Basic concepts, applications, and programming* (3rd ed.). Routledge.

Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). Lawrence Erlbaum Associates.

Field, A. (2018). *Discovering statistics using IBM SPSS statistics* (5th ed.). SAGE Publications.

Finney, S. J., & DiStefano, C. (2013). Nonnormal and categorical data in structural equation modeling. In G. R. Hancock & R. O. Mueller (Eds.), *Structural equation modeling: A second course* (2nd ed., pp. 439-492). Information Age Publishing.

Flora, D. B., & Curran, P. J. (2004). An empirical evaluation of alternative methods of estimation for confirmatory factor analysis with ordinal data. *Psychological Methods*, 9(4), 466-491. https://doi.org/10.1037/1082-989X.9.4.466

Fornell, C., Johnson, M. D., Anderson, E. W., Cha, J., & Bryant, B. E. (1996). The American customer satisfaction index: Nature, purpose, and findings. *Journal of Marketing*, 60(4), 7-18. https://doi.org/10.1177/002224299606000403

Grewal, D., Roggeveen, A. L., & Nordfält, J. (2017). The future of retailing. *Journal of Retailing*, 93(1), 1-6. https://doi.org/10.1016/j.jretai.2016.12.008

Gupta, S., & Zeithaml, V. (2006). Customer metrics and their impact on financial performance. *Marketing Science*, 25(6), 718-739. https://doi.org/10.1287/mksc.1060.0221

Hair, J. F., Black, W. C., Babin, B. J., & Anderson, R. E. (2019). *Multivariate data analysis* (8th ed.). Cengage Learning.

Heskett, J. L., Jones, T. O., Loveman, G. W., Sasser, W. E., & Schlesinger, L. A. (1994). Putting the service-profit chain to work. *Harvard Business Review*, 72(2), 164-174.

Hu, L. T., & Bentler, P. M. (1999). Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives. *Structural Equation Modeling*, 6(1), 1-55. https://doi.org/10.1080/10705519909540118

Jamieson, S. (2004). Likert scales: How to (ab)use them. *Medical Education*, 38(12), 1217-1218. https://doi.org/10.1111/j.1365-2929.2004.02012.x

Jones, P., Clarke-Hill, C., Comfort, D., & Hillier, D. (2010). Retail experience stores: Experiencing the brand at first hand. *Marketing Intelligence & Planning*, 28(3), 241-248. https://doi.org/10.1108/02634501011041408

Kline, R. B. (2016). *Principles and practice of structural equation modeling* (4th ed.). Guilford Press.

Kumar, V., Aksoy, L., Donkers, B., Venkatesan, R., Wiesel, T., & Tillmanns, S. (2010). Undervalued or overvalued customers: Capturing total customer engagement value. *Journal of Service Research*, 13(3), 297-310. https://doi.org/10.1177/1094670510375602

Li, C. H. (2016). Confirmatory factor analysis with ordinal data: Comparing robust maximum likelihood and diagonally weighted least squares. *Behavior Research Methods*, 48(3), 936-949. https://doi.org/10.3758/s13428-015-0619-7

Nevitt, J., & Hancock, G. R. (2001). Performance of bootstrapping approaches to model test statistics and parameter standard error estimation in structural equation modeling. *Structural Equation Modeling*, 8(3), 353-377. https://doi.org/10.1207/S15328007SEM0803_2

Norman, G. (2010). Likert scales, levels of measurement and the "laws" of statistics. *Advances in Health Sciences Education*, 15(5), 625-632. https://doi.org/10.1007/s10459-010-9222-y

Nourse, H. O., & Roulac, S. E. (1993). Linking real estate decisions to corporate strategy. *Journal of Real Estate Research*, 8(4), 475-494. https://doi.org/10.1080/10835547.1993.12090720

Podsakoff, P. M., MacKenzie, S. B., Lee, J. Y., & Podsakoff, N. P. (2003). Common method biases in behavioral research: A critical review of the literature and recommended remedies. *Journal of Applied Psychology*, 88(5), 879-903. https://doi.org/10.1037/0021-9010.88.5.879

Rhemtulla, M., Brosseau-Liard, P. É., & Savalei, V. (2012). When can categorical variables be treated as continuous? A comparison of robust continuous and categorical SEM estimation methods under suboptimal conditions. *Psychological Methods*, 17(3), 354-373. https://doi.org/10.1037/a0029315

Rondeau, E. P., Brown, R. K., & Lapides, P. D. (2012). *Facility management* (2nd ed.). John Wiley & Sons.

Rust, R. T., & Zahorik, A. J. (1993). Customer satisfaction, customer retention, and market share. *Journal of Retailing*, 69(2), 193-215. https://doi.org/10.1016/0022-4359(93)90003-2

Satorra, A., & Bentler, P. M. (2001). A scaled difference chi-square test statistic for moment structure analysis. *Psychometrika*, 66(4), 507-514. https://doi.org/10.1007/BF02296192

Sullivan, G. M., & Feinn, R. (2012). Using effect size—or why the P value is not enough. *Journal of Graduate Medical Education*, 4(3), 279-282. https://doi.org/10.4300/JGME-D-12-00156.1

Szymanski, D. M., & Henard, D. H. (2001). Customer satisfaction: A meta-analysis of the empirical evidence. *Journal of the Academy of Marketing Science*, 29(1), 16-35. https://doi.org/10.1177/0092070301291002

Tabachnick, B. G., & Fidell, L. S. (2019). *Using multivariate statistics* (7th ed.). Pearson.

Williams, P., & Naumann, E. (2011). Customer satisfaction and business performance: A firm-level analysis. *Journal of Services Marketing*, 25(1), 20-32. https://doi.org/10.1108/08876041111107032

---

**Appendix A: Statistical Output Tables**

**Table A1: Pearson Correlation Coefficients**

| Variable | BLDGAGE | CUSTSCORE | ROISCORE |
|----------|---------|-----------|----------|
| **BLDGAGE** | 1.000 | 0.274** | -0.193** |
| **CUSTSCORE** | 0.274** | 1.000 | 0.637** |
| **ROISCORE** | -0.193** | 0.637** | 1.000 |

*Note: ** Correlation is significant at the 0.01 level (2-tailed), N = 869*

**Table A2: Descriptive Statistics for Scale Variables**

| Variable | N | Mean | Std. Deviation | Minimum | Maximum |
|----------|---|------|----------------|---------|---------|
| BLDGAGE | 869 | 10.16 | 2.88 | 0.13 | 22.00 |
| ROISCORE | 869 | 15.26 | 3.62 | 5.00 | 30.00 |
| CUSTSCORE | 869 | 25.04 | 3.94 | 13.00 | 36.00 |

**Table A3: Hypothesis Testing Results**

| Hypothesis | Correlation Pair | Predicted Direction | Actual Result | Effect Size | Status |
|------------|------------------|-------------------|---------------|-------------|---------|
| H1 | CUSTSCORE ↔ ROISCORE | Positive | r = 0.637*** | Large | **Supported** |
| H2 | BLDGAGE ↔ CUSTSCORE | Negative | r = 0.274*** | Small-Medium | **Rejected** |
| H3 | BLDGAGE ↔ ROISCORE | Negative | r = -0.193*** | Small | **Supported** |

*Note: *** p < 0.001 (2-tailed), N = 869*

**Variable Definitions:**
- **BLDGAGE**: Building age in years (Scale/Continuous)
- **CUSTSCORE**: Customer satisfaction score, 1-100 scale (Scale/Continuous)
- **ROISCORE**: Return on investment score, 1-100 scale (Scale/Continuous)
