import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_ydata_profiling import st_profile_report
import seaborn as sns
# dataset
c = {0: 'anagrams', 1: 'anscombe', 2: 'attention', 3: 'brain_networks',
      4: 'car_crashes', 5: 'diamonds', 6: 'dots', 7: 'dowjones', 8: 'exercise', 
      9: 'flights', 10: 'fmri', 11: 'geyser', 12: 'glue', 13: 'healthexp', 14: 'iris',
        15: 'mpg', 16: 'penguins', 17: 'planets', 18: 'seaice', 19: 'taxis',
         20: 'tips', 21: 'titanic'}
st.header("Data set profile report")
# selectbox
selected_values=st.sidebar.selectbox('Select a dataset',list(c.values()))
# Display the selected value
st.write(f'You selected: {selected_values}')

dataset=(sns.load_dataset(selected_values))


pr = ProfileReport(dataset, title="Report")
st_profile_report(pr)



