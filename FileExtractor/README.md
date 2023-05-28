# FileExtractor

Copies files with specific names to a new folder

## How to use extractor.py 

```python
git clone https://github.com/khj3437/LightSnippetWithPython.git
cd FileExtractor 
```

Put the files in the targets folder

Open extractor.py with editor

Change {NAME} in extractor.py

target_name = "{NAME}"


```python
# Run
python extractor.py
```


## How to use extractor2.py

custom 'base_path' in extractor.py

Files in year-month-day folder move to year-month folder 

```python
# before 
2023 fodler
ㄴ 2023-01-01
  ㄴ 001.JPG
  ㄴ 001.PNG
ㄴ 2023-01-02
  ㄴ 001.MOV
  ㄴ 001.JPG
...
ㄴ2023-05-28 
  ㄴㄴ 001.PNG
```


```python
# run
python extractor2.py

# after 
2023-01
ㄴ2023-01-01-001.PNG
ㄴ2023-01-01-002.JPG
2023-02
...
```
