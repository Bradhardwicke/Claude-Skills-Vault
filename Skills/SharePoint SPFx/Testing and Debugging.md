---
name: spfx-testing-debugging
skill-id: "spfx:testing-debugging"
plugin: ""
category: SharePoint SPFx
tags: [skill, spfx, sharepoint, testing, debugging]
aliases: ["SPFx Testing", "SPFx Debug", "SPFx Workbench", "SPFx Unit Test"]
triggers:
  - SPFx testing
  - SPFx debugging
  - gulp serve SPFx
  - SPFx local workbench
  - SPFx hosted workbench
  - SPFx unit test
  - Jest SPFx
  - SPFx test web part
  - debug SPFx web part
  - SPFx source map
  - SPFx serve.json
  - SPFx browser debug
  - SPFx mock services
  - SPFx console logging
---

# SPFx Testing and Debugging

## Local Development Server

```bash
# Gulp projects
gulp serve                   # starts local workbench at https://localhost:4321
gulp serve --nobrowser       # starts server, does not open browser

# Heft projects (SPFx 1.22+)
heft start
```

**Local workbench** (`https://localhost:4321/temp/workbench.html`): sandboxed, no SharePoint context. Suitable for pure UI development.

**Hosted workbench** (`https://{tenant}.sharepoint.com/_layouts/15/workbench.aspx`): runs in real SharePoint context. Required for testing SharePoint data, Graph, user context.

## serve.json Configuration

```json
{
  "serveConfigurations": {
    "default": {
      "pageUrl": "https://contoso.sharepoint.com/sites/dev/SitePages/TestPage.aspx",
      "customActions": {},
      "fieldCustomizers": {}
    },
    "myExtension": {
      "pageUrl": "https://contoso.sharepoint.com/sites/dev/_layouts/15/workbench.aspx",
      "customActions": {
        "{extension-guid}": {
          "location": "ClientSideExtension.ApplicationCustomizer",
          "properties": {}
        }
      }
    }
  }
}
```

Run a specific config:
```bash
gulp serve --config myExtension
```

## Browser Debugging

1. Run `gulp serve`
2. Open browser DevTools > Sources tab
3. Find source maps under `webpack://` → `src/`
4. Set breakpoints directly in TypeScript source

Source maps are included automatically in debug builds (`--ship` disables them).

## Unit Testing with Jest

SPFx projects include Jest configuration by default (`jest.config.js`).

```bash
npm test              # run all tests
npm test -- --watch   # watch mode
npm test -- --coverage
```

### Mocking SPFx Context

```typescript
// __tests__/MyComponent.test.tsx
import * as React from 'react';
import { render, screen } from '@testing-library/react';
import MyComponent from '../components/MyComponent';

const mockContext = {
  pageContext: {
    web: { absoluteUrl: 'https://contoso.sharepoint.com/sites/test' },
    user: { displayName: 'Test User', email: 'test@contoso.com' }
  },
  spHttpClient: {
    get: jest.fn().mockResolvedValue({
      json: jest.fn().mockResolvedValue({ value: [] })
    })
  }
};

describe('MyComponent', () => {
  it('renders title', () => {
    render(<MyComponent title="Hello" context={mockContext as any} />);
    expect(screen.getByText('Hello')).toBeInTheDocument();
  });
});
```

### Mock Services with ServiceScope

Register mock implementations in tests:

```typescript
const serviceScope = ServiceScope.startNewRoot();
serviceScope.createAndProvide(MyService.serviceKey, MockMyService);
serviceScope.finish();
```

## Dependency Injection for Testability

Wrap data access in a service class registered with `ServiceScope`:

```typescript
import { ServiceKey, ServiceScope } from '@microsoft/sp-core-library';

export interface IDataService {
  getItems(): Promise<IItem[]>;
}

export class DataService implements IDataService {
  public static serviceKey = ServiceKey.create<IDataService>('MyApp:DataService', DataService);

  constructor(private serviceScope: ServiceScope) {}

  public async getItems(): Promise<IItem[]> {
    // real implementation
  }
}

// In web part:
const service = this.context.serviceScope.consume(DataService.serviceKey);
```

## Console Logging Best Practice

```typescript
import { Log } from '@microsoft/sp-core-library';

const LOG_SOURCE = 'MyWebPart';

Log.info(LOG_SOURCE, 'Component rendered');
Log.warn(LOG_SOURCE, 'Deprecated property used');
Log.error(LOG_SOURCE, new Error('Something went wrong'));
```

Logs appear in the browser console and can be filtered by source.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `ERR_CERT_AUTHORITY_INVALID` | Localhost cert not trusted | Run `gulp trust-dev-cert` |
| Web part not appearing in workbench | Manifest error or guid mismatch | Check browser console + manifest |
| 403 on REST calls | Missing permissions or wrong URL | Verify `absoluteUrl` and `_api` path |
| `Cannot read property 'context'` | Context not passed to component | Pass `this.context` as prop |
| Stale bundle in prod | Browser cache | Increment version in `package-solution.json` |
| Graph call returns 401 | Permissions not approved | Approve in SharePoint Admin > API access |
