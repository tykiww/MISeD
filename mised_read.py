
import json
from urllib import request
    
class MISeDData:
    def __init__(self, input):
        # URL of the raw file. Kinda dangerous but whateva.
        self.input = input
        self.url = f"https://raw.githubusercontent.com/tykiww/MISeD/main/mised/{self.input}.jsonl"
        self.local = f'mised/{input}.jsonl'
        self.options = ['train', 'test', 'validation']

    def parse_indexes(self, entry, meeting_length):
        """Finds the start and end points"""
        # unpack values
        vals = [value for d in entry for value in d.values()]

        # if there are no values to unpack, retrieve the entire meeting.
        if len(vals)==0:
            return [0, meeting_length]
        else:
            return [min(vals), max(vals)]

    def parse_speakers(self, entry):
        """Finds the names of the speakers in the meeting"""
        speakers = [i['speakerName'] for i in entry]
        return list(set(speakers))

    def index_meeting(self, meeting):
        """Gets the correct meeting snippet"""
        combine = [i['speakerName'] + ': ' + i['text'] for i in  meeting]
        return '\n'.join(combine)

    def retrieve_data_local(self): # kinda defunct, but useful.
        """retrieve MISeD data. Only works if done locally"""
        if self.input not in self.options:
            print('ha, sucka. choose train, test, or validation')
            return None
        else:
            with open(self.local, 'r') as file:
                data = [json.loads(line) for line in file]
                return data

    def retrieve_data_url(self):
        if self.input not in self.options:
            print('ha, sucka. choose train, test, or validation')
            return None
        else:
            with request.urlopen(self.url) as response:
                file_content = response.read().decode('utf-8')

            # Process the content as JSON Lines
            data = [json.loads(line) for line in file_content.splitlines()]
            return data
    
    # Convert necessary data
    def get(self,read_locally):
        
        # Get the data
        if read_locally:
            data = self.retrieve_data_local()
        else:
            data = self.retrieve_data_url()

        # empty list that we will eventually return.
        collect = []

        # Create a question-answer pair.
        for i in range(len(data)):
            # Get meeting and speakers 
            record = data[i]
            mtg = record['meeting']['transcriptSegments']
            mtg_len = len(mtg)
            speakers = self.parse_speakers(mtg)
            # prepare questions of interest.
            questions = record['dialog']['dialogTurns']
            
            # keep character length for summary

            for n in range(len(questions)):
                # Get speakers, question of interest, and response.
                query = questions[n]['query']
                response = questions[n]['response']

                # Get the meeting portion of interest
                if 'responseAttribution' in questions[n].keys():
                    indx = questions[n]['responseAttribution']['indexRanges']
                    indx = self.parse_indexes(indx, mtg_len)
                else:
                    # default to entire meeting
                    indx = [0, mtg_len]
                snippet = mtg[indx[0]:indx[1]]
                snippet = self.index_meeting(snippet)

                collect.append({'query': query,
                                'response': response,
                                'snippet': snippet,
                                'speakers': speakers,
                                })

        return collect


if __name__ == "__main__":
    # example to pull training dataset
    retriever = MISeDData('train')
    data = retriever.get()
