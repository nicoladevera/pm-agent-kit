# Visualization Standards

What makes a data chart analytically effective — independent of aesthetic preference. Use this to make every chart decision: type selection, titling, annotation, comparison anchors, label placement, style, and color. The visual output counterpart to `data-interpretation.md` (analytical standards) — that file governs how to reason about data; this file governs how to show what you found. For slide composition and layout when charts appear in presentations, see `slide-design.md`.

A chart that requires reading the prose to understand what it means has failed. The visual should carry the finding on its own.

---

## Chart Selection

Match the chart type to what the data needs to communicate, not to what looks interesting. The right chart makes the finding obvious at a glance. The wrong chart forces the reader to do the interpretation work you were supposed to do.

| If the question is about... | Use this chart | Why |
|-----------------------------|---------------|-----|
| Change over time / trend / anomaly | **Line chart** | Shows slope, inflection points, and anomaly windows. Annotate the key moment. |
| Comparing categories (ranking) | **Horizontal bar chart** | Labels are more readable than vertical. Sort by value, not alphabetically. |
| Funnel drop-off | **Horizontal waterfall or step bar** | Absolute counts at each stage; the drop-off magnitude is the story, not the conversion rate alone |
| Comparing groups on one metric | **Grouped bar chart** | Side-by-side comparison for ≤5 groups; more than 5, consider a dot plot |
| Distribution / spread across entities | **Dot plot or strip chart** | Shows where each team/cohort sits relative to the average; better than bars when rank ordering and spread both matter |
| Composition of a whole | **Stacked bar or donut** (max 5 segments) | Use only when the part-to-whole relationship is the finding |
| Correlation between two metrics | **Scatter plot** | Two axes, each entity is a point; annotate the outlier that drives the finding |
| Retention or cohort behavior over time | **Heatmap** | Rows = cohorts, columns = time periods, color = metric value |

**What not to use:**
- Pie charts with more than 4 segments — differences in arc length are nearly impossible to read accurately
- 3D charts — perspective distortion makes values unreadable
- Dual-axis charts — two y-axes require the reader to mentally reconcile two scales; split into two charts instead
- Area charts for multiple overlapping series — the overlap obscures the values

---

## Chart Type by Analysis Type

When producing charts for `data-analysis` skill output, use these defaults per analysis type. Deviate only when the data's shape clearly calls for a different treatment.

| Analysis type | Primary chart | Secondary chart (if a second finding warrants it) |
|--------------|--------------|---------------------------------------------------|
| Metric interpretation | Line/time-series with the key movement annotated | Bar showing the metric vs. baseline or benchmark |
| Funnel analysis | Horizontal waterfall — absolute users at each stage | Segmented or grouped bar at the biggest drop-off step |
| Cohort analysis | Grouped bar (cohorts × metric, same time window) | Dot plot or heatmap for retention over time |
| Anomaly investigation | Time series with the anomaly window highlighted | Breakdown bar showing which segment drives the scope |

---

## Insight-First Titling

The chart title is the most important element on the chart. It should state the finding — not describe the chart.

**Non-negotiable rule:** If the title could be reused on a different dataset, it is too generic. If a reader could look at the title without seeing the chart and still not know what you found, the title has failed.

| Describes the chart (wrong) | States the finding (right) |
|----------------------------|---------------------------|
| "xG per Shot by Team" | "Kansas City Creates 2× the Chance Quality of Utah Royals" |
| "Weekly Active Users Over Time" | "DAU Dropped 15% on March 17 — Same Day as the v2.4.1 Deploy" |
| "Activation Rate by Platform" | "Mobile Web Activation Is 12pp Below iOS — Concentrated at Step 5" |
| "Cohort Retention, Weeks 1–8" | "Users Who Complete Onboarding Retain at 2× the Rate of Those Who Skip It" |

The title is written after the analysis is complete — you need to know the finding before you can state it. Never title a chart before you have run the numbers.

---

## Annotation Standards

Every chart should annotate the data point the finding rests on. The annotation is what transforms a chart that shows data into a chart that makes an argument.

**What to annotate:**
- The outlier that changes the conclusion (e.g., the bar that is far above or below the others)
- The inflection point on a time series (when the trend changes direction)
- The anomaly window (the specific period where the anomaly occurred)
- The biggest drop-off step in a funnel
- The cohort that diverges most from the others

**How to annotate:**
- Use direct text labels on or next to the data point — not a separate legend entry
- Include the value and what it means: "0.116 xG/shot — 2× league avg" is more useful than "0.116"
- Keep annotations minimal — annotate the 1-3 most important points, not every data point
- Use an arrow or leader line only when the label would overlap the data point it describes

**Red flag:** A chart where the reader must scan every bar or point to find the one that matters. The annotation should direct the eye to the finding immediately.

---

## Comparison Anchors

A number without a comparison is uninterpretable. Every chart must give the reader a reference point.

**Required in every chart:**
- A benchmark line, reference line, or comparison series showing what "normal" or "expected" looks like
- Common anchors: league average, prior period, target, overall mean, industry benchmark

**How to render:**
- Show the benchmark as a horizontal dashed line (gray, labeled)
- Label the benchmark directly on the line: "League avg: 0.105" — not in a legend
- When comparing periods, use a lighter shade or dotted line for the prior period, solid for current

**Red flag:** A chart showing a metric value with no reference to whether that value is high, low, expected, or unusual. A conversion rate of 9.3% is meaningless without knowing the baseline. A bar of height 1.65 xG/game conveys nothing without a league average to compare against.

---

## Label Discipline

Put labels on the chart, not in a legend. Legend lookups interrupt reading and slow comprehension.

| Condition | Treatment |
|-----------|-----------|
| ≤12 categories (teams, cohorts, segments) | Direct labels — name each bar, line, or point on the chart |
| >12 categories | Legend acceptable, but consider whether 12+ categories belong on a single chart |
| Time series with 2-3 lines | Label the end of each line directly |
| Grouped bars | Label the group header, not each individual bar, unless the individual bar value is the finding |
| Scatter plot | Label the outlier points directly; other points can be unlabeled |

**Axis labels:** Always label both axes with the metric name and unit. "xG/Shot" not "Value." "Teams" not "Category."

**Value labels:** Include specific values on bar charts when the precise number matters. Omit when the relative magnitude is the finding and exact values would clutter the chart. When in doubt, include — readers can ignore a label they don't need, but can't recover a value that isn't there.

---

## Style and Density

Restraint is the default. Every element on the chart exists to support the finding. Elements that don't serve the finding should be removed.

**One chart, one message.** If you have two findings, produce two charts. Cramming two stories into one panel forces the reader to do the synthesis work that the chart was supposed to do. Exception: a secondary series explicitly included as a comparison anchor (e.g., prior period) is not a second message — it is context for the primary message.

**Maximum 5 data categories per chart.** More than five means the chart is a table, not a visualization. Group small categories into "Other" or produce a separate chart for a subset.

**Gridlines:** Horizontal gridlines are acceptable when precise value reading is required (e.g., a bar chart where the exact value matters). Remove them when the chart's story is about relative magnitude or trend shape, not precise values. Never use vertical gridlines.

**Chart borders, backgrounds, and decorative elements:** Remove. No box around the chart area. White or transparent background. No watermarks or logos unless explicitly required.

**Font size:** Minimum 10pt on saved PNGs at 150 DPI. Title: 12-14pt. Axis labels: 10-11pt. Annotations: 9-10pt. Nothing smaller than 9pt.

---

## Color

Color communicates meaning. Use it deliberately, not decoratively.

**Default rule:** One saturated color for the focal data point (the one the finding rests on). Gray for everything else. This directs attention to the finding without explanation.

**Functional color palette (apply consistently within and across charts in the same analysis):**

| Color | Meaning | Use for |
|-------|---------|---------|
| A single accent color (blue, teal, or brand color) | Focal / primary finding | The bar, line, or point the finding rests on |
| Gray (#999 or #bbb) | Baseline / context / everything else | All non-focal categories; comparison period data |
| Green | Positive / above expectation | Metrics beating target or overperforming xG |
| Red | Negative / below expectation | Metrics missing target or underperforming |
| Amber | Caution / approaching threshold | Metrics near a boundary |

**Maximum 3-5 colors per chart.** A chart where every bar is a different color has no focal point — it tells the reader everything is equally important, which means nothing is.

**No rainbow palettes.** Each color must map to a meaning, not just to visual differentiation. If a color has no consistent meaning, replace it with a shade of gray.

**Color category membership must be derived from the data, not hardcoded.** If red means "below average," compute which entities are below the average and color them red — do not manually select a subset. Hardcoding produces visually inconsistent charts where some below-average entities are red and others are gray, which signals a threshold that does not exist. The rule: if a color encodes a condition (below average, above target, in anomaly window), apply it to every entity that meets that condition.

---

## Technical Standards

**Save pattern (required):**
```python
plt.savefig(output_path, dpi=150, bbox_inches='tight')
plt.close()
```

`bbox_inches='tight'` prevents labels and titles from being clipped. `dpi=150` produces crisp PNGs at reasonable file size. Always call `plt.close()` immediately after saving — open figure state accumulates and causes rendering issues.

**File naming:**
- Primary chart: `YYYY-MM-DD-analysis-slug-chart.png`
- Additional charts: `YYYY-MM-DD-analysis-slug-chart_2.png`, `_3.png`, etc.
- Use the same date and slug as the corresponding `.md` artifact
- Save to `knowledge/data-analyses/` alongside the markdown file

**Figure size:**
- Default: `figsize=(10, 6)` for landscape charts (bar charts, line charts, scatter plots)
- Tall charts (horizontal bar with many categories): `figsize=(10, 8)` or wider as needed
- Adjust to ensure labels and annotations are not clipped

---

## Anti-Patterns

These fail consistently. Do not use them.

- **Title describes the chart instead of stating the finding.** "Conversion Rate by Cohort" is a label, not an insight. The title should answer the question "so what?"
- **No comparison anchor.** A metric with no benchmark is uninterpretable. Always show what "normal" looks like.
- **Legend when direct labels fit.** Legends slow reading. For ≤12 categories, label directly on the chart.
- **Two findings on one chart.** Forces the reader to synthesize. Split into two charts.
- **Rainbow color palette.** Every bar in a different color signals "everything is equally important." Use one accent color and gray.
- **Gridlines as decoration.** Remove gridlines unless precise value reading is required.
- **Values without units or context on axes.** "1.65" on a y-axis means nothing. "1.65 xG/game" does.
- **Annotations on every data point.** Annotate the 1-3 points the finding rests on. Labeling everything buries the finding.
- **Vertical text or rotated x-axis labels.** Rotate the chart to horizontal bars instead of rotating the labels.
