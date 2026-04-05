# Branding Guidelines

What branding elements matter for presentations and how to apply them consistently. Use this to ensure generated slides are visually coherent and professionally branded. This file defines the *standards* — what to capture, what consistency looks like, and how to apply brand elements. The actual brand values (colors, fonts, logos) for the current company live in `company/interfaces/branding.md`.

Consistent branding is not decoration. It signals professionalism and organizational alignment. A deck with inconsistent fonts, off-brand colors, or a pixelated logo undermines the content — the audience notices the visual noise before they engage with the argument.

---

## Branding Elements

### What to Capture

Every company brand has these elements. When populating `company/interfaces/branding.md`, capture all of them. When generating slides, apply them consistently.

| Element | What it includes | Why it matters |
|---------|-----------------|---------------|
| **Color palette** | Primary color (brand dominant), secondary color (accent/contrast), neutral colors (backgrounds, text), status colors (success/warning/error if applicable). All as hex values. | Colors create visual identity. Off-brand colors make slides look unauthorized or improvised. |
| **Typography** | Heading font (usually bold/impactful), body font (usually clean/readable), monospace font (for data or code if relevant). Include font weights (regular, bold, semibold). | Font consistency is the single most visible branding element. Mixed fonts look amateur. |
| **Logo** | Primary logo (full), icon/mark (small), light/dark variants. File paths or URLs. Clear space rules (minimum padding around the logo). | Logo misuse (stretching, wrong variant, insufficient padding) is the most common branding violation. |
| **Slide defaults** | Background color, text color, margin/padding, content alignment, header/footer conventions. | Consistent defaults mean every slide starts from the same visual baseline. |

### When Brand Values Are Missing

If `company/interfaces/branding.md` is absent or a stub, use these professional defaults. The palette, typography, and sizing are designed to look intentional and contemporary — not like a default template.

| Element | Default |
|---------|---------|
| Primary color | `#2D3142` (charcoal-navy) |
| Secondary color | `#4F5D75` (slate blue-gray) |
| Accent color | `#E07A5F` (terracotta) |
| Background | `#FAFAF8` (warm off-white) |
| Text color | `#2D3142` (matches primary — tonal cohesion) |
| Heading font | Georgia Bold (serif headings add authority; universally available) |
| Body font | Helvetica Neue Regular (Windows fallback: Arial Regular) |
| Font sizes | Title: 44pt, Heading: 32pt, Body: 24pt, Caption: 16pt |
| Logo | Omit — don't use a placeholder |

Flag in the context note that default branding was used because company branding context was unavailable.

---

## Slide Types and Branding Treatment

### Standard Slide Types

Every presentation uses a mix of these slide types. Each type defines a purpose and the branding treatment that applies. For layout composition (spatial arrangement, sizing, density), see `references/slide-design.md`.

#### Title Slide
- **Purpose:** Opening. Sets the topic, context, and presenter identity.
- **Branding:** Primary color as background or accent bar. Logo in corner (if available). Title in heading font at title size.

#### Section Divider
- **Purpose:** Marks transitions between major sections of the narrative.
- **Branding:** Secondary color or accent treatment. Consistent with title slide style. Minimal text — section title only.

#### Content Slide
- **Purpose:** The workhorse. Delivers information with a takeaway headline.
- **Branding:** White or neutral background. Headline in primary color. Body in text color.

#### Data Slide
- **Purpose:** Presents a chart, table, or quantitative evidence.
- **Branding:** Chart colors use the brand palette (primary, secondary, accent). Axes and labels in text color. Source citation in caption style. Avoid default chart colors from tools — they rarely match the brand.

#### Comparison Slide
- **Purpose:** Side-by-side comparison of 2-3 options, pillars, or parallel items.
- **Branding:** Use color coding from brand palette to distinguish the columns. Consistent formatting across all columns.

#### Quote/Callout Slide
- **Purpose:** Highlights a key user quote, finding, or provocative insight through isolation.
- **Branding:** Accent color for the quote mark or highlight. Clean background. Attribution in caption style.

#### Closing/Ask Slide
- **Purpose:** States the recommendation, ask, or next steps.
- **Branding:** Can use primary color background for emphasis (inverted text). Minimal supporting content.

#### Hero Number Slide
- **Purpose:** A single metric or number IS the insight. The number carries the argument.
- **Branding:** Number in primary or accent color at large scale. Context line in body text color. Source in caption style. Clean background.

#### Metrics/Dashboard Slide
- **Purpose:** Multiple KPIs or numbers carry equal weight — performance snapshot, scorecard.
- **Branding:** Numbers in primary color. Labels in text color. Optional trend indicators use functional colors (green/red/amber per color strategy). Consistent treatment across all metrics.

#### Timeline/Sequence Slide
- **Purpose:** Content is inherently sequential — roadmap phases, process steps, historical progression.
- **Branding:** Nodes or steps in primary or secondary color. Connecting lines in neutral color. Labels in text color. Active/current step can use accent color for emphasis.

#### Full-Bleed Image Slide
- **Purpose:** A photo, screenshot, or visual IS the primary content.
- **Branding:** Dark overlay (minimum 60% opacity) for text legibility when headline is overlaid. Headline in white or light text. Logo may be omitted if it competes with the image.

---

## Applying Branding to Generated Slides

### Slides Mode Implementation Guidance

When generating `.pptx` files with `python-pptx`, apply branding consistently:

#### Fonts
- Use the heading and body fonts from `company/interfaces/branding.md`.
- If the brand font isn't available on the system, fall back to the closest universally available font and note the substitution.
- Apply font sizes consistently: title slides largest, content slides standard, captions smallest.

#### Colors
- Apply primary color to backgrounds or headlines, secondary to accents or section dividers, neutral to body text, and accent color sparingly for emphasis.
- If `company/interfaces/branding.md` is absent or stub-level, use the documented defaults from this file and note that fallback in the context note.

#### Layouts
- Create or use slide layouts that match the slide types above.
- Maintain consistent margins across all slides.
- Align content to a grid — left-align text, consistent vertical spacing.
- If a requested visual cannot be rendered cleanly with `python-pptx`, use a simpler text or table treatment and note the limitation rather than inventing custom template fidelity.

#### Logo Placement
- If a logo file path is provided in `company/interfaces/branding.md`, place it consistently (typically top-right or bottom-right of every slide except the title slide).
- Respect clear space rules — the logo should have padding equal to at least its height on all sides.
- Never stretch or distort the logo. Maintain aspect ratio.

### HTML Implementation Guidance

When generating self-contained HTML presentation files, apply branding through CSS custom properties. This ensures the same brand identity from `company/interfaces/branding.md` renders consistently in HTML as it does in pptx.

#### CSS Custom Properties

Define all brand values in `:root` so they cascade to every slide element:

```css
:root {
  /* Colors */
  --brand-primary: #2D3142;       /* charcoal-navy — headlines, primary backgrounds */
  --brand-secondary: #4F5D75;     /* slate blue-gray — section dividers, secondary elements */
  --brand-accent: #E07A5F;        /* terracotta — emphasis, callouts, focal data points */
  --brand-background: #FAFAF8;    /* warm off-white — slide backgrounds */
  --brand-text: #2D3142;          /* matches primary — body text */
  --brand-text-light: #FFFFFF;    /* white — text on dark backgrounds */

  /* Functional colors */
  --color-positive: #4A7C59;      /* green — growth, success, targets met */
  --color-negative: #C1442E;      /* red — decline, risk, targets missed */
  --color-caution: #D4A843;       /* amber — approaching threshold, watch */
  --color-neutral: #9A9BA3;       /* gray — baseline, non-focal elements */

  /* Typography */
  --font-heading: 'Georgia', serif;
  --font-body: 'Helvetica Neue', 'Arial', sans-serif;
  --font-weight-heading: 700;
  --font-weight-body: 400;

  /* Spacing */
  --slide-padding: 5% 6%;
  --element-gap: 1.5rem;
}
```

These are the **default values** (matching the defaults in the "When Brand Values Are Missing" table above). When `company/interfaces/branding.md` provides actual brand values, substitute them into the custom properties at generation time. The CSS structure stays the same — only the values change.

#### Font Application

```css
.slide h1, .slide h2, .slide .tier-headline {
  font-family: var(--font-heading);
  font-weight: var(--font-weight-heading);
  color: var(--brand-primary);
}

.slide p, .slide li, .slide .tier-supporting {
  font-family: var(--font-body);
  font-weight: var(--font-weight-body);
  color: var(--brand-text);
}

.slide .tier-caption {
  font-family: var(--font-body);
  color: var(--brand-secondary);
}
```

If the brand specifies a web font that may not be installed locally, include an `@font-face` declaration with the font file base64-encoded inline in the CSS. The HTML file must remain fully self-contained — no external font URLs. If the font cannot be embedded (file too large or unavailable), fall back to the closest system font and note the substitution in the context note.

#### Color Application by Slide Type

Apply the same slide type branding treatments defined in the "Slide Types and Branding Treatment" section above, mapped to CSS:

| Slide type | CSS treatment |
|-----------|---------------|
| **Title slide** | `background: var(--brand-primary)` or accent bar via `border-top: 6px solid var(--brand-primary)`. Headline in `var(--brand-text-light)` if dark background, `var(--brand-primary)` if light. |
| **Section divider** | `background: var(--brand-secondary)`. Title text in `var(--brand-text-light)`. |
| **Content slide** | `background: var(--brand-background)`. Headline in `var(--brand-primary)`. Body in `var(--brand-text)`. |
| **Data slide** | Charts use `var(--brand-primary)`, `var(--brand-secondary)`, `var(--brand-accent)` for data series. Axis labels in `var(--brand-text)`. |
| **Hero number** | Number in `var(--brand-primary)` or `var(--brand-accent)`. Context line in `var(--brand-text)`. |
| **Quote/Callout** | Quote mark or highlight bar in `var(--brand-accent)`. Quote text in `var(--brand-text)`. Attribution in `var(--brand-secondary)`. |
| **Closing/Ask** | Can use `background: var(--brand-primary)` with `color: var(--brand-text-light)` for emphasis. |
| **Metrics row** | Numbers in `var(--brand-primary)`. Trend indicators use `var(--color-positive)`, `var(--color-negative)`, `var(--color-caution)`. |

#### Logo Placement

If a logo file path is provided in `company/interfaces/branding.md`, embed it as an inline `<img>` with a base64-encoded `src` (or inline SVG if the logo is SVG format). Position via CSS:

```css
.slide-logo {
  position: absolute;
  top: 4%;
  right: 4%;
  height: 2rem;
  width: auto;            /* maintain aspect ratio */
}
```

Place the logo on every slide except the title slide (consistent with pptx guidance). Respect clear space by ensuring no other elements overlap the logo area.

#### Contrast and Accessibility

- All text-on-background combinations must meet WCAG AA contrast (4.5:1 for body, 3:1 for large text) — same standard as pptx.
- Use `aria-label` on SVG chart elements for basic accessibility.
- Use semantic HTML: `<section>` for slides, `<h2>` for headlines, `<p>` for body text, `<figure>` for charts.

---

## Visual Consistency Standards

### What Consistency Means

- **Same fonts throughout.** No slide should use a font that isn't in the brand typography.
- **Same color application.** Headlines are always one color. Body text is always another. Charts always use the brand palette.
- **Same layout grid.** Content starts at the same position on every content slide. Margins are uniform.
- **Same emphasis treatment.** Bold is used consistently. Accent color means the same thing everywhere.

### Red Flags

- **Inconsistent fonts.** Arial on one slide, Helvetica on another, Times New Roman on a third. This happens when slides are assembled from multiple sources.
- **Too many colors.** More than 4-5 colors in a deck is visually noisy. Stick to the brand palette.
- **Default chart colors.** Excel/Sheets default colors (blue-orange-gray) look generic. Replace with brand palette colors.
- **Logo misuse.** Stretched, pixelated, wrong variant (dark logo on dark background), or inconsistent placement across slides.
- **Slide-to-slide visual jumps.** One slide has a white background, the next has a colored background, the next has a gradient — with no pattern to the variation. Backgrounds should be intentional (e.g., section dividers use color, content slides use white).
- **Wall of text.** For live presentations, any slide exceeding 25 words of body content or 5 bullets. For pre-reads, exceeding 60 words. If the slide reads like a document paragraph, move the detail to speaker notes. See `references/slide-design.md` for full density budgets by delivery context.
