# `tap-formbricks`

`tap-formbricks` is a Singer tap for Formbricks.

Built with the [Meltano Singer SDK](https://sdk.meltano.com).

## Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`
* `schema-flattening`
* `batch`

## Settings

| Setting | Required | Default | Description |
|:--------|:--------:|:-------:|:------------|
| api_key | True     | None    | The key to authenticate against the API service |
| flattening_enabled | False    | None    | 'True' to enable schema flattening and automatically expand nested properties. |

A full list of supported settings and capabilities is available by running: `tap-formbricks --about`

### Source Authentication and Authorization

To use `tap-formbricks`, you need to authenticate with the Formbricks API. After signing up for Formbricks, you can find your API key in the configuration's API key section.

## Installation

Install from PyPi:

```bash
pipx install tap-formbricks
```

Install from GitHub:

```bash
pipx install git+https://github.com/emilklindt/tap-formbricks.git@main
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
