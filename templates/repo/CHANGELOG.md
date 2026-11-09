# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), and this project follows [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

If you use release-please, it writes new entries at the top of this file from Conventional Commits. Edit the release pull request so each entry makes sense to a user. Before your first release, delete the Unreleased section and the link list at the bottom of this file: release-please writes its own headings with compare links and never updates them.

## [Unreleased]

### Added

- Short description of new behaviour, written for users.

## [1.1.0] - 2026-01-15

### Added

- CSV export for invoices.

### Changed

- Search results load 20 items per page instead of 50.

### Deprecated

- The `/v1/orders` endpoint. Use `/v2/orders`. Removal planned for 2.0.0, not before 2026-07-15.

### Fixed

- Expired refresh tokens are now rejected.

### Security

- Updated the XML parser to fix CVE-YYYY-NNNNN (affected versions 1.0.0 to 1.0.3).

## [1.0.0] - 2025-11-03

### Added

- First stable release.

[Unreleased]: https://example.com/your-org/PROJECT_NAME/compare/v1.1.0...HEAD
[1.1.0]: https://example.com/your-org/PROJECT_NAME/compare/v1.0.0...v1.1.0
[1.0.0]: https://example.com/your-org/PROJECT_NAME/releases/tag/v1.0.0
