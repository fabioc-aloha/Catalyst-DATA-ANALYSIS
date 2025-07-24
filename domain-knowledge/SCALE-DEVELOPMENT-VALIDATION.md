# Domain Knowledge - Scale Development and Validation in Python

**Domain**: PSYCHOMETRIC ANALYSIS - SCALE DEVELOPMENT AND VALIDATION
**Created**: July 24, 2025
**Last Updated**: July 24, 2025
**Learning Status**: Expert
**Complexity Level**: Advanced

## Learning Objectives

**Primary Goals**:
- [x] Master comprehensive scale development workflow in Python
- [x] Implement advanced reliability assessment techniques
- [x] Execute sophisticated validity testing procedures
- [x] Develop automated scale validation pipelines

**Success Criteria**:
- [x] Can develop new measurement scales from concept to validation
- [x] Can assess multiple forms of reliability and validity
- [x] Can detect and correct measurement issues
- [x] Can generate publication-ready psychometric reports

## Scale Development Lifecycle

### Phase 1: Item Generation and Content Validity

```python
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def content_validity_assessment(items_df, expert_ratings_df):
    """
    Assess content validity using expert ratings

    Parameters:
    - items_df: DataFrame with item content
    - expert_ratings_df: DataFrame with expert relevance ratings (1-4 scale)
    """

    # Calculate Content Validity Ratio (CVR) for each item
    def calculate_cvr(ratings):
        n_experts = len(ratings)
        n_essential = sum(ratings >= 3)  # Ratings of 3 or 4 considered essential
        cvr = (2 * n_essential - n_experts) / n_experts
        return cvr

    # Calculate Content Validity Index (CVI)
    cvi_results = {}
    for item in expert_ratings_df.columns:
        item_ratings = expert_ratings_df[item].dropna()
        cvr = calculate_cvr(item_ratings)
        cvi = (item_ratings >= 3).mean()  # Proportion rating 3 or 4

        cvi_results[item] = {
            'CVR': cvr,
            'CVI': cvi,
            'mean_rating': item_ratings.mean(),
            'std_rating': item_ratings.std()
        }

    return pd.DataFrame(cvi_results).T

def item_discrimination_analysis(df, scale_items, criterion='total_score'):
    """
    Analyze item discrimination through item-total correlations
    """

    if criterion == 'total_score':
        # Calculate total score excluding each item
        discrimination_results = {}
        for item in scale_items:
            other_items = [col for col in scale_items if col != item]
            total_score = df[other_items].sum(axis=1)

            # Corrected item-total correlation
            correlation = df[item].corr(total_score)

            # Item difficulty (mean response)
            difficulty = df[item].mean()

            discrimination_results[item] = {
                'item_total_correlation': correlation,
                'item_difficulty': difficulty,
                'item_variance': df[item].var()
            }

    return pd.DataFrame(discrimination_results).T
```

### Phase 2: Initial Item Analysis and Purification

```python
def comprehensive_item_analysis(df, scale_items, response_scale_max=7):
    """
    Perform comprehensive item analysis for scale purification
    """

    results = {
        'item_statistics': {},
        'reliability_if_deleted': {},
        'factor_loadings': {},
        'item_response_distributions': {}
    }

    # Basic item statistics
    for item in scale_items:
        item_data = df[item].dropna()

        results['item_statistics'][item] = {
            'mean': item_data.mean(),
            'std': item_data.std(),
            'median': item_data.median(),
            'min': item_data.min(),
            'max': item_data.max(),
            'skewness': stats.skew(item_data),
            'kurtosis': stats.kurtosis(item_data),
            'response_range_used': item_data.max() - item_data.min() + 1,
            'ceiling_effect': (item_data == response_scale_max).mean(),
            'floor_effect': (item_data == 1).mean()
        }

        # Response distribution
        results['item_response_distributions'][item] = item_data.value_counts().sort_index()

    # Reliability if item deleted
    for item in scale_items:
        remaining_items = [col for col in scale_items if col != item]
        alpha_without_item = cronbach_alpha(df, remaining_items)
        results['reliability_if_deleted'][item] = alpha_without_item

    return results

def identify_problematic_items(item_analysis_results, alpha_threshold=0.05):
    """
    Identify items that should be considered for removal
    """

    problematic_items = {}

    # Check each item against multiple criteria
    for item in item_analysis_results['item_statistics'].keys():
        issues = []

        # Low item-total correlation (< 0.3)
        if item in item_analysis_results.get('discrimination', {}):
            if item_analysis_results['discrimination'][item]['item_total_correlation'] < 0.3:
                issues.append('low_item_total_correlation')

        # High ceiling/floor effects (> 15%)
        item_stats = item_analysis_results['item_statistics'][item]
        if item_stats['ceiling_effect'] > 0.15:
            issues.append('ceiling_effect')
        if item_stats['floor_effect'] > 0.15:
            issues.append('floor_effect')

        # Extreme skewness (|skew| > 2)
        if abs(item_stats['skewness']) > 2:
            issues.append('extreme_skewness')

        # Low variance utilization
        theoretical_variance = ((item_stats['max'] - item_stats['min']) ** 2) / 12
        if item_stats['std'] ** 2 < 0.5 * theoretical_variance:
            issues.append('low_variance_utilization')

        # Reliability improvement if deleted
        current_alpha = cronbach_alpha(df, scale_items)  # Assume access to df and scale_items
        if item in item_analysis_results['reliability_if_deleted']:
            alpha_if_deleted = item_analysis_results['reliability_if_deleted'][item]
            if alpha_if_deleted > current_alpha + alpha_threshold:
                issues.append('reliability_improves_if_deleted')

        if issues:
            problematic_items[item] = issues

    return problematic_items
```

### Phase 3: Factor Structure Analysis

```python
from factor_analyzer import FactorAnalyzer, calculate_bartlett_sphericity, calculate_kmo
from factor_analyzer.utils import corr

def advanced_factor_analysis(df, scale_items, max_factors=None):
    """
    Comprehensive factor analysis with multiple extraction methods
    """

    # Prepare data
    factor_data = df[scale_items].dropna()

    if max_factors is None:
        max_factors = min(len(scale_items) // 2, len(scale_items) - 1)

    results = {
        'factorability_tests': {},
        'factor_solutions': {},
        'fit_indices': {}
    }

    # Test factorability
    chi_square, p_value = calculate_bartlett_sphericity(factor_data)
    kmo_all, kmo_model = calculate_kmo(factor_data)

    results['factorability_tests'] = {
        'bartlett_chi_square': chi_square,
        'bartlett_p_value': p_value,
        'kmo_overall': kmo_model,
        'kmo_individual': kmo_all
    }

    # Test multiple factor solutions
    for n_factors in range(1, max_factors + 1):

        # Principal axis factoring
        fa_paf = FactorAnalyzer(n_factors=n_factors, rotation='varimax', method='principal')
        fa_paf.fit(factor_data)

        # Maximum likelihood
        fa_ml = FactorAnalyzer(n_factors=n_factors, rotation='varimax', method='ml')
        fa_ml.fit(factor_data)

        results['factor_solutions'][n_factors] = {
            'paf': {
                'loadings': pd.DataFrame(fa_paf.loadings_, index=scale_items,
                                       columns=[f'Factor_{i+1}' for i in range(n_factors)]),
                'communalities': fa_paf.get_communalities(),
                'eigenvalues': fa_paf.get_eigenvalues()[0],
                'variance_explained': fa_paf.get_factor_variance()
            },
            'ml': {
                'loadings': pd.DataFrame(fa_ml.loadings_, index=scale_items,
                                       columns=[f'Factor_{i+1}' for i in range(n_factors)]),
                'communalities': fa_ml.get_communalities(),
                'eigenvalues': fa_ml.get_eigenvalues()[0],
                'variance_explained': fa_ml.get_factor_variance()
            }
        }

    return results

def parallel_analysis(df, scale_items, n_iterations=1000):
    """
    Perform parallel analysis to determine optimal number of factors
    """

    real_data = df[scale_items].dropna()
    n_vars = real_data.shape[1]
    n_obs = real_data.shape[0]

    # Get eigenvalues from real data
    correlation_matrix = real_data.corr()
    real_eigenvalues = np.linalg.eigvals(correlation_matrix)

    # Generate random eigenvalues
    random_eigenvalues = []
    for i in range(n_iterations):
        random_data = np.random.normal(size=(n_obs, n_vars))
        random_corr = np.corrcoef(random_data.T)
        random_eigvals = np.linalg.eigvals(random_corr)
        random_eigenvalues.append(sorted(random_eigvals, reverse=True))

    # Calculate percentiles of random eigenvalues
    random_eigenvalues = np.array(random_eigenvalues)
    percentile_95 = np.percentile(random_eigenvalues, 95, axis=0)

    # Determine number of factors
    n_factors = sum(real_eigenvalues > percentile_95)

    return {
        'real_eigenvalues': real_eigenvalues,
        'random_eigenvalues_95th': percentile_95,
        'suggested_factors': n_factors
    }
```

### Phase 4: Reliability Assessment

```python
def comprehensive_reliability_analysis(df, scale_items):
    """
    Calculate multiple reliability coefficients
    """

    reliability_results = {}

    # Cronbach's Alpha
    reliability_results['cronbach_alpha'] = cronbach_alpha(df, scale_items)

    # McDonald's Omega (more robust than alpha)
    reliability_results['mcdonald_omega'] = calculate_omega(df, scale_items)

    # Split-half reliability
    reliability_results['split_half'] = split_half_reliability(df, scale_items)

    # Inter-item correlations
    item_correlations = df[scale_items].corr()
    # Remove diagonal and get upper triangle
    mask = np.triu(np.ones_like(item_correlations), k=1).astype(bool)
    inter_item_corrs = item_correlations.where(mask).stack().dropna()

    reliability_results['inter_item_correlations'] = {
        'mean': inter_item_corrs.mean(),
        'std': inter_item_corrs.std(),
        'min': inter_item_corrs.min(),
        'max': inter_item_corrs.max(),
        'range_recommendation': 'Optimal range: 0.15-0.50'
    }

    return reliability_results

def calculate_omega(df, scale_items):
    """
    Calculate McDonald's Omega (composite reliability)
    Requires factor analysis results
    """

    # Perform single-factor analysis
    factor_data = df[scale_items].dropna()
    fa = FactorAnalyzer(n_factors=1, rotation=None)
    fa.fit(factor_data)

    loadings = fa.loadings_[:, 0]

    # Calculate omega
    sum_loadings_squared = np.sum(loadings) ** 2
    sum_error_variances = np.sum(1 - loadings ** 2)

    omega = sum_loadings_squared / (sum_loadings_squared + sum_error_variances)

    return omega

def split_half_reliability(df, scale_items):
    """
    Calculate split-half reliability with Spearman-Brown correction
    """

    # Split items into two halves
    n_items = len(scale_items)
    half1_items = scale_items[:n_items//2]
    half2_items = scale_items[n_items//2:]

    # Calculate half scores
    half1_score = df[half1_items].sum(axis=1)
    half2_score = df[half2_items].sum(axis=1)

    # Correlation between halves
    half_correlation = half1_score.corr(half2_score)

    # Spearman-Brown correction
    split_half_reliability = (2 * half_correlation) / (1 + half_correlation)

    return {
        'uncorrected_correlation': half_correlation,
        'spearman_brown_corrected': split_half_reliability
    }
```

### Phase 5: Validity Assessment

```python
def comprehensive_validity_assessment(df, scale_items, criterion_vars=None, convergent_scales=None,
                                    discriminant_scales=None, demographic_vars=None):
    """
    Assess multiple forms of validity
    """

    validity_results = {
        'construct_validity': {},
        'criterion_validity': {},
        'convergent_validity': {},
        'discriminant_validity': {},
        'known_groups_validity': {}
    }

    # Create scale score
    scale_score = df[scale_items].mean(axis=1)

    # Construct validity (factor analysis)
    fa = FactorAnalyzer(n_factors=1, rotation=None)
    factor_data = df[scale_items].dropna()
    fa.fit(factor_data)

    validity_results['construct_validity'] = {
        'factor_loadings': dict(zip(scale_items, fa.loadings_[:, 0])),
        'variance_explained': fa.get_factor_variance()[0][0],
        'communalities': dict(zip(scale_items, fa.get_communalities()))
    }

    # Criterion validity
    if criterion_vars:
        criterion_correlations = {}
        for var in criterion_vars:
            corr = scale_score.corr(df[var])
            # Calculate statistical significance
            n = len(df[[scale_items[0], var]].dropna())
            t_stat = corr * np.sqrt((n - 2) / (1 - corr**2))
            p_value = 2 * (1 - stats.t.cdf(abs(t_stat), n - 2))

            criterion_correlations[var] = {
                'correlation': corr,
                'p_value': p_value,
                'n': n
            }
        validity_results['criterion_validity'] = criterion_correlations

    # Convergent validity
    if convergent_scales:
        convergent_correlations = {}
        for scale_name, scale_vars in convergent_scales.items():
            other_scale = df[scale_vars].mean(axis=1)
            corr = scale_score.corr(other_scale)
            convergent_correlations[scale_name] = corr
        validity_results['convergent_validity'] = convergent_correlations

    # Discriminant validity
    if discriminant_scales:
        discriminant_correlations = {}
        for scale_name, scale_vars in discriminant_scales.items():
            other_scale = df[scale_vars].mean(axis=1)
            corr = scale_score.corr(other_scale)
            discriminant_correlations[scale_name] = corr
        validity_results['discriminant_validity'] = discriminant_correlations

    # Known-groups validity
    if demographic_vars:
        known_groups_results = {}
        for demo_var in demographic_vars:
            groups = df.groupby(demo_var)[scale_items].mean().mean(axis=1)

            # Perform ANOVA if more than 2 groups
            group_data = [df[df[demo_var] == group][scale_items].mean(axis=1).dropna()
                         for group in df[demo_var].unique() if pd.notna(group)]

            if len(group_data) > 2:
                f_stat, p_value = stats.f_oneway(*group_data)
                test_result = {'F_statistic': f_stat, 'p_value': p_value, 'test': 'ANOVA'}
            elif len(group_data) == 2:
                t_stat, p_value = stats.ttest_ind(group_data[0], group_data[1])
                test_result = {'t_statistic': t_stat, 'p_value': p_value, 'test': 't-test'}
            else:
                test_result = {'error': 'Insufficient groups for analysis'}

            known_groups_results[demo_var] = {
                'group_means': groups.to_dict(),
                'statistical_test': test_result
            }

        validity_results['known_groups_validity'] = known_groups_results

    return validity_results

def measurement_invariance_test(df, scale_items, group_var):
    """
    Test measurement invariance across groups (basic implementation)
    """

    groups = df[group_var].unique()
    invariance_results = {}

    for group in groups:
        if pd.notna(group):
            group_data = df[df[group_var] == group][scale_items].dropna()

            # Single factor analysis for each group
            fa = FactorAnalyzer(n_factors=1, rotation=None)
            fa.fit(group_data)

            invariance_results[group] = {
                'factor_loadings': dict(zip(scale_items, fa.loadings_[:, 0])),
                'n_observations': len(group_data)
            }

    # Compare factor loadings across groups
    loading_comparison = pd.DataFrame({
        group: results['factor_loadings']
        for group, results in invariance_results.items()
    })

    return {
        'group_results': invariance_results,
        'loading_comparison': loading_comparison
    }
```

### Phase 6: Scale Scoring and Norms

```python
def create_scale_scoring_system(df, scale_items, norm_groups=None):
    """
    Create comprehensive scoring system with norms
    """

    scoring_system = {
        'scale_items': scale_items,
        'scoring_method': 'mean',  # Could be sum, mean, or weighted
        'descriptive_statistics': {},
        'percentile_norms': {},
        'z_score_conversion': {},
        'norm_groups': {}
    }

    # Calculate scale scores
    scale_scores = df[scale_items].mean(axis=1)

    # Overall descriptive statistics
    scoring_system['descriptive_statistics'] = {
        'mean': scale_scores.mean(),
        'std': scale_scores.std(),
        'median': scale_scores.median(),
        'min': scale_scores.min(),
        'max': scale_scores.max(),
        'n': len(scale_scores.dropna())
    }

    # Percentile norms
    percentiles = [5, 10, 25, 50, 75, 90, 95]
    scoring_system['percentile_norms'] = {
        f'{p}th_percentile': np.percentile(scale_scores.dropna(), p)
        for p in percentiles
    }

    # Z-score conversion parameters
    scoring_system['z_score_conversion'] = {
        'mean': scale_scores.mean(),
        'std': scale_scores.std()
    }

    # Norm groups (if specified)
    if norm_groups:
        for group_var in norm_groups:
            group_norms = {}
            for group in df[group_var].unique():
                if pd.notna(group):
                    group_scores = df[df[group_var] == group][scale_items].mean(axis=1)
                    group_norms[group] = {
                        'mean': group_scores.mean(),
                        'std': group_scores.std(),
                        'n': len(group_scores.dropna()),
                        'percentiles': {
                            f'{p}th': np.percentile(group_scores.dropna(), p)
                            for p in percentiles
                        }
                    }
            scoring_system['norm_groups'][group_var] = group_norms

    return scoring_system

def generate_scale_manual(scale_name, scale_items, reliability_results, validity_results,
                         scoring_system, development_notes=""):
    """
    Generate comprehensive scale manual/documentation
    """

    manual = f"""
# {scale_name} - Scale Manual and Technical Report

## Scale Development Summary

**Scale Name**: {scale_name}
**Number of Items**: {len(scale_items)}
**Response Format**: [Specify Likert scale format]
**Development Date**: {pd.Timestamp.now().strftime('%Y-%m-%d')}

{development_notes}

## Scale Items

"""

    for i, item in enumerate(scale_items, 1):
        manual += f"{i}. {item}\n"

    manual += f"""

## Psychometric Properties

### Reliability
- Cronbach's Alpha: {reliability_results.get('cronbach_alpha', 'N/A'):.3f}
- McDonald's Omega: {reliability_results.get('mcdonald_omega', 'N/A'):.3f}
- Split-Half Reliability: {reliability_results.get('split_half', {}).get('spearman_brown_corrected', 'N/A'):.3f}

### Validity Evidence
- Factor structure supports unidimensional construct
- Convergent validity demonstrated through correlations with related measures
- Discriminant validity established through low correlations with unrelated constructs

## Scoring Instructions

**Scoring Method**: Calculate the mean of all item responses
**Missing Data**: Require at least 80% of items to be answered for valid score
**Score Range**: {scoring_system['descriptive_statistics']['min']:.2f} to {scoring_system['descriptive_statistics']['max']:.2f}

### Normative Data
- Sample Size: {scoring_system['descriptive_statistics']['n']}
- Mean: {scoring_system['descriptive_statistics']['mean']:.2f}
- Standard Deviation: {scoring_system['descriptive_statistics']['std']:.2f}

### Interpretation Guidelines
- Scores above {scoring_system['percentile_norms']['75th_percentile']:.2f} (75th percentile): High
- Scores between {scoring_system['percentile_norms']['25th_percentile']:.2f} and {scoring_system['percentile_norms']['75th_percentile']:.2f}: Average
- Scores below {scoring_system['percentile_norms']['25th_percentile']:.2f} (25th percentile): Low

## Technical Considerations
- Ensure appropriate sample representation
- Consider cultural and demographic factors in interpretation
- Regular validation recommended for new populations
"""

    return manual
```

## Integration with Survey Analysis Workflow

### Automated Scale Development Pipeline
```python
def automated_scale_development_pipeline(df, candidate_items, scale_name):
    """
    Complete automated scale development workflow
    """

    pipeline_results = {
        'initial_items': candidate_items,
        'item_analysis': {},
        'factor_analysis': {},
        'reliability_analysis': {},
        'validity_analysis': {},
        'final_scale': {},
        'recommendations': []
    }

    # Phase 1: Initial item analysis
    item_analysis = comprehensive_item_analysis(df, candidate_items)
    pipeline_results['item_analysis'] = item_analysis

    # Phase 2: Identify problematic items
    problematic_items = identify_problematic_items(item_analysis)
    if problematic_items:
        pipeline_results['recommendations'].append(
            f"Consider removing items: {list(problematic_items.keys())}"
        )

    # Phase 3: Factor analysis
    factor_results = advanced_factor_analysis(df, candidate_items)
    pipeline_results['factor_analysis'] = factor_results

    # Phase 4: Reliability assessment
    reliability_results = comprehensive_reliability_analysis(df, candidate_items)
    pipeline_results['reliability_analysis'] = reliability_results

    # Phase 5: Generate recommendations
    alpha = reliability_results['cronbach_alpha']
    if alpha < 0.7:
        pipeline_results['recommendations'].append(
            f"Reliability ({alpha:.3f}) below acceptable threshold (0.7)"
        )
    elif alpha > 0.95:
        pipeline_results['recommendations'].append(
            f"Reliability ({alpha:.3f}) may indicate redundancy"
        )

    # Phase 6: Final scale composition
    # Remove items that should be deleted based on analysis
    items_to_remove = []
    for item, issues in problematic_items.items():
        if 'reliability_improves_if_deleted' in issues:
            items_to_remove.append(item)

    final_items = [item for item in candidate_items if item not in items_to_remove]
    pipeline_results['final_scale'] = {
        'items': final_items,
        'reliability': cronbach_alpha(df, final_items),
        'n_items_removed': len(items_to_remove),
        'items_removed': items_to_remove
    }

    return pipeline_results
```

## Memory Consolidation Points

**Key Learnings**:
- Scale development requires systematic progression through multiple validation phases
- Python provides comprehensive tools for all aspects of psychometric analysis
- Automated pipelines can streamline scale development while maintaining rigor
- Multiple reliability and validity measures provide convergent evidence
- Documentation and manual creation are crucial for scale adoption

**Advanced Techniques Mastered**:
- Content validity assessment with expert ratings
- Parallel analysis for factor retention
- McDonald's Omega for composite reliability
- Measurement invariance testing
- Automated scale development pipelines

**Integration Points**:
- Links to SPSS-PYTHON-EQUIVALENTS.md for procedural knowledge
- Connects with business intelligence for scale implementation
- Supports research methodology for validation studies
- Enables automated reporting for stakeholder communication
