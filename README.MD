# Python Ctf Reader
## Installing

**To install this package you need to type this command
into console:**

```
pip install CtfReader
```

## Working

### First you need to import the library

```python
import CtfReader
```
or
```python
from CtfReader import CtfFile
```

### Create a Ctf File
```python
file = CtfFile("path to ctf file")
```

Or

```python
file = CtfReader.CtfFile("path to ctf file")
```

### Get all text from the file

```python
file.getText()
```

### Get all text by lines

```python
file.getAllLines()
```

### Read the file and print to console

```python
file.read()
```
