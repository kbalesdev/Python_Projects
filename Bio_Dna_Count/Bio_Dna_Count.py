from turtle import width
import pandas as pd
import streamlit as sl
import altair as alt
from PIL import Image

#%%
# Page Title

image = Image.open('dna-logo.jpg')

sl.image(image, use_column_width=True)

sl.write('''
# DNA Nucleotide Count Web App
This app counts the nucleotide composition of query DNA!
***
''')


#%%
# Input Text Box
sl.header('Enter DNA sequence')

sequence_input = ">DNA Query\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = sl.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence) # Concatenate list into a string

sl.write('''
***
''')

# Print the input DNA sequence
sl.header('INPUT (DNA Query)')
sequence

# DNA nucleotide count
sl.header('OUTPUT (DNA Nucleotide Count)')
sl.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X

sl.subheader('2. Print text')
sl.write('There are {0} adenine (A)'.format(X['A']))
sl.write('There are {0} thymine (T)'.format(X['T']))
sl.write('There are {0} guanine (G)'.format(X['G']))
sl.write('There are {0} cytosine (C)'.format(X['C']))

sl.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns= {'index':'nucleotide'})
sl.write(df)

sl.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

p = p.properties(
    width = alt.Step(60) # Controls width of the bar
)

sl.write(p)


#%%