---
name: spfx-react-fluent-ui
skill-id: "spfx:react-fluent-ui"
plugin: ""
category: SharePoint SPFx
tags: [skill, spfx, sharepoint, react, fluent-ui]
aliases: ["SPFx React", "Fluent UI SPFx", "SPFx Fluent", "Office UI Fabric SPFx"]
triggers:
  - SPFx React
  - Fluent UI SPFx
  - Office UI Fabric SPFx
  - SPFx components Fluent
  - "@fluentui/react SPFx"
  - SPFx Button Stack TextField
  - SharePoint modern UI components
  - React hooks SPFx
  - functional component SPFx
  - SPFx useState useEffect
---

# SPFx with React and Fluent UI

## Library Versions by SPFx Version

| SPFx | React | Fluent UI |
|---|---|---|
| 1.18+ | 17.x | @fluentui/react v8 (default) |
| 1.14–1.17 | 16.x | @fluentui/react v8 |
| < 1.14 | 16.x | office-ui-fabric-react v7 |

**Important:** SPFx bundles React. Do not add React as a dependency — reference the bundled version to avoid duplicate React errors.

## Functional Component with Hooks (recommended)

```typescript
import * as React from 'react';
import { useState, useEffect } from 'react';
import { Stack, Text, PrimaryButton, Spinner, SpinnerSize } from '@fluentui/react';
import { WebPartContext } from '@microsoft/sp-webpart-base';

interface IMyComponentProps {
  title: string;
  context: WebPartContext;
}

const MyComponent: React.FC<IMyComponentProps> = ({ title, context }) => {
  const [items, setItems] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // fetch data on mount
    context.spHttpClient
      .get(`${context.pageContext.web.absoluteUrl}/_api/web/lists`, SPHttpClient.configurations.v1)
      .then(r => r.json())
      .then(data => {
        setItems(data.value.map((l: any) => l.Title));
        setLoading(false);
      });
  }, []);

  if (loading) return <Spinner size={SpinnerSize.large} label="Loading..." />;

  return (
    <Stack tokens={{ childrenGap: 10 }}>
      <Text variant="xLarge">{title}</Text>
      {items.map((item, i) => (
        <Text key={i}>{item}</Text>
      ))}
      <PrimaryButton text="Refresh" onClick={() => setLoading(true)} />
    </Stack>
  );
};

export default MyComponent;
```

## Common Fluent UI v8 Components

| Component | Import | Use for |
|---|---|---|
| `PrimaryButton` / `DefaultButton` | `@fluentui/react` | Actions |
| `TextField` | `@fluentui/react` | Text input |
| `Dropdown` | `@fluentui/react` | Select lists |
| `Toggle` | `@fluentui/react` | Boolean settings |
| `Stack` | `@fluentui/react` | Layout |
| `Text` | `@fluentui/react` | Typography |
| `Spinner` | `@fluentui/react` | Loading state |
| `Dialog` | `@fluentui/react` | Modal dialogs |
| `DetailsList` | `@fluentui/react` | Data tables |
| `Panel` | `@fluentui/react` | Side panels |
| `MessageBar` | `@fluentui/react` | Notifications |

## Theming — Apply SharePoint Theme

```typescript
import { ThemeProvider } from '@fluentui/react';

// In web part render():
const theme = this.context.pageContext.theme;

ReactDom.render(
  <ThemeProvider theme={theme}>
    <MyComponent />
  </ThemeProvider>,
  this.domElement
);
```

## CSS Modules (SPFx default)

```typescript
import styles from './MyWebPart.module.scss';

// Usage
<div className={styles.myWebPart}>
  <div className={styles.container}>
    ...
  </div>
</div>
```

## PnP Reusable Controls

The `@pnp/spfx-controls-react` package provides ready-made SPFx-aware controls:

```bash
npm install @pnp/spfx-controls-react --save
```

Common controls: `PeoplePicker`, `ListView`, `RichText`, `FilePicker`, `Placeholder`, `WebPartTitle`, `TaxonomyPicker`, `DateTimePicker`.

```typescript
import { PeoplePicker, PrincipalType } from '@pnp/spfx-controls-react/lib/PeoplePicker';

<PeoplePicker
  context={this.props.context as any}
  titleText="Select people"
  personSelectionLimit={3}
  principalTypes={[PrincipalType.User]}
  onChange={(items) => console.log(items)}
/>
```
