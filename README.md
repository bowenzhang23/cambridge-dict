# Project: cambridge-dict

fetch vocabulary from [cambridge dictionary](https://dictionary.cambridge.org/).

display English/Chinese meanings, example sentences.

might be insteresting for Chinese-English learner, translator training sample generation ..

## Usage

### Search from terminal

steps: 

1) search the word "piggy"

```bash
./search.py piggy
```

2) output:

```text
OrderedDict([('title', ['piggy', 'piggy']),
             ('explain', ['a pig', 'like a pig']),
             ('explain_cn', ['猪，小猪', '像猪的']),
             ('example',
              ['Look at those cute little piggies, James!',
               "He's got little piggy eyes."]),
             ('example_cn', ['看那些可爱的小猪，詹姆斯！', '他长着猪眼似的小眼睛。']),
             ('phrase', []),
             ('audio_src',
              ['https://dictionary.cambridge.org/media/english-chinese-simplified/uk_pron/u/ukp/ukpic/ukpictu023.mp3',
               'https://dictionary.cambridge.org/media/english-chinese-simplified/us_pron/p/pig/piggy/piggy.mp3',
               'https://dictionary.cambridge.org/media/english-chinese-simplified/uk_pron/u/ukp/ukpic/ukpictu023.mp3',
               'https://dictionary.cambridge.org/media/english-chinese-simplified/us_pron/p/pig/piggy/piggy.mp3'])])
```

### Word list to markdown notes

search each words in the list and generate a pretty looking note in markdown format.

steps:

1) prepare an input file [input.txt](./input.txt)

2) run the dictionary

```bash
./note.py input.txt output.md --tag "My note"
```

3) after that, an output markdown file is generated: [output.md](./output.md)
