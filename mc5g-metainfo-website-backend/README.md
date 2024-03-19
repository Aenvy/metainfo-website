# CMS5G metainfo backend

This is an application layer for CMS5G metainfos.

## Environment variables

| Environment variable      | Required  | Description                                                   |
|---------------------------|-----------|---------------------------------------------------------------|
| `APPLICATION_URL`         |           | Public URL endpoint for this backend                          |
| `MONGODB_COLLECTION`      |           | MongoDB database to use                                       |
| `MONGODB_URL`             | ✓         | MongoDB connection URL to the metainfo database              |
| `STATIC_PATH`             |           | Path to the static directory to serve files from              |
| `RBACFILE`                | ✓         | Path to the role-based access control definition file        |
| `JENKINSFILE`             |           | Path to the Jenkins configuration file                        |
| `CERTFILE`                |           | Path to the public server certificate (HTTPS)                 |
| `KEYFILE`                 |           | Path to the private server key (HTTPS)                        |
| `OAUTH2_CLIENT_ID`        |           | OAuth2 client ID for authentication                           |
| `OAUTH2_CLIENT_SECRET`    |           | OAuth2 client secret for authentication                       |
| `OAUTH2_LOGIN_URL`        |           | OAuth2 API endpoint for authentication                        |
| `GITHUB_API_URL`          |           | GitHub API endpoint for user profile/team membership          |
| `SECRET_KEY`              |           | Secret key for encrypting session data                        |
| `METAINFO_MIGRATION_HISTORY_JENKINS_BASE_URL`      |           | URL for migrating metainfo history event jobs without an URL        |
| `METAINFO_MIGRATION_HISTORY_JENKINS_BASE_URL_NHSS` |           | URL for migrating metainfo history event jobs without an URL (NHSS) |

## Authentication and access control

Clients can either authenticate with OAuth2 (if configured), use bearer tokens or use anonymous access.

### OAuth2 authentication

The following environment variables are all required to enable OAuth2 authentication flow:
 * `APPLICATION_URL`
 * `OAUTH2_CLIENT_ID`
 * `OAUTH2_CLIENT_SECRET`
 * `OAUTH2_LOGIN_URL`

OAuth2 is only an authentication handshake, user and group membership are provided by a separate mechanism.

| Source            | Required environment variables    | Group source      |
|-------------------|-----------------------------------|-------------------|
| GitHub            | `GITHUB_API_URL`                  | Team memberships  |

### Bearer tokens

Bearer tokens can be configured in the RBAC definition file. To use a bearer token in a request, use the HTTP header `Authorization: Bearer <...>`.

### Role-based access control definition file

The RBAC definition file contains the security policy of the backend.

| Category          | Description                                           |
|-------------------|-------------------------------------------------------|
| `anonymous`       | Roles that any unauthenticated client has             |
| `authenticated`   | Roles that any authenticated client has               |
| `groups/<...>`    | Roles that any member of a particular group has       |
| `users/<...>`     | Roles that a specific user has                        |
| `bearers/<...>`   | Roles that a specific token has                       |

Role inheritance:
 * Users inherit roles from `authenticated` and every group they are part of.
 * Bearers do not inherit roles from any category.

See [this file](conf/rbac.yaml.sample) for an example.
