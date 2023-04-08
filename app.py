#Library
import streamlit as st

#write
st.write('software perkalian')
st.subheader('ini adalah aplikasi untuk mengalikan bilangan bulat')

#Input bilangan pertama
number1 = st.number_input('Masukan bilangan pertama')
st.write(f'Bilangan Pertama adalah {number1}')

#Input bilangan kedua
number2 = st.number_input('Masukan bilangan kedua')
st.write(f'Bilangan kedua adalah {number2}')
         
#hasil kali
hasil = number1*number2
      
if st.button('hitung'):
    st.writer(f'hasilk kali antara {number1} dan {number2} adalah {hasil}')
else:
    st.write('silahkan pencet tombol hitung!')
    