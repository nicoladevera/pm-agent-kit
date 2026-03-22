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

If `company/interfaces/branding.md` is absent or a stub, use clean professional defaults:

| Element | Default |
|---------|---------|
| Primary color | `#1a1a2e` (dark navy) |
| Secondary color | `#0f3460` (deep blue) |
| Accent color | `#e94560` (coral) |
| Background | `#ffffff` (white) |
| Text color | `#333333` (dark gray) |
| Heading font | Calibri Bold (universally available) |
| Body font | Calibri Regular |
| Font sizes | Title: 28pt, Heading: 22pt, Body: 16pt, Caption: 12pt |
| Logo | Omit — don't use a placeholder |

Flag in the context note that default branding was used because company branding context was unavailable.

---

## Slide Types and Layouts

### Standard Slide Types

Every presentation uses a mix of these slide types. Each has a specific layout purpose.

#### Title Slide
- **Purpose:** Opening. Sets the topic, context, and presenter identity.
- **Layout:** Large title text (centered or left-aligned), subtitle with context (date, audience, purpose), presenter name.
- **Branding:** Primary color as background or accent bar. Logo in corner (if available).

#### Section Divider
- **Purpose:** Marks transitions between major sections of the narrative.
- **Layout:** Section title only. Minimal text. Visual breathing room.
- **Branding:** Secondary color or accent treatment. Consistent with title slide style.

#### Content Slide
- **Purpose:** The workhorse. Delivers information with a takeaway headline.
- **Layout:** Headline at top (takeaway, not topic). Content below: bullets, short text, or data. One visual element maximum.
- **Branding:** White or neutral background. Heading in primary color. Body in text color.

#### Data Slide
- **Purpose:** Presents a chart, table, or quantitative evidence.
- **Layout:** Headline states the data takeaway. Chart or table fills the content area. Source citation at bottom.
- **Branding:** Chart colors use the brand palette (primary, secondary, accent). Axes and labels in text color. Avoid default chart colors from tools — they rarely match the brand.

#### Comparison Slide
- **Purpose:** Side-by-side comparison (before/after, us/them, option A/B).
- **Layout:** Two-column layout with clear labels. Consistent formatting on both sides.
- **Branding:** Use color coding from brand palette to distinguish the two sides.

#### Quote/Callout Slide
- **Purpose:** Highlights a key user quote, metric, or finding.
- **Layout:** Large quote or number. Attribution. Minimal supporting text.
- **Branding:** Accent color for the quote mark or highlight. Clean background.

#### Closing/Ask Slide
- **Purpose:** States the recommendation, ask, or next steps.
- **Layout:** Clear statement of what the audience should do. Supporting context minimal.
- **Branding:** Can use primary color background for emphasis (inverted text).

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
- **Wall of text.** Any slide with more than 6 bullet points or more than 30 words of body text is a document, not a slide. Move the detail to speaker notes.
