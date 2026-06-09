---
name: spfx-microsoft-graph
skill-id: "spfx:graph"
plugin: ""
category: SharePoint SPFx
tags: [skill, spfx, sharepoint, microsoft-graph]
aliases: ["SPFx Graph", "MSGraphClient SPFx", "Graph API SPFx", "MSGraphClientV3"]
triggers:
  - SPFx Microsoft Graph
  - MSGraphClientV3
  - msGraphClientFactory
  - Graph API web part
  - call Graph from SPFx
  - SPFx user profile Graph
  - SPFx Graph permissions
  - webApiPermissionRequests
  - SPFx Teams data Graph
  - SPFx sites drives Graph
  - "@microsoft/sp-http Graph"
  - graphFI PnPjs
---

# Microsoft Graph Integration from SPFx

## MSGraphClientV3 (built-in, recommended)

SPFx 1.15+ requires Graph SDK v3. The client is obtained from `this.context.msGraphClientFactory`.

### Basic Usage

```typescript
import { MSGraphClientV3 } from '@microsoft/sp-http';

// In render() or a service method:
const client: MSGraphClientV3 = await this.context.msGraphClientFactory.getClient('3');

// Get current user
const me = await client.api('/me').get();

// Get user's direct reports
const reports = await client.api('/me/directReports').select('displayName,jobTitle,mail').get();

// Get SharePoint sites
const sites = await client.api('/sites').search('contoso').get();

// Get files from OneDrive
const files = await client.api('/me/drive/root/children').get();

// Post — create Teams channel message
await client.api('/teams/{team-id}/channels/{channel-id}/messages')
  .post({ body: { content: 'Hello from SPFx' } });
```

### Using with React Hooks

```typescript
const [user, setUser] = useState<any>(null);

useEffect(() => {
  props.context.msGraphClientFactory
    .getClient('3')
    .then((client: MSGraphClientV3) => {
      return client.api('/me').select('displayName,mail,jobTitle').get();
    })
    .then(setUser);
}, []);
```

## Request Permissions in package-solution.json

Graph API calls require pre-approved scopes. Declare them in `config/package-solution.json`:

```json
{
  "solution": {
    "webApiPermissionRequests": [
      { "resource": "Microsoft Graph", "scope": "User.Read" },
      { "resource": "Microsoft Graph", "scope": "People.Read" },
      { "resource": "Microsoft Graph", "scope": "Sites.Read.All" },
      { "resource": "Microsoft Graph", "scope": "Mail.Read" },
      { "resource": "Microsoft Graph", "scope": "Calendars.Read" },
      { "resource": "Microsoft Graph", "scope": "TeamMember.Read.All" }
    ]
  }
}
```

A SharePoint admin must **approve** these permissions in the SharePoint Admin Centre under API access, or via PowerShell:

```powershell
Approve-SPOTenantServicePrincipalPermissionRequest -RequestId <guid>
```

## PnPjs Graph (graphFI)

For a fluent API over Graph in SPFx 1.18+:

```typescript
import { graphfi, GraphFI, SPFx as GraphSPFx } from '@pnp/graph';
import '@pnp/graph/users';
import '@pnp/graph/groups';
import '@pnp/graph/sites';

let _graph: GraphFI;

export const getGraph = (context?: WebPartContext): GraphFI => {
  if (context) {
    _graph = graphfi().using(GraphSPFx(context));
  }
  return _graph;
};

// Usage
const graph = getGraph();
const me = await graph.me();
const myGroups = await graph.me.memberOf();
const users = await graph.users.filter("startsWith(displayName,'Brad')")();
```

**Note:** When using both `@pnp/sp` and `@pnp/graph` in the same project, both export a `SPFx` named export. Alias one:

```typescript
import { SPFx as GraphSPFx } from '@pnp/graph';
import { SPFx as SpSPFx } from '@pnp/sp';
```

## AadHttpClient (third-party APIs)

For calling Azure AD-secured APIs other than Graph:

```typescript
import { AadHttpClient } from '@microsoft/sp-http';

const client = await this.context.aadHttpClientFactory.getClient('https://myapi.contoso.com');
const response = await client.get('https://myapi.contoso.com/api/data', AadHttpClient.configurations.v1);
const data = await response.json();
```

Declare in `webApiPermissionRequests`:
```json
{ "resource": "https://myapi.contoso.com", "scope": "user_impersonation" }
```

## Common Graph Endpoints for SharePoint Scenarios

| Scenario | Endpoint |
|---|---|
| Current user | `GET /me` |
| User profile photo | `GET /me/photo/$value` |
| User's manager | `GET /me/manager` |
| Team members | `GET /groups/{id}/members` |
| Site pages | `GET /sites/{site-id}/pages` |
| Search | `POST /search/query` |
| Planner tasks | `GET /me/planner/tasks` |
