# Test Automation Exercise

## How to set up the project

Clone the repo:

```shell
git clone https://github.com/oscarAguayo/apex_exercise.git
```

Dependencies: python >= 3.8

First create an environment and activate

```shell
python3 -m venv venv
```

On linux and macOS

```shell
source venv/bin/activate
```

On Windows

```shell
venv\Scripts\activate.bat
```

Install requirements dependencies

```shell
pip install -r requirements.txt
```

### Set the environment vars

Copy `.env.example` and rename to `.env` set the environment variables with your own data.

### Install playwright browsers

To install playwright browsers, if set empty option playwright will install all the browsers

```shell
playwright install [ | chromium | firefox | msedge | webkit]
```

For example, to install only chromium

```shell
playwright install chromium
```

## How to run

```shell
pytest
```

## Trace outputs

The trace outputs of all test are in `test-results` folder.

You need to execute

```shell
playwright show-trace <path/to/trace.zip>
```

To see the trace generated.

## Additional notes

The tests need to be executed `--headed` because the site detect the "headless" mode and block the requests.
