[![License](https://img.shields.io/github/license/jrappen/sublime-wkhtmltopdf.svg?style=flat-square)](https://github.com/jrappen/sublime-wkhtmltopdf/blob/master/LICENSE)
[![Required ST Build](https://img.shields.io/badge/ST-4074+-orange.svg?style=flat-square&logo=sublime-text)](https://www.sublimetext.com)
[![Downloads Package Control](https://img.shields.io/packagecontrol/dt/wkhtmltopdf.svg?style=flat-square)](https://packagecontrol.io/packages/wkhtmltopdf)
[![Latest tag](https://img.shields.io/github/tag/jrappen/sublime-wkhtmltopdf.svg?style=flat-square&logo=github)](https://github.com/jrappen/sublime-wkhtmltopdf/tags)
[![SublimeHQ Discord](https://img.shields.io/discord/280102180189634562?label=SublimeHQ%20Discord&logo=discord&style=flat-square)](https://discord.gg/D43Pecu)
[![Donate via PayPal](https://img.shields.io/badge/paypal.me-jrappen-009cde.svg?style=flat-square&logo=paypal)](https://www.paypal.me/jrappen)

# [`wkhtmltopdf`](http://wkhtmltopdf.org/downloads.html) plug-in for [Sublime Text](https://www.sublimetext.com)

> Convert HTML to PDF via `wkhtmltopdf` in Sublime Text.

* [Documentation](#documentation)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Source Code](#source-code)
* [Donations](#donations)

## Documentation

> Plugin documentation is available via the menu or command palette.

* English:
  <https://github.com/jrappen/sublime-wkhtmltodpf/blob/master/docs/en/README.md>
* German (Deutsch):
  <https://github.com/jrappen/sublime-wkhtmltodpf/blob/master/docs/de/README.md>

### Code of conduct

<https://github.com/jrappen/.github/blob/master/CODE_OF_CONDUCT.md>

### Contributing guide

<https://github.com/jrappen/.github/blob/master/CONTRIBUTING.md>

## Requirements

* This plug-in targets and is tested against the **latest Build** of [Sublime Text](https://www.sublimetext.com), currently requiring **`Build 4074`** or later.
* [Install Package Control](https://packagecontrol.io/installation)
    * Close and reopen Sublime Text after having installed Package Control.
* [`wkhtmltopdf`](http://wkhtmltopdf.org/downloads.html) must be in your `PATH`!

## Installation

Using **Package Control** required, as it keeps your packages (with their dependencies) up-to-date!

### Installation via Package Control

* Open the Command Palette (`Tools > Command Palette`).
* Choose `Package Control: Install Package`.
* Search for [`wkhtmltopdf` on Package Control](https://packagecontrol.io/packages/wkhtmltopdf) and select to install.

## Usage

Use either of the following two methods to convert an HTML document in the active view to PDF by selecting `wkhtmltopdf: Convert to PDF` from the:

* context menu
* command palette

Depending upon your settings this takes a while, see status bar for feedback.

### Settings

Run `wkhtmltopdf --extended-help` via the command line to check for available options. The default is:

```jsonc
//  Packages/wkhtmltopdf/.sublime/settings/wkhtmltopdf.sublime-settings

{
    "wkhtmltopdf.cmd_options": "--javascript-delay 10000 --outline-depth 8 --encoding utf-8"
}
```

You can adjust them via the command palette (`Preferences: wkhtmltopdf: Settings`) or the main menu (`Preferences > Package Settings > wkhtmltopdf > Settings`).

## Source Code

<https://www.github.com/jrappen/sublime-wkhtmltopdf>

### License

<https://github.com/jrappen/sublime-wkhtmltopdf/blob/master/LICENSE>

### Issues

Please use the command palette or main menu to report an issue.

## Donations

<https://www.paypal.me/jrappen>
