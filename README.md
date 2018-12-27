# HyTouch

HyTouch is a local package managing frontend for pip.

## Install

Using pip:

```bash
pip install hytouch
```

or just run src/hytouch if you have satisfied requirements.

## Requirement

- Python 3.7
  - Current HyTouch is hardcoded for Python 3.7. Other Python versions patch is planned
- Hy (>= 0.15.0) https://github.com/hylang/hy
- UNIX like CLI

## Usage

Place package.hy on your project root. Example:

```hy
(setv package {
  "dependencies"
  {"numpy" {}
   "hy==0.15.0" {}
   "jupyter" {}}

   "tasks"
   {"lab" ["jupyter" "lab"]
   "notebook" ["jupyter" "notebook"]
   "test" ["ls" "/home/takuma"]}})
```

- Variable "package" required as root element
- "dependencies" is a dictionary object, including package-name -> optional value
  - In current version, optional value is ignored
- "tasks" is a dictionary object, including task-name -> command params array

### Install packages

```bash
hytouch install
```

"dependencies" will be installed to PROJECT_ROOT/.hytouch

### Run task

```bash
hytouch run test
```

ls command will be executed.

## LICENSE

MIT
