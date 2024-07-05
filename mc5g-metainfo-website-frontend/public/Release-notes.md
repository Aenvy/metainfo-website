## Release 1.2

* Obtain releases correctly and sort them by prioritizing lastest tags over ealiest

## Release 1.1

* Release Page improvements: RC/Release filter is added for the main view of the release page, with only releases displayed by default. Side Panel also only shows releases. 
* Release notes added with this release and navigation to releases notes page is facilated through a button in the footer, available on every page.

## Release 1.0

### Initial Release

* Accessibility: Solutions, products, components, and releases are conveniently accessible directly from the homepage, presented in a dashboard-like format. Moreover, navigation to these sections is facilitated through dedicated buttons in the header, available on every page.
* Solution Level: Detailed information such as test campaigns (if available), build dependencies, runtime dependencies, and historical data are provided. Additionally, associated products and components can be easily accessed via the sidebar.
* Product Level: Offers comprehensive deliverables, component packages available as downloadable links, and a deeper historical overview.
* Release Level: Provides access to releases, a functionality absent in the V1 version. Still a work in progress, will have more features like displaying common components and many more changes in the future.
* Bug reports and/or feature ideas can be reported through a dedicated workflow in #ask-siths slack channel whose link is provided as a footer on every page.
* Login is facilitated through GitHub authentication. Permissions are using GitHub groups for RBAC. 
* Detect and show discrepancies: Can detect and show discrepancies in the common components in the solutions and products page. Future improvements include the implementation of a dependency check on the release page, with the ability to pinpoint which product isn't aligned.
