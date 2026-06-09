---
name: spfx-web-parts
skill-id: "spfx:web-parts"
plugin: ""
category: SharePoint SPFx
tags: [skill, spfx, sharepoint, web-parts]
aliases: ["SPFx Web Part", "Client-Side Web Part", "SPFx Component"]
triggers:
  - SPFx web part
  - client-side web part
  - build web part
  - render React web part
  - web part properties
  - BaseClientSideWebPart
  - web part render method
  - SPFx component
  - web part manifest
  - web part context
  - ReactDOM.render SPFx
  - onPropertyPaneFieldChanged
---

# SPFx Web Parts

## Anatomy of a Web Part

```typescript
import { BaseClientSideWebPart } from '@microsoft/sp-webpart-base';
import * as React from 'react';
import * as ReactDom from 'react-dom';

export interface IMyWebPartProps {
  description: string;
}

export default class MyWebPart extends BaseClientSideWebPart<IMyWebPartProps> {

  public render(): void {
    const element = React.createElement(MyComponent, {
      description: this.properties.description,
      context: this.context
    });
    ReactDom.render(element, this.domElement);
  }

  protected onDispose(): void {
    ReactDom.unmountComponentAtNode(this.domElement);
  }

  protected getPropertyPaneConfiguration(): IPropertyPaneConfiguration {
    return {
      pages: [{
        groups: [{
          groupFields: [
            PropertyPaneTextField('description', { label: 'Description' })
          ]
        }]
      }]
    };
  }
}
```

## Key Lifecycle Methods

| Method | When to Override |
|---|---|
| `render()` | Required — draws the component |
| `onInit()` | Async setup (PnPjs, Graph, services) — return `super.onInit()` |
| `onDispose()` | Unmount React tree, clean up timers |
| `onPropertyPaneFieldChanged()` | React to property changes |
| `onPropertyPaneConfigurationComplete()` | After pane closes |
| `getPropertyPaneConfiguration()` | Define pane fields |

## Web Part Manifest (`{name}.manifest.json`)

Key fields:

```json
{
  "id": "guid",
  "alias": "MyWebPart",
  "componentType": "WebPart",
  "version": "0.0.1",
  "requiresCustomScript": false,
  "supportedHosts": ["SharePointWebPart", "TeamsTab", "TeamsPersonalApp"]
}
```

`supportedHosts` controls where the web part can run: SharePoint pages, Teams tabs, Teams personal apps, Outlook, Office.com.

## Accessing Context

```typescript
// Web URL
this.context.pageContext.web.absoluteUrl

// Current user
this.context.pageContext.user.displayName
this.context.pageContext.user.email

// Site ID (for Graph)
this.context.pageContext.site.id

// Theme
this.context.microsoftTeams  // defined if running in Teams
```

## Isolated React Component Pattern

Pass `context` as a prop to child components rather than importing it globally. This keeps components testable and decoupled.

```typescript
interface IMyComponentProps {
  description: string;
  context: WebPartContext;
}
```

## Domain Isolated Web Parts — Deprecated

Domain isolated web parts retire **April 2, 2026**. Migrate to standard web parts using `AadHttpClient` or `MSGraphClientV3` for secure API calls instead.

## Preconfigured Entries

Define default property values for multiple instances in the manifest:

```json
"preconfiguredEntries": [{
  "groupId": "...",
  "group": { "default": "Under Development" },
  "title": { "default": "My Web Part" },
  "properties": {
    "description": "My Web Part"
  }
}]
```
