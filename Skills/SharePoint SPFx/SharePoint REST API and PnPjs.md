---
name: spfx-rest-pnpjs
skill-id: "spfx:rest-pnpjs"
plugin: ""
category: SharePoint SPFx
tags: [skill, spfx, sharepoint, rest-api, pnpjs]
aliases: ["SPFx PnPjs", "SPFx REST API", "PnP SharePoint", "@pnp/sp", "spHttpClient"]
triggers:
  - SPFx REST API
  - PnPjs SPFx
  - "@pnp/sp"
  - spHttpClient
  - SPHttpClient
  - get SharePoint list items SPFx
  - create list item SPFx
  - update list item SPFx
  - delete list item SPFx
  - SharePoint CRUD SPFx
  - pnp sp setup SPFx
  - getSP SPFx
  - spfi SPFx
  - PnPjs v4 SPFx
---

# SharePoint REST API and PnPjs in SPFx

## Option A: PnPjs (recommended)

PnPjs v4 requires SPFx 1.18+ and Node 18+. It wraps the SharePoint REST API with a fluent, chainable interface.

### Setup — initialise once in `onInit()`

```typescript
import { spfi, SPFI, SPFx } from '@pnp/sp';
import '@pnp/sp/webs';
import '@pnp/sp/lists';
import '@pnp/sp/items';
import '@pnp/sp/files';
import '@pnp/sp/folders';

// Create a module-level singleton
let _sp: SPFI;

export const getSP = (context?: WebPartContext): SPFI => {
  if (context) {
    _sp = spfi().using(SPFx(context));
  }
  return _sp;
};

// In web part onInit():
protected async onInit(): Promise<void> {
  getSP(this.context);
  return super.onInit();
}
```

### CRUD Operations

```typescript
const sp = getSP();

// Get all items
const items = await sp.web.lists.getByTitle('My List').items();

// Get with OData
const items = await sp.web.lists.getByTitle('Tasks')
  .items
  .select('Title', 'Status', 'AssignedTo/Title')
  .expand('AssignedTo')
  .filter("Status eq 'Active'")
  .orderBy('Title')
  .top(50)();

// Create item
const result = await sp.web.lists.getByTitle('My List').items.add({
  Title: 'New Item',
  Status: 'Active'
});

// Update item
await sp.web.lists.getByTitle('My List').items.getById(42).update({
  Title: 'Updated'
});

// Delete item
await sp.web.lists.getByTitle('My List').items.getById(42).delete();

// Get single item
const item = await sp.web.lists.getByTitle('My List').items.getById(42)();
```

### Files and Folders

```typescript
// Upload file
const fileResult = await sp.web.getFolderByServerRelativePath('/sites/mysite/Shared Documents')
  .files.addUsingPath('filename.txt', fileContent, { Overwrite: true });

// Get file content
const content = await sp.web.getFileByServerRelativePath('/sites/mysite/Shared Documents/file.txt')
  .getText();
```

### Batching

```typescript
import { createBatch } from '@pnp/sp';

const [batchedSP, execute] = sp.batched();

const p1 = batchedSP.web.lists.getByTitle('List1').items();
const p2 = batchedSP.web.lists.getByTitle('List2').items();

await execute();
const [items1, items2] = await Promise.all([p1, p2]);
```

## Option B: spHttpClient (raw REST)

Use when PnPjs is not available or for unsupported API endpoints.

```typescript
import { SPHttpClient, SPHttpClientResponse } from '@microsoft/sp-http';

// GET
const response: SPHttpClientResponse = await this.context.spHttpClient.get(
  `${this.context.pageContext.web.absoluteUrl}/_api/web/lists?$select=Title,Id`,
  SPHttpClient.configurations.v1
);
const data = await response.json();
const lists = data.value;

// POST (create item)
await this.context.spHttpClient.post(
  `${this.context.pageContext.web.absoluteUrl}/_api/web/lists/getbytitle('My List')/items`,
  SPHttpClient.configurations.v1,
  {
    headers: {
      'Accept': 'application/json;odata=nometadata',
      'Content-type': 'application/json;odata=nometadata',
      'odata-version': ''
    },
    body: JSON.stringify({ Title: 'New Item' })
  }
);
```

## OData Tips

- `$select` — choose fields to return (reduces payload)
- `$filter` — server-side filter; use `substringof`, `startswith` for text
- `$expand` — expand lookups: `$select=AssignedTo/Title&$expand=AssignedTo`
- `$orderby` — sort: `$orderby=Modified desc`
- `$top` — max items; default 100, max 5000 without paging
- For large lists use `$skiptoken` paging or PnPjs `.getPaged()`
