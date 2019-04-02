[![banner](https://raw.githubusercontent.com/oceanprotocol/art/master/github/repo-banner%402x.png)](https://oceanprotocol.com)

# osmosis-on-premise-driver

> 💧 Osmosis On-Premise Driver Implementation
> [oceanprotocol.com](https://oceanprotocol.com)

[![PyPI](https://img.shields.io/pypi/v/osmosis-on-premise-driver.svg)](https://pypi.org/project/osmosis-on-premise-driver/)
[![Build Status](https://travis-ci.com/oceanprotocol/osmosis-on-premise-driver.svg)](https://travis-ci.com/oceanprotocol/osmosis-on-premise-driver)
[![GitHub contributors](https://img.shields.io/github/contributors/oceanprotocol/osmosis-on-premise-driver.svg)](https://github.com/oceanprotocol/osmosis-on-premise-driver/graphs/contributors)
[![Codacy Badge](https://img.shields.io/codacy/grade/ad7aaa0326584eb0b52d69b0a36474bb.svg)](https://app.codacy.com/project/ocean-protocol/osmosis-on-premise-driver/dashboard)
[![Codacy coverage](https://img.shields.io/codacy/coverage/ad7aaa0326584eb0b52d69b0a36474bb.svg)](https://app.codacy.com/project/ocean-protocol/osmosis-on-premise-driver/dashboard)

---

## Table of Contents

- [Setup](#setup)
- [Code Style](#code-style)
- [Testing](#testing)
- [New Version](#new-version)
- [License](#license)

---

## Setup

You don't have to set any Brizo configuration settings or other configuration settings to use on-premise storage with Brizo. You just need to make sure that Brizo can resolve the file URLs. For more details, see [the tutorial about setting up on-premise storage](https://docs.oceanprotocol.com/tutorials/on-premise-for-brizo/).

## Code Style

Information about our Python code style is documented in this the [python-developer-guide](https://github.com/oceanprotocol/dev-ocean/blob/master/doc/development/python-developer-guide.md)
and the [python-style-guide](https://github.com/oceanprotocol/dev-ocean/blob/master/doc/development/python-style-guide.md).

## Testing

Automatic tests are setup via Travis, executing `tox`.
Our tests use the pytest framework.

## New Version

The `bumpversion.sh` script helps to bump the project version. You can execute the script using as first argument {major|minor|patch} to bump accordingly the version.

## License

```text
Copyright 2018 Ocean Protocol Foundation Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
