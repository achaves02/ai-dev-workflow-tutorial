# Tasks: Sales Analytics Dashboard

**Input**: Design documents from `/specs/001-sales-dashboard/`
**Prerequisites**: plan.md (required), spec.md (required), research.md

**Tests**: No automated tests requested. Manual testing will verify each user story.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

This project uses a single-file structure per the constitution:
- `app.py` - Main Streamlit application at repository root
- `requirements.txt` - Python dependencies at repository root
- `data/sales-data.csv` - Source data (already exists)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and environment setup

- [x] T001 Create Python virtual environment with `python -m venv venv`
- [x] T002 Create requirements.txt with streamlit>=1.31.0, pandas>=2.2.0, plotly>=5.18.0
- [x] T003 Install dependencies with `pip install -r requirements.txt`
- [x] T004 Create app.py with imports and page configuration in app.py

**Checkpoint**: Environment ready, empty dashboard shell runs with `streamlit run app.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Data loading infrastructure that ALL user stories depend on

**CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 Implement load_data() function with @st.cache_data decorator in app.py
- [x] T006 Add error handling for missing CSV file in app.py
- [x] T007 Add error handling for empty data in app.py
- [x] T008 Add dashboard title "ShopSmart Sales Dashboard" in app.py

**Checkpoint**: Foundation ready - data loads successfully, dashboard displays title

---

## Phase 3: User Story 1 - View Key Performance Indicators (Priority: P1)

**Goal**: Display Total Sales and Total Orders as prominent KPI metrics at the top of the dashboard

**Independent Test**: Load dashboard, verify Total Sales shows as formatted currency (e.g., $650,000) and Total Orders shows as formatted number (e.g., 482) in the top section

### Implementation for User Story 1

- [x] T009 [US1] Calculate total_sales as sum of total_amount column in app.py
- [x] T010 [US1] Calculate total_orders as count of unique order_id values in app.py
- [x] T011 [US1] Create two-column layout for KPI metrics using st.columns() in app.py
- [x] T012 [US1] Display Total Sales using st.metric() with currency formatting in app.py
- [x] T013 [US1] Display Total Orders using st.metric() with number formatting in app.py

**Checkpoint**: User Story 1 complete - KPIs visible at top, values match CSV calculations

---

## Phase 4: User Story 2 - Analyze Sales Trends Over Time (Priority: P2)

**Goal**: Display an interactive line chart showing monthly sales trends over the 12-month period

**Independent Test**: Verify line chart shows time on x-axis, sales on y-axis, tooltips display exact values on hover

### Implementation for User Story 2

- [x] T014 [US2] Create monthly sales aggregation using groupby and to_period('M') in app.py
- [x] T015 [US2] Create line chart using plotly.express.line() with markers in app.py
- [x] T016 [US2] Configure chart title "Sales Trend Over Time" and axis labels in app.py
- [x] T017 [US2] Add interactive tooltips showing month and sales amount in app.py
- [x] T018 [US2] Display chart using st.plotly_chart() with full width in app.py

**Checkpoint**: User Story 2 complete - trend chart shows 12 months of data with tooltips

---

## Phase 5: User Story 3 - Compare Sales by Product Category (Priority: P3)

**Goal**: Display a bar chart showing sales breakdown by the 5 product categories, sorted by value

**Independent Test**: Verify bar chart shows all 5 categories (Electronics, Accessories, Audio, Wearables, Smart Home) sorted highest to lowest with tooltips

### Implementation for User Story 3

- [x] T019 [US3] Create category sales aggregation using groupby('category') in app.py
- [x] T020 [US3] Sort category data by total_amount descending in app.py
- [x] T021 [US3] Create bar chart using plotly.express.bar() in app.py
- [x] T022 [US3] Configure chart title "Sales by Category" and axis labels in app.py
- [x] T023 [US3] Add interactive tooltips showing category and sales amount in app.py

**Checkpoint**: User Story 3 complete - category chart shows 5 categories sorted by value

---

## Phase 6: User Story 4 - Compare Sales by Geographic Region (Priority: P4)

**Goal**: Display a bar chart showing sales breakdown by the 4 geographic regions, sorted by value

**Independent Test**: Verify bar chart shows all 4 regions (North, South, East, West) sorted highest to lowest with tooltips

### Implementation for User Story 4

- [ ] T024 [US4] Create region sales aggregation using groupby('region') in app.py
- [ ] T025 [US4] Sort region data by total_amount descending in app.py
- [ ] T026 [US4] Create bar chart using plotly.express.bar() in app.py
- [ ] T027 [US4] Configure chart title "Sales by Region" and axis labels in app.py
- [ ] T028 [US4] Add interactive tooltips showing region and sales amount in app.py

**Checkpoint**: User Story 4 complete - region chart shows 4 regions sorted by value

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final layout, styling, and validation

- [ ] T029 Arrange category and region charts side-by-side using st.columns() in app.py
- [ ] T030 Verify dashboard loads in under 5 seconds
- [ ] T031 Verify all charts render in under 2 seconds
- [ ] T032 Test dashboard in Chrome, Firefox, Safari, and Edge browsers
- [ ] T033 Verify all displayed values match CSV calculations with 100% accuracy

**Checkpoint**: Dashboard complete and ready for deployment

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - US1 (P1): Can start immediately after Phase 2
  - US2 (P2): Can start after Phase 2 (independent of US1)
  - US3 (P3): Can start after Phase 2 (independent of US1, US2)
  - US4 (P4): Can start after Phase 2 (independent of US1, US2, US3)
- **Polish (Phase 7)**: Depends on all user stories being complete

### User Story Dependencies

All user stories are **independent** - they share the data loading foundation but add separate visualizations:

- **User Story 1 (P1)**: KPI metrics - no dependencies on other stories
- **User Story 2 (P2)**: Trend line chart - no dependencies on other stories
- **User Story 3 (P3)**: Category bar chart - no dependencies on other stories
- **User Story 4 (P4)**: Region bar chart - no dependencies on other stories

### Within Each User Story

Since this is a single-file application, tasks within each story should be executed sequentially:
1. Data aggregation first
2. Chart creation second
3. Configuration and tooltips last

### Parallel Opportunities

Since all code goes into a single file (`app.py`), parallelization is limited. However:
- Different developers could work on different user stories and merge changes
- Setup tasks T001-T003 can run in parallel (different files/commands)

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T004)
2. Complete Phase 2: Foundational (T005-T008)
3. Complete Phase 3: User Story 1 (T009-T013)
4. **STOP and VALIDATE**: Run dashboard, verify KPIs display correctly
5. Deploy MVP if ready - stakeholders can see Total Sales and Total Orders

### Incremental Delivery

1. Complete Setup + Foundational → Dashboard shell with title
2. Add User Story 1 → KPIs visible → **MVP deployed!**
3. Add User Story 2 → Trend chart added → Deploy update
4. Add User Story 3 → Category chart added → Deploy update
5. Add User Story 4 → Region chart added → Deploy update
6. Complete Polish → Final validation → Production ready

### Single Developer Strategy

Execute phases sequentially:
1. Phase 1: Setup (~5 min)
2. Phase 2: Foundational (~10 min)
3. Phase 3: User Story 1 (~15 min)
4. Phase 4: User Story 2 (~15 min)
5. Phase 5: User Story 3 (~10 min)
6. Phase 6: User Story 4 (~10 min)
7. Phase 7: Polish (~10 min)

---

## Notes

- All code goes into single file `app.py` per constitution
- No automated tests - manual testing validates each story
- Each user story adds independent value (can deploy after any story)
- Commit after each phase or logical group of tasks
- Reference Jira issues in commits if applicable (e.g., `ECOM-1: add KPI metrics`)
