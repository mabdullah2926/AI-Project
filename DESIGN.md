---
name: Autonomous Operations System
colors:
  surface: '#faf8ff'
  surface-dim: '#d2d9f4'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3ff'
  surface-container: '#eaedff'
  surface-container-high: '#e2e7ff'
  surface-container-highest: '#dae2fd'
  on-surface: '#131b2e'
  on-surface-variant: '#464554'
  inverse-surface: '#283044'
  inverse-on-surface: '#eef0ff'
  outline: '#767586'
  outline-variant: '#c7c4d7'
  surface-tint: '#494bd6'
  primary: '#4648d4'
  on-primary: '#ffffff'
  primary-container: '#6063ee'
  on-primary-container: '#fffbff'
  inverse-primary: '#c0c1ff'
  secondary: '#006c49'
  on-secondary: '#ffffff'
  secondary-container: '#6cf8bb'
  on-secondary-container: '#00714d'
  tertiary: '#196094'
  on-tertiary: '#ffffff'
  tertiary-container: '#3a79ae'
  on-tertiary-container: '#fdfcff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c0c1ff'
  on-primary-fixed: '#07006c'
  on-primary-fixed-variant: '#2f2ebe'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#cfe5ff'
  tertiary-fixed-dim: '#98cbff'
  on-tertiary-fixed: '#001d33'
  on-tertiary-fixed-variant: '#004a77'
  background: '#faf8ff'
  on-background: '#131b2e'
  surface-variant: '#dae2fd'
  surface-main: '#F9FAFB'
  sidebar-bg: '#0F172A'
  danger: '#EF4444'
  warning: '#F59E0B'
  border-subtle: '#E2E8F0'
  text-secondary: '#64748B'
  ai-purple: '#8B5CF6'
  fraud-coral: '#FF6B6B'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-mono:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 16px
  table-header:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  gutter: 24px
  margin-mobile: 16px
  sidebar-width: 260px
  container-max: 1440px
---

## Brand & Style

The design system is engineered for high-stakes e-commerce logistics, where AI-driven decision-making meets human oversight. The brand personality is **Technical, Reliable, and Transparent**, moving away from "Black Box" AI toward a "Glass Box" experience where every automated decision is auditable and clear.

The chosen style is **Corporate / Modern**, leaning heavily into a high-density, professional SaaS aesthetic. It prioritizes information hierarchy and functional clarity, utilizing a structured layout that balances data-rich tables with clear, actionable status indicators. The visual tone is authoritative yet accessible, designed to instill confidence in automated workflows.

## Colors

The palette is anchored by a deep **Slate-900 (Indigo-tinted)** for structural navigation, providing a grounded, professional frame for the content. The primary **Indigo (#6366F1)** is used for interactive states and primary focus, while **Success Green** and **Danger Red** provide immediate semantic feedback for return approvals and fraud alerts.

Backgrounds utilize a clean **Zinc-50 (#F9FAFB)** to maximize legibility and reduce eye strain during long-form data analysis. Accent colors, derived from the technical stack (Python Blue, CrewAI Coral), are reserved for metadata badges and agent-specific identifiers to maintain a clear "Audit Trail" visual language.

## Typography

The system utilizes **Inter** for all UI elements to ensure maximum legibility across dense data sets. **JetBrains Mono** is introduced specifically for technical identifiers—such as Order IDs, UUIDs, and SKUs—to differentiate raw data from UI labels.

Typography follows a strict rhythmic scale. Display styles use tighter letter spacing and heavier weights for immediate impact in dashboard summaries. Table headers are set in uppercase with increased tracking to create clear separation between the data grid and the metadata labels.

## Layout & Spacing

This design system uses a **fixed-fluid hybrid grid**. The sidebar remains at a fixed width of 260px to maintain navigation consistency, while the main content area utilizes a 12-column fluid grid that scales up to a 1440px max-width.

Spacing follows a **4px base unit** (0.25rem). Gutters are set to 24px on desktop to allow data-heavy cards to "breathe," while mobile views collapse margins to 16px. Information density is managed through specific "Context Gaps"—larger vertical spacing (32px+) is used between distinct logical blocks (e.g., between a Chart summary and a Data Table).

## Elevation & Depth

Hierarchy is established through **Tonal Layers** rather than heavy shadows. The main surface is the lowest layer, with cards sitting slightly "above" using a subtle 1px border and a soft, diffused ambient shadow (4px blur, 5% opacity).

High-priority elements, such as active modals or dropdown menus, use a more pronounced shadow to create distinct separation. For AI-generated reasoning blocks, a **subtle tint (Indigo-50)** is used as a background fill to signify "Machine Generated" content, distinguishing it from user-inputted data.

## Shapes

The design system employs **Rounded (0.5rem)** corners for the majority of UI components, including cards, input fields, and primary buttons. This provides a modern, approachable feel that offsets the technical density of the data.

Status badges and tags utilize a **Pill-shape** to distinguish them from interactive buttons. Internal elements like checkboxes or small utility icons use a tighter 4px radius to maintain a precise, technical appearance.

## Components

### Buttons & Inputs
Buttons use solid fills for primary actions and 1px borders with transparent backgrounds for secondary actions. Input fields feature a `Slate-200` border that shifts to `Indigo-600` on focus, paired with a subtle inner shadow to imply depth.

### Status Badges
Badges are critical for the "at-a-glance" experience. They use a "Soft Background" approach: a low-opacity version of the semantic color (e.g., 10% Green) with high-contrast text. 

### Data Tables
Tables are the core of the optimizer. They feature `sticky` headers, `Slate-50` zebra-striping for readability, and clear vertical alignment. "Risk Tiers" within tables are highlighted using localized background tints.

### Cards
Dashboard cards are the primary container. Each card must have a clear title, an optional icon/emoji for agent identification, and a footer area for "Audit" timestamps or metadata.

### AI Reasoning Blocks
A custom component used to display LLM output. It features a left-hand accent border (`Indigo-400`) and uses the `body-sm` typography to handle longer strings of explanatory text without breaking the dashboard layout.