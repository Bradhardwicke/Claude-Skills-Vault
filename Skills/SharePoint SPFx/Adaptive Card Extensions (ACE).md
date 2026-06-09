---
name: spfx-ace-viva-connections
skill-id: "spfx:ace"
plugin: ""
category: SharePoint SPFx
tags: [skill, spfx, sharepoint, ace, viva-connections]
aliases: ["SPFx ACE", "Adaptive Card Extension", "Viva Connections SPFx", "Viva Dashboard"]
triggers:
  - SPFx ACE
  - adaptive card extension
  - Viva Connections SPFx
  - Viva dashboard card
  - BaseAdaptiveCardExtension
  - card view SPFx
  - quick view SPFx
  - Viva Connections extensibility
  - SPFx Viva card
  - ACE state management
  - build ACE
  - ACE template card view
  - mediumCard ACE
  - largeCard ACE
---

# SPFx Adaptive Card Extensions (ACE) — Viva Connections

ACEs are SPFx components that render as cards on the Viva Connections dashboard and SharePoint pages. They use Adaptive Card JSON for UI (no React/HTML).

## Project Scaffolding

```bash
yo @microsoft/sharepoint
# Select: Adaptive Card Extension
# Template: Generic Card Template (or Primary Text, Image, etc.)
```

## Core Architecture

```
src/adaptiveCardExtensions/{name}/
├── {Name}AdaptiveCardExtension.ts    ← main class
├── cardView/
│   └── CardView.ts                   ← card face (dashboard)
├── quickView/
│   └── QuickView.ts                  ← expanded panel
└── {Name}AdaptiveCardExtension.manifest.json
```

## Main Extension Class

```typescript
import {
  BaseAdaptiveCardExtension,
  RenderType
} from '@microsoft/sp-adaptive-card-extension-base';

export interface IMyAceState {
  title: string;
  itemCount: number;
}

export default class MyAce
  extends BaseAdaptiveCardExtension<IMyAceProperties, IMyAceState> {

  public async onInit(): Promise<void> {
    this.state = {
      title: this.properties.title,
      itemCount: 0
    };

    // Register views
    this.cardNavigator.register(CARD_VIEW_REGISTRY_ID, () => new CardView());
    this.quickViewNavigator.register(QUICK_VIEW_REGISTRY_ID, () => new QuickView());

    // Fetch data
    await this._fetchData();
  }

  protected renderType(): RenderType {
    return RenderType.QuickView;
  }

  private async _fetchData(): Promise<void> {
    const sp = getSP(this.context);
    const items = await sp.web.lists.getByTitle('Tasks').items.top(5)();
    this.setState({ itemCount: items.length });
  }
}
```

## Card View

```typescript
import {
  BaseBasicCardView,
  IBasicCardParameters,
  IExternalLinkCardAction,
  IQuickViewCardAction
} from '@microsoft/sp-adaptive-card-extension-base';

export class CardView extends BaseBasicCardView<IMyAceProperties, IMyAceState> {
  public get data(): IBasicCardParameters {
    return {
      primaryText: `${this.state.itemCount} tasks pending`,
      title: this.properties.title,
      iconProperty: 'BullseyeTarget'
    };
  }

  public get onCardSelection(): IQuickViewCardAction | IExternalLinkCardAction {
    return {
      type: 'QuickView',
      parameters: { view: QUICK_VIEW_REGISTRY_ID }
    };
  }
}
```

## Quick View

```typescript
import { BaseAdaptiveCardView, IActionArguments } from '@microsoft/sp-adaptive-card-extension-base';

export class QuickView extends BaseAdaptiveCardView<IMyAceProperties, IMyAceState, IQuickViewData> {
  public get data(): IQuickViewData {
    return {
      title: this.state.title,
      itemCount: this.state.itemCount
    };
  }

  public get template(): ISPFxAdaptiveCard {
    return require('./template/QuickViewTemplate.json');
  }

  public async onAction(action: IActionArguments): Promise<void> {
    if (action.type === 'Submit') {
      if (action.id === 'refresh') {
        await this.context.sdks.microsoftTeams?.app.openLink('https://...');
      }
    }
  }
}
```

## Quick View Template (JSON — `template/QuickViewTemplate.json`)

```json
{
  "schema": "http://adaptivecards.io/schemas/adaptive-card.json",
  "type": "AdaptiveCard",
  "version": "1.5",
  "body": [
    {
      "type": "TextBlock",
      "text": "${title}",
      "weight": "Bolder",
      "size": "Large"
    },
    {
      "type": "TextBlock",
      "text": "${itemCount} items found"
    }
  ],
  "actions": [
    {
      "type": "Action.Submit",
      "id": "refresh",
      "title": "Refresh"
    }
  ]
}
```

## Card View Templates

| Template Base Class | Card Type | Size |
|---|---|---|
| `BaseBasicCardView` | Primary text + icon | Small |
| `BasePrimaryTextCardView` | Headline + description | Small/Medium |
| `BaseImageCardView` | Image + text | Medium |
| `BaseTextInputCardView` | Text input + button | Medium |
| `BaseSearchCardView` | Search box | Large |

## State Updates

```typescript
// Partial state update (triggers re-render)
this.setState({ itemCount: 42 });
```

## ACE Manifest Settings

```json
{
  "requiresCustomScript": false,
  "supportedHosts": ["Dashboard"],
  "preconfiguredEntries": [{
    "title": { "default": "My Card" },
    "description": { "default": "Shows task count" },
    "cardSize": "Medium",
    "properties": {
      "title": "Task Overview"
    }
  }]
}
```

## Deployment

ACEs are packaged in `.sppkg` like web parts. After deployment to the tenant app catalog, editors add them to the Viva Connections dashboard or to SharePoint pages that support ACEs.
