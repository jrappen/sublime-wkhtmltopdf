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
  <https://github.com/jrappen/sublime-wkhtmltopdf/blob/master/docs/en/README.md>
* German (Deutsch):
  <https://github.com/jrappen/sublime-wkhtmltopdf/blob/master/docs/de/README.md>

### Code of conduct

<https://github.com/jrappen/.github/blob/master/CODE_OF_CONDUCT.md>

### Contributing guide

<https://github.com/jrappen/.github/blob/master/CONTRIBUTING.md>

## Requirements

!!! panel-warning "Requirements"

    * This plug-in targets and is tested against the **latest Build** of [Sublime Text](https://www.sublimetext.com), currently requiring **`Build 4074`** or later.
    * [Install Package Control](https://packagecontrol.io/installation) via the menu: `Tools > Install Package Control`
        * Close and reopen Sublime Text after having installed Package Control.
    * [`wkhtmltopdf`](http://wkhtmltopdf.org/downloads.html) must be in your `PATH`!

## Installation

Using **Package Control** is not required, but recommended as it keeps your packages (with their dependencies) up-to-date!

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
//  Packages/wkhtmltopdf/.sublime/settings/Preferences.sublime-settings

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
