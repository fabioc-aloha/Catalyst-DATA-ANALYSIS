# Domain Knowledge - Structural Equation Modeling in Python

**Domain**: ADVANCED MULTIVARIATE ANALYSIS - STRUCTURAL EQUATION MODELING
**Created**: July 24, 2025
**Last Updated**: July 24, 2025
**Learning Status**: Expert
**Complexity Level**: Advanced

## Learning Objectives

**Primary Goals**:
- [x] Master SEM implementation in Python using multiple libraries
- [x] Develop expertise in model specification and identification
- [x] Execute comprehensive model evaluation and comparison
- [x] Implement advanced SEM techniques (multi-group, longitudinal, mediation)

**Success Criteria**:
- [x] Can specify and test complex structural models
- [x] Can assess model fit using multiple indices
- [x] Can conduct mediation and moderation analysis
- [x] Can perform multi-group SEM and measurement invariance testing

## SEM Libraries and Frameworks

### Primary Libraries
```python
import semopy              # Primary SEM library for Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Alternative approaches
# import lavaan (via rpy2)  # R's lavaan through Python
# import pymer4             # Mixed effects and some SEM capabilities
```

### SEM Model Components

```python
class SEMModel:
    """
    Comprehensive SEM model class for customer satisfaction analysis
    """

    def __init__(self, data, model_specification):
        self.data = data
        self.model_spec = model_specification
        self.model = None
        self.results = {}

    def specify_measurement_model(self, latent_factors):
        """
        Specify measurement model (CFA component)

        latent_factors: dict with factor names as keys and indicator lists as values
        """

        measurement_model = ""

        for factor, indicators in latent_factors.items():
            # Create factor specification
            factor_spec = f"{factor} =~ "
            factor_spec += " + ".join(indicators)
            measurement_model += factor_spec + "\n"

        return measurement_model

    def specify_structural_model(self, structural_paths):
        """
        Specify structural model (path relationships)

        structural_paths: list of tuples (predictor, outcome, path_type)
        """

        structural_model = ""

        for predictor, outcome, path_type in structural_paths:
            if path_type == "regression":
                structural_model += f"{outcome} ~ {predictor}\n"
            elif path_type == "covariance":
                structural_model += f"{predictor} ~~ {outcome}\n"

        return structural_model

    def fit_model(self):
        """
        Fit the complete SEM model
        """

        try:
            self.model = semopy.Model(self.model_spec)
            self.results = self.model.fit(self.data)
            return True
        except Exception as e:
            print(f"Model fitting error: {e}")
            return False

    def get_fit_indices(self):
        """
        Calculate comprehensive model fit indices
        """

        if not self.model or not self.results:
            return None

        # Get basic fit statistics
        fit_stats = semopy.calc_stats(self.model)

        fit_indices = {
            'chi_square': fit_stats.loc['Chi-square', 'Value'],
            'df': fit_stats.loc['Chi-square', 'DF'],
            'p_value': fit_stats.loc['Chi-square', 'p-value'],
            'cfi': fit_stats.loc['CFI', 'Value'],
            'tli': fit_stats.loc['TLI', 'Value'],
            'rmsea': fit_stats.loc['RMSEA', 'Value'],
            'rmsea_ci_lower': fit_stats.loc['RMSEA', 'CI Lower'],
            'rmsea_ci_upper': fit_stats.loc['RMSEA', 'CI Upper'],
            'srmr': fit_stats.loc['SRMR', 'Value'],
            'aic': fit_stats.loc['AIC', 'Value'],
            'bic': fit_stats.loc['BIC', 'Value']
        }

        return fit_indices

    def evaluate_fit(self, fit_indices):
        """
        Evaluate model fit against established criteria
        """

        evaluation = {
            'overall_fit': 'poor',
            'recommendations': []
        }

        # CFI and TLI criteria (> 0.95 excellent, > 0.90 acceptable)
        if fit_indices['cfi'] >= 0.95 and fit_indices['tli'] >= 0.95:
            cfi_tli_fit = 'excellent'
        elif fit_indices['cfi'] >= 0.90 and fit_indices['tli'] >= 0.90:
            cfi_tli_fit = 'acceptable'
        else:
            cfi_tli_fit = 'poor'
            evaluation['recommendations'].append("Improve CFI/TLI: Consider model modifications")

        # RMSEA criteria (< 0.05 excellent, < 0.08 acceptable)
        if fit_indices['rmsea'] <= 0.05:
            rmsea_fit = 'excellent'
        elif fit_indices['rmsea'] <= 0.08:
            rmsea_fit = 'acceptable'
        else:
            rmsea_fit = 'poor'
            evaluation['recommendations'].append("Improve RMSEA: Model may be misspecified")

        # SRMR criteria (< 0.05 excellent, < 0.08 acceptable)
        if fit_indices['srmr'] <= 0.05:
            srmr_fit = 'excellent'
        elif fit_indices['srmr'] <= 0.08:
            srmr_fit = 'acceptable'
        else:
            srmr_fit = 'poor'
            evaluation['recommendations'].append("Improve SRMR: Check residual correlations")

        # Overall assessment
        fit_levels = [cfi_tli_fit, rmsea_fit, srmr_fit]
        if all(level in ['excellent', 'acceptable'] for level in fit_levels):
            if fit_levels.count('excellent') >= 2:
                evaluation['overall_fit'] = 'excellent'
            else:
                evaluation['overall_fit'] = 'acceptable'

        evaluation['component_fit'] = {
            'cfi_tli': cfi_tli_fit,
            'rmsea': rmsea_fit,
            'srmr': srmr_fit
        }

        return evaluation
```

## Customer Satisfaction SEM Models

### Model 1: Basic Satisfaction-Loyalty Model

```python
def create_satisfaction_loyalty_model(df):
    """
    Basic two-factor model: Service Quality -> Satisfaction -> Loyalty
    """

    # Define measurement model
    measurement_model = """
    # Service Quality Factor
    ServiceQuality =~ sq_reliability + sq_responsiveness + sq_assurance + sq_empathy + sq_tangibles

    # Customer Satisfaction Factor
    Satisfaction =~ sat_overall + sat_quality + sat_service + sat_value

    # Customer Loyalty Factor
    Loyalty =~ loyalty_recommend + loyalty_repurchase + loyalty_advocate
    """

    # Define structural model
    structural_model = """
    # Structural paths
    Satisfaction ~ ServiceQuality
    Loyalty ~ Satisfaction + ServiceQuality
    """

    # Complete model specification
    full_model = measurement_model + structural_model

    return full_model

def estimate_satisfaction_loyalty_model(df):
    """
    Estimate and evaluate the satisfaction-loyalty model
    """

    model_spec = create_satisfaction_loyalty_model(df)
    sem_model = SEMModel(df, model_spec)

    if sem_model.fit_model():
        fit_indices = sem_model.get_fit_indices()
        fit_evaluation = sem_model.evaluate_fit(fit_indices)

        # Get parameter estimates
        estimates = semopy.inspect(sem_model.model, mode='est', std_est=True)

        results = {
            'model_specification': model_spec,
            'fit_indices': fit_indices,
            'fit_evaluation': fit_evaluation,
            'parameter_estimates': estimates,
            'model_object': sem_model
        }

        return results
    else:
        return None
```

### Model 2: Extended Service Quality Model (SERVQUAL)

```python
def create_servqual_model(df):
    """
    Five-factor SERVQUAL model with satisfaction and behavioral intentions
    """

    model_spec = """
    # SERVQUAL Five Factors
    Reliability =~ rel_1 + rel_2 + rel_3 + rel_4 + rel_5
    Responsiveness =~ resp_1 + resp_2 + resp_3 + resp_4
    Assurance =~ assur_1 + assur_2 + assur_3 + assur_4
    Empathy =~ emp_1 + emp_2 + emp_3 + emp_4 + emp_5
    Tangibles =~ tang_1 + tang_2 + tang_3 + tang_4

    # Outcome factors
    Satisfaction =~ sat_overall + sat_quality + sat_service + sat_value
    BehavioralIntentions =~ bi_recommend + bi_repurchase + bi_positive_wom + bi_complain

    # Structural relationships
    Satisfaction ~ Reliability + Responsiveness + Assurance + Empathy + Tangibles
    BehavioralIntentions ~ Satisfaction + Reliability + Responsiveness + Assurance + Empathy + Tangibles

    # Factor correlations (if needed)
    Reliability ~~ Responsiveness + Assurance + Empathy + Tangibles
    Responsiveness ~~ Assurance + Empathy + Tangibles
    Assurance ~~ Empathy + Tangibles
    Empathy ~~ Tangibles
    """

    return model_spec

def compare_nested_models(df, base_model_spec, alternative_model_spec):
    """
    Compare nested SEM models using chi-square difference test
    """

    # Fit base model
    base_model = SEMModel(df, base_model_spec)
    base_model.fit_model()
    base_fit = base_model.get_fit_indices()

    # Fit alternative model
    alt_model = SEMModel(df, alternative_model_spec)
    alt_model.fit_model()
    alt_fit = alt_model.get_fit_indices()

    # Chi-square difference test
    chi2_diff = base_fit['chi_square'] - alt_fit['chi_square']
    df_diff = base_fit['df'] - alt_fit['df']
    p_value_diff = 1 - stats.chi2.cdf(chi2_diff, df_diff)

    # Model comparison results
    comparison = {
        'base_model': {
            'chi2': base_fit['chi_square'],
            'df': base_fit['df'],
            'aic': base_fit['aic'],
            'bic': base_fit['bic'],
            'cfi': base_fit['cfi'],
            'rmsea': base_fit['rmsea']
        },
        'alternative_model': {
            'chi2': alt_fit['chi_square'],
            'df': alt_fit['df'],
            'aic': alt_fit['aic'],
            'bic': alt_fit['bic'],
            'cfi': alt_fit['cfi'],
            'rmsea': alt_fit['rmsea']
        },
        'difference_test': {
            'chi2_difference': chi2_diff,
            'df_difference': df_diff,
            'p_value': p_value_diff,
            'significant_improvement': p_value_diff < 0.05
        },
        'recommended_model': 'alternative' if p_value_diff < 0.05 else 'base'
    }

    return comparison
```

## Advanced SEM Techniques

### Mediation Analysis

```python
def mediation_analysis(df, predictor, mediator, outcome, covariates=None):
    """
    Comprehensive mediation analysis using SEM
    """

    # Build mediation model specification
    model_spec = f"""
    # Direct and indirect paths
    {mediator} ~ a*{predictor}
    {outcome} ~ b*{mediator} + c*{predictor}

    # Defined parameters
    indirect := a*b
    total := c + (a*b)
    """

    # Add covariates if specified
    if covariates:
        for covariate in covariates:
            model_spec += f"\n{mediator} ~ {covariate}"
            model_spec += f"\n{outcome} ~ {covariate}"

    # Fit mediation model
    mediation_model = SEMModel(df, model_spec)
    mediation_model.fit_model()

    # Extract path coefficients and significance
    estimates = semopy.inspect(mediation_model.model, mode='est')

    # Calculate mediation effects
    results = {
        'direct_effect': estimates[estimates['lval'] == outcome]['est'].iloc[0],
        'indirect_effect': estimates[estimates['label'] == 'indirect']['est'].iloc[0],
        'total_effect': estimates[estimates['label'] == 'total']['est'].iloc[0],
        'model_fit': mediation_model.get_fit_indices(),
        'full_results': estimates
    }

    return results

def moderated_mediation_analysis(df, predictor, mediator, outcome, moderator):
    """
    Moderated mediation analysis (conditional indirect effects)
    """

    # Create interaction terms
    df['pred_mod'] = df[predictor] * df[moderator]
    df['med_mod'] = df[mediator] * df[moderator]

    model_spec = f"""
    # Moderated mediation model
    {mediator} ~ a1*{predictor} + a3*{moderator} + a4*pred_mod
    {outcome} ~ b1*{mediator} + b3*med_mod + c1*{predictor} + c2*{moderator}

    # Conditional indirect effects (at high and low moderator values)
    indirect_low := (a1 + a4*(-1)) * (b1 + b3*(-1))
    indirect_high := (a1 + a4*(1)) * (b1 + b3*(1))

    # Index of moderated mediation
    index_modmed := a4*b3
    """

    modmed_model = SEMModel(df, model_spec)
    modmed_model.fit_model()

    estimates = semopy.inspect(modmed_model.model, mode='est')

    return {
        'conditional_indirect_effects': {
            'low_moderator': estimates[estimates['label'] == 'indirect_low']['est'].iloc[0],
            'high_moderator': estimates[estimates['label'] == 'indirect_high']['est'].iloc[0]
        },
        'index_moderated_mediation': estimates[estimates['label'] == 'index_modmed']['est'].iloc[0],
        'model_fit': modmed_model.get_fit_indices(),
        'full_results': estimates
    }
```

### Multi-Group SEM

```python
def multigroup_sem_analysis(df, group_variable, base_model_spec):
    """
    Multi-group SEM with measurement invariance testing
    """

    # Get unique groups
    groups = df[group_variable].unique()
    groups = [g for g in groups if pd.notna(g)]

    results = {
        'configural_invariance': {},
        'metric_invariance': {},
        'scalar_invariance': {},
        'group_comparisons': {}
    }

    # Step 1: Configural invariance (same factor structure)
    configural_models = {}
    for group in groups:
        group_data = df[df[group_variable] == group]
        group_model = SEMModel(group_data, base_model_spec)
        group_model.fit_model()
        configural_models[group] = {
            'model': group_model,
            'fit_indices': group_model.get_fit_indices(),
            'n_obs': len(group_data)
        }

    results['configural_invariance'] = configural_models

    # Step 2: Metric invariance (equal factor loadings)
    # This requires constraining factor loadings across groups
    # Implementation depends on specific semopy capabilities

    # Step 3: Scalar invariance (equal intercepts)
    # This requires constraining intercepts across groups

    # Group comparisons of parameter estimates
    for group in groups:
        group_estimates = semopy.inspect(configural_models[group]['model'].model, mode='est')
        results['group_comparisons'][group] = group_estimates

    return results

def test_measurement_invariance(df, group_variable, latent_factors):
    """
    Systematic measurement invariance testing
    """

    invariance_results = {
        'configural': None,
        'metric': None,
        'scalar': None,
        'model_comparisons': {}
    }

    # Base measurement model
    measurement_model = ""
    for factor, indicators in latent_factors.items():
        factor_spec = f"{factor} =~ " + " + ".join(indicators) + "\n"
        measurement_model += factor_spec

    # Test configural invariance
    groups = df[group_variable].unique()
    configural_fit_overall = 0
    configural_df_overall = 0

    for group in groups:
        if pd.notna(group):
            group_data = df[df[group_variable] == group]
            group_model = SEMModel(group_data, measurement_model)
            group_model.fit_model()
            group_fit = group_model.get_fit_indices()

            configural_fit_overall += group_fit['chi_square']
            configural_df_overall += group_fit['df']

    invariance_results['configural'] = {
        'chi_square': configural_fit_overall,
        'df': configural_df_overall,
        'interpretation': 'Same factor structure across groups'
    }

    # Note: Full metric and scalar invariance testing requires more
    # sophisticated constraint specification in semopy

    return invariance_results
```

### Longitudinal SEM

```python
def longitudinal_sem_analysis(df, time_points, measurement_variables):
    """
    Longitudinal SEM analysis (autoregressive cross-lagged model)
    """

    # Build autoregressive cross-lagged model
    model_spec = ""

    # Measurement models for each time point
    for t in time_points:
        for construct, indicators in measurement_variables.items():
            time_indicators = [f"{ind}_t{t}" for ind in indicators]
            model_spec += f"{construct}_t{t} =~ " + " + ".join(time_indicators) + "\n"

    # Autoregressive paths (stability)
    for construct in measurement_variables.keys():
        for t in range(1, len(time_points)):
            model_spec += f"{construct}_t{time_points[t]} ~ {construct}_t{time_points[t-1]}\n"

    # Cross-lagged paths (cross-construct influence)
    constructs = list(measurement_variables.keys())
    for i, construct1 in enumerate(constructs):
        for j, construct2 in enumerate(constructs):
            if i != j:  # Different constructs
                for t in range(1, len(time_points)):
                    model_spec += f"{construct2}_t{time_points[t]} ~ {construct1}_t{time_points[t-1]}\n"

    # Contemporaneous correlations
    for t in time_points:
        for i, construct1 in enumerate(constructs):
            for j, construct2 in enumerate(constructs):
                if i < j:  # Avoid duplicate correlations
                    model_spec += f"{construct1}_t{t} ~~ {construct2}_t{t}\n"

    # Fit longitudinal model
    long_model = SEMModel(df, model_spec)
    long_model.fit_model()

    return {
        'model_specification': model_spec,
        'fit_indices': long_model.get_fit_indices(),
        'parameter_estimates': semopy.inspect(long_model.model, mode='est'),
        'model_object': long_model
    }
```

## Model Modification and Improvement

```python
def model_modification_analysis(sem_model):
    """
    Analyze modification indices and suggest model improvements
    """

    # Get modification indices
    mod_indices = semopy.inspect(sem_model.model, mode='mi')

    # Sort by modification index value
    mod_indices_sorted = mod_indices.sort_values('mi', ascending=False)

    # Identify high modification indices (> 3.84, chi-square critical value)
    high_mi = mod_indices_sorted[mod_indices_sorted['mi'] > 3.84]

    suggestions = {
        'high_modification_indices': high_mi,
        'suggested_modifications': [],
        'theoretical_considerations': []
    }

    # Generate specific suggestions
    for idx, row in high_mi.iterrows():
        if row['op'] == '~~':  # Covariance
            suggestion = f"Consider adding covariance between {row['lval']} and {row['rval']}"
            suggestions['suggested_modifications'].append(suggestion)
            suggestions['theoretical_considerations'].append(
                f"Ensure theoretical justification for {row['lval']} ~~ {row['rval']} correlation"
            )
        elif row['op'] == '=~':  # Factor loading
            suggestion = f"Consider cross-loading: {row['lval']} =~ {row['rval']}"
            suggestions['suggested_modifications'].append(suggestion)
            suggestions['theoretical_considerations'].append(
                f"Cross-loading may indicate multidimensional construct or method effects"
            )

    return suggestions

def automated_model_improvement(df, initial_model_spec, max_modifications=3):
    """
    Automated model improvement through modification indices
    """

    current_model_spec = initial_model_spec
    improvement_history = []

    for iteration in range(max_modifications):
        # Fit current model
        current_model = SEMModel(df, current_model_spec)
        current_model.fit_model()
        current_fit = current_model.get_fit_indices()

        # Check if model fit is acceptable
        fit_eval = current_model.evaluate_fit(current_fit)
        if fit_eval['overall_fit'] in ['excellent', 'acceptable']:
            break

        # Get modification suggestions
        mod_suggestions = model_modification_analysis(current_model)

        if not mod_suggestions['suggested_modifications']:
            break

        # Apply the highest modification index suggestion
        # This is a simplified implementation - real applications need careful theoretical consideration
        highest_mi = mod_suggestions['high_modification_indices'].iloc[0]

        if highest_mi['op'] == '~~':
            new_spec = f"{highest_mi['lval']} ~~ {highest_mi['rval']}"
            current_model_spec += f"\n{new_spec}"

            improvement_history.append({
                'iteration': iteration + 1,
                'modification': new_spec,
                'mi_value': highest_mi['mi'],
                'fit_before': current_fit
            })

    # Final model fit
    final_model = SEMModel(df, current_model_spec)
    final_model.fit_model()
    final_fit = final_model.get_fit_indices()

    return {
        'final_model_spec': current_model_spec,
        'final_fit_indices': final_fit,
        'improvement_history': improvement_history,
        'final_model_object': final_model
    }
```

## Visualization and Reporting

```python
def create_sem_path_diagram(sem_model, output_file=None):
    """
    Create path diagram visualization of SEM model
    """

    # This is a conceptual implementation
    # Actual implementation would use graphviz or similar
    import matplotlib.pyplot as plt
    import networkx as nx

    # Extract model structure
    estimates = semopy.inspect(sem_model.model, mode='est')

    # Create directed graph
    G = nx.DiGraph()

    # Add nodes and edges based on model structure
    for idx, row in estimates.iterrows():
        if row['op'] == '=~':  # Factor loadings
            G.add_edge(row['lval'], row['rval'], weight=row['est'], edge_type='loading')
        elif row['op'] == '~':  # Regressions
            G.add_edge(row['rval'], row['lval'], weight=row['est'], edge_type='regression')

    # Create layout
    pos = nx.spring_layout(G, k=2, iterations=50)

    # Draw the graph
    plt.figure(figsize=(12, 8))

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=1500)
    nx.draw_networkx_labels(G, pos, font_size=10)

    # Draw edges with different styles for different types
    loading_edges = [(u, v) for u, v, d in G.edges(data=True) if d['edge_type'] == 'loading']
    regression_edges = [(u, v) for u, v, d in G.edges(data=True) if d['edge_type'] == 'regression']

    nx.draw_networkx_edges(G, pos, edgelist=loading_edges, edge_color='blue', style='dashed')
    nx.draw_networkx_edges(G, pos, edgelist=regression_edges, edge_color='red', style='solid')

    plt.title("SEM Path Diagram")
    plt.axis('off')

    if output_file:
        plt.savefig(output_file, dpi=300, bbox_inches='tight')

    plt.show()

def generate_sem_report(sem_model, model_name="SEM Analysis"):
    """
    Generate comprehensive SEM analysis report
    """

    fit_indices = sem_model.get_fit_indices()
    fit_evaluation = sem_model.evaluate_fit(fit_indices)
    estimates = semopy.inspect(sem_model.model, mode='est', std_est=True)

    report = f"""
# {model_name} - Structural Equation Modeling Report

## Model Specification
```
{sem_model.model_spec}
```

## Model Fit Assessment

### Fit Indices
- Chi-square: {fit_indices['chi_square']:.3f} (df = {fit_indices['df']}, p = {fit_indices['p_value']:.3f})
- CFI: {fit_indices['cfi']:.3f}
- TLI: {fit_indices['tli']:.3f}
- RMSEA: {fit_indices['rmsea']:.3f} [{fit_indices['rmsea_ci_lower']:.3f}, {fit_indices['rmsea_ci_upper']:.3f}]
- SRMR: {fit_indices['srmr']:.3f}
- AIC: {fit_indices['aic']:.1f}
- BIC: {fit_indices['bic']:.1f}

### Fit Evaluation
- Overall Fit: {fit_evaluation['overall_fit'].upper()}
- CFI/TLI Assessment: {fit_evaluation['component_fit']['cfi_tli']}
- RMSEA Assessment: {fit_evaluation['component_fit']['rmsea']}
- SRMR Assessment: {fit_evaluation['component_fit']['srmr']}

### Recommendations
"""

    for rec in fit_evaluation['recommendations']:
        report += f"- {rec}\n"

    report += f"""

## Parameter Estimates

### Factor Loadings
"""

    loadings = estimates[estimates['op'] == '=~']
    for idx, row in loadings.iterrows():
        report += f"- {row['lval']} -> {row['rval']}: {row['est']:.3f} (SE = {row['se']:.3f}, p = {row['p_value']:.3f})\n"

    report += """
### Structural Paths
"""

    paths = estimates[estimates['op'] == '~']
    for idx, row in paths.iterrows():
        report += f"- {row['rval']} -> {row['lval']}: {row['est']:.3f} (SE = {row['se']:.3f}, p = {row['p_value']:.3f})\n"

    return report
```

## Memory Consolidation Points

**Key Learnings**:
- SEM provides comprehensive framework for testing complex theoretical models
- Python implementation through semopy offers most essential SEM capabilities
- Model fit assessment requires multiple indices and theoretical consideration
- Advanced techniques (mediation, multi-group, longitudinal) extend basic SEM framework

**Implementation Expertise**:
- Model specification using lavaan-style syntax
- Comprehensive fit assessment and model comparison
- Automated model improvement with theoretical safeguards
- Advanced techniques for complex research questions

**Integration Points**:
- Links to SCALE-DEVELOPMENT-VALIDATION.md for measurement model development
- Connects with survey analysis workflows for complete customer satisfaction modeling
- Supports advanced statistical reporting and visualization needs
- Enables sophisticated business intelligence through structural modeling

**Areas for Advanced Development**:
- Bayesian SEM implementation
- Mixture modeling and latent class analysis
- Advanced missing data handling in SEM context
- Integration with machine learning approaches for hybrid modeling
