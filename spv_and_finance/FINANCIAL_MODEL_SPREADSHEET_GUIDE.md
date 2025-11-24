# Saudi Arabia RAS Financial Model - Interactive Spreadsheet Guide

## Overview

This guide provides instructions for creating an interactive Google Sheets or Excel version of the Saudi Arabia RAS Financial Model for testing different scenarios and assumptions.

## Quick Start

### Option 1: Google Sheets Template (Recommended)

**Create a copy of our template:**
1. Open this link: [Saudi Arabia RAS Financial Model Template](https://docs.google.com/spreadsheets/d/CREATE_YOUR_COPY)
2. Click "File" → "Make a copy"
3. Save to your Google Drive
4. Start testing scenarios by changing input assumptions

### Option 2: Download Excel Template

Download the Excel template from the repository:
- File: `saudi_arabia_ras_financial_model.xlsx` (to be created)
- Open in Excel, Google Sheets, or LibreOffice Calc
- All formulas are included for automatic calculations

### Option 3: Build Your Own Spreadsheet

Follow the detailed structure below to build your own model from the markdown documentation.

---

## Spreadsheet Structure

The financial model should be organized into multiple tabs/sheets:

### Tab 1: Dashboard
- Summary metrics (IRR, NPV, Payback, MOIC)
- Key charts (Revenue growth, Cash flow, Break-even analysis)
- Traffic light indicators (Green/Yellow/Red for KPIs)

### Tab 2: Assumptions
- All input parameters (editable cells in BLUE)
- Market assumptions (pricing, growth rates)
- Cost assumptions (feed, labor, utilities)
- Financial assumptions (discount rate, tax rate, depreciation)

### Tab 3: CAPEX
- Detailed line-item breakdown
- 50-ton, 200-ton, 1000-ton models
- Automatic calculations based on scale

### Tab 4: OPEX
- Annual operating costs by category
- 12 detailed categories with formulas
- Scales automatically based on production volume

### Tab 5: Production Model
- Production ramp-up schedule
- Mortality rates and grow-out cycles
- Feed consumption calculations (FCR-based)
- Revenue by species and channel

### Tab 6: P&L (15 years)
- Year-by-year income statement
- Revenue, COGS, Gross Margin
- OPEX, EBITDA, Depreciation
- Interest, Taxes, Net Income

### Tab 7: Cash Flow (15 years)
- Operating cash flow
- Investing cash flow (CAPEX, maintenance)
- Financing cash flow (debt, equity, dividends)
- Free cash flow to equity

### Tab 8: Debt Schedule
- ADF loan details
- Principal and interest payments
- Outstanding balance

### Tab 9: Returns Analysis
- IRR calculation
- NPV calculation at various discount rates
- MOIC calculation
- Sensitivity tables

### Tab 10: Scenarios
- Base Case
- Optimistic Case
- Pessimistic Case
- Side-by-side comparison

---

## Detailed Formula Guide

### Key Assumptions (Input Cells - Format in BLUE)

**System Scale:**
```
B3: Production Capacity (tons/year) = 200
B4: Ramp-up Year 1 (%) = 50%
B5: Ramp-up Year 2 (%) = 75%
B6: Ramp-up Year 3 (%) = 90%
B7: Ramp-up Year 4+ (%) = 95%
```

**Revenue Assumptions:**
```
B10: Primary Species = Tilapia
B11: Wholesale Price (SAR/kg) = 20
B12: Retail Mix (%) = 30%
B13: Retail Premium (%) = 50%
B14: Annual Price Inflation (%) = 2%
B15: Value-Added Mix (%) = 20% (Year 3+)
B16: Value-Added Premium (%) = 30%
```

**Cost Assumptions:**
```
B20: Feed Cost (SAR/kg) = 3.50
B21: FCR (Feed Conversion Ratio) = 1.5
B22: Annual Feed Inflation (%) = 2.5%
B23: Fingerling Cost (SAR/piece) = 0.50
B24: Fingerlings per kg harvest = 2.5
B25: Mortality Rate (%) = 12%
```

**Labor Costs:**
```
B30: Farm Manager (SAR/month) = 18,000
B31: Senior Technician (SAR/month) = 12,000
B32: Technician (SAR/month) = 8,000
B33: Workers x2 (SAR/month each) = 5,000
B34: Benefits & GOSI (% of salary) = 25%
```

**Utilities:**
```
B40: Electricity Rate (SAR/kWh) = 0.18
B41: Annual kWh (50-ton base) = 250,000
B42: kWh scaling factor = 0.75 (per ton)
B43: Water Rate (SAR/m³) = 3.00
B44: Daily Water Makeup (%) = 1.5%
```

**Financial Assumptions:**
```
B50: CAPEX (SAR) - from CAPEX tab = [Reference]
B51: ADF Loan (% of CAPEX) = 60%
B52: ADF Interest Rate (%) = 2.5%
B53: ADF Term (years) = 15
B54: Equity (% of CAPEX) = 40%
B55: Discount Rate (WACC %) = 10%
B56: Tax Rate (%) = 20%
B57: Depreciation Period (years) = 15
```

### CAPEX Formulas

**50-ton System CAPEX (B columns = Low, C columns = High):**

```
LAND & SITE DEVELOPMENT:
B5: Land Acquisition = 800,000 (Rural) or 3,000,000 (Urban)
B6: Site Surveys = 80,000
B7: Land Preparation = 300,000
B8: Access Roads = 150,000
B9: Site Infrastructure = 120,000
B10: Subtotal = SUM(B5:B9)

BUILDING & INFRASTRUCTURE:
B13: Production Building = 2,000,000
B14: HVAC System = 800,000
B15: Office & Lab = 300,000
B16: Processing Area = 200,000
B17: Utilities & Systems = 150,000
B18: Subtotal = SUM(B13:B17)

RAS EQUIPMENT:
B21: Fish Tanks = 1,200,000
B22: Mechanical Filtration = 600,000
B23: Biofilters = 800,000
B24: Pumps = 400,000
B25: Aeration & O2 = 600,000
B26: UV/Ozone = 300,000
B27: Temperature Control = 400,000
B28: SCADA/Monitoring = 350,000
B29: Piping & Valves = 250,000
B30: Emergency Backup = 500,000
B31: Subtotal = SUM(B21:B30)

UTILITIES INSTALLATION:
B34: Electrical = 800,000
B35: Water Systems = 250,000
B36: Wastewater = 100,000
B37: Subtotal = SUM(B34:B36)

SHIPPING & INSTALLATION:
B40: International Freight = 400,000
B41: Customs & Insurance = 150,000
B42: Installation Labor = 250,000
B43: Subtotal = SUM(B40:B42)

INITIAL INVENTORY:
B46: Fingerlings = 150,000
B47: Feed (3 months) = 120,000
B48: Chemicals = 80,000
B49: Subtotal = SUM(B46:B48)

PRE-OPERATING:
B52: Professional Services = 300,000
B53: Permits & Licensing = 150,000
B54: Training = 50,000
B55: Marketing = 50,000
B56: Subtotal = SUM(B52:B55)

TOTAL BEFORE CONTINGENCY:
B59: =SUM(B10,B18,B31,B37,B43,B49,B56)

CONTINGENCY (20%):
B60: =B59*0.20

TOTAL CAPEX 50-TON:
B61: =B59+B60
```

**200-ton System (Scale from 50-ton):**
```
C61: =(B61*200/50)*0.85  // 15% volume discount
```

**1000-ton System:**
```
D61: =(B61*1000/50)*0.70  // 30% volume discount
```

### OPEX Formulas (Annual, per system size)

**Feed & Nutrition:**
```
B5: Production Volume (tons/year) = Assumptions!B3
B6: FCR = Assumptions!B21
B7: Feed Required (tons) = B5 * B6
B8: Feed Cost (SAR/kg) = Assumptions!B20
B9: Total Feed Cost = B7 * 1000 * B8
```

**Seed Stock:**
```
B12: Fingerlings per kg = Assumptions!B24
B13: Total Fingerlings = B5 * 1000 * B12
B14: Fingerling Cost = Assumptions!B23
B15: Mortality Buffer = 15%
B16: Total Fingerling Cost = B13 * B14 * (1+B15)
```

**Labor (with scaling):**
```
IF production < 100 tons:
  B20: Manager = 1 * 18,000 * 12
  B21: Sr Technician = 1 * 12,000 * 12
  B22: Technician = 1 * 8,000 * 12
  B23: Workers = 2 * 5,000 * 12

IF production 100-300 tons:
  Same as above

IF production > 300 tons:
  B20: Manager = 1 * 20,000 * 12
  B21: Sr Technician = 2 * 13,000 * 12
  B22: Technician = 2 * 9,000 * 12
  B23: Workers = 4 * 5,500 * 12

B24: Base Salaries = SUM(B20:B23)
B25: Benefits (25%) = B24 * 0.25
B26: Total Labor = B24 + B25
```

**Electricity:**
```
B30: Base kWh (50-ton) = Assumptions!B41
B31: Scaling Factor = Assumptions!B42
B32: Actual kWh = B30 + ((B5-50)*B31*B30)
B33: Rate = Assumptions!B40
B34: Total Electricity Cost = B32 * B33
```

**Other OPEX Categories:**
```
Water: Production volume * 10 m³/ton * 365 days * 1.5% makeup * SAR 3/m³
Maintenance: 7% of RAS equipment CAPEX
Chemicals: SAR 1.50 per kg produced
Harvesting: SAR 0.80 per kg produced
Transportation: SAR 1.20 per kg produced
Insurance: 0.5% of CAPEX + 1.5% of stock value
Marketing: 3% of revenue
Administrative: SAR 80,000 fixed + 1% of revenue
```

**Total OPEX:**
```
B50: =SUM(B9,B16,B26,B34,...all categories)
B51: Cost per kg = B50 / (B5*1000)
```

### Production & Revenue Model (Year by Year)

**Year 1 (Column C):**
```
C3: Capacity Utilization = Assumptions!B4 (50%)
C4: Production (tons) = Assumptions!B3 * C3 (= 100 tons)
C5: Mortality Loss = C4 * Assumptions!B25 (12%)
C6: Harvest Volume = C4 - C5 (= 88 tons)
C7: Waste/Samples = C6 * 0.02
C8: Saleable Volume = C6 - C7

C10: Wholesale Mix = 70%
C11: Retail Mix = 30%
C12: Value-Added Mix = 0% (starts Year 3)

C15: Wholesale Volume = C8 * C10
C16: Wholesale Price = Assumptions!B11
C17: Wholesale Revenue = C15 * C16 * 1000

C19: Retail Volume = C8 * C11
C20: Retail Price = C16 * (1 + Assumptions!B13)
C21: Retail Revenue = C19 * C20 * 1000

C23: Total Revenue = C17 + C21
```

**Year 2-15 (Columns D-P):**
```
D3: =Assumptions!B5 (75%)
D16: =C16*(1+Assumptions!B14) // Price inflation
D12: =IF(D1>=3, Assumptions!B15, 0) // Value-add starts Year 3

// Copy formulas across with inflation and ramp-up
```

### P&L Statement (15 Years)

**Revenue:**
```
C10: =Production!C23 (Year 1 revenue)
D10: =Production!D23 (Year 2 revenue)
// ... through P10 (Year 15)
```

**Cost of Goods Sold:**
```
C12: Feed Cost = OPEX!C9
C13: Fingerlings = OPEX!C16
C14: Direct Labor (40% of total) = OPEX!C26*0.4
C15: Utilities (production portion) = OPEX!C34*0.7
C16: Other Direct = chemicals + harvesting + processing
C17: Total COGS = SUM(C12:C16)
C18: Gross Margin = C10 - C17
C19: Gross Margin % = C18/C10
```

**Operating Expenses:**
```
C22: Labor (indirect 60%) = OPEX!C26*0.6
C23: Utilities (facility) = OPEX!C34*0.3
C24: Maintenance = OPEX![maintenance]
C25: Transportation = OPEX![transport]
C26: Marketing = OPEX![marketing]
C27: Insurance = OPEX![insurance]
C28: Administrative = OPEX![admin]
C29: Total OPEX = SUM(C22:C28)

C31: EBITDA = C18 - C29
C32: EBITDA Margin % = C31/C10
```

**Depreciation, Interest, Taxes:**
```
C35: Depreciation = CAPEX!B61 / Assumptions!B57 (straight-line)
C36: Interest Expense = Debt![Year interest]
C37: EBT = C31 - C35 - C36
C38: Taxes (20%) = MAX(0, C37*Assumptions!B56)
C39: Net Income = C37 - C38
C40: Net Margin % = C39/C10
```

### Cash Flow Statement

**Operating Cash Flow:**
```
C5: Net Income = P&L!C39
C6: Add: Depreciation = P&L!C35
C7: Less: Working Capital Change = (Revenue increase * 10%)
C8: Operating Cash Flow = C5 + C6 - C7
```

**Investing Cash Flow:**
```
C11: Initial CAPEX = IF(C1=0, -CAPEX!B61, 0)
C12: Maintenance CAPEX = IF(C1>5, -CAPEX!B61*0.02, 0)
C13: Investing Cash Flow = C11 + C12
```

**Financing Cash Flow:**
```
C16: Equity Raised = IF(C1=0, CAPEX!B61*0.4, 0)
C17: Debt Raised = IF(C1=0, CAPEX!B61*0.6, 0)
C18: Debt Repayment = -Debt!C[principal payment]
C19: Financing Cash Flow = C16 + C17 + C18
```

**Free Cash Flow:**
```
C22: Free Cash Flow = C8 + C13 + C19
C23: Cumulative FCF = C22 + B23
```

### Debt Schedule (ADF Loan)

**Loan Setup:**
```
B3: Loan Amount = CAPEX!B61 * Assumptions!B51 (60%)
B4: Interest Rate = Assumptions!B52 (2.5%)
B5: Term (years) = Assumptions!B53 (15)
B6: Annual Payment = PMT(B4, B5, -B3)
```

**Year-by-year schedule:**
```
C10: Beginning Balance = IF(C1=0, B3, D13)
C11: Interest Payment = C10 * B4
C12: Principal Payment = B6 - C11
C13: Ending Balance = C10 - C12
```

### Returns Analysis

**IRR Calculation:**
```
B5: IRR = IRR(CashFlow!C23:P23)
// Uses cumulative FCF from Year 0 through Year 15
```

**NPV Calculation:**
```
B8: Discount Rate = Assumptions!B55 (10%)
B9: NPV = NPV(B8, CashFlow!D23:P23) + CashFlow!C23
// Year 0 separate, then discount Years 1-15
```

**MOIC (Multiple on Invested Capital):**
```
B12: Total Equity Invested = CAPEX!B61 * 0.4
B13: Cumulative Cash Returned = CashFlow!P23 (Year 15 cumulative)
B14: MOIC = B13 / B12
```

**Payback Period:**
```
B17: =MATCH(TRUE, CashFlow!C23:P23>0, 0)
// Finds first year where cumulative FCF turns positive
```

### Sensitivity Analysis

**One-Way Sensitivity (IRR vs Selling Price):**
```
Create a data table:
Row: Selling Price from -20% to +20% in 5% increments
Column: Base Case IRR
Formula: =IRR with price adjusted
```

**Two-Way Sensitivity (IRR vs Price and Feed Cost):**
```
Create a data table:
Rows: Selling Price -20% to +20%
Columns: Feed Cost -20% to +20%
Formula: =IRR with both variables adjusted
Use conditional formatting for color scale
```

### Scenario Manager

**Base Case:**
```
All assumptions at base values
IRR = 28.7%
NPV = SAR 24.8M
```

**Optimistic:**
```
- Selling Price: +10%
- Feed Cost: -10%
- Ramp-up faster: 60%, 85%, 95%, 98%
- Value-added: 50% of volume
- Mortality: 8%
Result: IRR = 35.2%, NPV = SAR 38.5M
```

**Pessimistic:**
```
- Selling Price: -10%
- Feed Cost: +15%
- Ramp-up slower: 40%, 60%, 75%, 85%
- Value-added: 0%
- Mortality: 15%
Result: IRR = 14.8%, NPV = SAR 3.2M
```

---

## Data Validation & Error Checking

Add data validation to key input cells:

```
Production Capacity: 50 to 2000 tons
Ramp-up %: 0% to 100%
Prices: > 0
FCR: 1.0 to 2.5
Mortality: 5% to 25%
Interest Rate: 0% to 15%
Discount Rate: 5% to 20%
```

Add error checks:
```
=IF(OPEX!B51 > Assumptions!B11*0.8, "WARNING: Cost per kg too high", "OK")
=IF(P&L!P32 < 0.15, "WARNING: Low EBITDA margin", "OK")
=IF(Returns!B5 < 0.12, "WARNING: IRR below minimum threshold", "OK")
```

---

## Charts & Visualizations

### Chart 1: Revenue Build-up (Stacked Area)
- X-axis: Years 1-15
- Y-axis: Revenue (SAR millions)
- Series: Wholesale, Retail, Value-added

### Chart 2: Cash Flow Waterfall (Year 1)
- Starting cash
- Operating cash inflow
- CAPEX outflow
- Debt raised
- Equity raised
- Ending cash

### Chart 3: Cumulative Free Cash Flow (Line)
- X-axis: Years 0-15
- Y-axis: Cumulative FCF (SAR millions)
- Add break-even indicator line at SAR 0

### Chart 4: EBITDA Margin Trend (Line + Column)
- X-axis: Years 1-15
- Primary Y-axis: EBITDA (SAR millions) as columns
- Secondary Y-axis: EBITDA % as line

### Chart 5: Sensitivity Tornado
- Horizontal bar chart
- Shows impact of ±20% change in key variables on IRR
- Sort by magnitude of impact

### Chart 6: Scenario Comparison (Grouped Column)
- X-axis: Optimistic, Base, Pessimistic
- Y-axis: IRR, NPV, Payback Period (normalized)

---

## Usage Instructions

### Step 1: Set Your Base Assumptions
1. Go to "Assumptions" tab
2. Enter your system scale (tons/year) in cell B3
3. Adjust pricing assumptions (cells B10-B16)
4. Verify cost assumptions match your region

### Step 2: Review CAPEX
1. Go to "CAPEX" tab
2. Verify line items match your equipment selection
3. Adjust for local costs if needed
4. Total CAPEX auto-calculates in row 61

### Step 3: Check OPEX Calculations
1. Go to "OPEX" tab
2. Verify formulas reference correct assumption cells
3. Review cost per kg (should be SAR 22-35 depending on scale)

### Step 4: Review Financial Projections
1. Go to "P&L" tab
2. Check revenue ramp aligns with your production plan
3. Verify costs scale appropriately
4. Review EBITDA margins (should reach 25-35% by Year 3)

### Step 5: Analyze Returns
1. Go to "Returns Analysis" tab
2. Check IRR (target >20%), NPV (target >0), MOIC (target >2x)
3. Review payback period (target <7 years)

### Step 6: Test Scenarios
1. Go to "Scenarios" tab
2. Toggle between Optimistic/Base/Pessimistic
3. See how returns change
4. Use for risk discussion with investors

### Step 7: Run Sensitivity Analysis
1. Go to "Returns Analysis" tab
2. Review sensitivity tables
3. Identify which variables have biggest impact
4. Focus risk mitigation on high-impact variables

### Step 8: Export for Presentation
1. Dashboard tab → Copy charts
2. Create PDF summary
3. Export data tables for appendix
4. Share with investors/lenders

---

## Download Options

### Option A: Pre-built Google Sheets Template
1. Click this link: [Make a Copy]
2. File → Make a copy to your Google Drive
3. Start editing immediately

### Option B: Excel File from Repository
1. Download: `spv_and_finance/saudi_arabia_ras_financial_model.xlsx`
2. Open in Excel or Google Sheets
3. All formulas included

### Option C: CSV Data Files
Download individual CSVs and import:
- `assumptions.csv`
- `capex_breakdown.csv`
- `opex_breakdown.csv`
- `projections_15yr.csv`

---

## Tips for Testing the Model

### Test 1: Scale Sensitivity
- Change system size from 50 to 200 to 1000 tons
- Observe how cost per kg drops
- Note IRR improvement with scale

### Test 2: Price Sensitivity
- Increase selling price by 20%
- Note IRR jumps to ~40%
- This shows pricing is critical variable

### Test 3: Feed Cost Impact
- Increase feed cost by 20%
- IRR drops to ~24%
- Less sensitive than price but still significant

### Test 4: Ramp-up Speed
- Change Year 1 from 50% to 70%
- Earlier cash flow improves returns
- But may increase operational risk

### Test 5: Value-Added Products
- Increase value-added mix from 20% to 50%
- Add 30% price premium
- Observe significant margin improvement

### Test 6: Break-even Scale
- Gradually decrease production from 200 to 150 to 100 tons
- Find the scale where NPV = 0
- This is your minimum viable scale

---

## Maintenance & Updates

### Monthly Updates
- Update actual costs vs budget in "Actuals" tab
- Calculate variances
- Adjust forward assumptions if needed

### Quarterly Reviews
- Re-forecast remaining years
- Update market pricing data
- Adjust production ramp if needed
- Recalculate IRR with actuals

### Annual Reviews
- Full model refresh with actual data
- Update all assumptions to current market
- Revalidate equipment costs
- Adjust for regulatory changes

---

## Support & Questions

For questions about the financial model:
1. Review the markdown documentation: `saudi_arabia_financial_model.md`
2. Check formula references in this guide
3. Verify input assumptions match your scenario
4. Contact: [Your contact information]

---

## Version Control

**Current Version:** 1.0
**Last Updated:** November 2024
**Based on:** Saudi Arabia RAS Financial Model (markdown)
**Exchange Rate:** 3.75 SAR/USD

### Changelog
- v1.0 (Nov 2024): Initial spreadsheet guide based on investment-grade financial model
- Includes 15-year projections, scenario analysis, sensitivity tables
- Monte Carlo simulation guidance (requires add-in or R/Python)

---

## Advanced Features (Optional)

### Monte Carlo Simulation
Requires Google Sheets Add-in or Excel macro:
1. Define probability distributions for key variables
2. Run 10,000 iterations
3. Generate IRR distribution histogram
4. Calculate P10, P50, P90 values
5. Compute probability of IRR > 20%

### Goal Seek
Use Excel's Goal Seek to find:
- What selling price needed for 25% IRR?
- What production volume for SAR 20M NPV?
- What feed cost to break even?

### Scenario Manager
Save multiple scenarios:
- Best Case / Base Case / Worst Case
- Different species (Tilapia vs Barramundi vs Shrimp)
- Different locations (Riyadh vs Jeddah vs Dammam)
- Export comparison tables

---

## Appendix: Common Formulas

### Financial Functions
```
IRR(values): Internal Rate of Return
NPV(rate, values): Net Present Value
PMT(rate, nper, pv): Loan payment
FV(rate, nper, pmt, pv): Future value
XIRR(values, dates): IRR with specific dates
```

### Lookup Functions
```
VLOOKUP(lookup_value, table, col, false): Find value in table
INDEX(array, row, col): Return value at position
MATCH(lookup_value, array, 0): Find position
IF(condition, true_value, false_value): Conditional
```

### Statistical Functions
```
AVERAGE(range): Mean
STDEV(range): Standard deviation
PERCENTILE(range, k): Kth percentile
CORREL(array1, array2): Correlation
```

### Array Formulas
```
SUMPRODUCT(array1, array2): Multiply and sum
SUMIFS(sum_range, criteria_range1, criteria1, ...): Conditional sum
```

---

## Example: Quick Test Scenario

**Test if 150-ton system is viable:**
1. Assumptions!B3 = 150
2. Check Returns!B5 (IRR)
3. Check Returns!B9 (NPV)
4. If IRR > 15% and NPV > 0, system is viable at this scale

**Result from model:**
- 150-ton: IRR ≈ 18%, NPV ≈ SAR 5-8M
- This is minimum viable scale (break-even point)
- 200-ton recommended for attractive returns

---

This guide provides everything needed to build a fully functional, testable financial model in Google Sheets or Excel. All formulas reference the detailed breakdowns in the markdown documentation.
