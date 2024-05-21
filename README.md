# PDFs to Word Cloud Generator

Python script that generates a word cloud from the text extracted from PDF files in a specified directory. 
The word cloud gives more prominence to words that appear more frequently in the source text.

## Dependencies

The script requires the following Python packages:

- PyPDF2
- wordcloud
- matplotlib
- nltk
- string
- collections

You can install these dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

To use the script, you need to specify the directory containing the PDFs and several lists of words:

- `exclude_words`: Words to be excluded from the word cloud.
- `important_words`: Words to be emphasized in the word cloud.
- `capitalized_words`: Words to be capitalized in the word cloud.
- `unimportant_words`: Words to be given less importance in the word cloud.

Here's an example of how to call the function:

```python
create_wordcloud('folder/with/pdfs', exclude_words, img_width, img_height, important_words, capitalized_words, unimportant_words)
```

## Output

The script will display the word cloud using matplotlib. By default, the word cloud is generated in black and white, with Times New Roman font and a white background.

## License

This project is licensed under the terms of the MIT license.
