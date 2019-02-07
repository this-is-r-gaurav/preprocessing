## United - Preprocessing

This is the cleaned branch of Original Preprocessing Library.

```commandline
git clone -b clean-preprocessing https://github.com/this-is-r-gaurav/preprocessing

cd preprocessing
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

```

### How to test

Currently not any testing Module. But You can do following task

* Stripping Html
* Stripping Comments
* Stripping 
* Strip NoN ascii
* Strip Duplicate WhiteSpace
* Expand Contractions: By default this is disabled 
since it need to download pre-trained models that is around 250 MB(Slim Version).
If you want to enable it just while creating object pass `Cleaner(sample_text, expand_contraction=True)`
* Contract digit words two original digit say your text have eighty-two then it will turn it into 82

```python
~/(venv)preprocessing$ python3 
>>> from preprocessing.text.cleaner import Cleaner
>>> sample = """<h1>Title Goes Here</h1>
<b>Bolded Text</b>
<i>Italicized Text</i>
<img src="this should all be gone"/>
<a href="this will be gone, too">But this will still be here!</a>
I run. He ran. She is running. Will they stop running?
I talked. She was talking. They talked to them about running. Who ran to the talking runner?
[Some text we don't want to keep is in here]
¡Sebastián, Nicolás, Alejandro and Jéronimo are going to the store tomorrow morning!
something... is! wrong() with.,; this :: sentence.
I can't do this anymore. I didn't know them. Why couldn't you have dinner at the restaurant?
My favorite movie franchises, in order: Indiana Jones; Marvel Cinematic Universe; Star Wars; Back to the Future; Harry Potter.
Don't do it.... Just don't. Billy! I know what you're doing. This is a great little house you've got here.
[This is some other unwanted text]
John: "Well, well, well."
James: "There, there. There, there."
&nbsp;&nbsp;
There are a lot of reasons not to do this. There are 101 reasons not to do it. 1000000 reasons, actually.
I have to go get 2 tutus from 2 different stores, too.
22    forty-five   1067   445
<!--This is a comment -->
I'm testing the preprocessing Library
{{Here is some stuff inside of double curly braces.}}
{Here is more stuff in single curly braces.}
[DELETE]
</body>"""
>>> cl = Cleaner(sample)
>>> print(cl)

```
