# Standard Operating Procedures (SOP) Template

## Overview

This document provides the framework for developing and maintaining Standard Operating Procedures (SOPs) for RAS (Recirculating Aquaculture System) operations. It includes the structure, guidelines, and complete example SOPs for common aquaculture activities.

---

## SOP Structure Framework

### Standard SOP Format

Every SOP should follow this structure:

```markdown
# SOP-[Number]: [Procedure Title]

## 1. Purpose
Clear statement of what the procedure accomplishes and why it matters.

## 2. Scope
- What activities are covered
- What personnel are affected
- What areas or systems are included
- What is explicitly excluded

## 3. Responsibilities
| Role | Responsibility |
|------|----------------|
| Role 1 | Specific duties |
| Role 2 | Specific duties |

## 4. Equipment and Materials
List all required:
- Equipment with specifications
- Consumables and supplies
- PPE requirements
- Documentation forms

## 5. Procedure
Step-by-step instructions with:
- Numbered sequential steps
- Critical parameters and limits
- Decision points and alternatives
- Time requirements

## 6. Quality Control Checks
Verification steps to ensure procedure was performed correctly.

## 7. Safety Considerations
Hazards and safety measures specific to this procedure.

## 8. Documentation Requirements
Forms, logs, and records to complete.

## 9. Troubleshooting
Common issues and corrective actions.

## 10. Revision History
| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
```

---

## Example SOP 1: Daily Water Quality Testing

### SOP-001: Daily Water Quality Testing Protocol

#### 1. Purpose
To ensure water quality parameters remain within optimal ranges for fish health and system performance through systematic daily monitoring.

#### 2. Scope
- **Applies to:** All production tanks, biofilters, and treatment systems
- **Personnel:** Aquaculture Technicians, Farm Manager
- **Frequency:** Twice daily (06:00 and 18:00)
- **Excludes:** Laboratory-grade testing (covered in SOP-015)

#### 3. Responsibilities

| Role | Responsibility |
|------|----------------|
| Aquaculture Technician | Conduct tests, record results, report anomalies |
| Farm Manager | Review logs, approve corrective actions |
| Maintenance Technician | Calibrate sensors, replace consumables |

#### 4. Equipment and Materials

**Equipment:**
- Multiparameter water quality meter (pH, DO, temperature)
- Handheld ammonia/nitrite test kit (colorimetric or photometric)
- Refractometer (for salinity if applicable)
- Thermometer (backup verification)

**Supplies:**
- Test reagents (ammonia, nitrite, nitrate, alkalinity)
- Sample bottles (clean, labeled)
- Calibration solutions (pH 4.0, 7.0, 10.0)
- Distilled water for rinsing

**PPE:**
- Nitrile gloves
- Safety glasses

**Documentation:**
- Water Quality Log (Form WQ-001)
- Anomaly Report Form (Form AR-001)

#### 5. Procedure

**Pre-Testing Preparation (10 minutes)**

1. Review previous day's readings for trends
2. Verify meter calibration (weekly) or perform if due
3. Prepare sample bottles, label with tank ID and time
4. Don PPE (gloves, safety glasses)

**Sampling Protocol (5 minutes per tank)**

5. Approach tank from upstream side
6. Submerge sample bottle 30 cm below surface, away from aeration
7. Collect minimum 200 mL sample
8. Record tank ID and time on bottle and log

**On-Site Testing (3 minutes per sample)**

9. Measure temperature first (least affected by delay)
   - Insert probe 20 cm below surface
   - Wait for reading to stabilize (30 seconds)
   - Record to nearest 0.1°C

10. Measure dissolved oxygen
    - Submerge DO probe at 30 cm depth
    - Wait for stabilization (60 seconds)
    - Record mg/L and % saturation

11. Measure pH
    - Rinse probe with sample water
    - Insert probe, wait for stabilization
    - Record to nearest 0.1 pH units

**Colorimetric Testing (5 minutes per parameter)**

12. Test for Total Ammonia Nitrogen (TAN)
    - Follow kit instructions precisely
    - Compare color at specified time (typically 5 minutes)
    - Record concentration in mg/L

13. Test for Nitrite
    - Follow kit instructions
    - Record concentration in mg/L

14. Test for Nitrate (if daily frequency required)
    - Follow kit instructions
    - Record concentration in mg/L

**Post-Testing (10 minutes)**

15. Rinse all equipment with distilled water
16. Store probes in appropriate storage solutions
17. Complete Water Quality Log (Form WQ-001)
18. Compare all readings against alarm thresholds

#### 6. Quality Control Checks

| Parameter | Optimal Range | Alert Level | Critical Level |
|-----------|---------------|-------------|----------------|
| Temperature | 26-28°C | ±2°C from target | ±4°C from target |
| Dissolved Oxygen | 6-8 mg/L | <5.5 or >9 mg/L | <4 mg/L |
| pH | 7.2-7.8 | <7.0 or >8.0 | <6.8 or >8.5 |
| TAN | <0.5 mg/L | 0.5-1.0 mg/L | >1.0 mg/L |
| Nitrite | <0.1 mg/L | 0.1-0.5 mg/L | >0.5 mg/L |
| Nitrate | <80 mg/L | 80-150 mg/L | >150 mg/L |

**Verification Steps:**
- [ ] All tanks tested within time window
- [ ] Results recorded legibly
- [ ] Anomalies flagged and reported
- [ ] Equipment cleaned and stored

#### 7. Safety Considerations

**Hazards:**
- Chemical reagents (skin/eye irritation)
- Slippery surfaces near tanks
- Electrical equipment near water

**Precautions:**
- Always wear PPE when handling reagents
- Report spills immediately
- Keep electrical equipment dry
- Follow MSDS for all chemicals

#### 8. Documentation Requirements

**Immediately:**
- Complete Water Quality Log (Form WQ-001) during testing
- Record any anomalies on Anomaly Report Form

**Daily:**
- Submit log to Farm Manager by end of shift
- Enter data into digital monitoring system

**Weekly:**
- Review trends with Farm Manager
- Verify calibration records

#### 9. Troubleshooting

| Issue | Possible Cause | Corrective Action |
|-------|---------------|-------------------|
| DO reading unstable | Air bubbles on probe | Remove, dry, re-insert probe |
| pH reading drifting | Probe needs calibration | Calibrate with fresh buffers |
| Ammonia always high | Test kit expired | Replace reagents |
| Inconsistent results | Improper sampling | Review sampling technique |

#### 10. Revision History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | Nov 2024 | Initial release | Farm Manager |

---

## Example SOP 2: Fish Feeding Protocol

### SOP-002: Fish Feeding Protocol

#### 1. Purpose
To ensure consistent, optimized feeding that maximizes growth performance while minimizing feed waste and water quality impact.

#### 2. Scope
- **Applies to:** All fish production tanks
- **Personnel:** Aquaculture Technicians, Workers
- **Frequency:** 2-4 times daily per feeding schedule
- **Species covered:** Tilapia, Barramundi (adjust parameters for other species)

#### 3. Responsibilities

| Role | Responsibility |
|------|----------------|
| Farm Manager | Set feeding rates, review FCR, adjust protocols |
| Aquaculture Technician | Calculate daily rations, supervise feeding, observe behavior |
| Workers | Execute feeding, report observations |

#### 4. Equipment and Materials

**Equipment:**
- Feed bins/hoppers (cleaned weekly)
- Weighing scale (1g accuracy)
- Feed scoops (dedicated per feed type)
- Feed broadcaster (if automated)

**Supplies:**
- Appropriate feed grade for fish size
- Feed log sheets (Form FL-001)

**PPE:**
- Gloves (optional, for handling)
- Footwear suitable for wet floors

#### 5. Procedure

**Pre-Feeding Preparation (15 minutes before first feed)**

1. Check feeding schedule posted at station
2. Review any special instructions (fasting tanks, reduced rations)
3. Verify correct feed type for each tank
4. Calculate total ration for each tank based on biomass and rate

**Ration Calculation:**

```
Daily Ration (kg) = Biomass (kg) × Feeding Rate (%)

Example:
- Tank biomass: 2,500 kg
- Feeding rate: 2.0%
- Daily ration: 2,500 × 0.02 = 50 kg/day
- Per feeding (4x daily): 12.5 kg
```

**Feeding Execution (5-10 minutes per tank)**

5. Approach tank calmly, avoid sudden movements
6. Weigh out calculated ration (+/- 50g accuracy)
7. Observe fish behavior before feeding
   - Normal: Fish active, responsive
   - Abnormal: Lethargic, surface gulping, off-feed

8. Begin broadcasting feed slowly
   - Distribute across water surface
   - Cover 50-70% of tank surface area
   - Observe feeding response

9. Continue feeding at pace fish consume
   - Feed should be consumed within 30-60 seconds of landing
   - Slow feeding if pellets sinking unconsumed

10. Stop feeding when:
    - Calculated ration is complete, OR
    - Fish show reduced interest (satiation)

11. Record actual amount fed (may be less than ration if satiation observed)

**Observation During Feeding**

12. Note and record:
    - Feeding response (aggressive, normal, slow, refused)
    - Visible health issues (lesions, parasites, abnormal swimming)
    - Dead or moribund fish
    - Uneaten feed (estimate %)

**Post-Feeding (10 minutes after feeding round)**

13. Return unused feed to storage (seal container)
14. Clean scales and scoops
15. Complete Feed Log (Form FL-001)
16. Report any anomalies to Technician/Manager

#### 6. Quality Control Checks

**Feeding Rate Guidelines by Species and Size:**

| Species | Size (g) | Temp (°C) | Feeding Rate (%BW/day) |
|---------|----------|-----------|------------------------|
| Tilapia | <50 | 26-28 | 4-6% |
| Tilapia | 50-200 | 26-28 | 3-4% |
| Tilapia | 200-500 | 26-28 | 2-3% |
| Tilapia | >500 | 26-28 | 1.5-2% |
| Barramundi | <100 | 28-30 | 4-5% |
| Barramundi | 100-500 | 28-30 | 2-3% |
| Barramundi | >500 | 28-30 | 1.5-2% |

**Feed Conversion Ratio (FCR) Targets:**

| Species | Target FCR | Acceptable FCR |
|---------|------------|----------------|
| Tilapia | 1.3-1.5 | <1.7 |
| Barramundi | 1.2-1.4 | <1.6 |

**Weekly FCR Calculation:**
```
FCR = Total Feed (kg) / Weight Gain (kg)
```

#### 7. Safety Considerations

- Store feed in cool, dry location (<25°C, <70% humidity)
- Check feed expiry dates; use FIFO rotation
- Report any mold, off-odors, or pest contamination
- Wash hands after handling feed

#### 8. Documentation Requirements

- Feed Log (Form FL-001): Complete after each feeding
- Weekly Feed Summary: Calculate weekly totals and FCR
- Anomaly reports: Submit same day for feeding refusals

#### 9. Troubleshooting

| Issue | Possible Cause | Corrective Action |
|-------|---------------|-------------------|
| Fish not feeding | Low DO, high ammonia, disease | Check water quality, reduce feeding |
| Feed sinking uneaten | Overfeeding, wrong pellet size | Reduce ration, adjust pellet size |
| High FCR | Poor feed quality, health issues | Review feed source, check fish health |
| Variable intake | Temperature fluctuations | Stabilize temperature, adjust schedule |

#### 10. Revision History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | Nov 2024 | Initial release | Farm Manager |

---

## Example SOP 3: Tank Cleaning and Disinfection

### SOP-003: Tank Cleaning and Disinfection

#### 1. Purpose
To maintain hygienic tank conditions, remove accumulated waste, and prevent disease transmission through systematic cleaning protocols.

#### 2. Scope
- **Applies to:** All fish culture tanks, grow-out tanks, quarantine tanks
- **Personnel:** Maintenance Technician, Workers
- **Frequency:** 
  - Routine cleaning: Daily (waste removal)
  - Deep cleaning: Between production cycles
  - Disinfection: After disease events or cycle completion

#### 3. Responsibilities

| Role | Responsibility |
|------|----------------|
| Farm Manager | Approve disinfection schedule, verify completion |
| Maintenance Technician | Supervise cleaning, prepare disinfectant solutions |
| Workers | Execute cleaning tasks, follow safety protocols |
| Aquaculture Technician | Confirm fish removal, water quality post-cleaning |

#### 4. Equipment and Materials

**Equipment:**
- Algae scrubbers and brushes
- Pressure washer (for deep cleaning)
- Submersible pump (for draining)
- Wet/dry vacuum

**Supplies:**
- Disinfectant (chlorine solution, Virkon S, or approved alternative)
- Neutralizing agent (sodium thiosulfate for chlorine)
- Clean buckets and containers
- Fresh water source

**PPE Required:**
- Rubber boots
- Waterproof apron
- Chemical-resistant gloves
- Safety glasses/face shield
- Respiratory protection (if using concentrated chemicals)

#### 5. Procedure

**Part A: Routine Daily Cleaning (15-20 minutes per tank)**

1. Conduct visual inspection of tank bottom through observation
2. Operate center drain for 2-3 minutes to flush settled solids
3. Check drain screen for blockages, clear if needed
4. Inspect tank walls for algae accumulation (note for weekly attention)
5. Remove any floating debris with net
6. Document cleaning in Daily Log

**Part B: Deep Cleaning (Between Cycles)**

*Preparation (1-2 hours before)*

7. Ensure fish have been harvested/transferred (verify tank empty)
8. Reduce water level to 10-20% of normal
9. Prepare cleaning equipment and PPE
10. Mix disinfectant solution per manufacturer instructions:
    - Chlorine: 100-200 ppm (10-20 mL bleach per 10 L water)
    - Virkon S: 1% solution (10g per liter)

*Draining and Initial Cleaning (1-2 hours)*

11. Drain tank completely via bottom drain
12. Collect and dispose of sludge appropriately
13. Rinse tank walls and bottom with pressure washer
14. Scrub all surfaces with brushes to remove biofilm
15. Pay special attention to:
    - Corners and joints
    - Inlet pipes and diffusers
    - Drain covers and screens
    - Areas below water line (algae accumulation)

*Disinfection (1-4 hours contact time)*

16. Apply disinfectant solution to all surfaces
    - For spray application: Even coverage, surfaces wet
    - For fill method: Fill tank with disinfectant solution
17. Allow contact time per product specifications:
    - Chlorine: Minimum 30 minutes at 100 ppm
    - Virkon S: Minimum 10 minutes
18. Document disinfectant concentration, contact time, and temperature

*Neutralization and Rinsing (1-2 hours)*

19. Drain disinfectant solution to waste treatment
20. If chlorine used: Add neutralizing agent (sodium thiosulfate)
    - Dose: 2x the chlorine concentration (mg/L)
21. Rinse thoroughly with clean water (minimum 3 full rinses)
22. Drain completely

*Verification (30 minutes)*

23. Test residual chlorine (must be <0.02 mg/L)
24. Test pH (should be neutral, 7.0-7.5)
25. Visually inspect all surfaces for cleanliness
26. Document cleaning completion

*Preparation for Restocking (2-4 hours)*

27. Refill tank with treated water
28. Verify all systems operational (aeration, circulation)
29. Test water quality before stocking
30. Allow 24-hour stabilization before restocking

#### 6. Quality Control Checks

**Cleaning Verification Checklist:**
- [ ] All visible organic matter removed
- [ ] No biofilm on walls or fittings
- [ ] Drains clear and functioning
- [ ] Inlet pipes clean inside
- [ ] No chemical residue (test confirms)
- [ ] Water parameters suitable for fish

**Disinfection Effectiveness:**

| Method | Concentration | Contact Time | Verification |
|--------|---------------|--------------|--------------|
| Chlorine | 100-200 ppm | 30+ min | Residual <0.02 ppm |
| Virkon S | 1% | 10+ min | Visual (pink color) |
| Heat | >60°C | 10+ min | Temperature log |
| UV | N/A | Continuous | Lamp hours |

#### 7. Safety Considerations

**Chemical Hazards:**
- Never mix chlorine with acids (toxic chlorine gas)
- Store chemicals in original containers, locked storage
- Follow MSDS for all products

**Physical Hazards:**
- Slippery surfaces when wet
- Heavy equipment (pumps, pressure washers)
- Confined space (inside large tanks)

**Required Precautions:**
- Two-person rule for entering large tanks
- Adequate ventilation during chemical use
- Emergency eyewash accessible
- First aid kit on site

#### 8. Documentation Requirements

- Tank Cleaning Log (Form TC-001)
- Disinfection Record (Form DR-001)
- Chemical usage log
- Restocking clearance sign-off

#### 9. Troubleshooting

| Issue | Cause | Corrective Action |
|-------|-------|-------------------|
| Persistent algae | Inadequate scrubbing | Use stronger brush, extend scrubbing time |
| Chemical smell after rinse | Insufficient rinsing | Additional rinse cycles |
| High chlorine residual | Over-concentration | Add more neutralizer, continue rinsing |
| Biofilm returns quickly | Incomplete disinfection | Extend contact time, check concentration |

#### 10. Revision History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | Nov 2024 | Initial release | Farm Manager |

---

## Example SOP 4: Fingerling Stocking

### SOP-004: Fingerling Receiving and Stocking

#### 1. Purpose
To ensure safe, stress-minimized transfer of fingerlings into production tanks with optimal survival and health outcomes.

#### 2. Scope
- **Applies to:** All incoming fingerling shipments
- **Personnel:** Farm Manager, Aquaculture Technician
- **Species:** Tilapia, Barramundi, Shrimp (adjust parameters accordingly)

#### 3. Responsibilities

| Role | Responsibility |
|------|----------------|
| Farm Manager | Approve stocking plan, verify supplier documentation |
| Aquaculture Technician | Lead stocking process, monitor acclimation |
| Worker | Assist with handling, record counts |

#### 4. Equipment and Materials

**Equipment:**
- Acclimation tanks or containers
- Aeration (battery backup available)
- Temperature-controlled water source
- Counting equipment (counters, scales for batch weighing)
- Nets (soft mesh, size-appropriate)

**Supplies:**
- Salt (sodium chloride, aquarium grade)
- Stress coat additive (if approved)
- Oxygen (cylinders or concentrator)
- Sample containers for health assessment

**Documentation:**
- Supplier health certificates
- Stocking Record Form (Form SR-001)
- Quarantine Log (if applicable)

#### 5. Procedure

**Pre-Arrival Preparation (24 hours before)**

1. Confirm delivery date and time with supplier
2. Review supplier health certificate and documentation
3. Prepare receiving area:
   - Clean acclimation tanks
   - Set temperature to match transport water (request from supplier)
   - Verify aeration operational
4. Prepare receiving tank:
   - Complete cleaning/disinfection (SOP-003)
   - Fill with treated water
   - Adjust temperature to target (gradually)
   - Test and document water quality

**Arrival and Initial Assessment (30 minutes)**

5. Inspect transport packaging for damage, leaks
6. Measure transport water quality immediately:
   - Temperature
   - pH
   - Dissolved oxygen
   - Ammonia (if possible)

7. Visual assessment of fingerlings:
   - Activity level (normal, lethargic)
   - Coloration (normal, pale, dark)
   - Physical condition (fins, scales, eyes)
   - Estimated mortality in transport

8. Document all observations on Receiving Log

**Acclimation Protocol (1-3 hours)**

*Temperature Acclimation:*

9. Float sealed bags in receiving tank for 15-20 minutes
   - Allows gradual temperature equalization
   - Avoid direct sunlight or heat sources

10. After floating, open bags but do not release fish

*Water Quality Acclimation:*

11. Add receiving tank water to bags gradually:
    - Start: 10% of bag volume every 10 minutes
    - Continue until bag water matches receiving tank

12. If pH difference >0.5 units:
    - Extend acclimation to 2-3 hours
    - Add water in 5% increments

13. If ammonia in transport water is high (>2 mg/L):
    - Do NOT add tank water (increases ammonia toxicity with pH rise)
    - Transfer fish quickly to fresh water
    - Increase aeration during transfer

**Transfer and Stocking (30-60 minutes)**

14. Gently net fish from bags to receiving tank
    - Use soft mesh nets, minimize air exposure
    - Do NOT pour transport water into system

15. Allow fish to recover in receiving tank (30-60 minutes):
    - Observe behavior
    - Confirm aeration adequate
    - Add salt if indicated (1-3 ppt for stress reduction)

16. Count or estimate fish:
    - Direct count for <1,000 fish
    - Batch weight method for larger quantities:
      ```
      Fish Count = Total Batch Weight / Average Individual Weight
      Sample minimum 100 fish for average weight
      ```

17. Transfer to production tank:
    - Use transport containers or gentle netting
    - Minimize handling and air exposure
    - Release fish gently below water surface

**Post-Stocking (First 24-72 hours)**

18. Monitor closely:
    - Check every 4 hours for first 24 hours
    - Observe swimming behavior, distribution in tank
    - Remove any mortalities immediately

19. Delay first feeding:
    - Wait minimum 24 hours after stocking
    - Start at 50% of normal ration
    - Increase to full ration over 3-5 days

20. Document:
    - Final count and weight
    - Stocking density (kg/m³)
    - Any observations or concerns

#### 6. Quality Control Checks

**Acclimation Targets:**

| Parameter | Maximum Difference | Acclimation Method |
|-----------|-------------------|-------------------|
| Temperature | ±2°C | Float bags, add water gradually |
| pH | ±0.5 units | Extended gradual acclimation |
| Salinity | ±5 ppt | Gradual dilution/concentration |
| DO | N/A | Maintain >5 mg/L in receiving tank |

**Stocking Density Guidelines:**

| Species | Fingerling Size | Max Stocking Density |
|---------|-----------------|----------------------|
| Tilapia | 1-5g | 5,000/m³ |
| Tilapia | 5-20g | 2,000/m³ |
| Tilapia | 20-50g | 500/m³ |
| Barramundi | 5-20g | 1,000/m³ |
| Barramundi | 20-50g | 300/m³ |

**Acceptance Criteria:**
- Mortality during transport: <2%
- Mortality within 72 hours post-stocking: <1%
- Fish actively swimming, distributed throughout tank
- Normal feeding response within 48-72 hours

#### 7. Safety Considerations

- Handle fish gently to minimize stress
- Maintain adequate hand hygiene
- Use appropriate nets (avoid injury)
- Dispose of transport water properly (not into environment)

#### 8. Documentation Requirements

- Stocking Record Form (Form SR-001)
- Supplier health certificates (filed)
- Water quality log (receiving conditions)
- Mortality log (transport and 72-hour post-stocking)

#### 9. Troubleshooting

| Issue | Cause | Corrective Action |
|-------|-------|-------------------|
| High transport mortality | Shipping stress, poor water quality | Document, claim from supplier |
| Fish gasping at surface | Low DO in transport/receiving | Increase aeration immediately |
| Fish clustering at inlet | Stress, temperature difference | Allow more acclimation time |
| Refusal to feed after 72h | Stress, disease, poor acclimation | Reduce density, check water quality |

#### 10. Revision History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | Nov 2024 | Initial release | Farm Manager |

---

## Example SOP 5: Disease Diagnosis and Treatment

### SOP-005: Fish Health Assessment and Disease Response

#### 1. Purpose
To establish systematic protocols for early disease detection, diagnosis, and treatment to minimize losses and prevent disease spread.

#### 2. Scope
- **Applies to:** All fish production systems
- **Personnel:** Farm Manager, Aquaculture Technician
- **Trigger:** Any observed health abnormality

#### 3. Responsibilities

| Role | Responsibility |
|------|----------------|
| Farm Manager | Approve treatments, contact veterinarian, regulatory reporting |
| Aquaculture Technician | Conduct health checks, collect samples, execute treatments |
| Worker | Report observations, assist with sampling |

#### 4. Equipment and Materials

**Diagnostic Equipment:**
- Dissection kit (scissors, forceps, scalpels)
- Microscope (40-400x magnification)
- Slides and cover slips
- Sterile swabs and sample containers
- Cooler with ice packs (for sample transport)

**Treatment Supplies:**
- Approved therapeutants (per veterinary guidance)
- Salt (sodium chloride)
- Formalin (37% formaldehyde) - if approved
- Hydrogen peroxide (35%) - if approved
- Antibiotics (prescription required)

**PPE:**
- Nitrile gloves
- Lab coat or apron
- Safety glasses

**Documentation:**
- Health Observation Form (Form HO-001)
- Treatment Log (Form TL-001)
- Sample Submission Form

#### 5. Procedure

**Part A: Routine Health Monitoring (Daily)**

1. Observe fish during feeding for:
   - Appetite (normal, reduced, absent)
   - Swimming behavior (normal, erratic, lethargic, spiraling)
   - Position in water column (normal distribution, surface gasping, bottom sitting)
   - Physical appearance (color, fin condition, lesions, swelling)

2. Document any abnormalities on Health Observation Form

3. Count and remove mortalities:
   - Record number, tank, estimated size
   - Examine fresh mortalities for external signs
   - Dispose properly (freezer for examination or incineration)

4. Calculate mortality rate:
   ```
   Daily Mortality % = (Mortalities / Starting Population) × 100
   Alert threshold: >0.1%/day (species-dependent)
   ```

**Part B: Enhanced Assessment (When Abnormalities Detected)**

5. Isolate affected tank (if feasible):
   - Minimize traffic between tanks
   - Dedicate equipment to affected tank
   - Increase biosecurity measures

6. Collect detailed observations:
   - Percentage of population affected (estimate)
   - Progression (acute, chronic)
   - Distribution pattern (random, clustered)

7. Conduct physical examination on sample fish:
   - Select 3-5 affected fish (live if possible)
   - Use anesthesia (MS-222 or clove oil) for handling
   
8. External examination:
   - Skin: Lesions, hemorrhages, discoloration, excess mucus
   - Fins: Erosion, rot, hemorrhage
   - Eyes: Cloudiness, exophthalmia (pop-eye)
   - Gills: Color (should be bright red), excess mucus, necrosis
   - Opercula: Movement rate, swelling
   - Abdomen: Distension, dropsy

9. Internal examination (necropsy):
   - Euthanize humanely (overdose anesthetic or rapid cooling)
   - Open abdomen, examine organs:
     - Liver: Color (should be red-brown), texture, size
     - Spleen: Size (enlarged?), color
     - Kidney: Swelling, color
     - Gut: Contents, inflammation
     - Swim bladder: Integrity

10. Microscopic examination:
    - Gill clip: Parasites, fungal elements
    - Skin scrape: External parasites
    - Gut contents: Internal parasites

11. Document all findings with photographs

**Part C: Sample Collection for Laboratory (If Needed)**

12. Collect samples for laboratory diagnosis:
    - Fresh mortalities (<4 hours dead)
    - Moribund fish (still alive but near death)
    - Tissues in appropriate fixative (10% formalin for histology)
    - Swabs in transport media (for bacteriology)

13. Label all samples clearly:
    - Date, time
    - Tank ID
    - Species
    - Clinical signs observed

14. Transport on ice (not frozen) to laboratory
15. Complete Sample Submission Form

**Part D: Treatment Protocols**

16. Consult with veterinarian for diagnosis and treatment plan
17. Select appropriate treatment based on diagnosis:

**Common Treatments:**

| Condition | Treatment | Dose | Duration |
|-----------|-----------|------|----------|
| Bacterial infection | Antibiotics (Rx) | Per veterinary prescription | 5-10 days |
| External parasites | Formalin bath | 25-50 ppm | 30-60 min |
| Protozoan parasites | Salt bath | 10-30 ppt | 10-30 min |
| Fungal infection | Salt + Malachite green | As directed | Variable |
| Stress/transport | Salt in tank | 1-3 ppt | Continuous |
| Fin rot (mild) | Improved water quality | N/A | Continuous |

18. Execute treatment:
    - Calculate dose precisely:
      ```
      Chemical (g) = Tank Volume (L) × Concentration (ppm) / 1000
      ```
    - Maintain adequate aeration (treatments increase O2 demand)
    - Monitor fish during treatment
    - Document treatment details

19. Post-treatment monitoring:
    - Observe response daily
    - Adjust feeding if needed
    - Continue until full course complete
    - Document outcome

**Part E: Reporting**

20. Report notifiable diseases to authorities (per regulations)
21. Update health records in database
22. Conduct root cause analysis
23. Implement preventive measures

#### 6. Quality Control Checks

**Health Thresholds:**

| Metric | Normal | Alert | Critical |
|--------|--------|-------|----------|
| Daily mortality | <0.05% | 0.05-0.1% | >0.1% |
| Feed intake | >90% of ration | 70-90% | <70% |
| Swimming behavior | Active, distributed | Clustering, surface | Erratic, listing |

**Treatment Effectiveness:**
- Mortality should decrease within 3-5 days of treatment
- If no improvement, reassess diagnosis and treatment

#### 7. Safety Considerations

**Chemical Handling:**
- Follow MSDS for all chemicals
- Never mix formalin with acids or oxidizers
- Adequate ventilation during treatments
- Emergency procedures for chemical exposure

**Biosecurity:**
- Wash hands between tanks
- Disinfect equipment after handling sick fish
- Limit personnel access to affected areas

**Food Safety:**
- Observe withdrawal periods for all treatments
- Do not harvest treated fish until cleared
- Document treatment dates and withdrawal periods

#### 8. Documentation Requirements

- Health Observation Form (daily)
- Treatment Log (all treatments)
- Sample Submission Form (lab samples)
- Mortality records
- Regulatory notifications (if applicable)

#### 9. Troubleshooting

| Symptom | Possible Causes | Diagnostic Steps |
|---------|-----------------|------------------|
| Mass mortality | Toxin, low DO, disease | Check water quality immediately |
| Off-feed | Stress, disease, water quality | Review recent changes, examine fish |
| Surface gasping | Low DO, gill damage | Measure DO, examine gills |
| Erratic swimming | Parasites, neurological | Microscopic examination |
| Skin lesions | Bacterial, parasites, trauma | Culture, microscopy |

#### 10. Revision History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | Nov 2024 | Initial release | Farm Manager |

---

## Example SOP 6: Equipment Maintenance (Pump and Biofilter)

### SOP-006: Critical Equipment Maintenance

#### 1. Purpose
To ensure reliable operation of essential RAS equipment through systematic preventive maintenance, reducing unplanned downtime and fish loss.

#### 2. Scope
- **Applies to:** Circulation pumps, aeration blowers, biofilters, UV systems
- **Personnel:** Maintenance Technician
- **Frequency:** Per maintenance schedule (daily/weekly/monthly/annual)

#### 3. Responsibilities

| Role | Responsibility |
|------|----------------|
| Farm Manager | Approve maintenance schedule, budget for parts |
| Maintenance Technician | Execute maintenance, maintain records |
| Aquaculture Technician | Report operational issues, verify system function |

#### 4. Equipment and Materials

**Tools:**
- Wrenches, screwdrivers, pliers
- Multimeter (electrical testing)
- Pressure gauge
- Flow meter (or ultrasonic meter)
- Vibration meter (optional)

**Supplies:**
- Lubricants (grease, oil)
- Replacement seals and O-rings
- Spare impellers
- UV lamps (for replacement)
- Cleaning chemicals

**PPE:**
- Safety glasses
- Work gloves
- Hearing protection (near pumps)
- Electrical safety equipment (lockout/tagout)

#### 5. Procedure

**Part A: Circulation Pump Maintenance**

*Daily Checks (5 minutes per pump):*

1. Visual inspection:
   - Check for leaks (mechanical seal, connections)
   - Verify normal operation (no unusual noise or vibration)
   - Check motor temperature (should not be hot to touch)

2. Operational verification:
   - Flow rate within normal range
   - Pressure within normal range
   - No cavitation sounds

*Weekly Checks (15 minutes per pump):*

3. Clean intake strainer/screen
4. Check coupling alignment (if applicable)
5. Verify electrical connections secure
6. Test backup pump operation

*Monthly Maintenance (30 minutes per pump):*

7. Measure and record:
   - Motor amperage (compare to baseline)
   - Inlet/outlet pressure
   - Flow rate
   - Vibration levels (if meter available)

8. Inspect:
   - Motor bearings (listen for roughness)
   - Shaft seal for wear
   - Impeller condition (if accessible)

9. Lubricate motor bearings (if grease fittings present)

*Annual Overhaul (2-4 hours per pump):*

10. Complete pump disassembly
11. Replace mechanical seals
12. Inspect/replace impeller if worn
13. Clean volute and all internal passages
14. Check motor insulation resistance
15. Replace bearings if needed
16. Reassemble and test
17. Update maintenance records

**Part B: Biofilter Maintenance**

*Daily Checks (10 minutes):*

18. Verify aeration operational (blowers running, bubbles visible)
19. Check water flow through biofilter
20. Observe media movement (if MBBR)
21. Monitor ammonia/nitrite in system (indicator of biofilter health)

*Weekly Maintenance (30 minutes):*

22. Clean biofilter influent screen
23. Inspect media for debris accumulation
24. Verify uniform flow distribution
25. Check for dead zones (areas without flow/aeration)
26. Test dissolved oxygen in biofilter (should be >4 mg/L)

*Monthly Maintenance (1 hour):*

27. Measure and record:
   - Ammonia removal rate
   - Nitrite levels
   - pH in biofilter
   - Alkalinity consumption

28. Check media fill level (should be 60-70% for MBBR)
29. Add media if needed (gradual addition)
30. Inspect aeration diffusers for clogging

*Quarterly/Annual:*

31. Deep clean influent/effluent pipes
32. Replace aeration diffusers if degraded
33. Consider media cleaning if heavily fouled (careful - preserve bacteria)

**Part C: Blower/Aerator Maintenance**

*Daily (5 minutes):*

34. Check operating sound (no unusual noise)
35. Verify output pressure normal
36. Check air filter (visual)

*Weekly (15 minutes):*

37. Clean or replace air intake filter
38. Check belt tension (if belt-driven)
39. Inspect discharge for proper flow

*Monthly (30 minutes):*

40. Measure discharge pressure and flow
41. Check motor amperage
42. Lubricate as per manufacturer
43. Inspect vibration isolators

*Annual:*

44. Replace air filters
45. Replace belts (if applicable)
46. Service motor bearings
47. Check all silencers and mufflers

**Part D: UV Sterilizer Maintenance**

*Daily (2 minutes):*

48. Verify UV lamp operational (indicator light or viewing port)
49. Check flow rate through unit

*Weekly (10 minutes):*

50. Check quartz sleeve for fouling
51. Verify UV intensity reading (if meter installed)

*Monthly (20 minutes):*

52. Clean quartz sleeve
53. Record lamp hours
54. Verify water clarity entering UV

*Annual or Per Manufacturer Schedule:*

55. Replace UV lamps (typically 8,000-12,000 hours)
56. Replace quartz sleeves if etched or damaged
57. Recalibrate or replace UV sensors
58. Clean all internal surfaces

#### 6. Quality Control Checks

**Equipment Performance Targets:**

| Equipment | Parameter | Normal Range | Action Threshold |
|-----------|-----------|--------------|------------------|
| Pump | Flow rate | Design ± 10% | <80% of design |
| Pump | Amp draw | Nameplate ± 10% | >120% of nameplate |
| Biofilter | Ammonia | <0.5 mg/L | >1.0 mg/L |
| Biofilter | DO | >4 mg/L | <3 mg/L |
| Blower | Pressure | Design ± 5% | <90% of design |
| UV | Intensity | >30 mW/cm² | <20 mW/cm² |

**Spare Parts Inventory:**

Maintain minimum stock:
- Pump seals: 2 per pump
- Impellers: 1 per pump type
- UV lamps: 1 per unit
- Air filters: 3-month supply
- Belts: 2 per blower

#### 7. Safety Considerations

**Electrical Safety:**
- Always use lockout/tagout before maintenance
- Verify power isolated before touching electrical components
- Use appropriate PPE for electrical work

**Mechanical Safety:**
- Allow rotating equipment to stop completely
- Support heavy components during disassembly
- Use proper lifting techniques

**Chemical Safety:**
- UV exposure hazard (do not look at operating lamps)
- Biofilter media may harbor pathogens

#### 8. Documentation Requirements

- Maintenance Log (Form ML-001): Record all maintenance activities
- Parts Usage Log: Track replacement parts
- Equipment Performance Log: Monthly readings
- Work Orders: For repairs and major maintenance

#### 9. Troubleshooting

| Issue | Possible Cause | Corrective Action |
|-------|---------------|-------------------|
| Pump low flow | Clogged strainer, worn impeller | Clean strainer, replace impeller |
| Pump high amperage | Blocked discharge, worn bearings | Check valve, replace bearings |
| Biofilter ammonia rising | Low DO, pH too low, overfeeding | Increase aeration, adjust pH, reduce feed |
| Blower low output | Clogged filter, belt slip | Replace filter, adjust belt |
| UV low intensity | Fouled sleeve, old lamp | Clean sleeve, replace lamp |

#### 10. Revision History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | Nov 2024 | Initial release | Farm Manager |

---

## Example SOP 7: Harvest Procedures

### SOP-007: Fish Harvest and Handling

#### 1. Purpose
To ensure humane, efficient harvest of market-ready fish with maximum product quality and minimal stress.

#### 2. Scope
- **Applies to:** All market-size fish harvests
- **Personnel:** Farm Manager, Aquaculture Technician, Workers
- **Timing:** Based on harvest schedule and market orders

#### 3. Responsibilities

| Role | Responsibility |
|------|----------------|
| Farm Manager | Approve harvest plan, coordinate logistics |
| Aquaculture Technician | Lead harvest, quality assessment, documentation |
| Workers | Execute harvest, grading, handling |
| Quality Control | Final product inspection, temperature monitoring |

#### 4. Equipment and Materials

**Harvest Equipment:**
- Seine nets or harvest nets (appropriate mesh size)
- Dip nets (soft mesh)
- Grading equipment (mechanical or manual graders)
- Harvest basins/tubs
- Crowding nets

**Handling Equipment:**
- Fish pumps (if available)
- Stunner (electrical or percussion)
- Bleeding tanks
- Ice or chilling system (slurry ice preferred)
- Packaging materials (boxes, bags, ice packs)
- Scales (10g accuracy)

**PPE:**
- Rubber boots
- Waterproof apron
- Gloves (nitrile or rubber)
- Hair nets (for processing)

#### 5. Procedure

**Pre-Harvest Preparation (24-48 hours before)**

1. Confirm market order quantity and specifications
2. Verify target fish meet harvest criteria:
   - Size: Within specified range (e.g., 400-600g)
   - Condition: Good body shape, no defects
   - Health: No visible disease signs

3. Implement pre-harvest fasting:
   - Tilapia: 24-48 hours without feed
   - Barramundi: 24-48 hours without feed
   - Purpose: Empty gut, reduce waste, improve flavor

4. Prepare harvest area:
   - Clean all equipment
   - Prepare ice or chilling system
   - Stage packaging materials
   - Verify scales calibrated

5. Coordinate logistics:
   - Transport vehicle scheduled
   - Buyer/market confirmed
   - Certificates prepared (if export)

**Harvest Day: Crowding and Capture (1-2 hours)**

6. Begin harvest early morning (cooler temperatures)

7. Reduce water level in harvest tank:
   - Drain to 50% of normal level
   - Maintain adequate aeration

8. Crowd fish gently using seine net:
   - Move slowly to minimize stress
   - Maintain high fish density area near drain

9. Capture fish:
   - Use dip nets or fish pump
   - Work in small batches (avoid overcrowding basins)
   - Minimize air exposure (<30 seconds)

10. Transfer to holding/grading area

**Grading and Selection (30 minutes per batch)**

11. Grade fish by size:
    - Separate into market categories
    - Remove undersized fish (return to tank)
    - Remove culls (off-grade, damaged)

12. Weigh batches:
    - Record batch weights
    - Calculate average individual weight
    - Count or estimate numbers

13. Quality inspection:
    - Check for defects, damage, parasites
    - Remove any unsuitable fish

**Stunning and Slaughter (if on-site processing)**

14. Stun fish immediately before slaughter:
    - Electrical stunning: 200-300V, 1-2 seconds
    - Percussion: Sharp blow to head
    - Verify loss of consciousness

15. Bleed fish immediately after stunning:
    - Cut gill arches
    - Allow bleeding for 2-5 minutes in chilled water
    - Purpose: Improve product quality, shelf life

16. Chill immediately:
    - Slurry ice: 50% ice, 50% water
    - Target temperature: 0-2°C within 30 minutes
    - Maintain until packaging

**Packaging and Transport (1-2 hours)**

17. Package fish:
    - Drain excess water
    - Layer with ice (fish:ice ratio 1:1 minimum)
    - Use insulated containers
    - Label with: Date, species, grade, weight, origin

18. Verify cold chain:
    - Product temperature: 0-4°C
    - Transport vehicle pre-cooled
    - Ice replenishment planned for long transport

19. Documentation:
    - Complete harvest record
    - Issue quality certificate
    - Prepare shipping documents

**Post-Harvest (Within 24 hours)**

20. Clean and disinfect:
    - All harvest equipment
    - Grading tables
    - Harvest area

21. Return undersized fish to growout

22. Update inventory records

23. Evaluate harvest efficiency:
    - Actual vs. planned quantity
    - Average weights achieved
    - Cull rate

#### 6. Quality Control Checks

**Pre-Harvest Criteria:**

| Parameter | Requirement |
|-----------|-------------|
| Average weight | Within target range (e.g., 450-550g) |
| Coefficient of variation | <20% (uniform size) |
| Condition factor | >1.8 (tilapia), >1.2 (barramundi) |
| Health status | No visible disease, parasites |
| Fasting period | Minimum 24 hours complete |

**Product Quality Standards:**

| Attribute | Acceptable | Reject |
|-----------|------------|--------|
| Skin | Intact, normal color | Lesions, discoloration |
| Fins | Complete, no erosion | Damaged, rotted |
| Eyes | Clear, normal | Cloudy, sunken |
| Gills | Bright red, clean | Brown, slimy |
| Body shape | Firm, well-shaped | Soft, deformed |
| Odor | Fresh, mild | Off-odor, ammonia |

**Temperature Monitoring:**

| Stage | Target | Maximum |
|-------|--------|---------|
| Harvest | Ambient | <30°C |
| Post-stun | 0-4°C | 7°C |
| Packaging | 0-2°C | 4°C |
| Transport | 0-4°C | 7°C |

#### 7. Safety Considerations

**Electrical:**
- Ensure stunner properly grounded
- Keep electrical equipment dry
- Follow lockout/tagout for maintenance

**Physical:**
- Slippery surfaces
- Heavy lifting (ice, fish containers)
- Sharp tools (bleeding knives)

**Biological:**
- Wash hands frequently
- Clean and disinfect equipment
- Proper waste disposal

#### 8. Documentation Requirements

- Harvest Record Form (Form HR-001)
- Quality Inspection Report
- Temperature Log
- Shipping Documents
- Certificates of origin/quality

#### 9. Troubleshooting

| Issue | Cause | Corrective Action |
|-------|-------|-------------------|
| High cull rate | Disease, poor grading pre-harvest | Improve health management, sample before harvest |
| Soft flesh | Stress, poor chilling | Reduce handling stress, faster chilling |
| Short shelf life | Inadequate bleeding, temperature abuse | Improve bleeding, verify cold chain |
| Bruising | Rough handling | Train staff, use softer nets |

#### 10. Revision History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | Nov 2024 | Initial release | Farm Manager |

---

## SOP Development Process

### Creating New SOPs

**Step 1: Identify the Need**
- Gap in existing procedures
- New equipment or process
- Incident or near-miss requiring formalization
- Regulatory or certification requirement

**Step 2: Draft the SOP**
- Follow standard template structure
- Include all relevant details
- Be specific with parameters and limits
- Include troubleshooting guidance

**Step 3: Review and Approval**
- Technical review by subject matter expert
- Safety review if applicable
- Management approval
- Assign SOP number and version

**Step 4: Training**
- Train all affected personnel
- Document training completion
- Assess competency

**Step 5: Implementation**
- Distribute SOP to work areas
- Make accessible (printed or digital)
- Begin enforcement

**Step 6: Periodic Review**
- Schedule: Annually or after incidents
- Update as needed
- Re-train if significant changes

### SOP Numbering Convention

```
SOP-[Category]-[Number]

Categories:
001-099: Water Quality & Monitoring
100-199: Fish Husbandry & Feeding
200-299: Health & Biosecurity
300-399: Equipment & Maintenance
400-499: Harvest & Processing
500-599: Safety & Emergency
600-699: Administrative

Example: SOP-101: Fish Feeding Protocol
```

---

## Related Documents

- [Monitoring and Reporting Template](./monitoring_and_reporting_template.md)
- [Onboarding Guide](../people_and_onboarding/onboarding_guide.md)
- [Water Quality and Biosecurity](../ras_knowledge_base/water_quality_and_biosecurity.md)

---

**Document Information:**
- Version: 1.0
- Last Updated: November 2024
- Review Schedule: Annual
