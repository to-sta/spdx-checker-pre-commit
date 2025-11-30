# CHANGELOG

All notable changes to this project are recorded here. Changelog has been added with version 0.1.4. The format is similar to the [Keep a Changelog]((https://keepachangelog.com/en/1.0.0/)) convention.

## [0.1.7] - 2025-11-30

### Changed

- Updated the pinned `spdx_checker` version to 0.1.19 to enable color support detection.


## [0.1.6] - 2025-11-30

### Added

- Added `fix` and `continue-on-error` flags


## [0.1.5] - 2025-11-20


### Added

- Introduced initial changelog file.

### Changed

- Switched to `require_serial = true` to avoid batch runs with `pre-commit run --all-files`
- Added error handling to remove traceback error