<h1 align="center">Salesforce Marketing Cloud CLI</h1>

A CLI application built with python that interfaces with [Salesforce Marketing Cloud (SFMC)](https://www.salesforce.com/products/marketing-cloud/overview/). Built this to help me achieve simple tasks that are just not that easily feasible in SFMC. Such as looking up an Data Extensions path, or making sure that certain automations have ran in the last 24 hours.

## Table of Contents
* [Demo](#demo)
* [Installation](#installation)
* [Configuration](#configuration)
* [Usage](#usage)

## Demo

## Installation

## Configuration

You will need this file: ```~/sfmc_cli_credentials.json```. Containing an array of Accounts and there credentials.

```json
[{
    "name": "Account Name",
    "client_id": "",
    "client_secret": ""
}]
```
To check any automations you will need this file ```~/sfmc_cli_automations_to_check.json```with the account and automation name you want to check.
```json
[
    {
        "account": "Account Name", // Should match what is in sfmc_cli_credentials.json
        "automations": ["An Automation", "Another Automation"]
    }
]
```

## Usage
