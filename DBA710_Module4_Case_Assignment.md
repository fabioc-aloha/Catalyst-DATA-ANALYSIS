# Statistical Analysis of Customer Satisfaction in Retail Electronics Chain: Assessment

**Student Name:** [Your Name]
**Course:** DBA 710
**Assignment:** Module 4 Case Assignment
**Date:** July 27, 2025

---

## Executive Summary

This business intelligence report analyzes customer satisfaction data from a retail electronics chain with 869 store locations across six states to identify actionable insights for operational optimization and strategic decision-making. The analysis employs three statistical methodologies to examine factors influencing customer experience outcomes: independent samples t-tests comparing corporate versus franchise ownership models, Pearson correlation analysis investigating relationships between operational metrics and customer satisfaction, and one-way analysis of variance (ANOVA) evaluating regional performance differences.

**Key Business Findings:**

- **Ownership Structure Impact**: Corporate-owned stores achieve statistically significant higher customer satisfaction scores compared to franchise operations (p = 0.007), indicating potential advantages in standardized operational protocols and resource allocation.

- **Operational Excellence Correlation**: A strong positive relationship exists between ROI performance and customer satisfaction (r = 0.637, p < 0.001), demonstrating that operational efficiency directly translates to enhanced customer experiences and explaining 40.6% of customer satisfaction variance.

- **Geographic Performance Variations**: Significant regional differences in customer satisfaction were identified (F = 8.550, p < 0.001), with Arizona stores leading performance benchmarks and Indiana locations requiring targeted improvement interventions.

- **Facility Investment Opportunities**: Moderate positive correlations between building age and customer satisfaction suggest that strategic facility modernization investments can yield both operational efficiency gains and improved customer experience outcomes.

**Strategic Recommendations**: Results support implementing differentiated regional strategies, investigating Arizona's operational best practices for replication across the organization, developing targeted improvement programs for underperforming markets, and prioritizing operational excellence initiatives that strengthen the ROI-customer satisfaction relationship.

This analysis provides evidence-based intelligence for strategic business optimization within the retail electronics industry, enabling data-driven decision-making for enhanced customer experience delivery and sustainable competitive advantage.

**Keywords:** customer satisfaction, retail analytics, business intelligence, operational excellence, regional performance optimization

---

## Introduction

Customer satisfaction serves as a performance indicator in the retail industry, influencing customer retention, profitability, and competitive advantage (Anderson & Mittal, 2000). In the retail electronics market, understanding the factors that drive customer satisfaction and identifying operational strategies that enhance customer experience outcomes is important for business success (Kumar & Reinartz, 2016).

This statistical analysis examines customer satisfaction data from a retail electronics chain operating 869 stores across six states (Arizona, California, Indiana, Missouri, Texas, and Washington). The organization employs both corporate-owned and franchise business models, providing an opportunity to investigate how ownership structure influences customer satisfaction outcomes (Bitner et al., 2021). Additionally, the geographic distribution of stores enables analysis of regional variations in customer experience performance (Porter, 2008).

The objective of this research is to conduct statistical analyses to identify relationships and differences in customer satisfaction across operational and geographic dimensions (Field, 2018). This study addresses three research questions using complementary analytical approaches:

1. Does ownership structure (corporate versus franchise) significantly influence customer satisfaction scores?
2. What relationships exist between operational metrics (ROI performance and facility age) and customer satisfaction outcomes?
3. Do customer satisfaction scores vary significantly across different geographic regions?

The analytical strategy employs three distinct statistical methodologies to examine different aspects of customer satisfaction variance. Independent samples t-tests examine categorical group differences in ownership structure, providing insights into whether business model decisions create measurable customer experience differences. Pearson correlation analysis examines continuous variable relationships between operational metrics and customer satisfaction, revealing the strength and direction of associations between performance indicators and customer outcomes. One-way analysis of variance examines geographic differences across multiple regions simultaneously, identifying location-specific factors that may influence customer experience quality.

This multi-method approach provides triangulation of findings, where convergent results across different analytical techniques strengthen confidence in the practical significance of the results. Each analysis contributes unique insights while building upon previous findings to create a understanding of customer satisfaction drivers in retail environments.

**Thesis Statement:** Statistical analysis of customer satisfaction data from a multi-state retail electronics chain reveals differences in customer experience outcomes based on ownership structure and geographic location, while demonstrating correlations between operational performance metrics and customer satisfaction scores, providing insights for strategic business optimization.

The following sections present three statistical analyses, each addressing research hypotheses through appropriate statistical methodologies (Maxwell et al., 2018). Results are presented in American Psychological Association (APA) format with interpretation of statistical and practical significance.

This analytical approach follows a systematic progression from examining fundamental group differences to exploring relationships between variables, concluding with geographic variance analysis. Each analysis builds upon previous findings to create a foundation for understanding the multiple factors that influence customer satisfaction outcomes in retail environments.

---

## Independent Samples T-Test: Corporate vs. Franchise Customer Satisfaction

The first analysis examines ownership structure as a potential driver of customer satisfaction differences. This investigation addresses whether the business model employed (corporate versus franchise operations) creates measurable differences in customer experience outcomes. The choice to begin with this analysis reflects the fundamental importance of ownership structure in retail operations, as it influences standardization, resource allocation, training protocols, and operational consistency (Lafontaine & Shaw, 2005).

Understanding ownership effects provides a foundation for subsequent analyses by establishing whether structural factors create baseline differences in performance. If ownership structure demonstrates significant effects, these must be considered when interpreting other relationships in the dataset. Conversely, if ownership shows minimal impact, attention can focus on operational and geographic factors as primary drivers of customer satisfaction variance.

### Research Question
To what extent does ownership structure (corporate versus franchise) influence customer satisfaction scores in retail electronics stores?

### Hypotheses
**H₀ (Null Hypothesis):** There is no difference in customer satisfaction scores between corporate-owned stores and franchise-owned stores.

**H₁ (Alternative Hypothesis):** There is a difference in customer satisfaction scores between corporate-owned stores and franchise-owned stores.

### Statistical Analysis
An independent samples t-test was conducted to examine differences in customer satisfaction scores between corporate-owned stores (n = 434) and franchise-owned stores (n = 435) (Field, 2018). The independent samples t-test is appropriate for this research question because it compares means between two independent groups when the dependent variable is continuous and approximately normally distributed.

Prior to analysis, statistical assumptions were evaluated to ensure the validity of test results. Levene's test for equality of variances was statistically significant, F = 4.89, p = 0.027, indicating heterogeneity of variance between the two ownership groups. This violation of the equal variances assumption required using the Welch t-test modification, which does not assume equal variances in the t-test calculation (Stevens, 2016). The use of the modified degrees of freedom and standard error calculations ensures accurate probability estimates despite unequal group variances.

### Results
An independent samples t-test revealed a statistically significant difference in customer satisfaction scores between corporate-owned stores and franchise-owned stores, t(867) = 2.696, p = 0.007. The statistical significance (p < 0.05) provides evidence to reject the null hypothesis and conclude that ownership structure influences customer satisfaction outcomes in this retail electronics chain.

The direction of the difference indicated that corporate-owned stores demonstrated higher customer satisfaction scores than franchise-owned stores. The effect size, calculated using Cohen's d, was small to medium based on conventional effect size interpretation guidelines (Cohen, 1988). This effect size indicates that while the difference is statistically significant, the practical magnitude of the difference represents a modest but measurable impact in the business context.

The statistically significant result, combined with the directional findings and effect size considerations, provides evidence that ownership structure creates measurable differences in customer experience outcomes, with corporate ownership associated with higher customer satisfaction levels. Hence, we reject the null hypothesis.

### Business Interpretation
The difference in customer satisfaction scores between corporate and franchise stores represents a modest practical difference in the business context (Kirk, 2013). This finding suggests that corporate ownership structure may provide operational advantages that translate to enhanced customer experiences, potentially through standardized training protocols, operational procedures, or improved resource allocation (Heskett et al., 2008). However, the small to medium effect size indicates that ownership structure accounts for a limited portion of the variance in customer satisfaction outcomes, suggesting that other factors may be equally or more important in driving customer experience excellence (Cohen, 1988).

---

## Pearson Correlation Analysis: Operational Metrics and Customer Satisfaction

The second analysis shifts focus from categorical group differences to continuous variable relationships. While the t-test analysis revealed whether ownership structure creates distinct customer satisfaction outcomes, correlation analysis examines how operational performance metrics relate to customer experience quality. This approach recognizes that customer satisfaction may be influenced by measurable operational factors that reflect facility quality, financial performance, and resource utilization efficiency.

Correlation analysis serves multiple analytical purposes in this study. First, it identifies the strength and direction of relationships between operational variables and customer satisfaction, providing insights into which factors may be most important for customer experience optimization. Second, it examines the intercorrelations among operational variables themselves, revealing whether facility age, financial performance, and customer satisfaction operate as independent factors or form interconnected performance dimensions.

The inclusion of both ROI performance and building age as predictor variables reflects different theoretical perspectives on customer satisfaction drivers. ROI performance represents financial efficiency and operational excellence, suggesting that well-managed operations translate to customer experience quality. Building age represents facility modernization and infrastructure quality, suggesting that physical environment characteristics influence customer perceptions and satisfaction outcomes.

### Research Question
What relationships exist between operational performance metrics (ROI scores and building age) and customer satisfaction outcomes in retail electronics stores?

### Hypotheses
**H₀ (Null Hypothesis):** There are no statistically significant correlations between operational metrics (ROI scores and building age) and customer satisfaction scores.

**H₁ (Alternative Hypothesis):** There are statistically significant correlations between operational metrics (ROI scores and building age) and customer satisfaction scores.

### Statistical Analysis
Pearson product-moment correlations were calculated to examine relationships between customer satisfaction scores and two operational variables: ROI performance scores and building age (in years) (Field, 2018). Pearson correlation analysis is appropriate for this research question because it examines linear relationships between continuous variables and provides both the strength and direction of associations.

Assumptions of linearity and normality were assessed prior to analysis through scatterplot examination and normality testing (Tabachnick & Fidell, 2019). Scatterplots revealed approximately linear relationships between variables, supporting the use of Pearson correlation. Normality testing indicated that while the variables showed some deviation from perfect normality, the large sample size (N = 869) provides robustness to moderate violations of normality assumptions due to the central limit theorem.

The analysis examined three correlation relationships: (1) ROI performance and customer satisfaction, (2) building age and customer satisfaction, and (3) ROI performance and building age. This approach provides insights into both predictor-outcome relationships and the intercorrelations among operational variables themselves. The dataset included complete cases for all 869 store locations, ensuring that correlation estimates are based on the full available sample without listwise deletion.

### Results
**ROI Performance and Customer Satisfaction:** A Pearson correlation revealed a statistically significant strong positive relationship between ROI performance scores and customer satisfaction scores, r(867) = 0.637, p < 0.001. The 95% confidence interval for the correlation coefficient was (0.580, 0.688). This correlation indicates that approximately 40.6% of the variance in customer satisfaction scores is associated with ROI performance outcomes.

**Building Age and Customer Satisfaction:** A Pearson correlation revealed a statistically significant moderate positive relationship between building age and customer satisfaction scores, r(867) = 0.274, p < 0.001. The 95% confidence interval for the correlation coefficient was (0.208, 0.338). This correlation indicates that approximately 7.5% of the variance in customer satisfaction scores is associated with building age.

**ROI Performance and Building Age:** A Pearson correlation revealed a statistically significant moderate negative relationship between ROI performance scores and building age, r(867) = -0.193, p < 0.001, indicating that newer facilities tend to achieve higher ROI performance.

Hence, we reject the null hypothesis for all three correlation relationships.

### Business Interpretation
The strong positive correlation (r = 0.637) between ROI performance and customer satisfaction demonstrates that operational excellence translates to enhanced customer experiences (Anderson et al., 2019). This finding suggests that investments in operational efficiency, cost management, and revenue optimization create improvements in customer satisfaction outcomes (Kumar & Reinartz, 2016). The moderate positive correlation between building age and customer satisfaction (r = 0.274) indicates that newer facilities contribute to customer experience quality, likely through improved technology, layout design, and aesthetic appeal (Zeithaml et al., 2020). The negative correlation between ROI and building age suggests that facility modernization represents a strategic investment opportunity, potentially generating both operational efficiency gains and customer satisfaction improvements (Fornell et al., 2016).

---

## One-Way Analysis of Variance: Regional Customer Satisfaction Differences

The third analysis examines geographic factors as determinants of customer satisfaction variance. While the previous analyses established ownership effects and operational relationships, geographic analysis addresses whether location-specific factors create systematic differences in customer experience outcomes. This investigation is important because geographic markets vary in demographics, competition, local economic conditions, management quality, and operational execution (Porter, 2008).

ANOVA methodology is appropriate for this research question because it examines differences across multiple geographic groups simultaneously while controlling for family-wise error rates that would inflate Type I error risk in multiple t-test comparisons. The analysis tests whether customer satisfaction varies significantly across the six states in the dataset, providing evidence for whether standardized approaches are sufficient or whether region-specific strategies may be necessary.

The geographic analysis builds upon previous findings by examining whether patterns identified in ownership and operational analyses vary by location. If significant regional differences exist, this suggests that local market factors, management effectiveness, or operational execution create geographic performance clusters. Such findings would indicate that successful practices in high-performing regions might be identified and replicated, while underperforming regions might require targeted intervention strategies.

The selection of state-level analysis reflects a balance between geographic granularity and analytical power. State-level grouping provides sufficient sample sizes for statistical testing while representing meaningful geographic markets with distinct regulatory, competitive, and demographic characteristics that may influence retail performance outcomes.

### Research Question
Do customer satisfaction scores vary significantly across different geographic regions (states) in the retail electronics chain?

### Hypotheses
**H₀ (Null Hypothesis):** There are no statistically significant differences in customer satisfaction scores across the six states (Arizona, California, Indiana, Missouri, Texas, Washington).

**H₁ (Alternative Hypothesis):** There are statistically significant differences in customer satisfaction scores across the six states.

### Statistical Analysis
A one-way analysis of variance (ANOVA) was conducted to examine differences in customer satisfaction scores across six states (Maxwell et al., 2018). One-way ANOVA is the appropriate statistical technique for this research question because it compares means across multiple independent groups (six states) while controlling for family-wise error rates that would be inflated if multiple t-tests were conducted.

The independent variable was STATE (categorical with six levels: Arizona, California, Indiana, Missouri, Texas, and Washington), and the dependent variable was CUSTSCORE (continuous customer satisfaction scores). Sample sizes ranged from 118 stores (Washington) to 194 stores (California), with a total sample of 869 stores. The unequal sample sizes reflect the natural distribution of stores across geographic markets rather than experimental design limitations.

Statistical assumptions were evaluated prior to analysis. Levene's test indicated heterogeneity of variance (F = 5.347, p < 0.001), representing a violation of the equal variances assumption. However, ANOVA is robust to moderate violations of this assumption given large sample sizes and relatively balanced groups (Field, 2018; Stevens, 2016). The substantial sample sizes in each state group (ranging from 118 to 194) provide sufficient power for detecting meaningful differences while maintaining robustness to assumption violations.

Fisher's Least Significant Difference (LSD) post-hoc testing was conducted to identify specific pairwise differences between states. LSD testing was selected over more conservative approaches (such as Bonferroni correction) because the research question specifically seeks to identify which states differ from others, and the exploratory nature of the geographic analysis supports a balance between Type I and Type II error protection.

### Results
The one-way ANOVA revealed a statistically significant difference in customer satisfaction scores between states, F(5, 863) = 8.550, p < 0.001, η² = 0.047. This represents a medium effect size according to Cohen's conventions (Cohen, 1988), indicating that approximately 4.7% of the variance in customer satisfaction is attributable to state differences.

**Descriptive Statistics by State:**
- Arizona: M = 26.00, SD = 4.29, n = 176
- California: M = 25.62, SD = 3.67, n = 194
- Indiana: M = 23.28, SD = 3.94, n = 124
- Missouri: M = 25.05, SD = 4.26, n = 128
- Texas: M = 24.61, SD = 2.77, n = 129
- Washington: M = 24.94, SD = 3.97, n = 118

**Post-Hoc Analysis Results:** LSD post-hoc testing identified nine statistically significant pairwise differences (p < 0.05). Arizona demonstrated the highest customer satisfaction scores, significantly outperforming Indiana (mean difference = 2.72, p < 0.001), Missouri (mean difference = 0.95, p = 0.035), Texas (mean difference = 1.40, p = 0.002), and Washington (mean difference = 1.06, p = 0.021). California also significantly outperformed Indiana (mean difference = 2.34, p < 0.001) and Texas (mean difference = 1.02, p = 0.020). Indiana consistently demonstrated the lowest performance, scoring significantly below all other states.

Hence, we reject the null hypothesis.

### Business Interpretation
The statistically significant regional differences in customer satisfaction reveal geographic variations in operational performance (Homburg et al., 2017). Arizona's superior performance (M = 26.00) establishes a benchmark for identifying and replicating operational practices across the organization (Porter, 2008). Indiana's consistently lower performance (M = 23.28) represents an improvement opportunity, suggesting operational challenges that require targeted interventions (Reichheld & Sasser, 1990). The 2.72-point difference between Arizona and Indiana, while representing a medium statistical effect size, translates to business impact in customer experience delivery (Kirk, 2013). These findings support implementing differentiated regional strategies rather than uniform approaches across all locations, with emphasis on investigating Arizona's success factors and addressing Indiana's performance deficiencies (Mittal & Kamakura, 2001).

---

## Discussion and Business Insights

The three statistical analyses conducted in this study (independent samples t-test, Pearson correlation analysis, and one-way ANOVA) provide complementary perspectives on customer satisfaction drivers within the retail electronics chain. Each analysis addresses different aspects of the research questions, and their convergent findings strengthen confidence in the practical significance of the results for business decision-making.

This discussion synthesizes findings across analyses to identify patterns, explore their business implications, and develop evidence-based recommendations for organizational improvement. The integration of results from multiple analytical approaches provides a foundation for understanding customer satisfaction as a multifaceted outcome influenced by structural, operational, and geographic factors operating simultaneously within the retail environment.

The statistical analysis reveals interconnected findings that provide insights for strategic business optimization. The convergence of results across multiple analytical approaches strengthens confidence in the practical significance of these findings and their applicability to business decision-making.

### Integrated Findings Analysis

The three statistical analyses demonstrate relationships that collectively provide understanding of customer satisfaction drivers within the retail electronics chain. The strong correlation between ROI performance and customer satisfaction (r = 0.637) provides understanding that operational excellence translates to customer experience outcomes. This relationship is contextualized by the ownership structure analysis, which reveals that corporate-owned stores achieve higher customer satisfaction scores, potentially through standardized operational protocols that enhance both efficiency and customer experience.

The regional ANOVA results add a geographic dimension to these findings, demonstrating that location-specific factors influence customer satisfaction outcomes. Arizona's superior performance and Indiana's consistently lower scores suggest that operational practices can be identified, studied, and potentially replicated across the organization. The correlation between building age and customer satisfaction provides an additional perspective for understanding these regional differences, as facility modernization may represent a factor in Arizona's success.

### Strategic Business Implications

These findings suggest that customer satisfaction optimization requires a multi-dimensional approach addressing operational excellence, ownership structure considerations, geographic factors, and facility investment strategies. The strong ROI-customer satisfaction correlation indicates that investments in operational efficiency and revenue optimization generate returns in customer experience quality. The moderate effect of ownership structure suggests that while corporate standardization provides advantages, the benefits are not overwhelming, indicating opportunities for franchise optimization through enhanced support and standardization protocols.

The regional variations revealed through the ANOVA analysis provide targets for both improvement (Indiana) and best practice identification (Arizona). The significant state differences suggest that one-size-fits-all approaches may be suboptimal, supporting the development of region-specific strategies that account for local market conditions, demographics, and operational challenges.

### Practical Recommendations

Based on these statistical findings, evidence-based recommendations emerge for organizational improvement (Zeithaml et al., 1996). First, the strong ROI-customer satisfaction correlation suggests that continued investment in operational excellence initiatives will generate customer experience improvements (Anderson & Fornell, 2000). Second, Arizona's superior performance warrants investigation to identify transferable best practices, particularly in areas such as staff training, inventory management, customer service protocols, and facility management (Heskett et al., 1994).

Third, Indiana's consistently poor performance across all comparative analyses indicates the need for intervention. This should include management assessment, operational process review, staff development programs, and potentially facility improvements (Reichheld & Sasser, 1990). Fourth, the positive correlation between building age and customer satisfaction, combined with the negative ROI-building age relationship, suggests that strategic facility modernization investments could improve customer satisfaction and operational efficiency (Porter, 2008).

### Study Limitations and Future Research

While these analyses provide statistical evidence for business decision-making, limitations should be acknowledged (Kirk, 2013). The cross-sectional design prevents causal inference, and the moderate effect sizes indicate that additional unmeasured variables likely influence customer satisfaction outcomes (Cohen, 1988). Future research should investigate specific operational practices that drive Arizona's superior performance, conduct longitudinal analyses to examine satisfaction trends over time, and explore additional variables such as staff training levels, inventory turnover rates, and local market competitive dynamics (Mittal & Kamakura, 2001).

---

## Conclusion and Recommended Actions

This statistical analysis identified relationships and differences in customer satisfaction across operational and geographic dimensions within a retail electronics chain through a systematic analytical approach. The three analytical methods (independent samples t-tests, Pearson correlation analysis, and one-way ANOVA) were selected to examine different aspects of customer satisfaction variance and converged to provide an evidence base for understanding customer satisfaction drivers and identifying strategic improvement opportunities.

The progression from categorical group analysis (ownership structure) to continuous variable relationships (operational metrics) to geographic variance analysis (state differences) provided a structured examination of customer satisfaction determinants. Each analysis contributed unique insights while building upon previous findings to develop understanding of the multiple factors that influence customer experience outcomes in retail environments.

The findings demonstrate that customer satisfaction in retail electronics is influenced by operational performance, ownership structure, geographic factors, and facility characteristics (Zeithaml et al., 1996). The correlation between ROI performance and customer satisfaction (r = 0.637) establishes operational excellence as a primary driver of customer experience outcomes (Anderson & Fornell, 2000). The regional differences revealed through ANOVA analysis, particularly Arizona's performance and Indiana's lower scores, provide targets for best practice identification and improvement initiatives (Heskett et al., 1994).

### Recommended Business Actions

Based on the statistical findings, the following evidence-based actions are recommended for immediate implementation:

**1. Operational Excellence Initiative (Priority: High)**
- Implement operational efficiency programs across all locations, leveraging the strong ROI-customer satisfaction correlation (r = 0.637)
- Establish performance monitoring systems that track both financial metrics and customer satisfaction outcomes
- Develop standardized operational protocols that enhance both efficiency and customer experience quality

**2. Arizona Best Practice Replication Program (Priority: High)**
- Conduct comprehensive operational assessment of Arizona stores to identify transferable success factors
- Implement pilot programs in underperforming regions using Arizona's proven methodologies
- Focus investigation on staff training protocols, inventory management systems, customer service procedures, and facility management practices

**3. Indiana Market Intervention Strategy (Priority: Critical)**
- Deploy immediate management assessment and operational review for Indiana locations
- Implement targeted staff development programs and enhanced operational support
- Consider facility improvement investments and enhanced franchise support protocols
- Establish 90-day improvement targets with measurable customer satisfaction benchmarks

**4. Strategic Facility Modernization Program (Priority: Medium)**
- Develop facility investment strategy leveraging the positive correlation between building age and customer satisfaction
- Prioritize modernization investments that deliver both operational efficiency gains and customer experience improvements
- Create facility upgrade standards that enhance customer experience while supporting operational excellence

**5. Differentiated Regional Strategy Development (Priority: Medium)**
- Abandon one-size-fits-all approaches in favor of region-specific operational strategies
- Account for local market conditions, demographics, and competitive environments in operational planning
- Establish regional performance benchmarks and customized improvement initiatives

**6. Enhanced Franchise Support Framework (Priority: Medium)**
- Develop enhanced standardization protocols and operational support for franchise locations
- Implement training programs that bridge the corporate-franchise performance gap
- Create franchise optimization initiatives that leverage corporate operational advantages

### Expected Business Impact

Implementation of these recommended actions will drive measurable improvements in customer experience delivery while enhancing operational efficiency and competitive positioning. The strong statistical relationships identified in this analysis provide confidence that targeted interventions in operational excellence, geographic performance optimization, and ownership model enhancement will yield significant business value.

The effect sizes observed across analyses indicate that while the identified factors are statistically significant and meaningful, customer satisfaction is influenced by multiple variables, many of which may not have been captured in this analysis. This finding suggests opportunities for future research to identify additional drivers of customer satisfaction and develop predictive models.

In conclusion, this statistical analysis provides a foundation for evidence-based decision-making and strategic planning within the retail electronics industry. The identification of geographic performance gaps, the quantification of operational excellence impacts, and the assessment of ownership structure effects enable targeted interventions designed to optimize customer satisfaction outcomes across the organization's geographic footprint. Implementation of these recommended actions will drive measurable improvements in customer experience delivery while enhancing operational efficiency and competitive positioning.

---

## References

Anderson, E. W., & Fornell, C. (2000). Foundations of the American customer satisfaction index. *Total Quality Management*, 11(7), 869-882. https://doi.org/10.1080/09544120050135425

Anderson, E. W., & Mittal, V. (2000). Strengthening the satisfaction-profit chain. *Journal of Service Research*, 3(2), 107-120. https://doi.org/10.1177/109467050032001

Anderson, S., Klein Pearo, L., & Widener, S. K. (2019). Drivers of service satisfaction: Linking customer satisfaction to the service concept and customer characteristics. *Journal of Service Research*, 22(3), 243-265. https://doi.org/10.1177/1094670519833675

Bitner, M. J., Zeithaml, V. A., & Gremler, D. D. (2021). *Services marketing: Integrating customer focus across the firm* (8th ed.). McGraw-Hill Education.

Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). Lawrence Erlbaum Associates.

Field, A. (2018). *Discovering statistics using IBM SPSS statistics* (5th ed.). SAGE Publications.

Fornell, C., Morgeson, F. V., & Hult, G. T. M. (2016). Stock returns on customer satisfaction do beat the market: Gauging the effect of a marketing intangible. *Journal of Marketing*, 80(5), 92-107. https://doi.org/10.1509/jm.15.0229

Heskett, J. L., Sasser, W. E., & Schlesinger, L. A. (1994). *The service profit chain: How leading companies link profit and growth to loyalty, satisfaction, and value*. Free Press.

Heskett, J. L., Jones, T. O., Loveman, G. W., Sasser, W. E., & Schlesinger, L. A. (2008). Putting the service-profit chain to work. *Harvard Business Review*, 86(7/8), 118-129.

Homburg, C., Jozić, D., & Kuehnl, C. (2017). Customer experience management: Toward implementing an evolving marketing concept. *Journal of the Academy of Marketing Science*, 45(3), 377-401. https://doi.org/10.1007/s11747-015-0460-7

Kaplan, R. S., & Norton, D. P. (1996). *The balanced scorecard: Translating strategy into action*. Harvard Business School Press.

Kirk, R. E. (2013). *Experimental design: Procedures for the behavioral sciences* (4th ed.). SAGE Publications.

Kumar, V., & Reinartz, W. (2016). Creating enduring customer value. *Journal of Marketing*, 80(6), 36-68. https://doi.org/10.1509/jm.15.0414

Lafontaine, F., & Shaw, K. L. (2005). Targeting managerial control: Evidence from franchising. *RAND Journal of Economics*, 36(1), 131-150.

Maxwell, S. E., Delaney, H. D., & Kelley, K. (2018). *Designing experiments and analyzing data: A model comparison perspective* (3rd ed.). Routledge.

Mittal, V., & Kamakura, W. A. (2001). Satisfaction, repurchase intent, and repurchase behavior: Investigating the moderating effect of customer characteristics. *Journal of Marketing Research*, 38(1), 131-142. https://doi.org/10.1509/jmkr.38.1.131.18832

Porter, M. E. (2008). *Competitive strategy: Techniques for analyzing industries and competitors*. Free Press.

Reichheld, F. F., & Sasser, W. E. (1990). Zero defections: Quality comes to services. *Harvard Business Review*, 68(5), 105-111.

Stevens, J. P. (2016). *Applied multivariate statistics for the social sciences* (6th ed.). Routledge.

Tabachnick, B. G., & Fidell, L. S. (2019). *Using multivariate statistics* (7th ed.). Pearson.

Zeithaml, V. A., Parasuraman, A., & Berry, L. L. (1996). *Delivering quality service: Balancing customer perceptions and expectations*. Free Press.

Zeithaml, V. A., Bitner, M. J., & Gremler, D. D. (2020). *Services marketing: Integrating customer focus across the firm* (7th ed.). McGraw-Hill Education.
