---
name: spfx-extensions
skill-id: "spfx:extensions"
plugin: ""
category: SharePoint SPFx
tags: [skill, spfx, sharepoint, extensions]
aliases: ["SPFx Extension", "Application Customizer", "Field Customizer", "Command Set", "Form Customizer"]
triggers:
  - SPFx extension
  - application customizer
  - field customizer
  - list view command set
  - form customizer
  - SPFx header footer
  - custom header SharePoint
  - custom footer SharePoint
  - toolbar command SharePoint
  - SharePoint list column render
  - BaseApplicationCustomizer
  - BaseFieldCustomizer
  - BaseListViewCommandSet
  - PlaceholderName.Top
  - PlaceholderName.Bottom
---

# SPFx Extensions

Four extension types for customising SharePoint UX beyond the web part canvas.

## 1. Application Customizer

Inject HTML into page header or footer placeholders. Runs on every page.

```typescript
import { BaseApplicationCustomizer, PlaceholderName } from '@microsoft/sp-application-base';

export default class HeaderFooterApplicationCustomizer
  extends BaseApplicationCustomizer<IHeaderFooterApplicationCustomizerProperties> {

  private _topPlaceholder: Placeholder | undefined;

  public onInit(): Promise<void> {
    this.context.placeholderProvider.changedEvent.add(this, this._renderPlaceholders);
    this._renderPlaceholders();
    return Promise.resolve();
  }

  private _renderPlaceholders(): void {
    if (!this._topPlaceholder) {
      this._topPlaceholder = this.context.placeholderProvider.tryCreateContent(
        PlaceholderName.Top,
        { onDispose: this._onDispose }
      );
    }
    if (this._topPlaceholder?.domElement) {
      this._topPlaceholder.domElement.innerHTML = `<div class="app-customizer-header">Hello</div>`;
    }
  }

  private _onDispose(): void {
    console.log('Disposed top placeholder');
  }
}
```

Deploy via tenant app catalog with `skipFeatureDeployment: true` for tenant-wide activation.

## 2. Field Customizer

Override how a list column renders. Replaces default field output with custom HTML/React.

```typescript
import { BaseFieldCustomizer, IFieldCustomizerCellEventParameters } from '@microsoft/sp-listview-extensibility';

export default class ColorFieldCustomizer
  extends BaseFieldCustomizer<IColorFieldCustomizerProperties> {

  public onRenderCell(event: IFieldCustomizerCellEventParameters): void {
    const value: string = event.fieldValue;
    event.domElement.innerHTML = `<div style="background:${value};width:20px;height:20px;"></div>`;
  }

  public onDisposeCell(event: IFieldCustomizerCellEventParameters): void {
    // clean up if needed
  }
}
```

Associate with a list column via `ClientSideComponentId` in the site column definition.

## 3. List View Command Set

Add custom buttons to list toolbar or item context menu.

```typescript
import {
  BaseListViewCommandSet,
  Command,
  IListViewCommandSetExecuteEventParameters,
  ListViewStateChangedEventArgs
} from '@microsoft/sp-listview-extensibility';

export default class MyCommandSet
  extends BaseListViewCommandSet<IMyCommandSetProperties> {

  public onInit(): Promise<void> {
    this.context.listView.listViewStateChangedEvent.add(this, this._onListViewStateChanged);
    return Promise.resolve();
  }

  private _onListViewStateChanged(args: ListViewStateChangedEventArgs): void {
    const compareOneCommand: Command = this.tryGetCommand('COMMAND_1');
    if (compareOneCommand) {
      // Show only when exactly one item is selected
      compareOneCommand.visible = this.context.listView.selectedRows?.length === 1;
    }
    this.raiseOnChange();
  }

  public onExecute(event: IListViewCommandSetExecuteEventParameters): void {
    switch (event.itemId) {
      case 'COMMAND_1':
        const row = event.selectedRows[0];
        alert(`Item: ${row.getValueByName('Title')}`);
        break;
    }
  }
}
```

## 4. Form Customizer (SPFx 1.15+)

Replace the default new/edit/display forms for a list with a custom React form.

```typescript
import { BaseFormCustomizer } from '@microsoft/sp-listview-extensibility';

export default class MyFormCustomizer
  extends BaseFormCustomizer<IMyFormCustomizerProperties> {

  public render(): void {
    ReactDom.render(
      React.createElement(MyForm, {
        context: this.context,
        item: this.context.item,        // existing item (edit/display)
        onSave: this._onSave,
        onClose: this._onClose
      }),
      this.domElement
    );
  }

  private _onSave = async (): Promise<void> => {
    await this.formSaved();
  }

  private _onClose = (): void => {
    this.formClosed();
  }
}
```

## Deployment

Extensions are registered on lists/sites via:
- CSOM/REST to set `ClientSideComponentId` and `ClientSideComponentProperties` on UserCustomActions
- PowerShell (PnP PowerShell): `Add-PnPCustomAction`
- CLI for Microsoft 365: `m365 spo customaction add`

Application customizers can be deployed tenant-wide via tenant-scoped feature.
