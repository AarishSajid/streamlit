import pandas as pd
import streamlit as st
import altair as alt
from collections import Counter

st.write("""
# DNA Nucleotide Count Web App

A dna nucleotide count web app using streamlit i made for practice
***
""")

st.header('Enter DNA sequence down below :)')

sequence = 'copy in your dna sequence here'

d_strand = st.text_area('DNA sequence', sequence, height=290)
d_strand = d_strand.splitlines()
d_strand = ''.join(d_strand)
d_strand = d_strand.upper()

st.write("""
         ***
            """)

st.header('Input DNA sequence')
d_strand

st.header('Output DNA nucleotide count')

def dna_nucleotide_count(seq):
    d = dict(Counter(seq))
    return d

ot = dna_nucleotide_count(d_strand)

st.write('There are ' + str(ot['A']) + ' adenine (A)')
st.write('There are ' + str(ot['T']) + ' thymine (T)')
st.write('There are ' + str(ot['G']) + ' guanine (G)')
st.write('There are ' + str(ot['C']) + ' cytosine (C)')
st.write('There are ' + str(ot['A'] + ot['T'] + ot['G'] + ot['C']) + ' total nucleotides')

df = pd.DataFrame(ot.items(), columns=['nucleotide', 'count'])

st.subheader("Composition of DNA sequence")
chart = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

chart = chart.properties(
    width=alt.Step(100)
)

st.write(chart)

