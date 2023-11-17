# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
import numpy as np

from streamlit.logger import get_logger

LOGGER = get_logger(__name__)





df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

def run():#sql-mhp-sandbox.database.windows.net
    
    st.set_page_config(
        page_title="Hellos",
        page_icon="👋",
    )

    st.write("# :balloon: Welcome to Streamlit! 👋")

    st.line_chart(df)

    st.sidebar.success("Select a demo above.")

    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    st.map(map_data)

    if st.checkbox('Show dataframe'):
      chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
      chart_data

    # Add a selectbox to the sidebar:
    add_selectbox = st.sidebar.selectbox(
      'How would you like to be contacted?',
      ('Email', 'Home phone', 'Mobile phone')
    )

    # Add a slider to the sidebar:
    add_slider = st.sidebar.slider(
      'Select a range of values',
      0.0, 100.0, (25.0, 75.0)
    )


if __name__ == "__main__":
    run()
