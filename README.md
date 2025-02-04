# 286_ai_text_poison
Dear chatgpt, please stop reading my problematic tweets >:(

**Key credits to [Confuseables](https://github.com/wanderingstan/Confusables) by [Stan James](https://github.com/wanderingstan)**

**Resources:**
- [How Does ChatGPT Read?](https://blog.georgeshakan.com/how-does-chatgpt-read/)
- [1 5 Byte Pair Encoding](https://www.youtube.com/watch?v=tOMjTCO0htA)

## Execution

There are 2 versions of the app, `console.py` (which is fully executed inside the command prompt) and `interface.py` which opens the app with a user-friendly interface.
They can be executed with:
```python .\console.py
python .\interface.py```
Respectively.

### Extras

**Thought Process:** For one, I am not a professional in A.I. and this program likely doesn't work the intended way but it funny in my mind. The thought process was simply to replace typical English characters with a variety of characters from other languages that look similar. While humans can see the visual similarity to understand what the "encrypted" text is, A.I. can not discriminate and will simply treat these characters differently (e.g. "o" and "Ö") have different values. Hypothetically, if this program was used on an extremely large scale, this could poison the dataset from A.I. to make incorrect correlations and thus have ill-formated output.

**Disclaimer:** I am not "anti-AI". Artificial Intelligence is a tool and is neutral in its existence. It is *how* A.I. is used and developed that I find problematic as key models are built on violating the intellectual property of others purely because it is posted on the internet. I believe that every creator has the right to protect their intellectual property, even to the extent of poisoning data for large language models.

**My Learning:** I discovered key gaps in my knowledge when it came to python as I coded this. For one, I only recently discovered python's ability to use Dictionaries alongside key-value pairs so I decided to use it to simplify the Confuseables list and clear out the confuseables that were too confusing and weren't accepted in Visual Studio. It was also the time for me to add an interface to my program instead of ugly command lines which taught me the use of TKinter which I expanded to the modernised CustomTKinter.
