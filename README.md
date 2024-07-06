\* cloned repository to manually correct some unclean text from jsonl files \*

This repository contains the **MISeD** (Meeting Information Seeking Dialogs) dataset - an information-seeking dialog dataset over meeting transcripts. 

The dataset and its semi-automatic creation methodology are described in the paper: [Efficient Data Generation for Source-grounded Information-seeking Dialogs: A Use Case for Meeting Transcripts](https://arxiv.org/pdf/2405.01121).

**MISeD** includes 432 dialogs over meeting transcripts from the [QMSum meeting corpus](https://github.com/Yale-LILY/QMSum).
We used 225 meetings across three domains: 134 Product Meetings (AMI), 58 Academic Meetings (ICSI), and 33 public Parliamentary Committee Meetings sourced from the Welsh Parliament and the Parliament of Canada.
Splits are similar to the QMSum splits, in a ratio of 70:15:15 for train:validation:test.

Each dataset instance includes:
1. A single dialog about a specific meeting transcript, containing up to ten query-response turns
2. Associated metadata
3. When relevant, a response is accompanied by a set of attributing transcript spans

For training and evaluating an agent model, each dialog is divided into task instances. Each such instance represents a single current query, incorporating its preceding dialog history along with the corresponding target response and its attributions.

The **WOZ** dataset is a fully manual version of MISeD, aimed to objectively test the value of training models with the **MISeD** data.

For those that want to use the helper class to load data, just clone this repository and directly pull the module or 
This should reduce time to get the data trainable into an instruction set.

```
# example pulling the training dataset
from mised_read import MISeDData

retriever = MISeDData('train') # only retrieves train, test, and validation as inputs.
data = retriever.get() # just a simple get.
```

Sample output snippet.

[{'query': 'Can you summarize the main points of the discussion on remote control design?',
  'response': 'Here are the main points of the discussion on remote control design:\n\n* The remote control should be user-friendly and accessible to a wide range of users, including 
older adults and children.\n* The remote should have a simple and intuitive design, with clear and easily recognizable buttons.\n* The remote could have a combination of physical 
buttons and an LCD display with menus for additional functions.\n* The remote could have a flip-top design to save space and provide a larger screen for the LCD display.',
 'snippet': "Project Manager: Um I'm Sarah, the Project Manager and this is our first meeting, surprisingly enough. ...,
 'speakers': ['Project Manager', 'Industrial Designer', 'Marketing', 'User Interface']} ...]


### Citation
[Efficient Data Generation for Source-grounded Information-seeking Dialogs: A Use Case for Meeting Transcripts](https://arxiv.org/pdf/2405.01121).
```
@misc{golany2024efficient,
      title={Efficient Data Generation for Source-grounded Information-seeking Dialogs: A Use Case for Meeting Transcripts}, 
      author={Lotem Golany and Filippo Galgani and Maya Mamo and Nimrod Parasol and Omer Vandsburger and Nadav Bar and Ido Dagan},
      year={2024},
      eprint={2405.01121},
      archivePrefix={arXiv},      
}
```

