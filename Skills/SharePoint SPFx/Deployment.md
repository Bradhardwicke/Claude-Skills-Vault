---
name: spfx-deployment
skill-id: "spfx:deployment"
plugin: ""
category: SharePoint SPFx
tags: [skill, spfx, sharepoint, deployment]
aliases: ["SPFx Deploy", "SPFx App Catalog", "sppkg", "SPFx Package"]
triggers:
  - SPFx deployment
  - deploy SPFx solution
  - SPFx app catalog
  - sppkg
  - package SPFx
  - tenant wide deployment SPFx
  - site collection app catalog
  - SPFx skip feature deployment
  - upload sppkg
  - SPFx production build
  - SPFx CDN deployment
  - package-solution.json
  - skipFeatureDeployment
  - SPFx Azure CDN
---

# SPFx Deployment

## Build for Production

```bash
gulp bundle --ship
gulp package-solution --ship
```

Output: `sharepoint/solution/{solution-name}.sppkg`

## Deploy to App Catalog

### Manual (SharePoint Admin Centre)

1. Go to SharePoint Admin Centre > More features > Apps > App Catalog
2. Upload `.sppkg` to **Apps for SharePoint** library
3. Choose: **Tenant-wide** (deploy to all sites) or **manual** (add to individual sites)

### CLI for Microsoft 365

```bash
# Add to tenant app catalog
m365 spo app add --filePath ./sharepoint/solution/my-solution.sppkg --overwrite

# Deploy (make available)
m365 spo app deploy --name my-solution-client-side-solution

# Add to specific site
m365 spo app install --id <app-id> --siteUrl https://contoso.sharepoint.com/sites/mysite
```

### PnP PowerShell

```powershell
Connect-PnPOnline -Url https://contoso-admin.sharepoint.com -Interactive

# Publish to tenant app catalog
Add-PnPApp -Path ./sharepoint/solution/my-solution.sppkg -Scope Tenant -Overwrite
Publish-PnPApp -Identity <app-id> -Scope Tenant

# Approve Graph/API permissions after deploy
Get-PnPTenantServicePrincipalPermissionRequests | Approve-PnPTenantServicePrincipalPermissionRequest
```

## Tenant-Wide vs Site-Collection Deployment

| | Tenant App Catalog | Site Collection App Catalog |
|---|---|---|
| Scope | All sites in tenant | One site collection |
| Admin required | SharePoint Admin | Site Owner |
| Tenant-wide activation | Yes (with `skipFeatureDeployment`) | No |
| Use case | Organisation-wide solutions | Team/project-specific solutions |

### Enable Tenant-Wide Activation

In `config/package-solution.json`:

```json
{
  "solution": {
    "skipFeatureDeployment": true,
    ...
  }
}
```

When uploading, check "Make this solution available to all sites in the organisation".

## package-solution.json Key Settings

```json
{
  "solution": {
    "name": "my-solution-client-side-solution",
    "id": "guid",
    "version": "1.2.0.0",
    "includeClientSideAssets": true,
    "skipFeatureDeployment": false,
    "isDomainIsolated": false,
    "developer": {
      "name": "Contoso",
      "websiteUrl": "https://contoso.com"
    },
    "webApiPermissionRequests": [],
    "features": [{
      "title": "My Solution Feature",
      "description": "...",
      "id": "guid",
      "version": "1.0.0.0",
      "componentIds": ["web-part-guid"]
    }]
  }
}
```

`includeClientSideAssets: true` bundles all JS/CSS into the `.sppkg` file (no external CDN needed). This is the default and recommended for most solutions.

## External CDN Option (Azure Storage)

For large solutions where asset caching matters:

```bash
# config/deploy-azure-storage.json
{
  "workingDir": "temp/deploy/",
  "account": "my-storage-account",
  "container": "my-spfx-container",
  "accessKey": "env:AZURE_STORAGE_KEY"
}

gulp deploy-azure-storage
```

Set `includeClientSideAssets: false` and configure CDN URL in `config/write-manifests.json`.

## Version Bump

Update both `package.json` version AND `config/package-solution.json` version before repackaging.

## Verifying Deployment

```bash
m365 spo app list --appCatalogUrl https://contoso.sharepoint.com/sites/appcatalog
m365 spo app get --name my-solution-client-side-solution
```
