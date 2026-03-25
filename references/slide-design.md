# Slide Design

What makes a slide visually effective independent of brand or narrative arc. Use this to make slide-level design decisions: hierarchy, layout, density, typography, and visual storytelling. The visual composition counterpart to `narrative-structure.md` (story craft) and `branding-guidelines.md` (brand identity and implementation). For which visual type to use (bar chart vs. line chart vs. table), see `narrative-structure.md`. For which specific colors and fonts to apply, see `branding-guidelines.md`. This file covers how to compose and render slides effectively.

A professionally designed slide is defined by restraint — knowing what to remove, not what to add. Every element earns its place. Default-template slides fail because they treat every element with equal weight, fill every gap with content, and use decoration where information should be.

---

## Information Hierarchy

### One Idea Per Slide

A slide with two ideas is two slides. If a slide's purpose can't be stated in one sentence, split it. The headline IS the one idea — everything else on the slide proves or reinforces it.

### Visual Tier System

Every slide uses 3-4 distinct visual tiers. Fewer means the hierarchy is flat (the audience can't tell what matters). More means the slide is cluttered.

| Tier | Role | Size Range |
|------|------|-----------|
| **Title / headline** | The takeaway claim | 36-60pt |
| **Key insight / number** | The focal evidence | 40-48pt |
| **Supporting content** | Data, bullets, explanatory text | 24-32pt |
| **Source / caption** | Attribution, footnotes | 14-18pt |

Not every slide uses all four tiers. A hero number slide might use three (headline, number, source). A content slide might use three (headline, body, source). But every slide must have at least three tiers with visible size differentiation.

### Pyramid Principle Per Slide

The headline states the conclusion. The content proves it. The visual reinforces it. If the content doesn't serve the headline, it belongs on a different slide or in speaker notes. Apply the signal-to-noise test: every element on the slide should answer "does this help the audience understand the headline's claim?" If not, remove it.

---

## Layout Composition

### Space Allocation

**60% white space. 30% content. 10% accent/emphasis.** This is the single most reliable indicator of professional vs. amateur slides. White space is not wasted space — it is the container that makes content readable and powerful.

### Grid Discipline

All content aligns to a consistent grid across every slide in the deck:
- Text starts at the same left margin on every content slide
- Charts align to the same content area
- Vertical spacing between elements is uniform
- Headlines sit at the same Y position across all content slides
- Content area starts at the same Y position across all content slides

### Layout Patterns

Choose the pattern that serves the content, not for variety's sake.

| Pattern | When to use | Composition |
|---------|------------|-------------|
| **Full-width content** | Default for text-heavy content slides | Headline top, content below, one visual element. Left-aligned. |
| **Split layout (40/60)** | Text and visual carry equal weight | Text left (40%), visual right (60%). Never text right — Western reading order starts left. |
| **Hero number** | The insight IS a single number | Large centered number (44-60pt), one-line context below (24pt), source at bottom (16pt). Minimal surrounding content. |
| **Full-bleed image** | Photo or screenshot is the primary content | Image fills slide. Dark overlay (minimum 60% opacity) for text legibility. Headline overlaid. |

### Anti-Patterns

- **Centered body text.** Harder to scan than left-aligned. Center alignment is acceptable only for title slides and hero numbers.
- **Content touching slide edges.** No breathing room destroys readability. Maintain consistent padding on all sides.
- **Inconsistent margins between slides.** Content that shifts position slide-to-slide looks assembled, not designed.

---

## Cognitive Load and Density

### Element Budget

Maximum **5-7 distinct visual elements** per slide. A headline, subtitle, chart, axis labels, source line, and logo counts as six elements. If a slide exceeds seven, it needs simplification.

### Word Budget by Delivery Context

Density depends on how the audience encounters the slides.

| Context | Word budget (body content) | Rationale |
|---------|---------------------------|-----------|
| **Live presentation** | 15-25 words | Audience listens; slides support, not replace, the speaker |
| **Pre-read / leave-behind** | 40-60 words | Audience reads without presenter; slides must stand alone |
| **Standalone reference** | Up to 80 words | Functions as a document page; acceptable density is higher |

### Bullet Discipline

- **3-5 bullets maximum.** More than five means the content needs restructuring — group into categories, split across slides, or push detail to speaker notes.
- **5-8 words per bullet.** Bullets are cues, not sentences. If a bullet needs a period, it's too long.

### Data Density

- **One primary data series per chart.** A second series is acceptable only for direct comparison (actual vs. target, this year vs. last year). Three or more series means the chart needs splitting or the insight needs reframing.
- **Maximum 3-5 data categories per chart.** A bar chart with twelve bars is a table, not a chart.

### Anti-Patterns

- **Wall of text.** More than 5 bullets or exceeding the word budget for the delivery context. Move detail to speaker notes.
- **4+ data series on one chart.** The audience can't distinguish the series. Split into multiple slides or highlight the one that matters.
- **More than 3 seconds to parse.** If the slide requires effort to decode, it's too dense. Simplify or split.

---

## Typography Rules

### Size Ranges

| Element | Minimum | Recommended | Maximum |
|---------|---------|-------------|---------|
| Title (title slide) | 36pt | 44pt | 60pt |
| Headline (content slides) | 28pt | 32pt | 44pt |
| Body text | 24pt | 24-28pt | 32pt |
| Caption / source | 14pt | 16pt | 18pt |

**Nothing below 14pt.** If text needs to be smaller than 14pt, it doesn't belong on the slide.

### Font Discipline

- **Two-font maximum.** One for headings, one for body. A third font for data labels or code is acceptable only if the brand specifies it.
- **Hierarchy through size and weight, not color.** Bold and size create hierarchy. Color creates meaning (emphasis, status, category). Using color as the primary hierarchy mechanism fails in grayscale and for colorblind viewers.

### Readability

- **Line spacing:** 1.2-1.5x for body text. 1.0-1.2x acceptable for tight bullet lists.
- **Left-align body text.** Center-aligned body text is harder to scan. Center alignment is acceptable only for title slides and hero numbers.
- **Contrast:** Dark text on light backgrounds as the default. Light text on dark backgrounds only for title slides, section dividers, or full-bleed image overlays.

---

## Color Strategy

This section governs color proportion and function — how to apply color effectively on slides. For which specific colors to use (hex values, brand palette), see `branding-guidelines.md`.

### The 60-30-10 Rule

| Proportion | Role | Typical application |
|------------|------|-------------------|
| **60%** | Dominant / background | Slide background, primary content area |
| **30%** | Secondary / structure | Content blocks, supporting visuals, secondary text areas |
| **10%** | Accent / emphasis | Callouts, key data points, CTAs, highlighted findings |

### Functional Color

Use color to communicate meaning, not to decorate. Apply consistently across all data slides in the deck.

| Color | Meaning | Use for |
|-------|---------|---------|
| Green | Positive / growth / success | Metrics that improved, targets met, positive trends |
| Red | Negative / decline / risk | Metrics that worsened, targets missed, risk indicators |
| Gray | Neutral / baseline / context | Comparison data, non-focal elements, historical baseline |
| Amber | Caution / watch / approaching threshold | Metrics nearing targets, emerging risks |

### Chart Color Discipline

- **Maximum 3-5 colors per chart.** More creates visual noise.
- **One saturated color for the focal data point, gray for everything else.** This directs attention to the insight. A chart where every bar is a different color has no focal point.
- **No rainbow palettes.** Each color in a chart should map to a meaning or a specific data category, not just differentiate for differentiation's sake.

### Contrast

WCAG AA minimum: 4.5:1 contrast ratio for body text, 3:1 for large text (above 24pt). Test any text-on-background combination, especially with brand colors that weren't designed for slide use.

---

## Visual Storytelling Decisions

For which visual type fits each narrative purpose, see `references/narrative-structure.md`. This section covers how to select and render the right visual treatment for each slide's content.

### Decision Tree

| If the content is... | Use this treatment |
|---------------------|--------------------|
| A single key number | **Hero number layout.** Large number (44-60pt), one-line context, source. No chart needed. |
| Comparing categories | **Horizontal bar chart.** Labels are more readable than vertical. Sort by value, not alphabetically. |
| A trend over time | **Line chart.** Clean, shows slope and inflection points. Annotate the key moment. |
| Composition of a whole | **Stacked bar or donut chart.** Maximum 5 segments. More than 5 → group small segments into "Other." |
| A process or relationship | **Simple diagram.** Maximum 5-7 nodes. If more complex, break into multiple slides showing each phase. |
| A product or UX point | **Screenshot with annotation.** Circle, arrow, or highlight the specific element. No full-page screenshots without focus. |
| A list of capabilities or benefits | **Icons with short labels.** Replace bullet points with icons for faster pattern recognition. 3-6 items maximum. |

### The Pairing Rule

The strongest slides pair three elements: **statistic + visual + narrative headline.** Example: "Support tickets dropped 40%" (headline) + bar chart showing the decline (visual) + "Self-service tooling eliminated the top 3 ticket categories" (supporting text). This combination drives retention significantly higher than any single element alone.

### Anti-Patterns

- **Generic stock photos.** Posed business people, handshakes, abstract shapes. These add no information and signal "template."
- **Clip art or cartoon icons in a professional context.** Use clean, consistent icon sets or no icons at all.
- **3D chart effects.** Distort data perception. Always use flat, 2D charts.
- **Decorative elements with no information purpose.** Borders, shapes, gradients, or patterns that don't encode data or guide the eye.

---

## Designed vs. Default

A quick self-check. Professional slides share these markers — if any are missing, the slide needs revision.

### Markers of Intentional Design

- [ ] **Intentional white space** — breathing room is planned, not leftover
- [ ] **Consistent visual language** — same grid, spacing, emphasis treatment across all slides
- [ ] **Specific, purposeful visuals** — every image, chart, or icon directly supports the headline claim
- [ ] **Restrained color** — 3-5 colors total, each used with a consistent function
- [ ] **Natural eye flow** — hierarchy guides the eye from primary to secondary to tertiary without effort
- [ ] **Precise spacing** — consistent margins, padding, and element positioning
- [ ] **Position consistency** — headlines, content areas, and footers at the same coordinates across slides of the same type

### What Screams "Default Template"

- Equal visual weight on all elements (flat hierarchy)
- Decorative backgrounds, patterns, or gradients with no purpose
- Generic stock imagery or placeholder visuals
- Excessive or random animations and transitions
- Every color in the palette used on a single slide
- Inconsistent styling between slides (font sizes shift, margins drift, color usage changes)
- Content that fills every available pixel (no white space strategy)
