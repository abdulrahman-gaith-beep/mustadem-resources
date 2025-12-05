# Mustadem Prompts Pipeline

This document contains improved, structured prompts and a complete project plan ready for Asana import.

## Table of Contents
1. [How to Use This Document](#how-to-use-this-document)
2. [Asana Import Instructions](#asana-import-instructions)
3. [Improved Prompts (1-8)](#improved-prompts)
4. [New Prompts (9-15)](#new-prompts-9-15)
5. [Prompt Chaining Workflows](#prompt-chaining-workflows)
6. [Agent Handoff Templates](#agent-handoff-templates)
7. [Quality Assurance Procedures](#quality-assurance-procedures)
8. [Tech Stack Overview](#tech-stack-overview)
9. [Troubleshooting Guide](#troubleshooting-guide)
10. [Progress Tracking](#progress-tracking)
11. [Quick Reference](#quick-reference)

---

## How to Use This Document

This guide explains how to effectively use the prompts in this document with different AI agents, tools, and team workflows.

### 🤖 Agent Assignment Guide

| Agent Type | Best For | Recommended Tool |
|------------|----------|------------------|
| **Research Agent** | Market research, competitor analysis, data gathering | Gemini 3, ChatGPT, Perplexity |
| **Writing Agent** | Long-form content, reports, documentation | Claude, ChatGPT |
| **Analysis Agent** | Data analysis, financial modeling, trends | Gemini 3, ChatGPT |
| **Coding Agent** | Automation, scripts, integrations | DeepSeek, GitHub Copilot |
| **Design Agent** | Visual assets, presentations, infographics | Canva AI, Midjourney |

### 🔗 How to Chain Prompts Together

1. **Sequential Chaining**: Complete one prompt before starting the next
   - Example: Research → Analysis → Content Creation → Implementation
   
2. **Parallel Chaining**: Run multiple prompts simultaneously
   - Example: Market Research + Competitor Analysis running in parallel
   
3. **Iterative Chaining**: Refine outputs through multiple passes
   - Example: Draft → Review → Refine → Finalize

### 📋 Quality Assurance Procedures

Before marking any deliverable as complete:
1. ✅ Verify all required outputs are present
2. ✅ Cross-check data accuracy with sources
3. ✅ Ensure formatting meets standards
4. ✅ Get stakeholder sign-off
5. ✅ Document lessons learned

### 🛠️ Tool Selection Guide

| Task Type | Primary Tool | Backup Tool |
|-----------|--------------|-------------|
| Complex Research | Gemini 3 | ChatGPT |
| Long Documents | Claude | ChatGPT |
| Quick Analysis | ChatGPT | Gemini 3 |
| Code/Automation | DeepSeek | GitHub Copilot |
| Project Tracking | Asana | Notion |
| Documentation | Notion | Google Docs |
| Presentations | Google Slides | Canva |
| Data Analysis | Google Sheets | Excel |

### 📊 Standard Pre-Execution Checklist

Before starting any prompt, ensure:
- [ ] 📁 Data sources identified and accessible
- [ ] 🔐 Access credentials obtained (if needed)
- [ ] 📝 Output format agreed upon with stakeholders
- [ ] 👥 Stakeholders notified of timeline
- [ ] ⏰ Timeline confirmed and realistic
- [ ] 🎯 Success criteria defined

---

## Asana Import Instructions

### How to Import the CSV to Asana

1. Open Asana and go to your desired project or create a new project
2. Click on the dropdown arrow next to the project name
3. Select "Import" > "CSV"
4. Upload the file: `asana_import_mustadem_pipeline.csv`
5. Map the columns:
   - Name → Task Name
   - Section → Section (Creates automatic sections)
   - Description → Task Description
   - Assignee → Assignee (leave empty for manual assignment)
   - Due Date → Due Date (fill in as needed)
   - Priority → Custom Field (create if needed)
   - Tags → Tags

### Sections Created
- **Mustadem Pipeline** - Core company initiatives
- **Other Ventures** - Personal and side projects
- **New Tasks** - Immediate action items
- **Nebras Company Profile** - Profile development tasks

---

## Improved Prompts

### 1. Farm Management System Deep Research Prompt

#### 📋 Pre-Execution Checklist
- [ ] Access to industry databases (FAO, World Bank, Statista)
- [ ] Company database subscriptions active
- [ ] Output format confirmed (Report, Deck, or Notion database)
- [ ] Timeline: 2-3 days for comprehensive research
- [ ] Stakeholder review meeting scheduled

#### 📝 Step-by-Step Breakdown

| Step | Action | Time | Tool | Output | Quality Check |
|------|--------|------|------|--------|---------------|
| 1 | Identify and list top 50 aquaculture technology companies globally | 2 hrs | Gemini 3/Perplexity | Company database | Verify company existence |
| 2 | Research RAS system providers and technologies | 3 hrs | Gemini 3 | Technology comparison matrix | Cross-check with vendor sites |
| 3 | Analyze sea cage monitoring solutions | 2 hrs | ChatGPT | Solution profiles | Verify product features |
| 4 | Research AI applications in aquaculture | 2 hrs | Gemini 3 | AI capability matrix | Check case studies |
| 5 | Document IoT sensor specifications and costs | 2 hrs | DeepSeek | Sensor database | Verify with suppliers |
| 6 | Analyze ERP systems for farm management | 2 hrs | ChatGPT | ERP comparison table | Demo verification |
| 7 | Identify market gaps and opportunities | 2 hrs | Claude | Gap analysis report | Team validation |
| 8 | Research regional market dynamics (Saudi/GCC) | 2 hrs | Gemini 3 | Market report | Local expert review |
| 9 | Create competitive landscape matrix | 1 hr | Google Sheets | Matrix document | Data accuracy check |
| 10 | Compile final report with recommendations | 2 hrs | Claude | Final report | Stakeholder review |

#### 🤖 Agent Assignment

| Agent Type | Tasks | Deliverable |
|------------|-------|-------------|
| **Research Agent** | Steps 1-4, 6, 8 | Raw data and research notes |
| **Analysis Agent** | Steps 5, 7, 9 | Analyzed matrices and comparisons |
| **Writing Agent** | Step 10 | Final compiled report |

#### 🔄 Follow-Up Prompts

After initial deliverable, use these for refinement:
1. "Deep dive into [specific technology] with implementation requirements"
2. "Create vendor comparison for [specific category] with pricing"
3. "Develop partnership outreach strategy for top 5 vendors"
4. "Build implementation roadmap for recommended solution"

#### ✅ Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Companies researched | 50+ | Database count |
| Technology categories covered | 10+ | Report sections |
| Actionable recommendations | 5+ | Executive summary items |
| Data recency | <6 months old | Source date verification |
| Report completeness | 100% deliverables | Checklist verification |

#### 📄 Core Prompt

```
Act as a senior agricultural technology consultant with 20+ years of experience in aquaculture systems and farm management technology. Conduct comprehensive research and analysis on the following:

**Primary Focus Areas:**

1. **Recirculating Aquaculture Systems (RAS)**
   - Current market leaders and their technologies
   - Key parameters monitored (water quality, temperature, pH, ammonia, nitrate, dissolved oxygen)
   - Collection methods (IoT sensors, automated testing, manual sampling)
   - Cost structures and ROI analysis
   - Scalability considerations

2. **Sea Cage Systems**
   - Environmental monitoring requirements
   - Structural monitoring and maintenance
   - Feed management optimization
   - Disease prediction and prevention
   - Weather and current integration

3. **Pond Farming Management**
   - Water quality management systems
   - Aeration and circulation optimization
   - Stocking density calculations
   - Harvest planning and logistics

**Technology Analysis:**

4. **AI Systems in Aquaculture**
   - Computer vision for fish health monitoring
   - Predictive analytics for growth optimization
   - Automated feeding systems
   - Disease early warning systems
   - Market price prediction algorithms

5. **Monitoring Systems & IoT**
   - Sensor types and accuracy requirements
   - Data transmission protocols
   - Real-time alert systems
   - Dashboard and reporting capabilities

6. **ERP Systems for Farms**
   - Inventory management
   - Financial tracking and reporting
   - Supply chain integration
   - Compliance and certification tracking
   - Multi-site management

**Competitive Analysis:**

7. **Market Leadership Strategy**
   - Current market gaps and unmet needs
   - Differentiation opportunities
   - Technology partnerships potential
   - White-label and OEM opportunities

8. **Species & Applications**
   - Fish species expertise (salmon, tilapia, catfish, shrimp, etc.)
   - Expansion to poultry monitoring
   - Livestock applications
   - Greenhouse integration possibilities

**Market Intelligence:**

9. **Market Trends Analysis**
   - Local Saudi Arabia market dynamics
   - GCC regional opportunities
   - Global market trends and projections
   - Regulatory landscape changes

10. **Future Technology Roadmap**
    - Emerging AI/ML applications
    - Blockchain for traceability
    - Autonomous feeding systems
    - Integrated biosecurity solutions

**Deliverables Expected:**
- Executive summary with key findings
- Competitive landscape matrix
- Technology stack recommendations
- Implementation roadmap (6-month, 1-year, 3-year)
- Investment requirements analysis
- Risk assessment and mitigation strategies

Please provide detailed, actionable insights with specific company names, product references, and quantified market data where available.
```

---

### 2. Local LLM Setup Prompt

#### 📋 Pre-Execution Checklist
- [ ] Server specifications documented (RAM, GPU, storage)
- [ ] Network isolation requirements confirmed
- [ ] Security compliance requirements listed
- [ ] Budget for hardware approved (if needed)
- [ ] IT team availability confirmed
- [ ] Timeline: 1-2 weeks for full implementation

#### 📝 Step-by-Step Breakdown

| Step | Action | Time | Tool | Output | Quality Check |
|------|--------|------|------|--------|---------------|
| 1 | Assess current server hardware capabilities | 2 hrs | Manual/Scripts | Hardware assessment doc | Verify specs against requirements |
| 2 | Define security and compliance requirements | 2 hrs | Claude | Security requirements doc | Legal/compliance review |
| 3 | Research and select appropriate LLM models | 4 hrs | Gemini 3 | Model comparison matrix | Test model capabilities |
| 4 | Design network isolation architecture | 3 hrs | DeepSeek | Architecture diagram | Security team review |
| 5 | Create installation procedures | 4 hrs | DeepSeek | Installation guide | Peer review |
| 6 | Develop security hardening checklist | 2 hrs | Claude | Security checklist | Security audit |
| 7 | Build API layer specifications | 3 hrs | DeepSeek | API documentation | Developer testing |
| 8 | Create user interface requirements | 2 hrs | Claude | UI specifications | User feedback |
| 9 | Develop testing and validation protocols | 2 hrs | Claude | Test plan | QA review |
| 10 | Compile user training materials | 3 hrs | Claude | Training docs/videos | User testing |

#### 🤖 Agent Assignment

| Agent Type | Tasks | Deliverable |
|------------|-------|-------------|
| **Research Agent** | Steps 3 | Model research and comparison |
| **Coding Agent** | Steps 4, 5, 7 | Technical architecture and code |
| **Writing Agent** | Steps 2, 6, 9, 10 | Documentation and guides |

#### 🔄 Follow-Up Prompts

1. "Create detailed Docker configuration for [selected model]"
2. "Develop fine-tuning strategy using company documents"
3. "Build monitoring dashboard for LLM performance"
4. "Create troubleshooting guide for common issues"
5. "Design backup and recovery procedures"

#### ✅ Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Model response accuracy | >90% on test queries | Accuracy testing |
| Query response time | <5 seconds average | Performance monitoring |
| Security compliance | 100% checklist | Security audit |
| User adoption rate | >80% of target users | Usage tracking |
| System uptime | >99% | Monitoring logs |

#### 📄 Core Prompt

```
Act as an enterprise AI infrastructure architect. Design and implement a secure, private LLM solution for a company server with the following requirements:

**Security Requirements:**
- Zero internet connectivity after initial setup
- Encryption at rest and in transit
- Access control and audit logging
- Data isolation from external networks

**Technical Specifications:**
1. Hardware requirements assessment for on-premise deployment
2. Recommended open-source LLM models (Llama 2, Mistral, etc.)
3. Fine-tuning strategy using company-specific data
4. API layer for internal application integration
5. User interface options for non-technical staff

**Implementation Steps:**
1. Server preparation and network isolation
2. Model selection based on use case requirements
3. Installation and configuration procedures
4. Security hardening checklist
5. Testing and validation protocols
6. User training materials
7. Maintenance and update procedures (offline)

**Deliverables:**
- Architecture diagram
- Hardware specification document
- Installation guide
- Security configuration guide
- User manual
- Troubleshooting guide
```

---

### 3. Value Chain Gap Analysis Agent Prompt

#### 📋 Pre-Execution Checklist
- [ ] Industry reports access (McKinsey, BCG, local studies)
- [ ] Current Mustadem capabilities documented
- [ ] Stakeholder input on strategic priorities
- [ ] Output format: Notion database + Executive presentation
- [ ] Timeline: 3-5 days for thorough analysis

#### 📝 Step-by-Step Breakdown

| Step | Action | Time | Tool | Output | Quality Check |
|------|--------|------|------|--------|---------------|
| 1 | Map complete food value chain (5 stages) | 3 hrs | Claude | Value chain diagram | Expert validation |
| 2 | Research each stage for technology gaps | 4 hrs | Gemini 3 | Gap inventory list | Cross-reference industry reports |
| 3 | Identify infrastructure gaps | 2 hrs | Gemini 3 | Infrastructure assessment | Local market verification |
| 4 | Document information and data gaps | 2 hrs | ChatGPT | Information gap analysis | Stakeholder input |
| 5 | Research financial access gaps | 2 hrs | Gemini 3 | Financial gap report | Industry expert review |
| 6 | Quantify impact of each gap | 3 hrs | Google Sheets | Impact assessment matrix | Data validation |
| 7 | Develop business models for top gaps | 4 hrs | Claude | Business model canvas (x5) | Team review |
| 8 | Create financial projections for each | 4 hrs | Excel | Financial models | CFO review |
| 9 | Build prioritization matrix | 2 hrs | Google Sheets | Priority matrix | Leadership alignment |
| 10 | Compile final report with recommendations | 3 hrs | Claude | Executive report | Stakeholder approval |

#### 🤖 Agent Assignment

| Agent Type | Tasks | Deliverable |
|------------|-------|-------------|
| **Research Agent** | Steps 1-5 | Raw research and gap identification |
| **Analysis Agent** | Steps 6, 8, 9 | Quantified analysis and matrices |
| **Writing Agent** | Steps 7, 10 | Business models and final report |

#### 🔄 Follow-Up Prompts

1. "Create detailed business plan for [specific opportunity]"
2. "Research potential partners for [gap solution]"
3. "Develop go-to-market strategy for [new service]"
4. "Build financial model with sensitivity analysis for [opportunity]"
5. "Create investor pitch for [selected venture]"

#### ✅ Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Gaps identified | 20+ across categories | Gap inventory count |
| Business opportunities developed | 5+ viable | Business model completion |
| Market size validation | All opportunities validated | Source documentation |
| Financial projections | 3-5 year models for top 5 | Model completeness |
| Stakeholder approval | Signed off | Meeting minutes |

#### 📄 Core Prompt

```
You are a strategic business analyst specializing in food value chain optimization. Your task is to:

**Analysis Framework:**

1. **Value Chain Mapping**
   - Input supply (seeds, feed, fertilizers, equipment)
   - Production (farming, processing, packaging)
   - Distribution (logistics, warehousing, cold chain)
   - Retail (wholesale, retail, e-commerce)
   - Consumer (B2C, B2B, export)

2. **Gap Identification Methodology**
   - Technology gaps (automation, digitization)
   - Infrastructure gaps (storage, transport, processing)
   - Information gaps (market intelligence, traceability)
   - Financial gaps (access to capital, insurance)
   - Skill gaps (training, expertise availability)

3. **Business Model Development**
   For each identified gap:
   - Problem statement with quantified impact
   - Proposed solution with unique value proposition
   - Revenue model (subscription, transaction, hybrid)
   - Required resources and partnerships
   - Market size and growth potential
   - Competitive landscape analysis
   - Implementation timeline
   - Financial projections (3-5 years)

4. **Prioritization Criteria**
   - Market size and growth rate
   - Entry barriers and competitive moat
   - Capital requirements
   - Time to profitability
   - Strategic alignment with Mustadem capabilities

**Output Format:**
Create a structured report with:
- Executive summary
- Gap analysis matrix (priority x impact)
- Top 5 business opportunity profiles
- Recommended next steps with owners and timelines
```

---

### 4. Agricultural Products Dropshipping Research Prompt

#### 📋 Pre-Execution Checklist
- [ ] Alibaba/supplier accounts set up
- [ ] Import regulation contacts identified
- [ ] E-commerce platform accounts ready
- [ ] Budget for samples allocated (SAR 2,000-5,000)
- [ ] Timeline: 2 weeks for comprehensive research

#### 📝 Step-by-Step Breakdown

| Step | Action | Time | Tool | Output | Quality Check |
|------|--------|------|------|--------|---------------|
| 1 | Research indoor farming systems market | 4 hrs | Gemini 3 | Market analysis report | Verify with local suppliers |
| 2 | Compile aquaculture equipment database | 4 hrs | Perplexity | Equipment database | Price validation |
| 3 | Research water management products | 3 hrs | Gemini 3 | Product catalog | Specification verification |
| 4 | Document automation and IoT products | 3 hrs | ChatGPT | Automation products list | Feature verification |
| 5 | Research import regulations for seeds | 4 hrs | Local research | Regulation summary | Legal review |
| 6 | Build US supplier contact database | 4 hrs | Alibaba/Web | Supplier database | MOQ verification |
| 7 | Build Turkey/Europe supplier database | 4 hrs | Alibaba/Web | Supplier database | Shipping cost validation |
| 8 | Benchmark competitor websites (US/EU) | 4 hrs | Web research | Competitive analysis | Feature comparison |
| 9 | Create pricing and margin analysis | 3 hrs | Excel | Pricing model | Profitability validation |
| 10 | Develop branding and positioning strategy | 3 hrs | Claude | Brand strategy doc | Market fit review |

#### 🤖 Agent Assignment

| Agent Type | Tasks | Deliverable |
|------------|-------|-------------|
| **Research Agent** | Steps 1-5, 6-8 | Market research and databases |
| **Analysis Agent** | Steps 9 | Financial and pricing analysis |
| **Writing Agent** | Step 10 | Strategy documents |

#### 🔄 Follow-Up Prompts

1. "Create product listings for top 20 products with Arabic translations"
2. "Develop supplier negotiation strategy for [category]"
3. "Build Shopify store structure for [product category]"
4. "Create marketing campaign for product launch"
5. "Design customer acquisition funnel"

#### ✅ Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Products researched | 200+ SKUs | Database count |
| Suppliers contacted | 50+ | Contact log |
| Margin potential | >30% average | Pricing analysis |
| Import compliance | 100% verified | Regulation checklist |
| Website benchmarks | 10+ analyzed | Benchmark report |

#### 📄 Core Prompt

```
You are an e-commerce specialist focusing on agricultural supplies. Conduct thorough market research for a dropshipping platform targeting small farmers in Saudi Arabia:

**Product Categories to Research:**

1. **Indoor Farming Systems**
   - Home hydroponics kits (NFT, DWC, ebb & flow)
   - Aeroponics systems
   - Aquaponics starter kits
   - Vertical farming solutions
   - Grow lights and controllers

2. **Aquaculture Equipment**
   - Small-scale aquariums and tanks
   - Filtration systems
   - Air pumps and aeration
   - Water quality test kits
   - Fish feed and nutrition

3. **Water Management**
   - Water pumps (submersible, centrifugal)
   - Drip irrigation systems
   - Water desalination units (small scale)
   - Water storage solutions
   - Filtration and treatment

4. **Farm Automation**
   - Environmental sensors (temperature, humidity, pH)
   - Automated dosing systems
   - Climate controllers
   - Timers and scheduling devices
   - Remote monitoring solutions

5. **Seeds and Growing Media**
   - Vegetable seeds (heirloom, hybrid)
   - Herb seeds
   - Microgreen supplies
   - Growing media (rockwool, coco coir, perlite)
   - Note: Document import regulations for Saudi Arabia

6. **Farm Tools and Accessories**
   - Hand tools
   - Pruning equipment
   - Harvesting tools
   - PPE and safety equipment
   - Storage and packaging

**Supplier Research:**
- US suppliers (contact list with MOQ, shipping terms)
- European suppliers (same format)
- Turkish suppliers (same format)
- Chinese suppliers (same format)

**Benchmark Websites:**
- US: list top 5 with product range and pricing analysis
- Europe: list top 5 with same analysis
- Identify what makes them successful

**Deliverables:**
1. Product database (Excel/CSV with SKUs, descriptions, prices, suppliers)
2. Supplier contact database
3. Import regulation summary for seeds and chemicals
4. Benchmark analysis report
5. Recommended branding and positioning strategy
6. Marketing channel recommendations
7. Pricing strategy with margin analysis
```

---

### 5. Personal Revenue FBA Agent Prompt

#### 📋 Pre-Execution Checklist
- [ ] Amazon Seller Central account active
- [ ] Noon.com seller account (optional)
- [ ] Alibaba account with buyer protection
- [ ] Initial capital ready (SAR 5,000-20,000)
- [ ] Timeline: 3 weeks for research + launch prep

#### 📝 Step-by-Step Breakdown

| Step | Action | Time | Tool | Output | Quality Check |
|------|--------|------|------|--------|---------------|
| 1 | Set up product research tools (Helium 10/Jungle Scout) | 2 hrs | Tool setup | Account ready | Subscription active |
| 2 | Research Amazon.sa top sellers and gaps | 6 hrs | Helium 10 | Opportunity list | BSR verification |
| 3 | Apply product selection filters | 4 hrs | Excel | Filtered product list | Criteria match |
| 4 | Analyze competition for top 20 products | 4 hrs | Helium 10 | Competition analysis | Review count validation |
| 5 | Calculate profit margins for each product | 3 hrs | Excel | Profit calculator | Include all FBA fees |
| 6 | Research Alibaba suppliers for top 10 | 6 hrs | Alibaba | Supplier database | Trade assurance verified |
| 7 | Request samples from top 5 suppliers | 2 hrs | Alibaba | Sample orders | Tracking confirmed |
| 8 | Develop Arabic keyword strategy | 3 hrs | Helium 10/ChatGPT | Keyword list | Search volume verified |
| 9 | Create listing optimization guide | 3 hrs | Claude | Optimization checklist | Best practices applied |
| 10 | Build launch strategy and PPC plan | 4 hrs | Claude | Launch playbook | Budget allocated |

#### 🤖 Agent Assignment

| Agent Type | Tasks | Deliverable |
|------------|-------|-------------|
| **Research Agent** | Steps 2-4, 6 | Product and supplier research |
| **Analysis Agent** | Steps 5 | Financial calculations |
| **Writing Agent** | Steps 8-10 | Listings and strategy docs |

#### 🔄 Follow-Up Prompts

1. "Optimize listing for [product] with A+ content"
2. "Create PPC campaign structure for [product]"
3. "Develop product photography brief for [product]"
4. "Build review generation strategy"
5. "Create inventory management system"

#### ✅ Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Products analyzed | 100+ | Research log |
| Viable opportunities | 10+ | Selection criteria pass |
| Profit margin | >35% | Calculator verification |
| Suppliers vetted | 20+ | Supplier database |
| Launch readiness | 100% checklist | Launch playbook |

#### 📄 Core Prompt

```
You are an Amazon FBA product research specialist for the Saudi Arabian market. Your task is to identify profitable product opportunities:

**Research Criteria:**

1. **Product Selection Filters**
   - Selling price: SAR 50-500
   - Monthly sales volume: minimum 100 units
   - Number of reviews on top listings: under 500
   - Seasonality: prefer evergreen products
   - Size: small/lightweight for lower FBA fees
   - Not dominated by major brands

2. **Market Analysis**
   - Search volume trends (Amazon.sa, noon.com)
   - Competition analysis (number of sellers, review counts)
   - Price point analysis
   - Profit margin calculation (min 30% after all costs)

3. **Supplier Identification**
   - Alibaba suppliers with trade assurance
   - Minimum order quantities under 500 units
   - Shipping costs to Saudi Arabia
   - Sample ordering process

4. **Listing Optimization**
   - Arabic keyword research
   - Image requirements and best practices
   - A+ content recommendations
   - PPC strategy initial setup

**Platform Expansion:**
- Amazon.sa strategy
- Noon.com integration
- Other Saudi e-commerce platforms
- Dropshipping fallback options

**Deliverables:**
1. Top 10 product opportunities with full analysis
2. Supplier shortlist for each product
3. Profit and loss calculator template
4. Launch checklist and timeline
5. Initial inventory investment calculation
```

---

### 6. SaaS/App Market Gap Analysis Prompt

#### 📋 Pre-Execution Checklist
- [ ] Access to app store analytics (Sensor Tower, App Annie)
- [ ] Saudi/GCC market reports available
- [ ] Vision 2030 documentation reviewed
- [ ] Technical team capacity assessed
- [ ] Timeline: 2-3 weeks for comprehensive analysis

#### 📝 Step-by-Step Breakdown

| Step | Action | Time | Tool | Output | Quality Check |
|------|--------|------|------|--------|---------------|
| 1 | Map 10 target market sectors | 2 hrs | Claude | Sector overview document | Completeness check |
| 2 | Research government digitization initiatives | 4 hrs | Gemini 3 | Government tech report | Source verification |
| 3 | Analyze education/e-learning gaps | 4 hrs | Gemini 3 | Sector analysis | Local market validation |
| 4 | Research healthcare tech opportunities | 4 hrs | Gemini 3 | Sector analysis | Regulatory review |
| 5 | Analyze fintech and financial services | 4 hrs | Gemini 3 | Sector analysis | SAMA compliance check |
| 6 | Research remaining sectors (5-10) | 8 hrs | Gemini 3 | Sector analyses | Market size verification |
| 7 | Score and prioritize opportunities | 4 hrs | Excel | Prioritization matrix | Criteria weighting review |
| 8 | Develop detailed concepts for top 10 | 8 hrs | Claude | Business concepts | Team validation |
| 9 | Create technical feasibility assessments | 6 hrs | DeepSeek | Technical specs | Developer review |
| 10 | Build go-to-market strategy outlines | 4 hrs | Claude | GTM strategies | Market fit review |

#### 🤖 Agent Assignment

| Agent Type | Tasks | Deliverable |
|------------|-------|-------------|
| **Research Agent** | Steps 1-6 | Market research and sector analyses |
| **Analysis Agent** | Step 7 | Prioritization matrix |
| **Coding Agent** | Step 9 | Technical feasibility |
| **Writing Agent** | Steps 8, 10 | Business concepts and strategies |

#### 🔄 Follow-Up Prompts

1. "Create MVP specification for [selected app]"
2. "Research regulatory requirements for [sector]"
3. "Develop user research plan for [concept]"
4. "Create wireframes and user flow for [app]"
5. "Build financial projections for [SaaS product]"

#### ✅ Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Sectors analyzed | 10 | Report completeness |
| Opportunities identified | 30+ | Opportunity database |
| Detailed concepts | 10 | Business plan completion |
| Technical assessments | 10 | Dev team validation |
| Vision 2030 alignment | All concepts aligned | Alignment matrix |

#### 📄 Core Prompt

```
You are a technology market analyst specializing in the Saudi and GCC markets. Identify opportunities for new apps, SaaS solutions, and AI-powered tools:

**Analysis Framework:**

1. **Market Sectors to Analyze**
   - Government services and digitization
   - Education and e-learning
   - Healthcare and wellness
   - Financial services and fintech
   - E-commerce and retail
   - Real estate and property tech
   - Transportation and logistics
   - Agriculture and food tech
   - Entertainment and media
   - HR and workforce management

2. **For Each Opportunity Identified:**
   - Problem statement with target user persona
   - Current solutions and their limitations
   - Proposed solution concept
   - Unique value proposition
   - Revenue model options
   - Market size (TAM, SAM, SOM)
   - Competitive moat analysis
   - Technical complexity assessment
   - Regulatory considerations
   - Estimated development timeline
   - Investment requirements

3. **Prioritization Criteria**
   - Market demand (search trends, survey data)
   - Competition intensity
   - Technical feasibility
   - Time to market
   - Revenue potential
   - Alignment with Vision 2030 initiatives

**Quality Requirements:**
- Each idea must include verifiable data sources
- Competitive analysis must name specific competitors
- Financial projections must show methodology
- All assumptions must be clearly stated

**Deliverables:**
1. Market opportunity database (Notion format)
2. Top 10 detailed business plans
3. Technical feasibility assessment for each
4. Recommended tech stack for development
5. Go-to-market strategy outlines
```

---

### 7. Investment Pitch Preparation Prompt

#### 📋 Pre-Execution Checklist
- [ ] Historical financials compiled
- [ ] Company metrics and KPIs documented
- [ ] Target investor list prepared
- [ ] Funding amount and use of funds defined
- [ ] Company legal documents ready
- [ ] Timeline: 1-2 weeks for complete package

#### 📝 Step-by-Step Breakdown

| Step | Action | Time | Tool | Output | Quality Check |
|------|--------|------|------|--------|---------------|
| 1 | Gather all company data and metrics | 4 hrs | Internal | Data compilation | CFO verification |
| 2 | Research market size data (TAM/SAM/SOM) | 4 hrs | Gemini 3 | Market sizing doc | Source verification |
| 3 | Create competitive landscape analysis | 4 hrs | Gemini 3 | Competition matrix | Market validation |
| 4 | Develop pitch deck narrative structure | 2 hrs | Claude | Outline document | Founder review |
| 5 | Design pitch deck slides (12-15 slides) | 8 hrs | Google Slides/Canva | Pitch deck | Design review |
| 6 | Build detailed financial model | 8 hrs | Excel | Financial model | Accountant review |
| 7 | Create executive summary (2 pages) | 3 hrs | Claude | Executive summary | Leadership approval |
| 8 | Prepare due diligence data room | 4 hrs | Google Drive | Organized data room | Completeness check |
| 9 | Develop FAQ document for investors | 3 hrs | Claude | FAQ document | Mock Q&A testing |
| 10 | Create investor outreach sequence | 2 hrs | Claude | Email templates | Personalization check |

#### 🤖 Agent Assignment

| Agent Type | Tasks | Deliverable |
|------------|-------|-------------|
| **Research Agent** | Steps 2, 3 | Market and competitive research |
| **Analysis Agent** | Step 6 | Financial modeling |
| **Writing Agent** | Steps 4, 7, 9, 10 | Narrative and documentation |
| **Design Agent** | Step 5 | Visual presentation |

#### 🔄 Follow-Up Prompts

1. "Create investor-specific customization for [investor type]"
2. "Develop 5-minute verbal pitch script"
3. "Build objection handling guide"
4. "Create term sheet negotiation strategy"
5. "Prepare for due diligence deep-dive in [area]"

#### ✅ Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Pitch deck completeness | 12-15 slides | Slide count and coverage |
| Financial model accuracy | All formulas verified | Audit check |
| Market data currency | <6 months old | Source dates |
| Data room readiness | 100% documents | Checklist verification |
| Stakeholder approval | Sign-off received | Approval documentation |

#### 📄 Core Prompt

```
You are a seasoned investment banker preparing pitch materials for a fish farming technology company. Create comprehensive investor materials:

**Company Profile: Mustadem**
- Engineering and consulting firm
- Specialization in aquaculture and sustainable infrastructure
- Key differentiators: integrated services, regional expertise, tech-forward approach

**Pitch Deck Structure:**

1. **Cover Slide**
   - Company name and tagline
   - Funding round and amount seeking

2. **Problem Statement**
   - Global protein demand statistics
   - Aquaculture industry challenges
   - Regional market inefficiencies

3. **Solution**
   - Product/service overview
   - Technology platform capabilities
   - Unique value proposition

4. **Market Opportunity**
   - Total Addressable Market (TAM)
   - Serviceable Addressable Market (SAM)
   - Serviceable Obtainable Market (SOM)
   - Growth projections with sources

5. **Business Model**
   - Revenue streams
   - Pricing strategy
   - Unit economics
   - Customer lifetime value

6. **Traction**
   - Current customers/projects
   - Revenue history and projections
   - Key milestones achieved
   - Partnerships secured

7. **Competition**
   - Competitive landscape matrix
   - Differentiation strategy
   - Barriers to entry

8. **Go-to-Market Strategy**
   - Customer acquisition approach
   - Sales cycle and process
   - Channel partnerships

9. **Team**
   - Key team members and backgrounds
   - Advisory board
   - Gaps and hiring plans

10. **Financials**
    - Historical financials (if available)
    - 5-year projections
    - Key assumptions
    - Use of funds

11. **Investment Ask**
    - Amount seeking
    - Valuation rationale
    - Use of proceeds
    - Expected milestones

12. **Appendix**
    - Detailed financial model
    - Market research sources
    - Technical architecture
    - Customer testimonials

**Deliverables:**
1. 15-slide pitch deck (PowerPoint/Google Slides)
2. Executive summary (2 pages)
3. Detailed financial model (Excel)
4. Due diligence data room checklist
5. FAQ document for investor meetings
```

---

### 8. Financial Model Testing Prompt

#### 📋 Pre-Execution Checklist
- [ ] Existing financial models collected
- [ ] Industry benchmarks gathered
- [ ] Economic study data accessible
- [ ] CFO/finance team available for review
- [ ] Timeline: 1-2 weeks for thorough testing

#### 📝 Step-by-Step Breakdown

| Step | Action | Time | Tool | Output | Quality Check |
|------|--------|------|------|--------|---------------|
| 1 | Collect and review existing models | 4 hrs | Excel | Model inventory | Version control setup |
| 2 | Document all model assumptions | 3 hrs | Excel/Notion | Assumption log | Stakeholder validation |
| 3 | Build sensitivity analysis | 4 hrs | Excel | Sensitivity tables | Range verification |
| 4 | Perform scenario analysis (best/base/worst) | 4 hrs | Excel | Scenario outputs | Assumption consistency |
| 5 | Run Monte Carlo simulation (if applicable) | 4 hrs | Excel/Python | Probability distributions | Statistical validation |
| 6 | Compare with Economic studies | 4 hrs | Excel | Comparison matrix | Variance explanation |
| 7 | Validate against operational benchmarks | 3 hrs | Research | Benchmark comparison | Industry alignment |
| 8 | Perform circular reference audit | 2 hrs | Excel | Clean model | Zero circulars |
| 9 | Create key metrics dashboard | 4 hrs | Excel/Sheets | Dashboard | Formula verification |
| 10 | Document and version control | 2 hrs | Notion/Git | Documentation | Review completed |

#### 🤖 Agent Assignment

| Agent Type | Tasks | Deliverable |
|------------|-------|-------------|
| **Analysis Agent** | Steps 1-9 | All financial analysis |
| **Coding Agent** | Step 5 (if Python needed) | Simulation code |
| **Writing Agent** | Step 10 | Documentation |

#### 🔄 Follow-Up Prompts

1. "Build investor-specific model version for [investor type]"
2. "Create detailed cost breakdown for [category]"
3. "Model alternative revenue scenarios"
4. "Perform competitive unit economics analysis"
5. "Build monthly cash flow waterfall"

#### ✅ Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Model accuracy | <5% variance from benchmarks | Comparison analysis |
| Assumption documentation | 100% documented | Documentation review |
| Circular references | Zero | Excel audit |
| Scenario coverage | 3+ scenarios | Scenario count |
| Validation completion | All steps verified | Checklist completion |

#### 📄 Core Prompt

```
You are a financial modeling expert. Build and test robust financial models against existing studies:

**Model Requirements:**

1. **Financial Model Components**
   - Revenue model (multiple scenarios)
   - Cost structure (fixed vs variable)
   - Capital expenditure schedule
   - Working capital requirements
   - Funding requirements and sources
   - Exit scenarios and valuations

2. **Testing Framework**
   - Sensitivity analysis (key variables)
   - Scenario analysis (best/base/worst)
   - Monte Carlo simulation
   - Stress testing

3. **Validation Against Studies**
   - Compare with Economic studies
   - Validate against Operational benchmarks
   - Cross-reference with Antigravity analysis
   - Industry benchmark comparison

4. **Output Requirements**
   - Income statement (monthly for 2 years, annual for 5)
   - Balance sheet projections
   - Cash flow statement
   - Key metrics dashboard (NPV, IRR, payback)
   - Investor returns analysis

**Quality Checks:**
- Circular reference audit
- Formula consistency verification
- Assumption documentation
- Version control implementation
```

---

## New Prompts (9-15)

### 9. Competitor Intelligence Automation Prompt

#### 📋 Pre-Execution Checklist
- [ ] List of known competitors compiled
- [ ] Monitoring tool accounts set up (Mention, Google Alerts)
- [ ] Notion database structure ready
- [ ] Social media monitoring access confirmed
- [ ] Timeline: 2 weeks for initial setup + ongoing

#### 📝 Step-by-Step Breakdown

| Step | Action | Time | Tool | Output | Quality Check |
|------|--------|------|------|--------|---------------|
| 1 | Identify top 20 global aquaculture competitors | 4 hrs | Gemini 3 | Competitor list | Market coverage verification |
| 2 | Research Saudi/GCC regional competitors | 4 hrs | Gemini 3 | Regional competitor list | Local validation |
| 3 | Create competitor database structure | 2 hrs | Notion | Database template | Field completeness |
| 4 | Document competitor products and pricing | 8 hrs | Web research | Product/pricing database | Accuracy verification |
| 5 | Set up Google Alerts for each competitor | 2 hrs | Google Alerts | Alert configurations | Alert delivery test |
| 6 | Configure social media monitoring | 3 hrs | Mention/Hootsuite | Social tracking | Coverage verification |
| 7 | Build website change detection | 3 hrs | Visualping/Distill | Change alerts | Detection testing |
| 8 | Create monthly report template | 2 hrs | Notion/Google Docs | Report template | Stakeholder review |
| 9 | Build automated data collection scripts | 4 hrs | DeepSeek | Scraping scripts | Legal compliance check |
| 10 | Document maintenance procedures | 2 hrs | Claude | SOP document | Team review |

#### 🤖 Agent Assignment

| Agent Type | Tasks | Deliverable |
|------------|-------|-------------|
| **Research Agent** | Steps 1-4 | Competitor research and database |
| **Coding Agent** | Steps 5-7, 9 | Automation setup |
| **Writing Agent** | Steps 8, 10 | Templates and documentation |

#### 🔄 Follow-Up Prompts

1. "Deep dive into [competitor] strategy and positioning"
2. "Analyze [competitor] recent product launch"
3. "Compare our pricing to [competitor] offerings"
4. "Create competitive response strategy for [market move]"
5. "Generate quarterly competitive trends report"

#### ✅ Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Competitors tracked | 20+ | Database count |
| Alert coverage | All competitors | Alert audit |
| Report delivery | Monthly | Schedule adherence |
| Intelligence freshness | <7 days old | Update timestamps |
| Actionable insights | 3+ per month | Insight tracking |

#### 📄 Core Prompt

```
Create an automated system to monitor competitors in the aquaculture space:

**Scope:**
- Identify top 20 competitors globally and in Saudi/GCC
- Track their product launches, pricing, partnerships
- Monitor their social media and website changes
- Set up alerts for news mentions
- Generate monthly competitor intelligence reports

**Data Points to Track:**
1. Company Information
   - Name, headquarters, size, funding status
   - Key personnel and leadership changes
   - Financial performance (if public)

2. Product/Service Intelligence
   - New product launches
   - Pricing changes
   - Feature updates
   - Technology partnerships

3. Marketing Activities
   - Campaign launches
   - Content themes
   - Event participation
   - Thought leadership positioning

4. Business Moves
   - Funding rounds
   - Acquisitions/mergers
   - Market expansion
   - Partnership announcements

**Deliverables:**
- Competitor database (Notion)
- Automated scraping scripts
- Monthly report template
- Alert system configuration
- Competitive positioning matrix
```

---

### 10. Customer Persona Development Prompt

#### 📋 Pre-Execution Checklist
- [ ] Existing customer data accessible
- [ ] Sales team interview scheduled
- [ ] Industry reports on customer segments available
- [ ] Customer interview permission obtained (if applicable)
- [ ] Timeline: 2 weeks for comprehensive personas

#### 📝 Step-by-Step Breakdown

| Step | Action | Time | Tool | Output | Quality Check |
|------|--------|------|------|--------|---------------|
| 1 | Analyze existing customer data | 4 hrs | Excel/CRM | Customer analysis | Data completeness |
| 2 | Interview sales team for insights | 3 hrs | Interviews | Interview notes | Key theme identification |
| 3 | Research commercial fish farmer segment | 4 hrs | Gemini 3 | Segment profile | Market validation |
| 4 | Research small-scale farmer segment | 4 hrs | Gemini 3 | Segment profile | Market validation |
| 5 | Research government projects segment | 4 hrs | Gemini 3 | Segment profile | Stakeholder input |
| 6 | Research processing companies segment | 4 hrs | Gemini 3 | Segment profile | Industry validation |
| 7 | Research institutions segment | 3 hrs | Gemini 3 | Segment profile | Academic input |
| 8 | Create detailed persona documents | 6 hrs | Claude | 5 persona documents | Team review |
| 9 | Build journey maps for each persona | 6 hrs | Miro/Claude | 5 journey maps | Sales team validation |
| 10 | Develop sales playbooks per persona | 6 hrs | Claude | Sales playbook | Sales team testing |

#### 🤖 Agent Assignment

| Agent Type | Tasks | Deliverable |
|------------|-------|-------------|
| **Research Agent** | Steps 1-7 | Segment research |
| **Writing Agent** | Steps 8-10 | Personas, maps, playbooks |
| **Design Agent** | Step 9 (visual) | Journey map visuals |

#### 🔄 Follow-Up Prompts

1. "Create email sequence tailored for [persona]"
2. "Develop objection handling guide for [persona]"
3. "Build case study template for [persona]"
4. "Design demo script for [persona]"
5. "Create ROI calculator for [persona]"

#### ✅ Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Personas developed | 5 complete | Document completion |
| Journey maps | 5 complete | Map completion |
| Sales team adoption | >80% | Usage tracking |
| Lead qualification improvement | +20% | Conversion tracking |
| Stakeholder approval | All signed off | Approval log |

#### 📄 Core Prompt

```
Create detailed customer personas for Mustadem's fish farming clients:

**Target Segments:**
1. Commercial fish farmers (large scale)
2. Small-scale farmers (startups)
3. Government aquaculture projects
4. Fish processing companies
5. Research institutions

**For Each Persona, Include:**

1. **Demographics & Firmographics**
   - Company size and structure
   - Geographic location
   - Years in operation
   - Annual revenue/budget range
   - Number of employees

2. **Pain Points & Challenges**
   - Top 5 operational challenges
   - Technology gaps
   - Resource constraints
   - Regulatory pressures
   - Market challenges

3. **Decision-Making Process**
   - Key decision makers
   - Influencers in purchase
   - Approval process
   - Typical timeline
   - Evaluation criteria

4. **Budget & Investment**
   - Annual technology budget
   - Investment priorities
   - ROI expectations
   - Funding sources
   - Payment preferences

5. **Communication Preferences**
   - Preferred channels (email, phone, in-person)
   - Content consumption habits
   - Industry events attended
   - Trusted information sources
   - Best times to reach

6. **Common Objections**
   - Top 5 sales objections
   - Competitor considerations
   - Risk concerns
   - Implementation fears

7. **Value Drivers**
   - Primary motivations
   - Success metrics
   - Long-term goals
   - Quick wins needed

**Deliverables:**
- 5 detailed persona documents (2-3 pages each)
- Customer journey maps for each persona
- Sales playbook tailored to each persona
- Marketing message framework per persona
- Objection handling guide per persona
```

---

### 11. Content Marketing Engine Prompt

#### 📋 Pre-Execution Checklist
- [ ] Brand guidelines documented
- [ ] Website CMS access confirmed
- [ ] Social media accounts set up
- [ ] Content calendar tool selected (Notion/Asana)
- [ ] Subject matter experts identified
- [ ] Timeline: 3 weeks for system setup + ongoing

#### 📝 Step-by-Step Breakdown

| Step | Action | Time | Tool | Output | Quality Check |
|------|--------|------|------|--------|---------------|
| 1 | Conduct SEO keyword research | 6 hrs | Ahrefs/Semrush | Keyword database | Search volume verification |
| 2 | Develop content pillars strategy | 3 hrs | Claude | Content strategy doc | Alignment with goals |
| 3 | Create 6-month content calendar | 4 hrs | Notion/Asana | Content calendar | Resource availability check |
| 4 | Write 20 blog post outlines | 8 hrs | Claude | Blog outlines | SEO alignment |
| 5 | Develop 5 case study templates | 4 hrs | Claude | Case study templates | Brand alignment |
| 6 | Create email sequence frameworks | 4 hrs | Claude | Email templates | Conversion goals |
| 7 | Build social media schedule | 4 hrs | Hootsuite/Buffer | Social calendar | Platform requirements |
| 8 | Develop video script templates | 4 hrs | Claude | Video templates | Production feasibility |
| 9 | Create content creation workflows | 3 hrs | Notion | Workflow documentation | Team review |
| 10 | Set up content performance tracking | 3 hrs | Google Analytics | Analytics dashboard | Metric accuracy |

#### 🤖 Agent Assignment

| Agent Type | Tasks | Deliverable |
|------------|-------|-------------|
| **Research Agent** | Step 1 | Keyword research |
| **Writing Agent** | Steps 2-6, 8 | All content templates |
| **Design Agent** | Supporting graphics | Visual templates |
| **Analysis Agent** | Step 10 | Analytics setup |

#### 🔄 Follow-Up Prompts

1. "Write full blog post for [outline topic]"
2. "Create social media campaign for [content piece]"
3. "Develop lead magnet from [blog post]"
4. "Build email nurture sequence for [persona]"
5. "Create infographic from [data/report]"

#### ✅ Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Blog posts outlined | 20+ | Calendar count |
| Content calendar | 6 months | Calendar completeness |
| Email sequences | 3+ complete | Sequence count |
| Social media schedule | 4 weeks ahead | Schedule coverage |
| Workflow documentation | 100% complete | Doc review |

#### 📄 Core Prompt

```
Build a comprehensive content marketing system:

**Content Types:**
1. Blog posts (SEO-optimized, 1,500-2,500 words)
2. Case studies (customer success stories)
3. White papers (technical deep-dives)
4. Social media content (LinkedIn, Twitter, YouTube)
5. Email sequences (nurture and promotional)
6. Video scripts (explainers, demos, testimonials)
7. Infographics (data visualization)

**Content Topics:**
1. Fish farming best practices
   - Water quality management
   - Feeding optimization
   - Disease prevention
   - Harvest planning

2. Technology in aquaculture
   - Automation benefits
   - IoT implementation
   - AI applications
   - Data analytics

3. Business of fish farming
   - ROI calculations
   - Market trends
   - Sustainability practices
   - Regulatory compliance

4. Customer success
   - Implementation stories
   - Results achieved
   - Lessons learned
   - Best practices shared

**Distribution Strategy:**
1. LinkedIn (primary B2B channel)
   - 3-5 posts per week
   - Mix of educational and promotional
   - Employee advocacy program

2. Website blog
   - 2 new posts per week
   - SEO optimization
   - Internal linking strategy

3. Email newsletter
   - Weekly digest
   - Monthly deep-dive
   - Promotional campaigns

4. Industry publications
   - Guest article placements
   - Thought leadership pieces
   - Research contributions

5. Conference presentations
   - Speaking opportunities
   - Booth materials
   - Follow-up content

**Deliverables:**
- 6-month content calendar
- 20 blog post outlines with SEO keywords
- 5 case study templates
- Email sequence framework (welcome, nurture, sales)
- Social media schedule template
- Content creation workflow documentation
- Style guide and brand voice guidelines
- Performance tracking dashboard
```

---

### 12. Sales Process Automation Prompt

#### 📋 Pre-Execution Checklist
- [ ] CRM platform selected (HubSpot/Salesforce)
- [ ] Current sales process documented
- [ ] Email marketing tool integrated
- [ ] Lead sources identified
- [ ] Timeline: 4 weeks for full implementation

#### 📝 Step-by-Step Breakdown

| Step | Action | Time | Tool | Output | Quality Check |
|------|--------|------|------|--------|---------------|
| 1 | Document current sales process | 4 hrs | Interviews | Process map | Sales team validation |
| 2 | Design lead scoring model | 4 hrs | HubSpot | Scoring criteria | Historical data testing |
| 3 | Create website form automation | 4 hrs | HubSpot | Form workflows | Submission testing |
| 4 | Build LinkedIn outreach sequences | 6 hrs | Sales Navigator | Outreach templates | Response rate tracking |
| 5 | Develop email drip campaigns | 8 hrs | HubSpot | Email sequences | A/B testing plan |
| 6 | Configure lead routing rules | 3 hrs | HubSpot | Routing automation | Assignment verification |
| 7 | Build proposal template library | 6 hrs | Google Docs/PandaDoc | Proposal templates | Quality review |
| 8 | Create dynamic pricing calculator | 4 hrs | Excel/Google Sheets | Calculator tool | Formula verification |
| 9 | Set up pipeline reporting | 4 hrs | HubSpot | Dashboards | Metric accuracy |
| 10 | Document sales playbook | 6 hrs | Claude | Sales playbook | Team training |

#### 🤖 Agent Assignment

| Agent Type | Tasks | Deliverable |
|------------|-------|-------------|
| **Research Agent** | Step 1 | Process documentation |
| **Coding Agent** | Steps 2-6, 8, 9 | CRM configurations |
| **Writing Agent** | Steps 4, 5, 7, 10 | Templates and playbook |

#### 🔄 Follow-Up Prompts

1. "Optimize email sequence for [stage/persona]"
2. "Create follow-up cadence for [lead source]"
3. "Build competitive displacement playbook"
4. "Develop qualification question framework"
5. "Create sales training module for [topic]"

#### ✅ Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Email sequences | 10+ complete | Sequence count |
| Proposal templates | 5+ | Template library |
| Lead response time | <4 hours | Automation logs |
| Pipeline visibility | 100% | Dashboard accuracy |
| Team adoption | 100% | Usage tracking |

#### 📄 Core Prompt

```
Design and implement automated sales processes:

**Lead Generation:**
1. Website Form Automation
   - Smart forms with progressive profiling
   - Automatic lead capture and enrichment
   - Thank you page personalization
   - Follow-up sequence triggers

2. LinkedIn Outreach Sequences
   - Connection request templates
   - Follow-up message sequences
   - Content sharing automation
   - InMail templates

3. Email Drip Campaigns
   - Welcome series (5 emails)
   - Nurture sequences (10+ emails)
   - Re-engagement campaigns
   - Event-triggered emails

4. Lead Scoring System
   - Demographic scoring criteria
   - Behavioral scoring triggers
   - Engagement score calculation
   - Sales-ready thresholds

**Lead Qualification:**
1. Automated Qualification Questions
   - BANT framework implementation
   - Custom qualification criteria
   - Scoring integration

2. CRM Integration
   - Field mapping
   - Data sync rules
   - Duplicate management
   - Custom objects

3. Lead Routing Rules
   - Geographic assignment
   - Size/industry routing
   - Round-robin distribution
   - Capacity management

4. Follow-Up Sequences
   - Stage-based sequences
   - Time-based triggers
   - Behavior-based triggers
   - Re-engagement automation

**Proposal Generation:**
1. Template Library
   - Standard proposal template
   - Enterprise proposal template
   - Government proposal template
   - Quick quote template
   - Renewal proposal template

2. Dynamic Pricing Calculators
   - Product/service configurator
   - Volume discounting
   - Bundle pricing
   - ROI calculator

3. Automated Proposal Assembly
   - Dynamic content insertion
   - Pricing automation
   - Approval workflows
   - Version control

4. E-Signature Integration
   - DocuSign/HelloSign setup
   - Signature workflows
   - Reminder automation
   - Signed document storage

**Pipeline Management:**
1. Stage Definitions
   - Clear entry/exit criteria
   - Required fields per stage
   - Probability percentages
   - Average time in stage

2. Automation Rules
   - Stage progression triggers
   - Task creation automation
   - Notification rules
   - Deal rot alerts

3. Reporting Dashboards
   - Pipeline health metrics
   - Rep performance
   - Activity tracking
   - Conversion analytics

4. Forecast Tracking
   - Weighted pipeline
   - Commit vs. best case
   - Historical accuracy
   - Trend analysis

**Deliverables:**
- HubSpot/CRM fully configured
- 10+ email sequences ready to deploy
- 5 proposal templates
- Complete sales playbook
- Training materials for team
- Dashboard and reporting setup
```

---

### 13. Partnership Development Prompt

#### 📋 Pre-Execution Checklist
- [ ] Partnership goals defined
- [ ] Legal template access confirmed
- [ ] Partnership owner designated
- [ ] Budget for partner activities approved
- [ ] Timeline: 4 weeks for strategy + ongoing

#### 📝 Step-by-Step Breakdown

| Step | Action | Time | Tool | Output | Quality Check |
|------|--------|------|------|--------|---------------|
| 1 | Define partnership strategy and goals | 3 hrs | Claude | Strategy document | Leadership approval |
| 2 | Research equipment manufacturer partners | 6 hrs | Gemini 3 | Partner database | Coverage verification |
| 3 | Research feed supplier partners | 4 hrs | Gemini 3 | Partner database | Market coverage |
| 4 | Research financial/government partners | 4 hrs | Gemini 3 | Partner database | Relationship mapping |
| 5 | Research technology provider partners | 4 hrs | Gemini 3 | Partner database | Integration feasibility |
| 6 | Create partnership model templates | 4 hrs | Claude | Model documentation | Legal review |
| 7 | Develop outreach email templates | 4 hrs | Claude | Email templates | Response optimization |
| 8 | Create partnership proposal deck | 6 hrs | Google Slides | Proposal deck | Design review |
| 9 | Build agreement templates | 4 hrs | Claude/Legal | Agreement templates | Legal approval |
| 10 | Create partner onboarding process | 4 hrs | Claude | Onboarding guide | Partner feedback |

#### 🤖 Agent Assignment

| Agent Type | Tasks | Deliverable |
|------------|-------|-------------|
| **Research Agent** | Steps 2-5 | Partner research and databases |
| **Writing Agent** | Steps 1, 6, 7, 9, 10 | Strategy and templates |
| **Design Agent** | Step 8 | Proposal presentation |

#### 🔄 Follow-Up Prompts

1. "Create customized proposal for [specific partner]"
2. "Develop co-marketing plan with [partner]"
3. "Build integration roadmap for [tech partner]"
4. "Create partner success metrics dashboard"
5. "Develop partner tier structure"

#### ✅ Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Partners identified | 100+ | Database count |
| Outreach templates | 5+ | Template count |
| Agreement templates | 3 types | Legal approval |
| Partnership deck | 1 complete | Design review |
| Onboarding process | Documented | Process testing |

#### 📄 Core Prompt

```
Create a systematic partnership strategy:

**Target Partner Categories:**
1. Equipment Manufacturers
   - RAS system providers
   - Sensor/IoT manufacturers
   - Feeding system vendors
   - Water treatment equipment

2. Feed Suppliers
   - Major feed companies
   - Specialty feed producers
   - Nutrition consultants
   - Feed technology providers

3. Financial Institutions
   - Agricultural lenders
   - Development banks
   - Insurance providers
   - Investment funds

4. Government Agencies
   - Ministry of Agriculture
   - Saudi Aquaculture Society
   - Research funding bodies
   - Export promotion agencies

5. Research Institutions
   - Universities with aquaculture programs
   - Research centers
   - Innovation labs
   - Industry associations

6. Technology Providers
   - ERP vendors
   - Cloud platform providers
   - AI/ML companies
   - Data analytics firms

7. Distribution Channels
   - Agricultural distributors
   - E-commerce platforms
   - Industry marketplaces
   - Regional resellers

**Partnership Models:**
1. Referral Agreements
   - Commission structure
   - Lead sharing rules
   - Attribution tracking
   - Payment terms

2. Revenue Sharing
   - Joint offering structure
   - Revenue split models
   - Cost allocation
   - Reporting requirements

3. Co-Marketing
   - Joint campaign planning
   - Content collaboration
   - Event participation
   - Lead sharing

4. Technology Integration
   - API partnerships
   - Data sharing agreements
   - Joint development
   - White-label licensing

5. White-Label Offerings
   - Product rebranding rights
   - Pricing structures
   - Support responsibilities
   - Quality standards

**Outreach Strategy:**
1. Partner Identification Criteria
   - Market alignment score
   - Capability assessment
   - Cultural fit evaluation
   - Financial stability check

2. Outreach Templates
   - Initial introduction email
   - Follow-up sequence
   - Meeting request
   - Value proposition summary
   - Reference offer

3. Value Proposition Framework
   - Equipment partners value prop
   - Feed partners value prop
   - Financial partners value prop
   - Tech partners value prop
   - Distribution value prop

4. Agreement Templates
   - Basic referral agreement
   - Revenue share agreement
   - Co-marketing agreement
   - Technology partnership agreement

5. Onboarding Process
   - Welcome package
   - Training materials
   - Portal access setup
   - Success metrics alignment
   - Regular check-in schedule

**Deliverables:**
- Target partner database (100+ contacts)
- 5 outreach email templates
- Partnership proposal deck
- 3 agreement templates (legal-reviewed)
- Partner onboarding guide
- Partner success metrics framework
- Partnership tier structure
```

---

### 14. Operations Manual Creation Prompt

#### 📋 Pre-Execution Checklist
- [ ] Current processes documented informally
- [ ] Process owners identified
- [ ] Stakeholder interviews scheduled
- [ ] Documentation platform selected (Notion/Confluence)
- [ ] Timeline: 6 weeks for all manuals

#### 📝 Step-by-Step Breakdown

| Step | Action | Time | Tool | Output | Quality Check |
|------|--------|------|------|--------|---------------|
| 1 | Interview process owners for sales ops | 4 hrs | Interviews | Interview notes | Coverage verification |
| 2 | Document sales operations processes | 8 hrs | Claude | Sales ops manual | Process owner review |
| 3 | Interview process owners for delivery | 4 hrs | Interviews | Interview notes | Coverage verification |
| 4 | Document project delivery processes | 8 hrs | Claude | Delivery manual | PM review |
| 5 | Interview process owners for client success | 3 hrs | Interviews | Interview notes | Coverage verification |
| 6 | Document client success processes | 6 hrs | Claude | Client success manual | Team review |
| 7 | Interview finance team | 3 hrs | Interviews | Interview notes | Coverage verification |
| 8 | Document financial operations | 6 hrs | Claude | Finance manual | CFO review |
| 9 | Create process flowcharts for all manuals | 8 hrs | Miro/Lucidchart | Flowcharts | Accuracy verification |
| 10 | Compile template library | 4 hrs | Google Drive | Template folder | Completeness check |

#### 🤖 Agent Assignment

| Agent Type | Tasks | Deliverable |
|------------|-------|-------------|
| **Research Agent** | Steps 1, 3, 5, 7 | Interviews and notes |
| **Writing Agent** | Steps 2, 4, 6, 8 | Manual documents |
| **Design Agent** | Step 9 | Flowcharts and visuals |

#### 🔄 Follow-Up Prompts

1. "Create training video script for [process]"
2. "Develop quick reference card for [manual]"
3. "Build checklist version of [process]"
4. "Create troubleshooting guide for [area]"
5. "Develop onboarding training for [role]"

#### ✅ Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Manuals completed | 4 | Document completion |
| Processes documented | 50+ | Process count |
| Flowcharts created | 20+ | Visual count |
| Templates created | 30+ | Template count |
| Stakeholder approval | All signed off | Approval log |

#### 📄 Core Prompt

```
Develop comprehensive operations manuals for Mustadem:

**1. Sales Operations Manual**

Chapter 1: Lead Management
- Lead source definitions
- Lead capture processes
- Lead qualification criteria
- Lead routing procedures
- Lead nurturing guidelines

Chapter 2: CRM Usage Guide
- Data entry standards
- Activity logging requirements
- Pipeline management rules
- Reporting procedures
- Integration usage

Chapter 3: Proposal Development
- Proposal request process
- Scope definition guidelines
- Pricing procedures
- Approval workflows
- Revision management

Chapter 4: Contract Management
- Contract templates usage
- Negotiation guidelines
- Approval authority matrix
- Signature procedures
- Contract storage/retrieval

**2. Project Delivery Manual**

Chapter 1: Project Intake
- Request submission process
- Initial assessment criteria
- Feasibility evaluation
- Resource availability check
- Kickoff scheduling

Chapter 2: Scope Definition
- Requirements gathering process
- Scope documentation standards
- Change request procedures
- Sign-off requirements

Chapter 3: Resource Allocation
- Skill matching process
- Capacity planning
- Team assignment
- Conflict resolution

Chapter 4: Quality Assurance
- Quality standards definition
- Review checkpoints
- Testing procedures
- Defect management
- Final approval process

Chapter 5: Client Communication
- Communication cadence
- Status reporting templates
- Escalation procedures
- Meeting management

Chapter 6: Handover Procedures
- Deliverable packaging
- Documentation requirements
- Training delivery
- Support transition
- Closure documentation

**3. Client Success Manual**

Chapter 1: Client Onboarding
- Welcome process
- Kickoff meeting agenda
- Account setup procedures
- Training delivery
- Success criteria definition

Chapter 2: Ongoing Engagement
- Check-in cadence
- Health score tracking
- Issue identification
- Success planning

Chapter 3: Issue Resolution
- Issue intake process
- Severity classification
- Resolution procedures
- Escalation paths
- Root cause analysis

Chapter 4: Growth Opportunities
- Upsell identification
- Cross-sell procedures
- Expansion planning
- Reference requests

Chapter 5: Renewal Process
- Renewal timeline
- Preparation checklist
- Pricing review
- Contract preparation
- Renewal negotiation

**4. Financial Operations Manual**

Chapter 1: Invoicing
- Invoice creation process
- Invoice review/approval
- Delivery procedures
- AR tracking
- Collection procedures

Chapter 2: Expense Management
- Expense policy
- Submission procedures
- Approval workflows
- Reimbursement process
- Travel policies

Chapter 3: Financial Reporting
- Report definitions
- Data collection procedures
- Report preparation
- Review schedules
- Distribution lists

Chapter 4: Budget Management
- Budget planning process
- Variance tracking
- Forecast updates
- Reallocation procedures

**Deliverables:**
- 4 comprehensive operations manuals
- Process flowcharts for each major process
- Template library (forms, checklists, reports)
- Video script outlines for training
- Quick reference guides (1-page summaries)
- Glossary of terms
- Role responsibility matrices
```

---

### 15. KPI Dashboard Development Prompt

#### 📋 Pre-Execution Checklist
- [ ] Data sources identified and accessible
- [ ] Dashboard platform selected (Data Studio/Tableau/Power BI)
- [ ] Stakeholder requirements gathered
- [ ] Data refresh frequency agreed
- [ ] Timeline: 3 weeks for full dashboard

#### 📝 Step-by-Step Breakdown

| Step | Action | Time | Tool | Output | Quality Check |
|------|--------|------|------|--------|---------------|
| 1 | Define KPI requirements with stakeholders | 4 hrs | Interviews | KPI list | Stakeholder sign-off |
| 2 | Map data sources for each KPI | 4 hrs | Spreadsheet | Data map | Source accessibility |
| 3 | Design sales metrics dashboard | 6 hrs | Data Studio | Sales dashboard | Data accuracy |
| 4 | Design financial metrics dashboard | 6 hrs | Data Studio | Finance dashboard | CFO review |
| 5 | Design operations metrics dashboard | 6 hrs | Data Studio | Ops dashboard | PM review |
| 6 | Design marketing metrics dashboard | 6 hrs | Data Studio | Marketing dashboard | Data accuracy |
| 7 | Create data integration connections | 6 hrs | Data Studio/Zapier | Data connections | Sync verification |
| 8 | Set up automated refresh schedules | 2 hrs | Data Studio | Refresh config | Timing verification |
| 9 | Configure alert notifications | 3 hrs | Email/Slack | Alert rules | Trigger testing |
| 10 | Create executive summary template | 3 hrs | Google Slides | Summary template | Leadership review |

#### 🤖 Agent Assignment

| Agent Type | Tasks | Deliverable |
|------------|-------|-------------|
| **Research Agent** | Steps 1, 2 | Requirements and mapping |
| **Coding Agent** | Steps 3-8 | Dashboard development |
| **Writing Agent** | Step 10 | Summary template |

#### 🔄 Follow-Up Prompts

1. "Add [new metric] to dashboard"
2. "Create drill-down view for [metric]"
3. "Build comparison dashboard for [time period]"
4. "Develop forecast visualization"
5. "Create mobile-friendly dashboard version"

#### ✅ Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Dashboard sections | 4 complete | Section count |
| KPIs tracked | 30+ | Metric count |
| Data refresh | Real-time/daily | Refresh verification |
| Alerts configured | 10+ | Alert count |
| User adoption | 100% leadership | Usage tracking |

#### 📄 Core Prompt

```
Create a comprehensive KPI tracking system:

**1. Sales Metrics Dashboard**

Pipeline Metrics:
- Total pipeline value (SAR)
- Pipeline by stage
- New opportunities added (weekly/monthly)
- Opportunities advanced/stalled
- Average deal size
- Pipeline velocity

Conversion Metrics:
- Lead to opportunity rate
- Opportunity to proposal rate
- Proposal to close rate
- Overall win rate
- Loss reason analysis

Activity Metrics:
- Calls/meetings completed
- Emails sent
- Proposals generated
- Demos delivered

Performance Metrics:
- Sales cycle length (by segment)
- Average time in each stage
- Rep performance comparison
- Quota attainment

**2. Financial Metrics Dashboard**

Revenue Metrics:
- Monthly revenue (actual vs. target)
- Quarterly revenue tracking
- Revenue by service line
- Revenue by customer segment
- Revenue concentration (top customers)

Profitability Metrics:
- Gross margin by project
- Net profit margin
- Service line profitability
- Customer profitability

Cash Flow Metrics:
- Cash position
- Accounts receivable aging
- Days sales outstanding (DSO)
- Cash burn rate
- Runway calculation

Budget Metrics:
- Budget vs. actual by category
- Variance analysis
- YTD spending trends
- Forecast accuracy

**3. Operations Metrics Dashboard**

Project Metrics:
- Projects in progress
- On-time delivery rate
- Projects over budget
- Resource utilization
- Backlog size

Quality Metrics:
- Customer satisfaction scores
- Issue/defect rates
- First-time-right percentage
- Rework hours

Delivery Metrics:
- Average project duration
- Milestone achievement rate
- Scope change frequency
- Hand-off success rate

Capacity Metrics:
- Team utilization rate
- Billable vs. non-billable hours
- Overtime trends
- Hiring needs forecast

**4. Marketing Metrics Dashboard**

Website Metrics:
- Monthly visitors
- Traffic sources breakdown
- Bounce rate
- Time on site
- Conversion rate

Lead Generation:
- Leads by source
- Lead quality score distribution
- Cost per lead
- Lead to MQL conversion

Content Performance:
- Blog post views
- Content downloads
- Social media engagement
- Email open/click rates

Campaign ROI:
- Campaign performance
- Cost per acquisition
- Marketing influenced pipeline
- Attribution analysis

**Deliverables:**
- Google Data Studio dashboard (or Power BI/Tableau)
- Data integration setup documentation
- Automated daily/weekly/monthly reports
- Alert configurations for key thresholds
- Executive summary template (weekly)
- User guide for dashboard navigation
- Data dictionary
```

---

## Prompt Chaining Workflows

These workflows demonstrate how to chain multiple prompts together for complex initiatives.

### Workflow 1: New Client Acquisition 🎯

**Objective:** Acquire a new enterprise client from initial targeting to closed deal

| Step | Prompt | Action | Output | Duration |
|------|--------|--------|--------|----------|
| 1 | Prompt #10 (Persona) | Identify target client type | Persona profile | Day 1 |
| 2 | Prompt #11 (Content) | Create relevant content | Blog posts, case study | Days 2-5 |
| 3 | Prompt #9 (Competitor Intel) | Research competitor positioning | Competitive brief | Day 3 |
| 4 | Prompt #12 (Sales) | Generate outreach sequence | Email sequence | Days 4-5 |
| 5 | Prompt #7 (Pitch) | Prepare proposal | Pitch deck, proposal | Days 7-10 |
| 6 | Prompt #15 (Dashboard) | Track in pipeline | Dashboard updates | Ongoing |

**Chaining Notes:**
- Persona informs content topics
- Content supports outreach credibility
- Competitor intel shapes positioning
- All tracked in unified dashboard

---

### Workflow 2: New Service Launch 🚀

**Objective:** Launch a new consulting service from concept to market

| Step | Prompt | Action | Output | Duration |
|------|--------|--------|--------|----------|
| 1 | Prompt #3 (Value Chain) | Identify opportunity gap | Gap analysis | Week 1 |
| 2 | Prompt #1 (Research) | Deep market research | Market analysis | Week 2 |
| 3 | Prompt #8 (Financial) | Build service financial model | Pro forma | Week 3 |
| 4 | Prompt #7 (Pitch) | Create service package | Service deck | Week 4 |
| 5 | Prompt #11 (Content) | Develop marketing materials | Content package | Week 5 |
| 6 | Prompt #12 (Sales) | Launch go-to-market | Sales sequences | Week 6 |

**Chaining Notes:**
- Value chain gap validates opportunity
- Research provides market sizing
- Financial model proves viability
- Marketing and sales execute launch

---

### Workflow 3: Partner Ecosystem Build 🤝

**Objective:** Develop a partner ecosystem for channel expansion

| Step | Prompt | Action | Output | Duration |
|------|--------|--------|--------|----------|
| 1 | Prompt #3 (Value Chain) | Identify partnership opportunities | Gap analysis | Week 1 |
| 2 | Prompt #13 (Partnership) | Research and prioritize partners | Partner database | Weeks 2-3 |
| 3 | Prompt #10 (Persona) | Create partner personas | Partner profiles | Week 3 |
| 4 | Prompt #11 (Content) | Create partner-focused content | Content package | Week 4 |
| 5 | Prompt #12 (Sales) | Develop partner outreach | Outreach sequences | Week 5 |
| 6 | Prompt #14 (Operations) | Create partner onboarding | Operations manual | Week 6 |

**Chaining Notes:**
- Value chain identifies where partners add value
- Partner research and personas inform outreach
- Operations manual ensures consistent onboarding

---

### Workflow 4: Operational Excellence Initiative ⚙️

**Objective:** Systematize operations for scalable growth

| Step | Prompt | Action | Output | Duration |
|------|--------|--------|--------|----------|
| 1 | Prompt #14 (Operations) | Document current processes | Operations manuals | Weeks 1-4 |
| 2 | Prompt #12 (Sales) | Automate sales processes | CRM automation | Weeks 2-3 |
| 3 | Prompt #15 (Dashboard) | Build performance tracking | KPI dashboards | Weeks 3-4 |
| 4 | Prompt #2 (LLM) | Set up AI for internal efficiency | LLM deployment | Weeks 4-6 |
| 5 | Prompt #11 (Content) | Create training content | Training materials | Week 5 |
| 6 | Prompt #8 (Financial) | Measure operational ROI | Financial analysis | Week 6 |

**Chaining Notes:**
- Documentation precedes automation
- Dashboards enable measurement
- Training ensures adoption
- Financial analysis proves value

---

### Workflow 5: Investment Readiness Program 💰

**Objective:** Prepare company for investment round

| Step | Prompt | Action | Output | Duration |
|------|--------|--------|--------|----------|
| 1 | Prompt #1 (Research) | Complete market research | Market analysis | Week 1 |
| 2 | Prompt #9 (Competitor) | Build competitive intelligence | Competitor brief | Week 2 |
| 3 | Prompt #8 (Financial) | Develop and test models | Financial models | Weeks 2-3 |
| 4 | Prompt #15 (Dashboard) | Create investor metrics | Dashboard | Week 3 |
| 5 | Prompt #7 (Pitch) | Prepare pitch materials | Pitch deck, data room | Weeks 4-5 |
| 6 | Prompt #10 (Persona) | Create investor personas | Investor profiles | Week 4 |

**Chaining Notes:**
- Research and competitive intel inform positioning
- Financial models provide investor-ready numbers
- Dashboard demonstrates operational maturity
- Investor personas personalize outreach

---

## Agent Handoff Templates

Use these templates when assigning work to AI agents or team members.

### 📊 Research Agent Template

```
RESEARCH REQUEST

Objective: [Clear one-sentence goal]
Example: "Identify top 20 aquaculture technology companies globally"

Context: [Background information]
Example: "Mustadem needs to understand competitive landscape for investor pitch"

Scope: [What to include/exclude]
- Include: [specific items]
- Exclude: [specific items]
- Geographic focus: [regions]
- Time period: [dates]

Data Sources to Use:
- [ ] Industry databases
- [ ] Company websites
- [ ] News articles
- [ ] Academic papers
- [ ] Other: [specify]

Format Required:
- [ ] Spreadsheet/database
- [ ] Report document
- [ ] Presentation
- [ ] Other: [specify]

Deadline: [Date/time]

Quality Criteria:
- [ ] All sources verified and cited
- [ ] Data is current (<6 months old)
- [ ] Coverage is comprehensive
- [ ] Formatting is consistent
- [ ] Ready for stakeholder review
```

---

### ✍️ Writing Agent Template

```
WRITING REQUEST

Document Type: [Report/Deck/Email/Blog/Manual/etc.]

Audience: [Who will read this]
- Role: [Job titles]
- Knowledge level: [Beginner/Intermediate/Expert]
- Relationship to company: [Customer/Investor/Partner/Internal]

Purpose: [What should this document achieve]
- Primary goal:
- Secondary goal:

Key Messages: [3-5 main points to convey]
1. 
2. 
3. 
4. 
5. 

Tone: [Professional/Technical/Casual/Persuasive/Educational]

Length: [Word count or page count]

Structure Required:
- [ ] Executive summary
- [ ] Sections/chapters
- [ ] Bullet points
- [ ] Visuals/diagrams
- [ ] Action items

References/Source Materials:
- [Link/file 1]
- [Link/file 2]

Template/Style Guide: [Link if available]

Deadline: [Date/time]

Review Process:
- [ ] First draft by: [date]
- [ ] Review by: [person]
- [ ] Final version by: [date]
```

---

### 📈 Analysis Agent Template

```
ANALYSIS REQUEST

Analysis Type: [Financial/Market/Competitive/Operational/etc.]

Objective: [Clear one-sentence goal]

Data Sources:
- Source 1: [location/access]
- Source 2: [location/access]
- Source 3: [location/access]

Analysis Required:
- [ ] Trend analysis
- [ ] Comparative analysis
- [ ] Variance analysis
- [ ] Scenario analysis
- [ ] Other: [specify]

Key Questions to Answer:
1. 
2. 
3. 

Output Format:
- [ ] Executive summary
- [ ] Charts/graphs
- [ ] Data tables
- [ ] Recommendations
- [ ] Next steps

Tools to Use:
- [ ] Excel/Google Sheets
- [ ] Python/R
- [ ] Tableau/Power BI
- [ ] Other: [specify]

Deadline: [Date/time]

Quality Criteria:
- [ ] Methodology documented
- [ ] Assumptions stated
- [ ] Data validated
- [ ] Peer reviewed
- [ ] Actionable insights included
```

---

### 💻 Coding Agent Template

```
CODING REQUEST

Project Type: [Automation/Integration/Script/Application/etc.]

Objective: [Clear one-sentence goal]

Technical Requirements:
- Language: [Python/JavaScript/etc.]
- Framework: [if applicable]
- Platform: [deployment target]

Inputs:
- Data source 1: [format, location]
- Data source 2: [format, location]

Outputs:
- Expected output 1: [format, location]
- Expected output 2: [format, location]

Functional Requirements:
1. 
2. 
3. 

Non-Functional Requirements:
- Performance: [speed/scale requirements]
- Security: [requirements]
- Reliability: [uptime/error handling]

Integration Points:
- System 1: [API/method]
- System 2: [API/method]

Testing Requirements:
- [ ] Unit tests
- [ ] Integration tests
- [ ] User acceptance testing

Deadline: [Date/time]

Deliverables:
- [ ] Working code
- [ ] Documentation
- [ ] Deployment instructions
- [ ] Maintenance guide
```

---

### 🎨 Design Agent Template

```
DESIGN REQUEST

Design Type: [Presentation/Infographic/UI/Document Layout/etc.]

Purpose: [What should the design achieve]

Audience: [Who will view this]

Brand Guidelines: [Link to brand guide if available]

Content to Include:
- [ ] Text content: [link/document]
- [ ] Data/charts: [link/document]
- [ ] Images: [provided/source needed]

Style Requirements:
- Colors: [palette/hex codes]
- Fonts: [font names]
- Style: [Modern/Classic/Technical/etc.]

Dimensions:
- Format: [16:9/Letter/A4/Web/etc.]
- Resolution: [requirement]

Inspiration/Examples:
- [Link 1]
- [Link 2]

Number of Versions: [how many options needed]

Deadline: [Date/time]

Deliverables:
- [ ] Source files (Figma/Canva/etc.)
- [ ] Exported files (PDF/PNG/etc.)
- [ ] Editable template version
```

---

## Quality Assurance Procedures

### 📋 Universal Review Checklist

Before marking any deliverable complete:

**Content Quality**
- [ ] Objective achieved (matches original request)
- [ ] Information is accurate and verified
- [ ] Sources are cited where applicable
- [ ] Language is clear and professional
- [ ] No spelling/grammar errors

**Formatting**
- [ ] Consistent formatting throughout
- [ ] Proper headings and structure
- [ ] Visual elements are clear
- [ ] Branding guidelines followed
- [ ] Print/screen ready

**Completeness**
- [ ] All required sections included
- [ ] No placeholder text remaining
- [ ] All links/references working
- [ ] Supporting files attached
- [ ] Version clearly marked

**Approval**
- [ ] Self-review completed
- [ ] Peer review (if required)
- [ ] Stakeholder review scheduled
- [ ] Final sign-off obtained
- [ ] Archived properly

### 🔄 Revision Guidelines

**Minor Revisions (same day)**
- Typos and formatting fixes
- Small content adjustments
- Clarification of existing points

**Major Revisions (1-3 days)**
- Structural changes
- New sections or content
- Significant rewriting

**Full Rework (3-5 days)**
- Complete restructuring
- New research required
- Change in objective/scope

### 📂 Version Control

**Naming Convention:**
`[Document Name]_v[Major].[Minor]_[Date]`

Example: `Sales_Playbook_v2.3_20241127`

**Version History Log:**
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v1.0 | [date] | [name] | Initial draft |
| v1.1 | [date] | [name] | Review feedback |
| v2.0 | [date] | [name] | Major revision |

### 📁 Archive Procedures

1. **Active Documents:** Current working versions in main folder
2. **Archive:** Previous versions in dated subfolders
3. **Retention:** Keep last 5 major versions minimum
4. **Backup:** Weekly automated backup

---

## Tech Stack Overview

### Primary Tools

| Tool | Purpose | Strength | Cost | Best For |
|------|---------|----------|------|----------|
| GitHub Copilot | Code assistance | Light, efficient | $10/mo | Daily coding tasks |
| Antigravity | AI development | Free, powerful but RAM-heavy | Free | Complex AI projects |
| VS Code | Coding | Cheap, light | Free | All development |
| Gemini 3 | Research, graphs, dashboards | Handles chaos data well | Free tier | Research, analysis |
| ChatGPT | General AI tasks | Versatile | $20/mo | Daily AI tasks |
| Claude | Long-form content | Best organized output | $20/mo | Reports, documents |
| Grok AI | Speed tasks | Speed, free API tier | Free | Quick queries |
| Notion | Documentation, AI integration | Central knowledge base | $10/mo | Knowledge management |
| Asana | Project & team management | Good integrations | Free-$25/mo | Task tracking |
| Google Workspace | Collaboration | Ultra Gemini integration | $12/mo | Team collaboration |
| DeepSeek | Coding | Free, good quality | Free | Code generation |

### Tool Selection by Task Type

| Task | Primary Tool | Alternative | Notes |
|------|-------------|-------------|-------|
| Market Research | Gemini 3 | Perplexity | Best for complex queries |
| Long Reports | Claude | ChatGPT | Superior structure |
| Quick Analysis | ChatGPT | Gemini 3 | Fast turnaround |
| Code Generation | DeepSeek | GitHub Copilot | Free + quality |
| Automation Scripts | DeepSeek | Python + GPT | Complex workflows |
| Data Visualization | Google Sheets | Excel | Easy sharing |
| Dashboards | Data Studio | Tableau | Free + powerful |
| Presentations | Google Slides | Canva | Brand consistency |
| Documentation | Notion | Confluence | AI integration |
| Project Management | Asana | Monday.com | Better for agile |

### Integration Instructions

**Notion + AI Integration:**
1. Enable Notion AI in workspace settings
2. Use `/ai` command for summaries and content
3. Connect to Asana via Zapier for task sync
4. Use database relations for knowledge linking

**Google Workspace + Gemini:**
1. Enable Gemini for Workspace add-on
2. Use in Gmail, Docs, Sheets, Slides
3. Access via side panel in each app
4. Works with existing documents

**CRM + Marketing Stack:**
1. HubSpot as central CRM
2. Connect to Google Workspace
3. Integrate email sequences
4. Sync with analytics

### Cost Optimization

| Tier | Monthly Cost | Tools Included |
|------|-------------|----------------|
| Essential | ~$50 | ChatGPT, Notion, Google Workspace |
| Standard | ~$100 | + Claude, HubSpot free, Asana |
| Professional | ~$200 | + Specialized tools, API access |

### Training Resources

| Tool | Training Resource | Time to Learn |
|------|------------------|---------------|
| Notion | notion.so/guides | 2-4 hours |
| Asana | academy.asana.com | 2-3 hours |
| HubSpot | academy.hubspot.com | 4-8 hours |
| Google Data Studio | google.com/datastudio | 3-4 hours |
| Claude/ChatGPT | prompt-engineering.com | 2-3 hours |

---

## Troubleshooting Guide

### 🚨 Common Issues and Solutions

#### Issue: AI Agent Not Producing Desired Output

**Symptoms:**
- Output doesn't match expectations
- Missing key information
- Wrong format or structure

**Solutions:**
1. **Improve the prompt:**
   - Be more specific about requirements
   - Provide examples of desired output
   - Break complex requests into steps
   
2. **Check context:**
   - Ensure all necessary background is provided
   - Remove conflicting instructions
   - Clarify ambiguous terms

3. **Try different agent:**
   - Claude for structured documents
   - Gemini for research tasks
   - ChatGPT for general tasks

4. **Iterate:**
   - Ask for revisions with specific feedback
   - Build output incrementally
   - Validate intermediate outputs

---

#### Issue: Missing Data or Resources

**Symptoms:**
- Cannot access required databases
- Data sources unavailable
- Missing credentials

**Solutions:**
1. **Identify alternative sources:**
   - Use multiple data sources
   - Cross-reference for accuracy
   - Document data gaps

2. **Request access:**
   - Contact IT/admin for credentials
   - Request team member sharing
   - Use trial/demo accounts

3. **Work around gaps:**
   - Use estimates with clear assumptions
   - Flag missing data in deliverables
   - Plan data collection activities

---

#### Issue: Timeline Conflicts

**Symptoms:**
- Deadline not achievable
- Resource conflicts
- Dependencies not met

**Solutions:**
1. **Reprioritize:**
   - Identify critical path items
   - Defer non-essential tasks
   - Parallel process where possible

2. **Communicate early:**
   - Alert stakeholders immediately
   - Propose revised timeline
   - Document impact

3. **Reduce scope:**
   - Deliver MVP first
   - Phase deliverables
   - Focus on highest-value items

---

#### Issue: Quality Concerns

**Symptoms:**
- Deliverables below standards
- Errors or inaccuracies
- Poor formatting

**Solutions:**
1. **Add review steps:**
   - Implement peer review
   - Use checklists
   - Add QA gate before delivery

2. **Provide feedback:**
   - Document specific issues
   - Create improvement plan
   - Train on standards

3. **Use templates:**
   - Standardize formats
   - Provide examples
   - Create style guides

---

#### Issue: Integration Failures

**Symptoms:**
- Tools not syncing
- Data not flowing
- API errors

**Solutions:**
1. **Check connections:**
   - Verify API credentials
   - Test integrations manually
   - Review error logs

2. **Troubleshoot systematically:**
   - Isolate the failure point
   - Test components individually
   - Document for future reference

3. **Use workarounds:**
   - Manual data transfer temporarily
   - Alternative tools
   - Simplified workflow

---

### 🆘 Escalation Path

| Issue Level | Response Time | Escalate To |
|-------------|---------------|-------------|
| Minor (cosmetic) | 1 day | Team lead |
| Moderate (functional) | 4 hours | Project manager |
| Major (blocker) | 1 hour | Department head |
| Critical (business impact) | Immediate | Executive team |

---

## Progress Tracking

### 📊 Prompt Execution Status

| # | Prompt | Status | Owner | Completion % | Notes |
|---|--------|--------|-------|--------------|-------|
| 1 | Farm Management System Research | 🔴 Not Started | TBD | 0% | Pending assignment |
| 2 | Local LLM Setup | 🔴 Not Started | TBD | 0% | Hardware needed |
| 3 | Value Chain Gap Analysis | 🔴 Not Started | TBD | 0% | Pending assignment |
| 4 | Agricultural Dropshipping Research | 🔴 Not Started | TBD | 0% | Pending assignment |
| 5 | FBA Product Research | 🔴 Not Started | TBD | 0% | Pending assignment |
| 6 | SaaS/App Market Gap Analysis | 🔴 Not Started | TBD | 0% | Pending assignment |
| 7 | Investment Pitch Preparation | 🟡 In Progress | TBD | 25% | Priority item |
| 8 | Financial Model Testing | 🔴 Not Started | TBD | 0% | Awaiting prompt 7 |
| 9 | Competitor Intelligence | 🔴 Not Started | TBD | 0% | Pending assignment |
| 10 | Customer Persona Development | 🔴 Not Started | TBD | 0% | Pending assignment |
| 11 | Content Marketing Engine | 🔴 Not Started | TBD | 0% | Pending assignment |
| 12 | Sales Process Automation | 🔴 Not Started | TBD | 0% | Pending assignment |
| 13 | Partnership Development | 🔴 Not Started | TBD | 0% | Pending assignment |
| 14 | Operations Manual Creation | 🔴 Not Started | TBD | 0% | Pending assignment |
| 15 | KPI Dashboard Development | 🔴 Not Started | TBD | 0% | Pending assignment |

### 🚦 Status Legend

| Status | Symbol | Meaning |
|--------|--------|---------|
| Not Started | 🔴 | Work has not begun |
| In Progress | 🟡 | Actively being worked on |
| Completed | 🟢 | Finished and approved |
| Blocked | ⚪ | Cannot proceed due to blocker |
| On Hold | 🔵 | Paused intentionally |

### 📅 Weekly Status Update Template

```
WEEKLY STATUS UPDATE - [Date]

**Completed This Week:**
- [Item 1]
- [Item 2]

**In Progress:**
- [Item 1] - [% complete] - [Expected completion]
- [Item 2] - [% complete] - [Expected completion]

**Blocked Items:**
- [Item] - [Blocker description] - [Help needed]

**Next Week Focus:**
- [Priority 1]
- [Priority 2]

**Resource Needs:**
- [Resource 1]
- [Resource 2]

**Key Risks:**
- [Risk 1] - [Mitigation]
```

---

## Quick Reference

### Priority Legend
- **Critical** - Must complete before Dubai trip
- **High** - Complete within 1-2 weeks
- **Medium** - Complete within 1 month
- **Low** - Complete when resources available

### Key Contacts & Actions (Enhanced)

| Contact | Action | Priority | Last Contact | Next Step | Decision Authority | Preferred Channel |
|---------|--------|----------|--------------|-----------|-------------------|-------------------|
| Ivar | Email re: Kevin investment | High | TBD | Send follow-up | Introducer | Email |
| AL Khansaa | Email re: SPV | High | TBD | Schedule call | Legal decision | Email |
| LEO | Message re: investment | High | TBD | Initial outreach | Investor | WhatsApp |
| Farid | Message re: investment/CFO | High | TBD | Discuss role | CFO potential | WhatsApp |
| Raf Ali | Email re: legal representation | High | TBD | Send requirements | Legal advisor | Email |
| Sayaka | Investment discussion | High | TBD | Schedule meeting | Investor | Email |
| Kevin | Due diligence | High | TBD | Prepare materials | Lead investor | Email/Call |
| Abdullah AlQarni | Meeting - ask for help | High | TBD | Request meeting | Strategic advisor | Phone |
| Mohamed Almajed | Meeting - investment | High | TBD | Send pitch deck | Investor | Email |

### Contact Relationship Tracker

| Contact | Relationship Status | Engagement Level | Opportunity Value |
|---------|--------------------|--------------------|-------------------|
| Kevin | Active discussion | High | Primary investment |
| Sayaka | Initial contact | Medium | Secondary investment |
| Abdullah AlQarni | Warm relationship | High | Strategic guidance |
| Mohamed Almajed | Cold | Low | Potential investment |

### Key Deadlines
- [ ] Investment pitch ready before Dubai trip
- [ ] MOU with Ayham/Aseer signed
- [ ] Nebras profile transfer completed
- [ ] Intersect action plan created

### Quick Action Items
- [ ] Send pitch deck to priority contacts
- [ ] Complete financial model updates
- [ ] Prepare due diligence materials
- [ ] Schedule investor meetings

---

*Generated for Mustadem Project Pipeline*
*Import CSV file to Asana for task tracking*
*Last Updated: [Date]*
