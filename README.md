# EzIO

> An easy input/output utils package.

## Setup

### Prerequisites

Before getting started, make sure you have the following requisites:

- Python (>=3.11)
- Pip
- Git

### Instalation

1) Clone this repository.
   
```sh
git clone https://git.t3.daimlertruck.com/SANTCA2/ezio.git
cd ezio
```

2) [Optional] Create and activate a virtual environment.
   
```sh
python -m venv venv
venv\scripts\activate
```

3) Install dependencies.

```sh
pip install -r requirements.txt
```

## Usage

`EzIO` leverages popular data-wrangling packages, such as `pandas`, to provide simplified interfaces for loading and saving tables. By employing the facade design pattern, developers gain the flexibility to seamlessly switch data sources without requiring modifications to their project's source code. This abstraction enables easy adaptation to varying data formats or storage mechanisms, enhancing the adaptability and maintainability of projects.

To achieve this flexibility, `EzIO` depends on a `TOML` configuration file. This file should include a well-organized list of tables, each associated with its respective URI, source, and type. This structured configuration allows `EzIO` to dynamically adapt to different data sources, making it straightforward for developers to manage and switch between tables without the need for code modifications.

This is how the configuration file should be structured:

```toml
# sources must be defined and configured
[sources.mySource]
type = "localFileSystem" # currently the only supported type

[layer.table]
uri = "path\\to\\my\\table"
source = "mySource"
type = "txt" # in the case of local file systems, the file type
```

To load the example table above, use the following code snippet:

```python
load_table("layer", "table")
```

Which would be equivalent to:

```python
pd.read_csv("path\\to\\my\\table")
```

If the source file is changed, all that is needed is to update the `TOML` configuration file and the code will still work.