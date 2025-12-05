"""
Visualization Module for RAS Financial Models
Generates charts and graphs for financial analysis
"""

from typing import List, Dict, Optional
import json


class FinancialVisualizer:
    """Create text-based visualizations for financial models"""
    
    @staticmethod
    def create_bar_chart(data: List[float], labels: List[str], title: str, width: int = 60) -> str:
        """Create a simple text-based bar chart"""
        max_val = max(data) if data else 1
        min_val = min(data) if data else 0
        
        chart = [f"\n{title}", "=" * width]
        
        for label, value in zip(labels, data):
            # Calculate bar length
            if max_val != min_val:
                bar_len = int((value - min_val) / (max_val - min_val) * (width - 25))
            else:
                bar_len = 0
            
            bar = "█" * max(0, bar_len)
            chart.append(f"{label:<12} │{bar} {value:>12,.0f}")
        
        return "\n".join(chart)
    
    @staticmethod
    def create_cash_flow_waterfall(metrics: List[Dict], max_years: int = 10) -> str:
        """Create text representation of cash flow waterfall"""
        output = ["\n💰 CASH FLOW WATERFALL", "=" * 80]
        
        for i, m in enumerate(metrics[:max_years + 1]):
            year = m['year']
            cf = m['cash_flow']
            cum_cf = m['cumulative_cash_flow']
            
            # Create visual representation
            bar_width = 40
            if i == 0:
                bar = "▼" * min(bar_width, int(abs(cf) / 100000))
                output.append(f"Year {year:>2} │ {bar} ${cf:>15,.0f} │ Cumulative: ${cum_cf:>15,.0f}")
            else:
                if cf > 0:
                    bar = "▲" * min(bar_width, int(cf / 100000))
                else:
                    bar = "▼" * min(bar_width, int(abs(cf) / 100000))
                
                marker = "+" if cum_cf >= 0 else "-"
                output.append(f"Year {year:>2} │ {bar} ${cf:>15,.0f} │ [{marker}] ${cum_cf:>15,.0f}")
        
        return "\n".join(output)
    
    @staticmethod
    def create_profitability_dashboard(summary: Dict) -> str:
        """Create a dashboard view of key profitability metrics"""
        perf = summary.get('financial_performance', {})
        inv = summary.get('investment_summary', {})
        prod = summary.get('production_metrics', {})
        
        dashboard = [
            "\n" + "=" * 80,
            "📊 FINANCIAL DASHBOARD",
            "=" * 80,
            "",
            "┌─────────────────────────────────────────────────────────────────────────────┐",
            "│ KEY INVESTMENT METRICS                                                      │",
            "├─────────────────────────────────────────────────────────────────────────────┤",
            f"│  Total Investment:        ${inv.get('total_capex', 0):>20,.2f}                      │",
            f"│  Equity Required:         ${inv.get('equity_investment', 0):>20,.2f}                      │",
            f"│  Debt Financing:          ${inv.get('debt_financing', 0):>20,.2f}                      │",
            "└─────────────────────────────────────────────────────────────────────────────┘",
            "",
            "┌─────────────────────────────────────────────────────────────────────────────┐",
            "│ RETURN METRICS                                                              │",
            "├─────────────────────────────────────────────────────────────────────────────┤",
            f"│  NPV @ 12%:               ${perf.get('npv_at_12_percent', 0):>20,.2f}                      │",
            f"│  Internal Rate of Return: {perf.get('irr_percent', 0):>20.2f}%                     │",
            f"│  Payback Period:          {perf.get('payback_period_years', 0):>20.2f} years                │",
            "└─────────────────────────────────────────────────────────────────────────────┘",
            "",
            "┌─────────────────────────────────────────────────────────────────────────────┐",
            "│ OPERATIONAL METRICS (Annual Average)                                        │",
            "├─────────────────────────────────────────────────────────────────────────────┤",
            f"│  Revenue:                 ${perf.get('average_annual_revenue', 0):>20,.2f}                      │",
            f"│  EBITDA:                  ${perf.get('average_annual_ebitda', 0):>20,.2f}                      │",
            f"│  EBITDA Margin:           {perf.get('average_ebitda_margin_percent', 0):>20.2f}%                     │",
            f"│  Net Income:              ${perf.get('average_annual_net_income', 0):>20,.2f}                      │",
            "└─────────────────────────────────────────────────────────────────────────────┘",
            "",
            "┌─────────────────────────────────────────────────────────────────────────────┐",
            "│ PRODUCTION METRICS                                                          │",
            "├─────────────────────────────────────────────────────────────────────────────┤",
            f"│  Annual Production:       {prod.get('annual_production_kg', 0):>20,.2f} kg                  │",
            f"│  Production Cycles/Year:  {prod.get('production_cycles_per_year', 0):>20.1f}                       │",
            f"│  Survival Rate:           {prod.get('survival_rate_percent', 0):>20.2f}%                     │",
            f"│  Feed Conversion Ratio:   {prod.get('feed_conversion_ratio', 0):>20.2f}                       │",
            "└─────────────────────────────────────────────────────────────────────────────┘",
            "=" * 80,
        ]
        
        return "\n".join(dashboard)
    
    @staticmethod
    def create_sensitivity_table(sensitivity_results: List[Dict], parameter_name: str) -> str:
        """Create formatted sensitivity analysis table"""
        output = [
            f"\n🔍 SENSITIVITY ANALYSIS: {parameter_name}",
            "=" * 80,
            f"{'Variation':<12} {'Value':<20} {'NPV ($)':<20} {'IRR (%)':<15} {'Payback':<15}",
            "-" * 80
        ]
        
        for result in sensitivity_results:
            var = result['multiplier']
            val = result['parameter_value']
            npv = result['npv']
            irr = result['irr'] * 100
            pb = result['payback_period']
            
            output.append(
                f"{var:>8.0%}    "
                f"{val:<20.2f} "
                f"${npv:>18,.0f} "
                f"{irr:>13.2f}% "
                f"{pb:>13.2f} yrs"
            )
        
        return "\n".join(output)


class ReportGenerator:
    """Generate comprehensive PDF-ready reports"""
    
    @staticmethod
    def generate_executive_summary(model) -> str:
        """Generate executive summary text"""
        summary = model.generate_summary_report()
        visualizer = FinancialVisualizer()
        
        output = [
            "\n" + "=" * 80,
            "EXECUTIVE SUMMARY",
            "RAS Fish Farming Financial Analysis",
            "=" * 80,
            "",
            "PROJECT OVERVIEW",
            "-" * 80,
        ]
        
        proj = summary['project_summary']
        output.extend([
            f"Model Date: {proj['model_date'][:10]}",
            f"Project Duration: {proj['project_years']} years",
            f"System Capacity: {proj['system_volume_m3']:,.0f} cubic meters",
            f"Annual Production: {proj['annual_production_kg']:,.0f} kg ({proj['annual_production_kg']/1000:.1f} tonnes)",
        ])
        
        # Add dashboard
        output.append(visualizer.create_profitability_dashboard(summary))
        
        # Add cash flow waterfall
        output.append(visualizer.create_cash_flow_waterfall(summary['year_by_year_metrics']))
        
        # Investment recommendation
        output.extend([
            "",
            "=" * 80,
            "INVESTMENT RECOMMENDATION",
            "=" * 80,
            ""
        ])
        
        perf = summary['financial_performance']
        npv = perf['npv_at_12_percent']
        irr = perf['irr_percent']
        payback = perf['payback_period_years']
        
        if npv > 0 and irr > 15 and payback < 7:
            recommendation = "STRONG BUY"
            rationale = "Project shows strong financial returns with positive NPV, high IRR, and reasonable payback period."
        elif npv > 0 and irr > 12:
            recommendation = "BUY"
            rationale = "Project is financially viable with acceptable returns."
        elif npv > 0:
            recommendation = "CONSIDER"
            rationale = "Project is marginally profitable. Consider optimization opportunities."
        else:
            recommendation = "REJECT"
            rationale = "Project does not meet minimum financial requirements."
        
        output.extend([
            f"Recommendation: {recommendation}",
            f"Rationale: {rationale}",
            "",
            "Key Strengths:",
        ])
        
        if irr > 15:
            output.append("  ✓ Excellent internal rate of return")
        if payback < 6:
            output.append("  ✓ Quick payback period")
        if perf['average_ebitda_margin_percent'] > 30:
            output.append("  ✓ Strong operational margins")
        
        output.extend([
            "",
            "=" * 80,
        ])
        
        return "\n".join(output)
    
    @staticmethod
    def generate_full_report(model, include_sensitivity: bool = True) -> str:
        """Generate complete financial analysis report"""
        output = [ReportGenerator.generate_executive_summary(model)]
        
        if include_sensitivity:
            output.append("\n\n" + "=" * 80)
            output.append("SENSITIVITY ANALYSIS")
            output.append("=" * 80)
            
            # Run multiple sensitivity analyses
            visualizer = FinancialVisualizer()
            
            # Fish price sensitivity
            price_sens = model.sensitivity_analysis('fish_price_per_kg', [0.8, 0.9, 1.0, 1.1, 1.2])
            output.append(visualizer.create_sensitivity_table(price_sens, "Fish Price per kg"))
            
            # Survival rate sensitivity
            survival_sens = model.sensitivity_analysis('survival_rate', [0.85, 0.90, 0.92, 0.95, 0.98])
            output.append(visualizer.create_sensitivity_table(survival_sens, "Survival Rate"))
            
            # FCR sensitivity
            fcr_sens = model.sensitivity_analysis('feed_conversion_ratio', [1.4, 1.3, 1.2, 1.1, 1.0])
            output.append(visualizer.create_sensitivity_table(fcr_sens, "Feed Conversion Ratio"))
        
        return "\n".join(output)


def main():
    """Example usage of visualization tools"""
    from ras_financial_model import create_default_model
    
    print("Generating Financial Report...")
    
    model = create_default_model()
    report_gen = ReportGenerator()
    
    # Generate full report
    full_report = report_gen.generate_full_report(model, include_sensitivity=True)
    print(full_report)
    
    # Save to file
    with open('ras_financial_report.txt', 'w') as f:
        f.write(full_report)
    
    print("\n\n✅ Full report saved to: ras_financial_report.txt")


if __name__ == "__main__":
    main()
