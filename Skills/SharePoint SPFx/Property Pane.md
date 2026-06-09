---
name: spfx-property-pane
skill-id: "spfx:property-pane"
plugin: ""
category: SharePoint SPFx
tags: [skill, spfx, sharepoint, property-pane]
aliases: ["SPFx Property Pane", "Web Part Properties", "SPFx Settings Panel"]
triggers:
  - SPFx property pane
  - web part property pane
  - getPropertyPaneConfiguration
  - PropertyPaneTextField
  - PropertyPaneDropdown
  - PropertyPaneToggle
  - PropertyPaneSlider
  - PropertyPaneCheckbox
  - reactive vs non-reactive property pane
  - dynamic property pane
  - property pane field types
  - custom property pane field
  - PropertyPaneChoiceGroup
  - disableReactivePropertyChanges
---

# SPFx Property Pane Configuration

## Scaffold

Override `getPropertyPaneConfiguration()` in `BaseClientSideWebPart`:

```typescript
import {
  IPropertyPaneConfiguration,
  PropertyPaneTextField,
  PropertyPaneDropdown,
  PropertyPaneToggle,
  PropertyPaneSlider,
  PropertyPaneCheckbox,
  PropertyPaneChoiceGroup,
  PropertyPaneLink,
  PropertyPaneLabel,
  PropertyPaneHorizontalRule
} from '@microsoft/sp-property-pane';

protected getPropertyPaneConfiguration(): IPropertyPaneConfiguration {
  return {
    pages: [
      {
        header: { description: strings.PropertyPaneDescription },
        groups: [
          {
            groupName: strings.BasicGroupName,
            groupFields: [
              PropertyPaneTextField('title', {
                label: 'Title',
                placeholder: 'Enter a title',
                description: 'Displayed at the top of the web part',
                multiline: false,
                maxLength: 100
              }),
              PropertyPaneDropdown('listName', {
                label: 'Source List',
                options: this._listOptions,    // loaded async in onInit
                disabled: !this._listOptions.length
              }),
              PropertyPaneToggle('showDescription', {
                label: 'Show description',
                onText: 'Yes',
                offText: 'No'
              }),
              PropertyPaneSlider('itemCount', {
                label: 'Number of items',
                min: 1,
                max: 20,
                step: 1,
                showValue: true
              }),
              PropertyPaneChoiceGroup('layout', {
                label: 'Layout',
                options: [
                  { key: 'list', text: 'List', iconProps: { officeFabricIconFontName: 'List' } },
                  { key: 'grid', text: 'Grid', iconProps: { officeFabricIconFontName: 'GridViewMedium' } }
                ]
              })
            ]
          }
        ]
      }
    ]
  };
}
```

## Reactive vs Non-Reactive

**Reactive (default):** web part re-renders instantly as user types/selects.

**Non-reactive:** web part only updates when user clicks Apply.

```typescript
protected get disableReactivePropertyChanges(): boolean {
  return true;   // non-reactive
}
```

Use non-reactive when property changes trigger expensive API calls.

## Dynamic Pane (fields depend on other properties)

```typescript
protected onPropertyPaneFieldChanged(propertyPath: string, oldValue: any, newValue: any): void {
  if (propertyPath === 'listName' && newValue !== oldValue) {
    // Load columns for the newly selected list
    this._loadListColumns(newValue).then(() => {
      this.context.propertyPane.refresh();   // force pane re-render
    });
  }
}
```

## Loading Async Data for Dropdown Options

```typescript
private _listOptions: IDropdownOption[] = [];

protected async onInit(): Promise<void> {
  await super.onInit();
  const sp = getSP(this.context);
  const lists = await sp.web.lists.filter('Hidden eq false').select('Title')();
  this._listOptions = lists.map(l => ({ key: l.Title, text: l.Title }));
}
```

## Multi-Page Property Pane

```typescript
return {
  pages: [
    {
      header: { description: 'Data Settings' },
      groups: [{ groupFields: [/* data fields */] }]
    },
    {
      header: { description: 'Display Settings' },
      groups: [{ groupFields: [/* display fields */] }]
    }
  ]
};
```

## Custom Property Pane Field

For complex controls not covered by built-in fields, implement `IPropertyPaneField<TProps>`:

```typescript
import { IPropertyPaneField, PropertyPaneFieldType } from '@microsoft/sp-property-pane';

// Use PropertyPaneCustomField for quick inline custom fields:
import { PropertyPaneCustomField } from '@microsoft/sp-property-pane';

PropertyPaneCustomField({
  key: 'myCustomField',
  onRender: (elem: HTMLElement) => {
    ReactDom.render(<MyCustomControl onChange={...} />, elem);
  },
  onDispose: (elem: HTMLElement) => {
    ReactDom.unmountComponentAtNode(elem);
  }
})
```

## Localisation

Property pane strings go in `src/webparts/{name}/loc/en-us.js` and the interface in `mystrings.d.ts`. Reference with `strings.MyKey` after importing `* as strings from 'MyWebPartStrings'`.
