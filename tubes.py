import streamlit as st
import string

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #198754;
    color:#ffffff;
    }
</style>""", unsafe_allow_html=True)

st.get_option("theme.primaryColor")
st.write("""
# Lexical Analyzer dan Parser Program

""")
st.write('S (Subject) : aki | nini')
st.write('V (Verb) :  neda | wawasuh | gegel')
st.write('O (Object) :  calana | sapatu | sapeda | surabi | kameja')
st.write('Contoh : aki neda surabi')
sentence = st.text_input("Masukkan Kalimat: ", placeholder="Masukkan kalimat S V O")
validasi = st.button("Validasi Grammar")

input_string = sentence.lower()+'#'
tokens = sentence.lower().split()
tokens.append('EOS')

# inisialisasi
alphabet_list = list(string.ascii_lowercase)
state_list = [
                'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9',
                'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19',
                'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29',
                'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39',
                'q40', 'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47'
            ]

transition_table = {}

for state in state_list:
    for alphabet in alphabet_list:
        transition_table[(state, alphabet)] = 'error'
        transition_table[(state, '#')] = 'error'
        transition_table[(state, ' ')] = 'error'

# spasi sebelum input
transition_table['q0', ' '] = 'q0'

# transisi table untuk Aki
transition_table[('q0', 'a')] = 'q1'
transition_table[('q1', 'k')] = 'q2'
transition_table[('q2', 'i')] = 'q3'
transition_table[('q3', ' ')] = 'q47'
transition_table[('q3', '#')] = 'accept'
transition_table[('q47', ' ')] = 'q47'
transition_table[('q47', '#')] = 'accept'

# transisi table untuk Nini
transition_table[('q0', 'n')] = 'q4'
transition_table[('q4', 'i')] = 'q5'
transition_table[('q5', 'n')] = 'q6'
transition_table[('q6', 'i')] = 'q7'
transition_table[('q7', ' ')] = 'q47'
transition_table[('q7', '#')] = 'accept'
transition_table[('q47', ' ')] = 'q47'
transition_table[('q47', '#')] = 'accept'

# transisi table untuk Neda
transition_table[('q0', 'n')] = 'q4'
transition_table[('q4', 'e')] = 'q8'
transition_table[('q8', 'd')] = 'q9'
transition_table[('q9', 'a')] = 'q10'
transition_table[('q10', ' ')] = 'q47'
transition_table[('q10', '#')] = 'accept'
transition_table[('q47', ' ')] = 'q47'
transition_table[('q47', '#')] = 'accept'

# transisi table untuk Wawasuh
transition_table[('q0', 'w')] = 'q11'
transition_table[('q11', 'a')] = 'q12'
transition_table[('q12', 'w')] = 'q13'
transition_table[('q13', 'a')] = 'q14'
transition_table[('q14', 's')] = 'q15'
transition_table[('q15', 'u')] = 'q16'
transition_table[('q16', 'h')] = 'q17'
transition_table[('q17', ' ')] = 'q47'
transition_table[('q17', '#')] = 'accept'
transition_table[('q47', ' ')] = 'q47'
transition_table[('q47', '#')] = 'accept'

# transisi table untuk Gegel
transition_table[('q0', 'g')] = 'q18'
transition_table[('q18', 'e')] = 'q19'
transition_table[('q19', 'g')] = 'q20'
transition_table[('q20', 'e')] = 'q21'
transition_table[('q21', 'l')] = 'q22'
transition_table[('q22', ' ')] = 'q47'
transition_table[('q22', '#')] = 'accept'
transition_table[('q47', ' ')] = 'q47'
transition_table[('q47', '#')] = 'accept'

# transisi table untuk Calana
transition_table[('q0', 'c')] = 'q23'
transition_table[('q23', 'a')] = 'q24'
transition_table[('q24', 'l')] = 'q25'
transition_table[('q25', 'a')] = 'q26'
transition_table[('q26', 'n')] = 'q27'
transition_table[('q27', 'a')] = 'q28'
transition_table[('q28', ' ')] = 'q47'
transition_table[('q28', '#')] = 'accept'
transition_table[('q47', ' ')] = 'q47'
transition_table[('q47', '#')] = 'accept'

# transisi table untuk Kameja
transition_table[('q0', 'k')] = 'q29'
transition_table[('q29', 'a')] = 'q24'
transition_table[('q24', 'm')] = 'q30'
transition_table[('q30', 'e')] = 'q31'
transition_table[('q31', 'j')] = 'q32'
transition_table[('q32', 'a')] = 'q33'
transition_table[('q33', ' ')] = 'q47'
transition_table[('q33', '#')] = 'accept'
transition_table[('q47', ' ')] = 'q47'
transition_table[('q47', '#')] = 'accept'

# transisi table untuk Sapeda
transition_table[('q0', 's')] = 'q34'
transition_table[('q34', 'a')] = 'q24'
transition_table[('q24', 'p')] = 'q35'
transition_table[('q35', 'e')] = 'q36'
transition_table[('q36', 'd')] = 'q37'
transition_table[('q37', 'a')] = 'q38'
transition_table[('q38', ' ')] = 'q47'
transition_table[('q38', '#')] = 'accept'
transition_table[('q47', ' ')] = 'q47'
transition_table[('q47', '#')] = 'accept'

# transisi table untuk Sapatu
transition_table[('q0', 's')] = 'q34'
transition_table[('q34', 'a')] = 'q24'
transition_table[('q24', 'p')] = 'q35'
transition_table[('q35', 'a')] = 'q39'
transition_table[('q39', 't')] = 'q40'
transition_table[('q40', 'u')] = 'q41'
transition_table[('q41', ' ')] = 'q47'
transition_table[('q41', '#')] = 'accept'
transition_table[('q47', ' ')] = 'q47'
transition_table[('q47', '#')] = 'accept'

# transisi table untuk Surabi
transition_table[('q0', 's')] = 'q34'
transition_table[('q34', 'u')] = 'q42'
transition_table[('q42', 'r')] = 'q43'
transition_table[('q43', 'a')] = 'q44'
transition_table[('q44', 'b')] = 'q45'
transition_table[('q45', 'i')] = 'q46'
transition_table[('q46', ' ')] = 'q47'
transition_table[('q46', '#')] = 'accept'
transition_table[('q47', ' ')] = 'q47'
transition_table[('q47', '#')] = 'accept'

# menambahkan token baru untuk huruf pertama yang diulang
transition_table[('q47', 'a')] = 'q1'
transition_table[('q47', 'n')] = 'q4'
transition_table[('q47', 'w')] = 'q11'
transition_table[('q47', 'g')] = 'q18'
transition_table[('q47', 'c')] = 'q23'
transition_table[('q47', 'k')] = 'q29'
transition_table[('q47', 's')] = 'q34'

# definition untuk simbol non-terminal dan simbol terminal
non_terminal = ['S', 'subject', 'verb', 'object']
terminals = ['aki', 'nini', 'neda', 'wawasuh',
                'gegel', 'calana', 'sapatu', 'sapeda', 'surabi', 'kameja']

# definition untuk parse table
parse_table = {}

parse_table[('S', 'aki')] = ['subject', 'verb', 'object']
parse_table[('S', 'nini')] = ['subject', 'verb', 'object']
parse_table[('S', 'neda')] = ['error']
parse_table[('S', 'wawasuh')] = ['error']
parse_table[('S', 'gegel')] = ['error']
parse_table[('S', 'calana')] = ['error']
parse_table[('S', 'sapatu')] = ['error']
parse_table[('S', 'sapeda')] = ['error']
parse_table[('S', 'surabi')] = ['error']
parse_table[('S', 'kameja')] = ['error']
parse_table[('S', 'EOS')] = ['error']

parse_table[('subject', 'aki')] = ['aki']
parse_table[('subject', 'nini')] = ['nini']
parse_table[('subject', 'neda')] = ['error']
parse_table[('subject', 'wawasuh')] = ['error']
parse_table[('subject', 'gegel')] = ['error']
parse_table[('subject', 'calana')] = ['error']
parse_table[('subject', 'sapatu')] = ['error']
parse_table[('subject', 'sapeda')] = ['error']
parse_table[('subject', 'surabi')] = ['error']
parse_table[('subject', 'kameja')] = ['error']
parse_table[('subject', 'EOS')] = ['error']


parse_table[('verb', 'aki')] = ['error']
parse_table[('verb', 'nini')] = ['error']
parse_table[('verb', 'neda')] = ['neda']
parse_table[('verb', 'wawasuh')] = ['wawasuh']
parse_table[('verb', 'gegel')] = ['gegel']
parse_table[('verb', 'calana')] = ['error']
parse_table[('verb', 'sapatu')] = ['error']
parse_table[('verb', 'sapeda')] = ['error']
parse_table[('verb', 'surabi')] = ['error']
parse_table[('verb', 'kameja')] = ['error']
parse_table[('verb', 'EOS')] = ['error']

parse_table[('object', 'aki')] = ['error']
parse_table[('object', 'nini')] = ['error']
parse_table[('object', 'neda')] = ['error']
parse_table[('object', 'wawasuh')] = ['error']
parse_table[('object', 'gegel')] = ['error']
parse_table[('object', 'calana')] = ['calana']
parse_table[('object', 'sapatu')] = ['sapatu']
parse_table[('object', 'sapeda')] = ['sapeda']
parse_table[('object', 'surabi')] = ['surabi']
parse_table[('object', 'kameja')] = ['kameja']
parse_table[('object', 'EOS')] = ['error']


# lexical analyzer main program
if validasi:
    idx_char = 0
    state = 'q0'
    current_token = ''
    while state != 'accept':
        current_char = input_string[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state == 'q3':
            st.write('current token: ', current_token, ', valid')
            current_token = ''
        if state == 'q7':
            st.write('current token: ', current_token, ', valid')
            current_token = ''
        if state == 'q10':
            st.write('current token: ', current_token, ', valid')
            current_token = ''
        if state == 'q17':
            st.write('current token: ', current_token, ', valid')
            current_token = ''
        if state == 'q22':
            st.write('current token: ', current_token, ', valid')
            current_token = ''
        if state == 'q28':
            st.write('current token: ', current_token, ', valid')
            current_token = ''
        if state == 'q33':
            st.write('current token: ', current_token, ', valid')
            current_token = ''
        if state == 'q38':
            st.write('current token: ', current_token, ', valid')
        if state == 'q41':
            st.write('current token: ', current_token, ', valid')
        if state == 'q46':
            st.write('current token: ', current_token, ', valid')
        if state == 'error':
            st.write('error')
            break
        idx_char = idx_char + 1

    # conclusion
    if state == 'accept':
        st.write('Semua token di input : ', sentence, ', valid')

    # parser main program

    # Stack initialization
    stack = []
    stack.append('#')
    stack.append('S')

    # Input reading initialization
    idx_token = 0
    symbol = tokens[idx_token]

    # parsing
    while (len(stack) > 0):
        top = stack[len(stack)-1]
        st.write('top= ', top)
        st.write('symbol= ', symbol)
        if top in terminals:
            st.write('top adalah simbol terminal')
            if top == symbol:
                stack.pop()
                idx_token = idx_token+1
                symbol = tokens[idx_token]
                if symbol == 'EOS':
                    st.write('isi stack: ', str(stack))
                    stack.pop()
            else:
                st.write('error')
                break
        elif top in non_terminal:
            st.write('top adalah symbol non-terminal')
            if parse_table[(top, symbol)][0] != 'error':
                stack.pop()
                symbols_to_be_paused = parse_table[(top, symbol)]
                for i in range(len(symbols_to_be_paused)-1, -1, -1):
                    stack.append(symbols_to_be_paused[i])
            else:
                st.write('error')
                break
        else:
            st.write('error')
            break
        st.write('isi stack:', str(stack))
        st.markdown("""---""")

    # conclusion
    st.write()
    if symbol == 'EOS' and len(stack) == 0:
        st.success('input string: '+sentence+' diterima, sesuai Grammar')
        st.spinner('Please wait...')
    else:
        st.error('Error, input string '+sentence+
                ' tidak diterima, tidak sesuai dengan Grammar. Grammar harus S O V')
    

