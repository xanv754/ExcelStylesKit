# Changelog
All changes to the library.

## [Unreleased]

## [2.0.1] - 2026-07-01
### Changed
- Updated README documentation
- Updated CI configuration
- Fixed repository name in badges

## [2.0.0] - 2026-07-01
### Added
- New `ExcelManager` class for higher-level Excel file management
- Header styles support
- Method to render table in terminal
- Styling methods for font, border, alignment, background colour, row height, and column width
- New `StyleConfig` class for declarative style configuration
- Cell validation with unit tests
- GitHub Actions workflows: CI, Black formatter, and PyPI publish
- PR template

### Changed
- Refactored package to `exceltablekit` layout with improved architecture
- Restructured `Cell`, `Table`, and related classes
- Renamed attributes and methods for clarity
- Validation logic refactored and renamed functions

### Fixed
- Excluded tests from package build

## [0.0.3] - 2025-02-05
### Added
- Available to install with pip
