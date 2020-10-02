# How to use

## Install

```bash
pip install translate-comment-out
```

## Use by CLI

In directory that include `sample.js`,

```bash
tco sample.js --dest ja > sample_ja.js
```

## Use by Python

```python
from translate_comment_out import translator


translated_source = translator.translate(filepath='sample.js')
print(translated_source)
```
