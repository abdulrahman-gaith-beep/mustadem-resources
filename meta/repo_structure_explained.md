# Repository Structure Explained

## Overview

This document explains the organization of the Mustadem knowledge base repository. Understanding this structure will help you navigate content efficiently and contribute effectively.

## Folder Organization

### Repository Root
```
mustadem-resources/
├── README.md                    # Main repository introduction
├── ENHANCED_TASK_LIST.md        # Development roadmap and task tracking
├── TASK_LIST_FOR_NEXT_AGENT.md  # Agent handoff documentation
├── company/                     # Company information
├── meta/                        # Repository documentation
├── operations_as_a_service/     # Operations templates and guides
├── people_and_onboarding/       # HR and training materials
├── project_delivery/            # Project management resources
├── ras_knowledge_base/          # Technical RAS documentation
├── sales_and_marketing/         # Sales tools and templates
├── spv_and_finance/             # Financial models and guides
└── templates/                   # Client-facing templates
```

### Folder Descriptions

#### `company/`
**Purpose:** Core company documentation and identity materials

| File | Description |
|------|-------------|
| `mission_vision_values.md` | Company mission, vision, values, and sustainability commitment |
| `mustadem_overview.md` | Company profile, capabilities, leadership, and contact information |

**Use Cases:**
- Understanding company positioning and values
- Investor and client presentations
- Employee onboarding materials

---

#### `meta/`
**Purpose:** Documentation about the repository itself

| File | Description |
|------|-------------|
| `CONTRIBUTING.md` | Guidelines for contributing to the knowledge base |
| `repo_structure_explained.md` | This document - repository organization guide |

**Use Cases:**
- New contributor orientation
- Repository maintenance
- Documentation standards reference

---

#### `operations_as_a_service/`
**Purpose:** Operational templates, SOPs, and service documentation

| File | Description |
|------|-------------|
| `SOP_template.md` | Standard Operating Procedures framework and examples |
| `monitoring_and_reporting_template.md` | Daily, weekly, and monthly reporting templates |
| `service_offerings.md` | Service packages, pricing models, and SLAs |

**Use Cases:**
- Farm operations management
- Service delivery to clients
- Staff training on procedures
- Client reporting and communication

---

#### `people_and_onboarding/`
**Purpose:** Human resources and employee development materials

| File | Description |
|------|-------------|
| `onboarding_guide.md` | New employee orientation and training program |
| `roles_and_responsibilities_template.md` | Job descriptions and organizational structure |

**Use Cases:**
- New hire onboarding
- Role definition and hiring
- Performance management
- Organizational planning

---

#### `project_delivery/`
**Purpose:** Project management frameworks and checklists

| File | Description |
|------|-------------|
| `project_lifecycle_overview.md` | Complete project phases from feasibility to operations |
| `design_phase_checklist.md` | Detailed design phase activities and requirements |
| `construction_phase_checklist.md` | Construction activities and quality checkpoints |
| `operations_handover_checklist.md` | Handover procedures and documentation transfer |
| `client_kickoff_template.md` | Initial client meeting structure and materials |

**Use Cases:**
- Project planning and scheduling
- Quality assurance checkpoints
- Client communication
- Team coordination

---

#### `ras_knowledge_base/`
**Purpose:** Technical reference documentation for RAS systems

| File | Description |
|------|-------------|
| `ras_basics.md` | Introduction to RAS technology and core concepts |
| `water_quality_and_biosecurity.md` | Water parameters, monitoring, and disease prevention |
| `species_and_feeding_strategies.md` | Species selection and nutrition management |
| `common_failure_modes_and_mitigations.md` | Risk identification and prevention strategies |
| `system_design_principles.md` | Engineering guidelines and calculations |

**Use Cases:**
- Technical training and reference
- Troubleshooting and problem-solving
- System design guidance
- Client education

---

#### `sales_and_marketing/`
**Purpose:** Sales tools and customer engagement resources

| File | Description |
|------|-------------|
| `ideal_customer_profiles.md` | Target customer descriptions and characteristics |
| `discovery_call_questions.md` | Sales qualification and needs assessment framework |
| `proposal_template_outline.md` | Client proposal structure and content guide |

**Use Cases:**
- Lead qualification
- Sales presentations
- Proposal development
- Market positioning

---

#### `spv_and_finance/`
**Purpose:** Financial models, investment structures, and funding guidance

| File | Description |
|------|-------------|
| `saudi_arabia_financial_model.md` | Comprehensive Saudi market financial model |
| `saudi_arabia_financial_model_backup.md` | Backup version of financial model |
| `financial_model_assumptions_template.md` | Template for creating custom financial projections |
| `investment_pitch_outline.md` | Investor presentation structure and content |
| `spv_structure_overview.md` | Legal entity and governance guidance |
| `FINANCIAL_MODEL_SPREADSHEET_GUIDE.md` | Guide to financial spreadsheet usage |

**Use Cases:**
- Investment analysis and planning
- Investor presentations
- SPV formation guidance
- Financial projections

---

#### `templates/`
**Purpose:** Client-facing templates for project initiation

| File | Description |
|------|-------------|
| `client_brief_template.md` | Initial client information gathering |
| `site_survey_template.md` | Physical site assessment checklist |
| `RAS_system_requirements_template.md` | Technical requirements specification |

**Use Cases:**
- Client intake process
- Site evaluation
- Project scoping
- Requirements documentation

---

## File Naming Conventions

### General Rules

1. **Use lowercase** with underscores for multi-word names
   - ✅ `water_quality_and_biosecurity.md`
   - ❌ `Water-Quality-And-Biosecurity.md`

2. **Be descriptive** but concise
   - ✅ `design_phase_checklist.md`
   - ❌ `checklist.md`

3. **Use standard suffixes** for document types
   - `_template.md` - Fillable templates
   - `_checklist.md` - Checklist documents
   - `_overview.md` - Summary documents
   - `_guide.md` - How-to documents

4. **Avoid special characters** except underscores
   - ✅ `sop_template.md`
   - ❌ `sop-template (v2).md`

### Naming Patterns by Folder

| Folder | Pattern | Example |
|--------|---------|---------|
| `company/` | `topic_name.md` | `mission_vision_values.md` |
| `meta/` | `CAPS_for_standard_files.md` | `CONTRIBUTING.md` |
| `operations_as_a_service/` | `topic_template.md` | `SOP_template.md` |
| `project_delivery/` | `phase_checklist.md` | `design_phase_checklist.md` |
| `ras_knowledge_base/` | `topic_and_subtopic.md` | `water_quality_and_biosecurity.md` |
| `templates/` | `purpose_template.md` | `site_survey_template.md` |

## Navigation Guide

### By User Role

**New Employees**
1. Start with `company/mission_vision_values.md`
2. Review `people_and_onboarding/onboarding_guide.md`
3. Study `ras_knowledge_base/` for technical foundation
4. Reference `operations_as_a_service/` for daily procedures

**Project Managers**
1. Use `project_delivery/project_lifecycle_overview.md` for planning
2. Reference phase-specific checklists during execution
3. Apply `templates/` for client interactions

**Sales Team**
1. Review `company/mustadem_overview.md` for positioning
2. Use `sales_and_marketing/` for customer engagement
3. Reference `spv_and_finance/` for financial discussions

**Technical Staff**
1. Master `ras_knowledge_base/` documents
2. Apply `operations_as_a_service/SOP_template.md`
3. Use `operations_as_a_service/monitoring_and_reporting_template.md`

**Investors/Finance**
1. Start with `spv_and_finance/saudi_arabia_financial_model.md`
2. Review `spv_and_finance/investment_pitch_outline.md`
3. Understand `spv_and_finance/spv_structure_overview.md`

### By Task

| Task | Primary Documents |
|------|-------------------|
| Evaluate new project | `templates/client_brief_template.md`, `spv_and_finance/financial_model_assumptions_template.md` |
| Assess site | `templates/site_survey_template.md` |
| Design system | `ras_knowledge_base/system_design_principles.md`, `templates/RAS_system_requirements_template.md` |
| Manage operations | `operations_as_a_service/SOP_template.md`, `operations_as_a_service/monitoring_and_reporting_template.md` |
| Prepare proposal | `sales_and_marketing/proposal_template_outline.md`, `spv_and_finance/saudi_arabia_financial_model.md` |
| Onboard client | `project_delivery/client_kickoff_template.md` |
| Train staff | `people_and_onboarding/onboarding_guide.md`, `ras_knowledge_base/` |

## Related Resources

### Internal Cross-References

Each document in the repository includes a "Related Documents" section with links to related content. Key relationships:

**Company Context:**
- `company/mission_vision_values.md` ↔ `company/mustadem_overview.md`

**Operations Chain:**
- `operations_as_a_service/service_offerings.md` → `operations_as_a_service/SOP_template.md` → `operations_as_a_service/monitoring_and_reporting_template.md`

**Project Flow:**
- `templates/client_brief_template.md` → `project_delivery/project_lifecycle_overview.md` → phase checklists → `project_delivery/operations_handover_checklist.md`

**Sales to Finance:**
- `sales_and_marketing/discovery_call_questions.md` → `sales_and_marketing/proposal_template_outline.md` → `spv_and_finance/investment_pitch_outline.md`

**Technical Foundation:**
- `ras_knowledge_base/ras_basics.md` → other RAS knowledge base documents → `templates/RAS_system_requirements_template.md`

### External Resources

**Saudi Government:**
- Agricultural Development Fund (ADF): adf.gov.sa
- MEWA: mewa.gov.sa
- Naama Platform: naama.sa

**Industry Standards:**
- Best Aquaculture Practices (BAP)
- Aquaculture Stewardship Council (ASC)
- Global G.A.P.

**Research & Learning:**
- FAO Aquaculture Resources
- World Aquaculture Society
- Regional aquaculture associations

## Document Maintenance

### Update Frequency

| Folder | Review Frequency | Reason |
|--------|------------------|--------|
| `company/` | Annual | Stable content |
| `meta/` | Annual | Process documentation |
| `operations_as_a_service/` | Quarterly | Operational refinements |
| `people_and_onboarding/` | Semi-annual | Policy changes |
| `project_delivery/` | Quarterly | Process improvements |
| `ras_knowledge_base/` | Quarterly | Technical updates |
| `sales_and_marketing/` | Quarterly | Market changes |
| `spv_and_finance/` | Quarterly | Financial data updates |
| `templates/` | Semi-annual | Template refinements |

### Version Control

All documents include version information:
```markdown
**Document Information:**
- Version: X.X
- Last Updated: Month Year
- Review Schedule: Frequency
```

---

**Document Information:**
- Version: 1.0
- Last Updated: November 2024
- Review Schedule: Annual
